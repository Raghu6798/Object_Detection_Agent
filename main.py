import os
import json
import re
import requests
from io import BytesIO
from typing import List, Dict, Tuple, Optional, Union
import time

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from google import genai
from google.genai import types
from pydantic import BaseModel, Field, ValidationError, RootModel
from loguru import logger

import os
from typing import List, Dict, Any, Optional, Union
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from PIL import Image
import base64
from io import BytesIO


from dotenv import load_dotenv

load_dotenv()

# ==============================================================================
# 1. LOGGING CONFIGURATION
# ==============================================================================

def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None):
    """
    Configure loguru logging with custom format and multiple outputs.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path to save logs
    """
    # Remove default handler
    logger.remove()
    
    # Custom format with colors and emojis for better readability
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
    
    # Add console handler
    logger.add(
        sink=lambda msg: print(msg, end=""),
        format=log_format,
        level=log_level,
        colorize=True
    )
    
    # Add file handler if specified
    if log_file:
        logger.add(
            sink=log_file,
            format=log_format,
            level=log_level,
            rotation="10 MB",
            retention="7 days",
            compression="zip"
        )
    
    logger.info("🚀 Logging system initialized")

# Initialize logging
setup_logging(log_level="DEBUG", log_file="object_detection.log")

# ==============================================================================
# 2. PYDANTIC DATA MODELS FOR INPUT/OUTPUT VALIDATION
# ==============================================================================

class Detection(BaseModel):
    """
    Represents a single detected object with its bounding box and label.
    Pydantic ensures that the data conforms to this structure.
    """
    box_2d: Tuple[int, int, int, int] = Field(..., description="Bounding box in [ymin, xmin, ymax, xmax] format")
    label: str = Field(..., description="A descriptive label for the detected object")

class DetectionResponse(RootModel):
    """
    Represents the expected output from the Gemini API: a list of detections.
    Using RootModel allows us to validate a JSON array at the top level.
    """
    root: List[Detection]

# ==============================================================================
# 3. THE OBJECT DETECTION AGENT WITH COMPREHENSIVE LOGGING
# ==============================================================================

