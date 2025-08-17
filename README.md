# Computer Vision Object Detection Agent

A powerful Python-based object detection system leveraging Google's Gemini 2.5 Pro Vision API for comprehensive image analysis. This agent provides general object detection, specialized construction safety analysis, and batch processing capabilities with robust validation and logging.

## 🚀 Features

- **General Object Detection**: Detect and label objects in any image with bounding boxes
- **Construction Safety Analysis**: Specialized detection for safety equipment, workers, and compliance monitoring
- **Batch Processing**: Process multiple images simultaneously with organized output
- **Custom Analysis**: Use custom prompts for specific detection requirements
- **Robust Validation**: Pydantic models ensure data integrity and type safety
- **Comprehensive Logging**: Detailed logging with loguru for debugging and monitoring
- **Multiple Input Sources**: Support for URLs, file paths, and byte data
- **LangChain Integration**: Ready-to-use tools for AI agent workflows

## 📋 Requirements

- Python 3.8+
- Google API Key with Gemini API access
- Required Python packages (see Installation)

## 🛠️ Installation

1. **Clone or download the detection script**

2. **Install required dependencies:**
\`\`\`bash
pip install google-generativeai pydantic loguru matplotlib pillow requests python-dotenv langchain-google-genai langgraph langchain-core
\`\`\`

3. **Set up environment variables:**
Create a `.env` file in your project directory:
\`\`\`env
GOOGLE_API_KEY=your_google_api_key_here
\`\`\`

## 🎯 Quick Start

### Basic Object Detection

```python
from detection import ObjectDetectionAgent
import os

# Initialize the agent
api_key = os.getenv("GOOGLE_API_KEY")
agent = ObjectDetectionAgent(api_key)

# Detect objects in an image
result_image, detections = agent.process_image(
    "path/to/your/image.jpg",
    show_result=True,
    save_path="result.jpg"
)

# Print detected objects
for detection in detections:
    print(f"Found: {detection.label} at {detection.box_2d}")