class ObjectDetectionAgent:
    """
    Computer Vision Object Detection Agent using Google's Gemini 1.5 Pro.
    Detects objects in images, validates the output, and draws bounding boxes.
    Enhanced with comprehensive loguru logging.
    """

    def __init__(self, api_key: str):
        """Initialize the agent with Google API key"""
        logger.info("🔧 Initializing ObjectDetectionAgent")
        
        if not api_key:
            logger.critical("❌ Google API key is required but not provided")
            raise ValueError("Google API key is required.")
        
        logger.debug(f"🔑 API key provided ")
        
        try:
            self.client = genai.Client(api_key=api_key)
            self.model_name = "gemini-2.5-pro"
            logger.success(f"✅ Successfully initialized Gemini client with model: {self.model_name}")
        except Exception as e:
            logger.critical(f"❌ Failed to initialize Gemini client: {e}")
            raise

    def load_image(self, image_source: Union[str, bytes]) -> Tuple[Image.Image, Image.Image]:
        """
        Load image from URL, file path, or bytes.

        Args:
            image_source: URL string, file path, or image bytes

        Returns:
            Tuple of (Gemini image part, PIL Image)
        """
        start_time = time.time()
        logger.info("📥 Starting image loading process")
        
        try:
            if isinstance(image_source, str):
                if image_source.startswith(('http://', 'https://')):
                    logger.info(f"🌐 Loading image from URL: {image_source}")
                    logger.debug("📡 Making HTTP request to fetch image")
                    
                    response = requests.get(image_source, timeout=30)
                    response.raise_for_status()
                    image_bytes = response.content
                    
                    logger.debug(f"📊 Downloaded {len(image_bytes)} bytes from URL")
                    
                else:
                    logger.info(f"📁 Loading image from file: {image_source}")
                    
                    if not os.path.exists(image_source):
                        logger.error(f"❌ Image file not found: {image_source}")
                        raise FileNotFoundError(f"Image file not found: {image_source}")
                    
                    file_size = os.path.getsize(image_source)
                    logger.debug(f"📊 File size: {file_size} bytes")
                    
                    with open(image_source, 'rb') as f:
                        image_bytes = f.read()
                    
                    logger.debug(f"📖 Successfully read {len(image_bytes)} bytes from file")
                    
            elif isinstance(image_source, bytes):
                logger.info("📥 Loading image from provided bytes")
                logger.debug(f"📊 Bytes length: {len(image_source)}")
                image_bytes = image_source
            else:
                logger.error("❌ Invalid image source type provided")
                raise TypeError("image_source must be a URL (str), file path (str), or bytes.")

            logger.debug("🖼️ Converting bytes to PIL Image")
            pil_image = Image.open(BytesIO(image_bytes)).convert("RGB")
            
            logger.debug(f"📏 Image dimensions: {pil_image.size[0]}x{pil_image.size[1]}")
            logger.debug(f"🎨 Image mode: {pil_image.mode}")
            
            load_time = time.time() - start_time
            logger.success(f"✅ Image loaded successfully in {load_time:.2f}s")
            
            return pil_image, pil_image
            
        except requests.RequestException as e:
            logger.error(f"🌐 HTTP request failed: {e}")
            raise
        except IOError as e:
            logger.error(f"📁 File I/O error: {e}")
            raise
        except Exception as e:
            logger.critical(f"❌ Unexpected error during image loading: {e}")
            raise

    def detect_objects(self, image_part: Image.Image, custom_prompt: Optional[str] = None) -> str:
        """
        Send image to Gemini for object detection.

        Args:
            image_part: PIL Image object.
            custom_prompt: Optional custom prompt for detection.

        Returns:
            Raw response text from Gemini.
        """
        start_time = time.time()
        logger.info("🤖 Starting object detection with Gemini API")
        
        default_prompt = """Detect all prominent objects in this image.
        For each object, provide:
        - A bounding box in format [ymin, xmin, ymax, xmax] normalized to 0-1000
        - A descriptive label

        Return ONLY a JSON array in this format:
        [
            {"box_2d": [ymin, xmin, ymax, xmax], "label": "object_name"},
            {"box_2d": [ymin, xmin, ymax, xmax], "label": "object_name"}
        ]

        No other text, just the JSON array."""

        prompt = custom_prompt or default_prompt
        
        if custom_prompt:
            logger.info("📝 Using custom detection prompt")
            logger.debug(f"Custom prompt: {custom_prompt[:100]}...")
        else:
            logger.info("📝 Using default detection prompt")
        
        logger.debug(f"🎯 Model: {self.model_name}")
        logger.debug("📤 Sending request to Gemini API")
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name, 
                contents=[prompt, image_part]
            )
            
            api_time = time.time() - start_time
            
            if hasattr(response, 'text') and response.text:
                response_length = len(response.text)
                logger.success(f"✅ Received response from Gemini API in {api_time:.2f}s")
                logger.debug(f"📊 Response length: {response_length} characters")
                logger.debug(f"📋 Response preview: {response.text[:200]}...")
                return response.text
            else:
                logger.warning("⚠️ Empty response received from Gemini API")
                return ""
                
        except Exception as e:
            logger.error(f"❌ Gemini API call failed: {e}")
            logger.debug(f"🔍 Error type: {type(e).__name__}")
            raise

    def parse_detections(self, response_text: str) -> List[Detection]:
        """
        Parse and validate object detections from Gemini response using Pydantic.

        Args:
            response_text: Raw response from Gemini.

        Returns:
            A list of validated Detection objects.
        """
        logger.info("🔍 Starting detection parsing and validation")
        logger.debug(f"📄 Input response length: {len(response_text)}")
        
        if not response_text.strip():
            logger.warning("⚠️ Empty response text provided for parsing")
            return []
        
        # Clean the response to extract only the JSON part
        logger.debug("🧹 Searching for JSON content in response")
        json_match = re.search(r'```(?:json)?\n([\s\S]*?)\n```|(\[[\s\S]*\])', response_text)
        
        if not json_match:
            logger.error("❌ No valid JSON block or array found in the response")
            logger.debug("📋 Raw response for debugging:")
            logger.debug(response_text)
            return []

        # Prioritize the first non-empty group
        json_str = next((group for group in json_match.groups() if group is not None), None)
        
        if not json_str:
            logger.error("❌ Could not extract JSON string from the response")
            return []
        
        logger.debug(f"📦 Extracted JSON string: {json_str[:200]}...")
        logger.debug("🔧 Attempting Pydantic validation")

        try:
            # Use Pydantic to parse and validate the JSON at the same time
            validated_response = DetectionResponse.model_validate_json(json_str)
            detections = validated_response.root
            
            logger.success(f"✅ Successfully parsed and validated {len(detections)} detections")
            
            # Log detection details
            for i, detection in enumerate(detections):
                logger.debug(f"🎯 Detection {i+1}: {detection.label} at {detection.box_2d}")
            
            return detections
            
        except ValidationError as e:
            logger.error(f"❌ Pydantic validation failed: {e}")
            logger.debug("📋 Raw JSON string that failed validation:")
            logger.debug(json_str)
            return []
        except json.JSONDecodeError as e:
            logger.error(f"❌ Failed to decode JSON: {e}")
            logger.debug("📋 Raw JSON string that failed decoding:")
            logger.debug(json_str)
            return []

    def draw_detections(self, image: Image.Image, detections: List[Detection],
                       box_color: str = "red", text_color: str = "white",
                       box_width: int = 3) -> Image.Image:
        """
        Draw bounding boxes and labels on image.

        Args:
            image: PIL Image to draw on.
            detections: List of validated Detection objects.
            box_color: Color for bounding boxes.
            text_color: Color for text labels.
            box_width: Width of bounding box lines.

        Returns:
            Image with drawn detections.
        """
        start_time = time.time()
        logger.info(f"🎨 Starting to draw {len(detections)} detections on image")
        logger.debug(f"🖼️ Image size: {image.size}")
        logger.debug(f"🎨 Drawing parameters - box_color: {box_color}, text_color: {text_color}, box_width: {box_width}")
        
        if not detections:
            logger.warning("⚠️ No detections provided for drawing")
            return image
        
        image_copy = image.copy()
        draw = ImageDraw.Draw(image_copy)
        w, h = image_copy.size
        
        logger.debug("🔤 Loading font for text rendering")
        try:
            font = ImageFont.truetype("arial.ttf", size=20)
            logger.debug("✅ Successfully loaded arial.ttf font")
        except IOError:
            font = ImageFont.load_default()
            logger.debug("⚠️ Fallback to default font (arial.ttf not found)")

        successful_drawings = 0
        
        for i, detection in enumerate(detections):
            logger.debug(f"🎯 Drawing detection {i+1}/{len(detections)}: {detection.label}")
            
            try:
                # Access data via model attributes
                box = detection.box_2d
                label = detection.label

                ymin, xmin, ymax, xmax = box[0], box[1], box[2], box[3]
                logger.debug(f"📦 Normalized coordinates: ymin={ymin}, xmin={xmin}, ymax={ymax}, xmax={xmax}")
                
                # Convert normalized coords (0-1000) to pixel coords
                pixel_box = [
                    int(xmin / 1000 * w), int(ymin / 1000 * h),
                    int(xmax / 1000 * w), int(ymax / 1000 * h)
                ]
                logger.debug(f"📏 Pixel coordinates: {pixel_box}")
                
                # Validate pixel coordinates
                if (pixel_box[0] >= pixel_box[2] or pixel_box[1] >= pixel_box[3] or 
                    any(coord < 0 for coord in pixel_box) or
                    pixel_box[2] > w or pixel_box[3] > h):
                    logger.warning(f"⚠️ Invalid bounding box for {label}: {pixel_box}")
                    continue
                
                # Draw bounding box
                draw.rectangle(pixel_box, outline=box_color, width=box_width)
                logger.debug(f"📦 Drew bounding box for {label}")
                
                # Draw label background and text
                text_bbox = draw.textbbox((pixel_box[0], pixel_box[1]), label, font=font)
                text_height = text_bbox[3] - text_bbox[1]
                text_width = text_bbox[2] - text_bbox[0]
                
                # Background rectangle for text
                background_coords = [
                    (pixel_box[0], pixel_box[1] - text_height - 4), 
                    (pixel_box[0] + text_width + 4, pixel_box[1])
                ]
                draw.rectangle(background_coords, fill=box_color)
                
                # Text
                draw.text((pixel_box[0] + 2, pixel_box[1] - text_height - 2), 
                         label, fill=text_color, font=font)
                
                logger.debug(f"📝 Drew label '{label}' for detection {i+1}")
                successful_drawings += 1
                
            except Exception as e:
                logger.error(f"❌ Error drawing detection {i+1} ({detection.label}): {e}")
                continue

        draw_time = time.time() - start_time
        logger.success(f"✅ Successfully drew {successful_drawings}/{len(detections)} detections in {draw_time:.2f}s")
        
        if successful_drawings != len(detections):
            logger.warning(f"⚠️ {len(detections) - successful_drawings} detections failed to draw")

        return image_copy
    
    def process_image(self, image_source: Union[str, bytes],
                     custom_prompt: Optional[str] = None,
                     show_result: bool = True,
                     save_path: Optional[str] = None) -> Tuple[Image.Image, List[Detection]]:
        """
        Complete pipeline: load image, detect objects, validate, draw results.

        Args:
            image_source: URL, file path, or image bytes.
            custom_prompt: Optional custom detection prompt.
            show_result: Whether to display the result using matplotlib.
            save_path: Optional path to save the result image.

        Returns:
            Tuple of (processed image, list of validated Detection objects).
        """
        pipeline_start = time.time()
        logger.info("🚀 Starting complete image processing pipeline")
        
        try:
            # Step 1: Load image
            logger.info("🔄 Step 1/4: Loading image...")
            image_part, pil_image = self.load_image(image_source)

            # Step 2: Detect objects
            logger.info("🔄 Step 2/4: Detecting objects...")
            response_text = self.detect_objects(image_part, custom_prompt)

            # Step 3: Parse and validate
            logger.info("🔄 Step 3/4: Parsing and validating detections...")
            detections = self.parse_detections(response_text)

            if not detections:
                logger.warning("⚠️ No valid objects detected!")
                return pil_image, []

            # Step 4: Draw results
            logger.info("🔄 Step 4/4: Drawing bounding boxes...")
            result_image = self.draw_detections(pil_image, detections)

            # Save results if requested
            if save_path:
                logger.info(f"💾 Saving result to {save_path}")
                try:
                    result_image.save(save_path)
                    logger.success(f"✅ Successfully saved result to {save_path}")
                except Exception as e:
                    logger.error(f"❌ Failed to save result: {e}")

            # Display results if requested
            if show_result:
                logger.info("🖼️ Displaying result using matplotlib")
                try:
                    plt.figure(figsize=(12, 8))
                    plt.imshow(result_image)
                    plt.axis('off')
                    plt.title(f"Detected {len(detections)} objects")
                    plt.show()
                    logger.debug("✅ Successfully displayed result")
                except Exception as e:
                    logger.error(f"❌ Failed to display result: {e}")

            # Log final summary
            pipeline_time = time.time() - pipeline_start
            logger.success(f"🎉 Pipeline completed successfully in {pipeline_time:.2f}s")
            logger.info(f"📊 Detection Summary:")
            logger.info(f"   Total objects detected: {len(detections)}")
            
            for i, detection in enumerate(detections, 1):
                logger.info(f"   {i}. {detection.label}")

            return result_image, detections
            
        except Exception as e:
            pipeline_time = time.time() - pipeline_start
            logger.critical(f"❌ Pipeline failed after {pipeline_time:.2f}s: {e}")
            raise
    
    def batch_process(self, image_sources: List[Union[str, bytes]],
                     output_dir: str = "results") -> List[Tuple[Optional[Image.Image], List[Detection]]]:
        """
        Process multiple images in batch.

        Args:
            image_sources: List of image sources (URLs, paths, or bytes).
            output_dir: Directory to save results.

        Returns:
            List of (processed image, detections list) tuples.
        """
        batch_start = time.time()
        logger.info(f"🚀 Starting batch processing of {len(image_sources)} images")
        logger.info(f"📁 Output directory: {output_dir}")
        
        # Create output directory
        try:
            os.makedirs(output_dir, exist_ok=True)
            logger.debug(f"✅ Created/verified output directory: {output_dir}")
        except Exception as e:
            logger.error(f"❌ Failed to create output directory: {e}")
            raise
        
        results = []
        successful_processes = 0
        
        for i, image_source in enumerate(image_sources):
            image_start = time.time()
            logger.info(f"🔄 Processing image {i+1}/{len(image_sources)}")
            logger.debug(f"📋 Current image source type: {type(image_source)}")
            
            try:
                # Generate appropriate filename
                filename = f"result_{i+1}.jpg"
                if isinstance(image_source, str) and not image_source.startswith('http'):
                    base_name = os.path.basename(image_source)
                    filename = f"result_{os.path.splitext(base_name)[0]}.jpg"
                
                save_path = os.path.join(output_dir, filename)
                logger.debug(f"💾 Will save to: {save_path}")
                
                result = self.process_image(image_source, show_result=False, save_path=save_path)
                results.append(result)
                successful_processes += 1
                
                image_time = time.time() - image_start
                logger.success(f"✅ Successfully processed image {i+1} in {image_time:.2f}s")
                
            except Exception as e:
                image_time = time.time() - image_start
                logger.error(f"❌ Error processing image {i+1} after {image_time:.2f}s: {e}")
                logger.debug(f"🔍 Error details: {type(e).__name__}: {str(e)}")
                results.append((None, []))

        batch_time = time.time() - batch_start
        
        # Final batch summary
        logger.info(f"📊 Batch Processing Summary:")
        logger.info(f"   Total images: {len(image_sources)}")
        logger.info(f"   Successful: {successful_processes}")
        logger.info(f"   Failed: {len(image_sources) - successful_processes}")
        logger.info(f"   Total time: {batch_time:.2f}s")
        logger.info(f"   Average time per image: {batch_time/len(image_sources):.2f}s")
        
        if successful_processes == len(image_sources):
            logger.success("🎉 All images processed successfully!")
        elif successful_processes > 0:
            logger.warning(f"⚠️ Partial success: {successful_processes}/{len(image_sources)} images processed")
        else:
            logger.critical("❌ All image processing failed!")

        return results


def get_detection_agent():
    """Get or create the object detection agent instance."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable must be set")
    return ObjectDetectionAgent(api_key)

@tool
def detect_objects_in_image(image_path: str, custom_prompt: Optional[str] = None) -> Dict[str, Any]:
    """
    Detect objects in an image using Google's Gemini Vision API.
    
    Args:
        image_path: Path to the image file or URL to analyze
        custom_prompt: Optional custom prompt for specific detection requirements
        
    Returns:
        Dictionary containing detection results with object labels and bounding boxes
    """
    try:
        agent = get_detection_agent()
        result_image, detections = agent.process_image(
            image_path, 
            custom_prompt=custom_prompt,
            show_result=False,
            save_path=None
        )
        
        # Convert detections to serializable format
        detection_results = []
        for detection in detections:
            detection_results.append({
                "label": detection.label,
                "bounding_box": detection.box_2d,
                "coordinates": {
                    "ymin": detection.box_2d[0],
                    "xmin": detection.box_2d[1], 
                    "ymax": detection.box_2d[2],
                    "xmax": detection.box_2d[3]
                }
            })
        
        return {
            "success": True,
            "total_objects": len(detection_results),
            "detections": detection_results,
            "message": f"Successfully detected {len(detection_results)} objects in the image"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to detect objects: {str(e)}"
        }

@tool
def detect_construction_safety_equipment(image_path: str) -> Dict[str, Any]:
    """
    Specialized tool for detecting construction safety equipment and workers.
    
    Args:
        image_path: Path to construction site image file or URL
        
    Returns:
        Dictionary with safety equipment detection results
    """
    construction_prompt = """
    Analyze this construction site image. Detect all people and safety equipment.
    Specifically look for:
    - workers (label as 'worker')
    - hard hats (label as 'hard_hat')
    - safety vests (label as 'safety_vest')
    - construction equipment (label as 'equipment')
    - vehicles (label as 'vehicle')

    Return ONLY a valid JSON array. Each object must have "box_2d" and "label".
    Example format: [{"box_2d": [y1, x1, y2, x2], "label": "worker"}]
    """
    
    try:
        agent = get_detection_agent()
        result_image, detections = agent.process_image(
            image_path,
            custom_prompt=construction_prompt,
            show_result=False,
            save_path=None
        )
        
        # Categorize detections by safety equipment
        safety_summary = {
            "workers": 0,
            "hard_hats": 0,
            "safety_vests": 0,
            "equipment": 0,
            "vehicles": 0,
            "other": 0
        }
        
        detection_results = []
        for detection in detections:
            detection_data = {
                "label": detection.label,
                "bounding_box": detection.box_2d
            }
            detection_results.append(detection_data)
            
            # Count by category
            label_lower = detection.label.lower()
            if "worker" in label_lower:
                safety_summary["workers"] += 1
            elif "hard_hat" in label_lower or "helmet" in label_lower:
                safety_summary["hard_hats"] += 1
            elif "safety_vest" in label_lower or "vest" in label_lower:
                safety_summary["safety_vests"] += 1
            elif "equipment" in label_lower:
                safety_summary["equipment"] += 1
            elif "vehicle" in label_lower:
                safety_summary["vehicles"] += 1
            else:
                safety_summary["other"] += 1
        
        return {
            "success": True,
            "total_objects": len(detection_results),
            "safety_summary": safety_summary,
            "detections": detection_results,
            "safety_compliance": {
                "workers_with_potential_safety_gear": safety_summary["hard_hats"] + safety_summary["safety_vests"],
                "total_workers": safety_summary["workers"]
            },
            "message": f"Detected {len(detection_results)} objects including {safety_summary['workers']} workers"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Failed to analyze construction safety: {str(e)}"
        }

@tool
def batch_detect_objects(image_paths: List[str], output_directory: str = "construction_safety_analysis") -> Dict[str, Any]:
    """
    Process multiple images for object detection in batch.
    
    Args:
        image_paths: List of image file paths or URLs to process
        output_directory: Directory to save processed images with bounding boxes
        
    Returns:
        Dictionary with batch processing results
    """
    try:
        agent = get_detection_agent()
        results = agent.batch_process(image_paths, output_dir=output_directory)
        
        batch_summary = {
            "total_images": len(image_paths),
            "successful_processes": 0,
            "failed_processes": 0,
            "total_objects_detected": 0,
            "results_per_image": []
        }
        
        for i, (result_image, detections) in enumerate(results):
            if result_image is not None:
                batch_summary["successful_processes"] += 1
                batch_summary["total_objects_detected"] += len(detections)
                
                image_result = {
                    "image_index": i,
                    "image_path": image_paths[i],
                    "objects_detected": len(detections),
                    "detections": [{"label": d.label, "bounding_box": d.box_2d} for d in detections]
                }
            else:
                batch_summary["failed_processes"] += 1
                image_result = {
                    "image_index": i,
                    "image_path": image_paths[i],
                    "objects_detected": 0,
                    "error": "Processing failed"
                }
            
            batch_summary["results_per_image"].append(image_result)
        
        return {
            "success": True,
            "batch_summary": batch_summary,
            "output_directory": output_directory,
            "message": f"Processed {batch_summary['successful_processes']}/{batch_summary['total_images']} images successfully"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Batch processing failed: {str(e)}"
        }

@tool
def analyze_image_with_custom_prompt(image_path: str, analysis_prompt: str) -> Dict[str, Any]:
    """
    Analyze an image with a completely custom prompt for specific detection needs.
    
    Args:
        image_path: Path to image file or URL
        analysis_prompt: Custom prompt describing what to detect and how to format the response
        
    Returns:
        Dictionary with custom analysis results
    """
    try:
        agent = get_detection_agent()
        if save_path is None:
            import os
            base_name = os.path.basename(image_path).split('.')[0] if isinstance(image_path, str) else "construction_analysis"
            save_path = f"{base_name}_safety_analysis.jpg"
        
        result_image, detections = agent.process_image(
            image_path,
            custom_prompt=analysis_prompt,
            show_result=False,
            save_path=save_path
        )
        
        detection_results = []
        for detection in detections:
            detection_results.append({
                "label": detection.label,
                "bounding_box": detection.box_2d
            })
        
        return {
            "success": True,
            "custom_prompt_used": analysis_prompt,
            "total_objects": len(detection_results),
            "detections": detection_results,
            "message": f"Custom analysis completed, found {len(detection_results)} objects"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Custom analysis failed: {str(e)}"
        }

# List of all available tools for easy import
DETECTION_TOOLS = [
    detect_objects_in_image,
    detect_construction_safety_equipment, 
    batch_detect_objects,
    analyze_image_with_custom_prompt
]


def create_detection_agent():
    """
    Create a LangGraph agent with object detection capabilities.
    
    Make sure to set these environment variables:
    - GOOGLE_API_KEY: For Gemini Vision API
    - ANTHROPIC_API_KEY: For Claude model
    """
    
    # Initialize the language model
    model = ChatGoogleGenerativeAI(
        model = "gemini-2.5-pro",
        api_key = os.getenv("GOOGLE_API_KEY")
    )
    
    # Create the agent with detection tools
    agent = create_react_agent(
        model=model,
        tools=DETECTION_TOOLS,
        prompt="""You are an AI assistant specialized in computer vision and object detection.
        
        You have access to powerful object detection tools that can:
        1. Detect general objects in any image
        2. Analyze construction sites for safety equipment
        3. Process multiple images in batch
        4. Perform custom analysis with specific prompts
        
        When users ask about analyzing images, use the appropriate detection tool.
        Always provide clear, detailed responses about what was detected and where.
        
        For construction sites, pay special attention to safety compliance.
        For general images, describe all detected objects and their locations.
        """
    )
    
    return agent

def main():
    """Example usage of the detection agent for a medical imaging task."""
    
    # Check required environment variables
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        logger.critical("❌ GOOGLE_API_KEY environment variable not set!")
        return

    # 1. Create an instance of your object detection logic
    try:
        detection_service = ObjectDetectionAgent(api_key=api_key)
        logger.info("✅ Object Detection service initialized.")
    except Exception as e:
        logger.error(f"🔥 Failed to initialize the detection service: {e}")
        return

    # 2. Define the image and the new custom radiology prompt
    image_path = r"C:\\Users\\Raghu\\Downloads\\Incidence_response_agent\\Computer_Vision_Agent\\assets\\Construction-workers.jpg"
    output_dir = "batch_results"
    
    # A robust, specific prompt for the radiology task
    custom_radiology_prompt = """
    You are a highly-efficient and accurate computer vision AI. Your sole purpose is to analyze an image, identify all distinct and prominent objects, and return their locations and labels in a structured format.

**Your Goal:**
Detect all significant objects in the provided image. For objects that are part of a group (e.g., a crowd of people, a fleet of cars), identify the most distinct instances.

**Output Requirements (Strictly Enforced):**
For each object you detect, you MUST provide:
1.  `box_2d`: A bounding box in the precise format `[ymin, xmin, ymax, xmax]`, with coordinates normalized to a 0-1000 scale.
2.  `label`: A common, descriptive, lowercase name for the object (e.g., 'car', 'person', 'tree', 'building').

**CRITICAL INSTRUCTION:**
Your entire response MUST be ONLY a valid JSON array of detection objects.
- Do NOT include any introductory text, explanations, summaries, markdown code fences (like ```json), or any text whatsoever outside of the JSON array.
- Your response must begin with `[` and end with `]`.
- If no objects are confidently detected, you MUST return an empty array: `[]`.

**Example of a valid response for an image containing a person and a bicycle:**
[
    {"box_2d":, "label": "person"},
    {"box_2d":, "label": "bicycle"}
]
    """

    # 3. Call the processing method directly
    print(f"🔍 Analyzing image '{os.path.basename(image_path)}'...")
    
    try:
        # Define where to save the output image
        output_filename = f"detected_{os.path.basename(image_path)}"
        save_path = os.path.join(output_dir, output_filename)
        
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Call your reliable Python code directly
        result_image, detections = detection_service.process_image(
            image_source=image_path,
            custom_prompt=custom_radiology_prompt,
            show_result=True,
            save_path=save_path
        )

        if detections:
            print(f"✅ Analysis complete. Found {len(detections)} potential anomalies. Result saved to '{save_path}'")
        else:
            print(f"⚠️ Analysis complete, but no valid anomalies were detected or returned by the model.")

    except Exception as e:
        print(f"❌ An error occurred during image processing: {e}")


if __name__ == "__main__":
    main()