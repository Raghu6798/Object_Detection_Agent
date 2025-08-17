Directory structure:
└── microsoft-poml/
    ├── README.md
    ├── AGENTS.md
    ├── azure-pipelines.yml
    ├── bump-version.js
    ├── CODE_OF_CONDUCT.md
    ├── jest.config.js
    ├── language-configuration.json
    ├── LICENSE
    ├── mkdocs.yml
    ├── package.json
    ├── poml.tmLanguage.json
    ├── pyproject.toml
    ├── RAI_README.md
    ├── SECURITY.md
    ├── SUPPORT.md
    ├── tsconfig.json
    ├── typedoc.json
    ├── vscodeignore.js
    ├── webpack.config.cli.js
    ├── webpack.config.extension.js
    ├── webpack.config.webview.js
    ├── .env.azure-pipelines
    ├── .eslintrc.js
    ├── .npmrc
    ├── .prettierrc
    ├── .vscode-test.mjs
    ├── .vscodeignore
    ├── docs/
    │   ├── index.md
    │   ├── language/
    │   │   ├── components.md
    │   │   ├── ir.md
    │   │   ├── meta.md
    │   │   ├── quickstart.md
    │   │   ├── standalone.md
    │   │   └── proposals/
    │   │       └── poml_extended.md
    │   ├── python/
    │   │   ├── core.md
    │   │   ├── index.md
    │   │   └── integration.md
    │   ├── typescript/
    │   │   └── index.md
    │   └── vscode/
    │       ├── configuration.md
    │       ├── features.md
    │       └── index.md
    ├── examples/
    │   ├── README.md
    │   ├── 101_explain_character.poml
    │   ├── 102_render_xml.poml
    │   ├── 103_word_todos.poml
    │   ├── 104_financial_analysis.poml
    │   ├── 105_write_blog_post.poml
    │   ├── 106_research.poml
    │   ├── 107_read_report_pdf.poml
    │   ├── 201_orders_qa.poml
    │   ├── 202_arc_agi.poml
    │   ├── 301_generate_poml.poml
    │   ├── _generate_expects.py
    │   ├── assets/
    │   │   ├── 101_tom_and_jerry.docx
    │   │   ├── 101_tom_introduction.txt
    │   │   ├── 104_mag7.xlsx
    │   │   ├── 201_order_instructions.json
    │   │   ├── 201_orderlines.csv
    │   │   ├── 201_orders.csv
    │   │   └── 202_arc_agi_data.json
    │   └── expects/
    │       ├── 101_explain_character.txt
    │       ├── 102_render_xml.txt
    │       ├── 103_word_todos.txt
    │       ├── 104_financial_analysis.txt
    │       ├── 105_write_blog_post.txt
    │       ├── 106_research.txt
    │       ├── 107_read_report_pdf.txt
    │       ├── 201_orders_qa.txt
    │       ├── 202_arc_agi.txt
    │       └── 301_generate_poml.txt
    ├── gallery/
    │   ├── ask.poml
    │   ├── chat.poml
    │   ├── edit.poml
    │   ├── latex_edit.poml
    │   ├── latex_write.poml
    │   ├── pdf_understanding.poml
    │   ├── table_understanding.poml
    │   └── word_understanding.poml
    ├── media/
    │   └── style.css
    ├── packages/
    │   ├── poml/
    │   │   ├── base.tsx
    │   │   ├── cli.ts
    │   │   ├── essentials.tsx
    │   │   ├── file.tsx
    │   │   ├── index.ts
    │   │   ├── presentation.tsx
    │   │   ├── version.ts
    │   │   ├── components/
    │   │   │   ├── document.tsx
    │   │   │   ├── index.ts
    │   │   │   ├── instructions.tsx
    │   │   │   ├── message.tsx
    │   │   │   ├── table.tsx
    │   │   │   ├── tree.tsx
    │   │   │   ├── utils.tsx
    │   │   │   └── webpage.tsx
    │   │   ├── reader/
    │   │   │   ├── base.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── meta.ts
    │   │   │   ├── poml.tsx
    │   │   │   ├── segment.ts
    │   │   │   └── text.tsx
    │   │   ├── tests/
    │   │   │   ├── base.test.tsx
    │   │   │   ├── components.test.tsx
    │   │   │   ├── essentials.test.tsx
    │   │   │   ├── file.test.tsx
    │   │   │   ├── index.test.tsx
    │   │   │   ├── instructions.test.tsx
    │   │   │   ├── meta.test.tsx
    │   │   │   ├── presentation.test.tsx
    │   │   │   ├── schema.test.ts
    │   │   │   ├── table.test.tsx
    │   │   │   ├── tokenCounterImage.test.ts
    │   │   │   ├── trace.test.tsx
    │   │   │   ├── util.test.tsx
    │   │   │   ├── writer.test.tsx
    │   │   │   └── assets/
    │   │   │       ├── galleryTest.json
    │   │   │       ├── includeChild.poml
    │   │   │       ├── includeNested.poml
    │   │   │       ├── includeNumber.poml
    │   │   │       ├── peopleList.json
    │   │   │       ├── sampleWebpage.html
    │   │   │       ├── sampleWord.docx
    │   │   │       ├── wikitqSampleData.csv
    │   │   │       ├── wikitqSampleData.xlsx
    │   │   │       └── directory/
    │   │   │           ├── .ignoremeplease
    │   │   │           ├── anotherdirectory/
    │   │   │           │   ├── 123.jsx
    │   │   │           │   └── 456.cpp
    │   │   │           └── nested1/
    │   │   │               └── nested2/
    │   │   │                   ├── nested3/
    │   │   │                   │   └── nested5/
    │   │   │                   │       └── nestedFile.txt
    │   │   │                   └── nested4/
    │   │   │                       └── .ignoreplease
    │   │   └── util/
    │   │       ├── audio.ts
    │   │       ├── fs.ts
    │   │       ├── image.ts
    │   │       ├── index.ts
    │   │       ├── pdf.ts
    │   │       ├── reactRender.ts
    │   │       ├── schema.ts
    │   │       ├── tokenCounterImage.ts
    │   │       ├── trace.ts
    │   │       ├── xmlContentAssist.d.ts
    │   │       └── xmlContentAssist.js
    │   ├── poml-build/
    │   │   ├── package.json
    │   │   ├── rollup.config.js
    │   │   └── tsconfig.json
    │   ├── poml-vscode/
    │   │   ├── extension.ts
    │   │   ├── settings.ts
    │   │   ├── chat/
    │   │   │   ├── gallery.ts
    │   │   │   └── participant.ts
    │   │   ├── command/
    │   │   │   ├── addResources.ts
    │   │   │   ├── index.ts
    │   │   │   ├── promptGallery.ts
    │   │   │   ├── showPreview.ts
    │   │   │   ├── showSource.ts
    │   │   │   ├── telemetry.ts
    │   │   │   └── testCommand.ts
    │   │   ├── lsp/
    │   │   │   ├── documentFormatter.ts
    │   │   │   ├── parseComments.ts
    │   │   │   └── server.ts
    │   │   ├── panel/
    │   │   │   ├── content.tsx
    │   │   │   ├── manager.ts
    │   │   │   ├── panel.ts
    │   │   │   └── types.ts
    │   │   ├── test-fixtures/
    │   │   │   ├── badInclude.poml
    │   │   │   ├── badSyntax.poml
    │   │   │   ├── badSyntaxLsp.poml
    │   │   │   ├── includeMain.poml
    │   │   │   └── test.poml
    │   │   ├── tests/
    │   │   │   ├── commands.test.ts
    │   │   │   ├── diagnosticsDuplicate.test.ts
    │   │   │   ├── extension.test.ts
    │   │   │   ├── includeDiagnostics.test.ts
    │   │   │   ├── lsp.test.ts
    │   │   │   ├── panelAutoAdd.test.ts
    │   │   │   ├── panelContent.test.ts
    │   │   │   ├── panelContentMapping.test.ts
    │   │   │   └── preview.test.ts
    │   │   └── util/
    │   │       ├── commandManager.ts
    │   │       ├── dispose.ts
    │   │       ├── file.ts
    │   │       ├── logger.ts
    │   │       ├── telemetryClient.ts
    │   │       ├── telemetryServer.ts
    │   │       └── topmostLineMonitor.ts
    │   └── poml-vscode-webview/
    │       ├── index.ts
    │       ├── scrollSync.ts
    │       ├── state.ts
    │       ├── toolbar.ts
    │       ├── util.ts
    │       └── tests/
    │           ├── jumpToSource.test.ts
    │           ├── messageCopy.test.ts
    │           ├── toolbar.test.ts
    │           └── util.test.ts
    ├── python/
    │   ├── poml/
    │   │   ├── __init__.py
    │   │   ├── __main__.py
    │   │   ├── _version.py
    │   │   ├── api.py
    │   │   ├── cli.py
    │   │   ├── prompt.py
    │   │   └── integration/
    │   │       ├── __init__.py
    │   │       ├── agentops.py
    │   │       ├── langchain.py
    │   │       ├── mlflow.py
    │   │       └── weave.py
    │   └── tests/
    │       ├── test_basic.py
    │       ├── test_examples.py
    │       ├── test_poml_formats.py
    │       └── manual/
    │           ├── example_agentops_original.py
    │           ├── example_agentops_poml.py
    │           ├── example_mlflow_langchain_poml.py
    │           ├── example_mlflow_original.py
    │           ├── example_mlflow_poml.py
    │           ├── example_poml.poml
    │           ├── example_weave_original.py
    │           └── example_weave_poml.py
    └── .github/
        └── workflows/
            ├── check-version.yml
            ├── docs.yml
            ├── models.yml
            ├── publish-npm.yml
            ├── publish-pypi.yml
            ├── publish-vscode.yml
            ├── publish.yml
            └── test.yml


Files Content:

================================================
FILE: README.md
================================================
# POML: Prompt Orchestration Markup Language

[![Documentation](https://img.shields.io/badge/docs-microsoft.github.io-blue)](https://microsoft.github.io/poml/)
[![VSCode Extension](https://img.shields.io/visual-studio-marketplace/v/poml-team.poml)](https://marketplace.visualstudio.com/items?itemName=poml-team.poml)
[![PyPI](https://img.shields.io/pypi/v/poml)](https://pypi.org/project/poml/)
[![npm (latest)](https://img.shields.io/npm/v/pomljs)](https://www.npmjs.com/package/pomljs)
[![Test Status](https://github.com/microsoft/poml/actions/workflows/test.yml/badge.svg)](https://github.com/microsoft/poml/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/FhMCqWzAn6)

**POML (Prompt Orchestration Markup Language)** is a novel markup language designed to bring structure, maintainability, and versatility to advanced prompt engineering for Large Language Models (LLMs). It addresses common challenges in prompt development, such as lack of structure, complex data integration, format sensitivity, and inadequate tooling. POML provides a systematic way to organize prompt components, integrate diverse data types seamlessly, and manage presentation variations, empowering developers to create more sophisticated and reliable LLM applications.

## Demo Video

[![The 5-minute guide to POML](https://i3.ytimg.com/vi/b9WDcFsKixo/maxresdefault.jpg)](https://youtu.be/b9WDcFsKixo)

## Key Features

* **Structured Prompting Markup**: Employs an HTML-like syntax with semantic components such as `<role>`, `<task>`, and `<example>` to encourage modular design, enhancing prompt readability, reusability, and maintainability.
* **Comprehensive Data Handling**: Incorporates specialized data components (e.g., `<document>`, `<table>`, `<img>`) that seamlessly embed or reference external data sources like text files, spreadsheets, and images, with customizable formatting options.
* **Decoupled Presentation Styling**: Features a CSS-like styling system that separates content from presentation. This allows developers to modify styling (e.g., verbosity, syntax format) via `<stylesheet>` definitions or inline attributes without altering core prompt logic, mitigating LLM format sensitivity.
* **Integrated Templating Engine**: Includes a built-in templating engine with support for variables (`{{ }}`), loops (`for`), conditionals (`if`), and variable definitions (`<let>`) for dynamically generating complex, data-driven prompts.
* **Rich Development Toolkit**:
    * **IDE Extension (Visual Studio Code)**: Provides essential development aids like syntax highlighting, context-aware auto-completion, hover documentation, real-time previews, inline diagnostics for error checking, and integrated interactive testing.
    * **Software Development Kits (SDKs)**: Offers SDKs for Node.js (JavaScript/TypeScript) and Python for seamless integration into various application workflows and popular LLM frameworks.

## Quick Start

Here's a very simple POML example. Please put it in a file named `example.poml`. Make sure it resides in the same directory as the `photosynthesis_diagram.png` image file.

```xml
<poml>
  <role>You are a patient teacher explaining concepts to a 10-year-old.</role>
  <task>Explain the concept of photosynthesis using the provided image as a reference.</task>

  <img src="photosynthesis_diagram.png" alt="Diagram of photosynthesis" />

  <output-format>
    Keep the explanation simple, engaging, and under 100 words.
    Start with "Hey there, future scientist!".
  </output-format>
</poml>
```

This example defines a role and task for the LLM, includes an image for context, and specifies the desired output format. With the POML toolkit, the prompt can be easily rendered with a flexible format, and tested with a vision LLM.

## Installation

### Visual Studio Code Extension

Install from [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=poml-team.poml).

You can also install the extension manually by downloading the `.vsix` file from our [GitHub releases page](https://github.com/microsoft/poml/releases) and installing it in VS Code via the Extensions view.

Before testing prompts with the POML toolkit, make sure you have configured your preferred LLM model, API key, and endpoint. If these are not set, prompt testing will not work.

**To configure in Visual Studio Code:**
- Open the extension settings (open "Settings" and search for "POML").
- Set your model provider (e.g., OpenAI, Azure, Google), API key, and endpoint URL in the POML section.
- Alternatively, you can add these settings directly to your `settings.json` file.

### Node.js (via npm)

```bash
npm install pomljs
```

### Python (via pip)

```bash
pip install poml
```

For development or local installation, you might use `pip install -e .` from a cloned repository.

**Refer to the [documentation](https://microsoft.github.io/poml) for more details on installing the nightly build.**

## Documentation

For detailed information on POML syntax, components, styling, templating, SDKs, and the VS Code extension, please refer to our [documentation](https://microsoft.github.io/poml).

## Learn More

* **Watch our Demo Video on YouTube:** [POML Introduction & Demo](https://youtu.be/b9WDcFsKixo)
* **Join our Discord community:** Connect with the team and other users on our [Discord server](https://discord.gg/FhMCqWzAn6).
* **Read the Research Paper (coming soon):** For an in-depth understanding of POML's design, implementation, and evaluation, check out our paper: [Paper link TBD](TBD).

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## Responsible AI

This project has been evaluated and certified to comply with the Microsoft Responsible AI Standard. The team will continue to monitor and maintain the repository, addressing any severe issues, including potential harms, if they arise. For more details, refer to the [Responsible AI Readme](RAI_README.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



================================================
FILE: AGENTS.md
================================================
# Agent Contributor Guide

This repository contains a TypeScript/JavaScript project together with a lite Python SDK.
These instructions are for agents like Codex to contribute changes.

## Repository Structure
- **packages/poml** – Core TypeScript package of POML parsing and rendering.
- **packages/poml-vscode** – VS Code Extension package of POML.
- **packages/poml-vscode-webview** – The VS Code Webview frontend JS/TS code.
- **python/** – Python SDK and CLI implementation.
- **examples/** – Sample POML files.
- **docs/** – Project documentation.

## Environment Setup
- **Node.js**: version 22.x (20.x should also work)
- **Python**: version 3.11 (3.10 or 3.12 should also work)

```bash
npm ci
npm run build-webview
npm run build-cli
python -m pip install -e .[dev]
```

## Testing Instructions
After your changes you must verify that everything still builds and tests pass.
Execute the following commands from the repository root:

```bash
npm run build-webview
npm run build-cli
npm run lint
npm test
python -m pytest python/tests
```

If you have updated the VS Code extension, please run the extension tests with:

```bash
xvfb-run -a npm run compile && xvfb-run -a npm run test-vscode
```

Update the component specifications if you have updated the type annotations and documentations of the components.

```bash
npm run generate-component-spec
```

## PR Instructions
Use clear titles and summaries. Include relevant references to documentation when modifying or adding features.



================================================
FILE: azure-pipelines.yml
================================================
trigger: none

pr: none

pool:
  vmImage: 'ubuntu-latest'

variables:
  - name: GITHUB_REPO
    value: 'microsoft/poml'
  # RUN_ID should be set at the queue time.
  # - name: RUN_ID
  #   value: '15574923104'

stages:
- stage: DownloadAndPublish
  displayName: 'Download GitHub Artifacts and Publish to Marketplace'
  jobs:
  - job: PublishVSIX
    displayName: 'Download and Publish VSIX Files'
    steps:
    - task: NodeTool@0
      displayName: 'Use Node.js'
      inputs:
        versionSpec: '22.x'

    - script: |
        npm install -g vsce
      displayName: 'Install VSCE'

    - script: |
        set -e

        # Create artifacts directory
        mkdir -p artifacts
        
        # Get list of artifacts from GitHub Actions run
        echo "Fetching artifacts from GitHub Actions run..."
        artifacts_response=$(curl -s -H "Authorization: token $(GITHUB_PAT)" \
          "https://api.github.com/repos/$(GITHUB_REPO)/actions/runs/$(RUN_ID)/artifacts")
        
        echo "Artifacts response:"
        echo "$artifacts_response" | jq '.'
        
        # Download each artifact
        echo "$artifacts_response" | jq -r '.artifacts[] | .archive_download_url' | while read -r download_url; do
          if [ -n "$download_url" ]; then
            echo "Downloading artifact from: $download_url"
            artifact_name=$(echo "$artifacts_response" | jq -r --arg url "$download_url" '.artifacts[] | select(.archive_download_url == $url) | .name')
            echo "Artifact name: $artifact_name"
            
            curl -L -H "Authorization: token $(GITHUB_PAT)" \
              "$download_url" -o "artifacts/${artifact_name}.zip"
            
            # Extract the zip file
            cd artifacts
            unzip -o "${artifact_name}.zip"
            rm "${artifact_name}.zip"
            cd ..
          fi
        done
        
        echo "Contents of artifacts directory:"
        find artifacts -type f -name "*.vsix" | head -20
      displayName: 'Download GitHub Action Artifacts'
      env:
        GITHUB_PAT: $(GITHUB_PAT)

    - script: |
        set -e

        # Function to parse target from filename
        parse_target() {
          local filename="$1"
          local basename=$(basename "$filename" .vsix)
          
          # Extract platform part from filename like: poml-darwin-arm64-0.0.5.vsix
          if [[ $basename =~ ^[^-]+-([^-]+)-([^-]+)-[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
            local os="${BASH_REMATCH[1]}"
            local arch="${BASH_REMATCH[2]}"
            
            # Map to VS Code marketplace target identifiers
            case "$os-$arch" in
              "darwin-arm64") echo "darwin-arm64" ;;
              "darwin-x64") echo "darwin-x64" ;;
              "linux-arm64") echo "linux-arm64" ;;
              "linux-x64") echo "linux-x64" ;;
              "win32-x64") echo "win32-x64" ;;
              *) echo "universal" ;;
            esac
          else
            echo "universal"
          fi
        }
        
        # Find all VSIX files and publish them
        find artifacts -type f -name "*.vsix" | while read -r vsix_file; do
          echo "Publishing VSIX file: $vsix_file"
          
          # Extract version and name from filename for logging
          filename=$(basename "$vsix_file")
          echo "Processing file: $filename"
          
          # Parse target platform
          target=$(parse_target "$vsix_file")
          echo "Detected target platform: $target"
          
          # Publish to VS Code Marketplace with target
          # Target already set at packaging so it's not needed here
          if [ "$target" = "universal" ]; then
            echo "Publishing as universal package..."
            # echo "vsce publish --packagePath \"$vsix_file\" --pat $(VSCE_PAT)"
            vsce publish --packagePath "$vsix_file" --pat $(VSCE_PAT)
          else
            echo "Publishing with target: $target"
            # echo "vsce publish --packagePath \"$vsix_file\" --target \"$target\" --pat $(VSCE_PAT)"
            # vsce publish --packagePath "$vsix_file" --target "$target" --pat $(VSCE_PAT)
            vsce publish --packagePath "$vsix_file" --pat $(VSCE_PAT)
          fi
          
          if [ $? -eq 0 ]; then
            echo "Successfully published: $filename (target: $target)"
          else
            echo "Failed to publish: $filename (target: $target)"
            exit 1
          fi
        done
        
        # Check if any VSIX files were found
        vsix_count=$(find artifacts -type f -name "*.vsix" | wc -l)
        if [ $vsix_count -eq 0 ]; then
          echo "No VSIX files found in artifacts!"
          exit 1
        else
          echo "Successfully processed $vsix_count VSIX files"
        fi
      displayName: 'Publish VSIX Files to Marketplace'
      env:
        VSCE_PAT: $(VSCE_PAT)



================================================
FILE: bump-version.js
================================================
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function updateNodeJSVersions(baseVersion, timestamp) {
  const version = timestamp ? `${baseVersion}-nightly.${timestamp}` : baseVersion;
  
  // Update root package.json
  const rootPackageJsonPath = path.join(__dirname, 'package.json');
  let rootContent = fs.readFileSync(rootPackageJsonPath, 'utf8');
  rootContent = rootContent.replace(/"version": ".*?"/, `"version": "${version}"`);
  fs.writeFileSync(rootPackageJsonPath, rootContent);
  console.log(`Updated package.json version to: ${version}`);
  
  // Update packages/poml-build/package.json
  const buildPackageJsonPath = path.join(__dirname, 'packages/poml-build/package.json');
  if (fs.existsSync(buildPackageJsonPath)) {
    let buildContent = fs.readFileSync(buildPackageJsonPath, 'utf8');
    buildContent = buildContent.replace(/"version": ".*?"/, `"version": "${version}"`);
    fs.writeFileSync(buildPackageJsonPath, buildContent);
    console.log(`Updated packages/poml-build/package.json version to: ${version}`);
  }
  
  // Update packages/poml/version.ts
  const versionTsPath = path.join(__dirname, 'packages/poml/version.ts');
  if (fs.existsSync(versionTsPath)) {
    let content = fs.readFileSync(versionTsPath, 'utf8');
    content = content.replace(/export const POML_VERSION = ".*"/, `export const POML_VERSION = "${version}"`);
    fs.writeFileSync(versionTsPath, content);
    console.log(`Updated packages/poml/version.ts to: ${version}`);
  }
  
  // Update package-lock.json (both root version and packages."" version)
  const packageLockPath = path.join(__dirname, 'package-lock.json');
  if (fs.existsSync(packageLockPath)) {
    let content = fs.readFileSync(packageLockPath, 'utf8');
    // Update root version
    content = content.replace(/^  "version": ".*?",$/m, `  "version": "${version}",`);
    // Update packages."" version
    content = content.replace(/^      "version": ".*?",$/m, `      "version": "${version}",`);
    fs.writeFileSync(packageLockPath, content);
    console.log(`Updated package-lock.json version to: ${version}`);
  }
}

function updatePythonVersions(baseVersion, timestamp) {
  const version = timestamp ? `${baseVersion}.dev${timestamp}` : baseVersion;
  
  // Update pyproject.toml
  const pyprojectPath = path.join(__dirname, 'pyproject.toml');
  if (fs.existsSync(pyprojectPath)) {
    let content = fs.readFileSync(pyprojectPath, 'utf8');
    content = content.replace(/^version = ".*"$/m, `version = "${version}"`);
    fs.writeFileSync(pyprojectPath, content);
    console.log(`Updated pyproject.toml version to: ${version}`);
  }
  
  // Update python/poml/_version.py
  const versionPath = path.join(__dirname, 'python/poml/_version.py');
  if (fs.existsSync(versionPath)) {
    let content = fs.readFileSync(versionPath, 'utf8');
    content = content.replace(/__version__ = '.*'/, `__version__ = '${version}'`);
    fs.writeFileSync(versionPath, content);
    console.log(`Updated _version.py to: ${version}`);
  }
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.length < 1 || args.length > 3) {
    console.error('Usage: node bump-version.js <base-version> [timestamp] [--python-only|--nodejs-only]');
    console.error('Examples:');
    console.error('  node bump-version.js 0.1.7                    # Update both sides to 0.1.7');
    console.error('  node bump-version.js 0.1.7 202508120345       # Update both with nightly versions');
    console.error('  node bump-version.js 0.1.7 --python-only      # Update only Python side');
    console.error('  node bump-version.js 0.1.7 202508120345 --nodejs-only  # Update only Node.js nightly');
    process.exit(1);
  }
  
  const [baseVersion, timestampOrFlag, modeFlag] = args;
  let timestamp = null;
  let mode = 'both'; // 'both', 'python', 'nodejs'
  
  // Parse arguments
  if (timestampOrFlag) {
    if (timestampOrFlag === '--python-only') {
      mode = 'python';
    } else if (timestampOrFlag === '--nodejs-only') {
      mode = 'nodejs';
    } else if (/^\d{12,14}$/.test(timestampOrFlag)) {
      timestamp = timestampOrFlag;
      if (modeFlag === '--python-only') {
        mode = 'python';
      } else if (modeFlag === '--nodejs-only') {
        mode = 'nodejs';
      }
    } else {
      console.error('Invalid timestamp format. Should be YYYYMMDDHHMM or YYYYMMDDHHMMSS');
      process.exit(1);
    }
  }
  
  try {
    if (mode === 'both' || mode === 'nodejs') {
      updateNodeJSVersions(baseVersion, timestamp);
    }
    
    if (mode === 'both' || mode === 'python') {
      updatePythonVersions(baseVersion, timestamp);
    }
    
    console.log('\nVersion bump completed successfully!');
    if (mode === 'both' || mode === 'nodejs') {
      const jsVersion = timestamp ? `${baseVersion}-nightly.${timestamp}` : baseVersion;
      console.log(`JS version: ${jsVersion}`);
    }
    if (mode === 'both' || mode === 'python') {
      const pythonVersion = timestamp ? `${baseVersion}.dev${timestamp}` : baseVersion;
      console.log(`Python version: ${pythonVersion}`);
    }
  } catch (error) {
    console.error('Error updating versions:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = { updateNodeJSVersions, updatePythonVersions };


================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Microsoft Open Source Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns



================================================
FILE: jest.config.js
================================================
/** @type {import('ts-jest').JestConfigWithTsJest} **/
module.exports = {
  testEnvironment: 'node',
  transform: {
    '^.+.tsx?$': ['ts-jest', {}],
  },
  roots: ['<rootDir>/packages/poml/tests', '<rootDir>/packages/poml-vscode-webview/tests'],
  moduleDirectories: ['node_modules', 'packages'],

  // Handle the PDF parsing worker teardown issue
  forceExit: true,
  detectOpenHandles: true,
  // Increase timeout for async operations like PDF parsing
  testTimeout: 30000
};



================================================
FILE: language-configuration.json
================================================
{
  "comments": {
    "blockComment": ["<!--", "-->"]
  },
  "brackets": [
    ["<!--", "-->"],
    ["<", ">"],
    ["{", "}"],
    ["(", ")"]
  ],
  "autoClosingPairs": [
    { "open": "{", "close": "}" },
    { "open": "[", "close": "]" },
    { "open": "(", "close": ")" },
    { "open": "\"", "close": "\"", "notIn": ["string"] },
    { "open": "'", "close": "'", "notIn": ["string"] },
    { "open": "<!--", "close": "-->", "notIn": ["comment", "string"] }
  ],
  "surroundingPairs": [
    { "open": "'", "close": "'" },
    { "open": "\"", "close": "\"" },
    { "open": "{", "close": "}" },
    { "open": "[", "close": "]" },
    { "open": "(", "close": ")" },
    { "open": "<", "close": ">" }
  ],
  "colorizedBracketPairs": [],
  "folding": {
    "markers": {
      "start": "^\\s*<!--\\s*#region\\b.*-->",
      "end": "^\\s*<!--\\s*#endregion\\b.*-->"
    }
  },
  "wordPattern": {
    "pattern": "(-?\\d*\\.\\d\\w*)|([^\\`\\~\\!\\@\\#\\$\\%\\^\\&\\*\\(\\)\\=\\+\\[\\{\\]\\}\\\\\\|\\;\\:\\'\\\"\\,\\.\\<\\>\\/\\?\\s]+)"
  }
}



================================================
FILE: LICENSE
================================================
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


================================================
FILE: mkdocs.yml
================================================
site_name: POML Documentation
site_url: https://microsoft.github.io/poml
repo_url: https://github.com/microsoft/poml
repo_name: microsoft/poml
edit_uri: edit/main/docs/


theme:
  name: material
  logo: media/logo-64-white.png
  favicon: media/logo-16-purple.png
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - scheme: default
      primary: deep purple
      accent: deep purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: deep purple
      accent: deep purple
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [python]
          options:
            show_source: true
            show_root_heading: true
            show_symbol_type_heading: true
            show_symbol_type_toc: true
            docstring_style: google
            heading_level: 2

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - admonition
  - pymdownx.details
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true

nav:
  - Language:
    - Getting Started: index.md
    - Quick Start: language/quickstart.md
    - Write .poml Files: language/standalone.md
    - Meta: language/meta.md
    - References:
      - Components: language/components.md
    - Deep Dive:
      - IR Specification: language/ir.md
    - Proposals:
      - Extended POML: language/proposals/poml_extended.md
  - Visual Studio Code:
    - Extension Overview: vscode/index.md
    - Features: vscode/features.md
    - Configuration: vscode/configuration.md
  - TypeScript:
    - Overview: typescript/index.md
    - Modules:
      - index: typescript/reference/index.md
      - base: typescript/reference/base.md
      - cli: typescript/reference/cli.md
      - essentials: typescript/reference/essentials.md
      - file: typescript/reference/file.md
      - writer: typescript/reference/writer.md
      - components: typescript/reference/components.md
  - Python:
    - Overview: python/index.md
    - References:
      - Core: python/core.md
      - Integration: python/integration.md

extra:
  version:
    provider: mike
    default: latest


================================================
FILE: package.json
================================================
{
  "name": "poml",
  "publisher": "poml-team",
  "displayName": "POML",
  "description": "Prompt Orchestration Markup Language",
  "repository": {
    "type": "git",
    "url": "https://github.com/microsoft/poml"
  },
  "icon": "media/icon/poml-icon-128.png",
  "version": "0.0.8",
  "engines": {
    "vscode": "^1.95.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [
    "onWebviewPanel:poml.preview",
    "onChatParticipant:poml.runner"
  ],
  "main": "./dist/extension.js",
  "contributes": {
    "viewsContainers": {
      "activitybar": [
        {
          "id": "poml",
          "title": "POML",
          "icon": "./media/icon/poml-icon-16.svg"
        }
      ]
    },
    "views": {
      "poml": [
        {
          "id": "pomlPromptGallery",
          "name": "Prompt Gallery"
        }
      ]
    },
    "languages": [
      {
        "id": "poml",
        "aliases": [
          "POML",
          "poml"
        ],
        "extensions": [
          ".poml"
        ],
        "configuration": "./language-configuration.json",
        "icon": {
          "light": "./media/icon/poml-icon-16.svg",
          "dark": "./media/icon/poml-icon-16.svg"
        }
      }
    ],
    "grammars": [
      {
        "language": "poml",
        "scopeName": "source.poml",
        "path": "./poml.tmLanguage.json"
      }
    ],
    "configurationDefaults": {
      "[poml]": {
        "editor.wordWrap": "on",
        "editor.indentSize": 2
      }
    },
    "commands": [
      {
        "command": "poml.test",
        "title": "Test current prompt on Chat Models",
        "category": "POML",
        "icon": "$(play)"
      },
      {
        "command": "poml.testNonChat",
        "title": "Test current prompt on Text Completion Models",
        "category": "POML",
        "icon": "$(play)"
      },
      {
        "command": "poml.testRerun",
        "title": "Clear output and rerun last test",
        "category": "POML",
        "icon": "$(refresh)"
      },
      {
        "command": "poml.testAbort",
        "title": "Abort current prompt test",
        "category": "POML",
        "icon": "$(stop)"
      },
      {
        "command": "poml.showPreview",
        "title": "Open POML Preview",
        "category": "POML",
        "icon": {
          "light": "./media/icon/preview.svg",
          "dark": "./media/icon/preview-inverse.svg"
        }
      },
      {
        "command": "poml.showPreviewToSide",
        "title": "Open POML Preview to the Side",
        "category": "POML",
        "icon": {
          "light": "./media/icon/preview-right-pane-16x.svg",
          "dark": "./media/icon/preview-right-pane-16x-inverse.svg"
        }
      },
      {
        "command": "poml.showLockedPreviewToSide",
        "title": "Open Locked POML Preview",
        "category": "POML",
        "icon": {
          "light": "./media/icon/preview-right-pane-16x.svg",
          "dark": "./media/icon/preview-right-pane-16x-inverse.svg"
        }
      },
      {
        "command": "poml.showSource",
        "title": "Show Source File",
        "category": "POML",
        "icon": {
          "light": "./media/icon/view-source.svg",
          "dark": "./media/icon/view-source-inverse.svg"
        }
      },
      {
        "command": "poml.addContextFile",
        "title": "Add Context File",
        "category": "POML"
      },
      {
        "command": "poml.addStylesheetFile",
        "title": "Add Stylesheet File",
        "category": "POML"
      },
      {
        "command": "poml.removeContextFile",
        "title": "Remove Context File",
        "category": "POML"
      },
      {
        "command": "poml.removeStylesheetFile",
        "title": "Remove Stylesheet File",
        "category": "POML"
      },
      {
        "command": "poml.telemetry.completion",
        "title": "Telemetry: Completion",
        "category": "POML"
      },
      {
        "command": "poml.gallery.addPrompt",
        "title": "Add Prompt",
        "category": "POML",
        "icon": "$(plus)"
      },
      {
        "command": "poml.gallery.deletePrompt",
        "title": "Delete Prompt",
        "category": "POML",
        "icon": "$(trashcan)"
      },
      {
        "command": "poml.gallery.editPrompt",
        "title": "Edit Prompt",
        "category": "POML",
        "icon": "$(pencil)"
      }
    ],
    "chatParticipants": [
      {
        "id": "poml.runner",
        "fullName": "POML",
        "name": "poml",
        "description": "Run a POML chat"
      }
    ],
    "menus": {
      "editor/title": [
        {
          "command": "poml.showPreviewToSide",
          "when": "editorLangId == poml",
          "alt": "poml.showPreview",
          "group": "navigation"
        },
        {
          "command": "poml.showSource",
          "when": "pomlPreviewFocus",
          "group": "navigation"
        }
      ],
      "view/title": [
        {
          "command": "poml.gallery.addPrompt",
          "when": "view == pomlPromptGallery",
          "group": "navigation"
        }
      ],
      "view/item/context": [
        {
          "command": "poml.gallery.deletePrompt",
          "when": "view == pomlPromptGallery && viewItem == pomlPrompt.user",
          "group": "inline"
        },
        {
          "command": "poml.gallery.editPrompt",
          "when": "view == pomlPromptGallery && viewItem == pomlPrompt.user",
          "group": "inline"
        }
      ],
      "editor/title/run": [
        {
          "command": "poml.test",
          "group": "navigation@0",
          "when": "editorLangId == poml"
        },
        {
          "command": "poml.testNonChat",
          "group": "navigation@1",
          "when": "editorLangId == poml"
        },
        {
          "command": "poml.testRerun",
          "group": "navigation@2",
          "when": "editorLangId == poml"
        },
        {
          "command": "poml.testAbort",
          "group": "navigation@3",
          "when": "editorLangId == poml"
        }
      ]
    },
    "configuration": {
      "type": "object",
      "title": "POML",
      "order": 20,
      "properties": {
        "poml.languageModel.provider": {
          "type": "string",
          "description": "Language Model Provider",
          "enum": [
            "openai",
            "microsoft",
            "anthropic",
            "google"
          ],
          "enumItemLabels": [
            "OpenAI",
            "Azure OpenAI",
            "Anthropic",
            "Google GenAI"
          ],
          "default": "openai",
          "markdownDescription": "The language model provider to send your prompt to."
        },
        "poml.languageModel.model": {
          "type": "string",
          "description": "Language Model Name (or Deployment Name)",
          "default": "gpt-4o",
          "markdownDescription": "The name of language model to use. It can be the deployment name for Azure OpenAI, or the model code name for Anthropic and Google."
        },
        "poml.languageModel.temperature": {
          "type": "number",
          "description": "Language Model Sampling Temperature",
          "default": 0.5,
          "markdownDescription": "The sampling temperature parameter for the language model.",
          "minimum": 0,
          "maximum": 2
        },
        "poml.languageModel.maxTokens": {
          "type": "number",
          "description": "Language Model Maximum Completion Tokens",
          "default": 0,
          "markdownDescription": "The maximum number of completion tokens. Use 0 for unlimited number of tokens."
        },
        "poml.languageModel.apiKey": {
          "type": "string",
          "description": "Language Model API Key",
          "default": "",
          "markdownDescription": "The API token for the language model provider."
        },
        "poml.languageModel.apiUrl": {
          "type": "string",
          "description": "Language Model API URL",
          "default": "",
          "markdownDescription": "The API endpoint for the language model provider. When using Azure OpenAI, this should be the endpoint of the deployment, e.g., `https://westeurope.api.cognitive.microsoft.com/`. Or it can be `https://api.example.com/v2/` for OpenAI-like providers."
        },
        "poml.languageModel.apiVersion": {
          "type": "string",
          "description": "Language Model API Version",
          "default": "",
          "markdownDescription": "The API version for the language model provider (mostly used for OpenAI and Azure OpenAI)."
        },
        "poml.telemetry.connection": {
          "type": "string",
          "default": "",
          "markdownDescription": "(Development setting) Telemetry Connection String"
        },
        "poml.scrollPreviewWithEditor": {
          "type": "boolean",
          "default": true,
          "description": "(Planned) Double click in the POML preview to switch to the editor.",
          "scope": "resource"
        },
        "poml.markEditorSelection": {
          "type": "boolean",
          "default": true,
          "description": "(Planned) Mark the current editor selection in the POML preview.",
          "scope": "resource"
        },
        "poml.scrollEditorWithPreview": {
          "type": "boolean",
          "default": true,
          "description": "(Planned) When a POML preview is scrolled, update the view of the editor.",
          "scope": "resource"
        },
        "poml.doubleClickToSwitchToEditor": {
          "type": "boolean",
          "default": true,
          "description": "(Planned) When a POML editor is scrolled, update the view of the preview.",
          "scope": "resource"
        },
        "poml.trace": {
          "type": "string",
          "enum": [
            "off",
            "verbose"
          ],
          "default": "off",
          "description": "Enable/disable tracing of the POML extension.",
          "scope": "window"
        }
      }
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run build-extension",
    "build-extension": "webpack-cli --config webpack.config.extension.js",
    "build-extension-dev": "webpack-cli --config webpack.config.extension.js --mode development",
    "watch-extension": "webpack-cli --config webpack.config.extension.js --mode development --watch",
    "build-webview": "webpack-cli --config webpack.config.webview.js",
    "build-cli": "webpack-cli --config webpack.config.cli.js",
    "generate-component-spec": "npm run compile && node ./out/poml-vscode/lsp/parseComments.js && npm run compile && node ./out/poml-vscode/lsp/parseComments.js",
    "generate-vscodeignore": "node ./vscodeignore.js",
    "compile": "tspc -p ./",
    "watch": "tspc -watch -p ./",
    "package": "vsce package",
    "package:win": "vsce package --target win32-x64",
    "pretest": "npm run compile && npm run lint",
    "lint": "eslint packages",
    "test": "jest",
    "test-vscode": "vscode-test",
    "typedoc": "typedoc",
    "docs:serve": "npm run generate-component-spec && npm run typedoc && mkdocs serve",
    "docs:build": "npm run generate-component-spec && npm run typedoc && mkdocs build"
  },
  "devDependencies": {
    "@accessibility-insights/eslint-plugin": "^1.3.2",
    "@rollup/plugin-commonjs": "^28.0.6",
    "@rollup/plugin-json": "^6.1.0",
    "@types/d3-dsv": "~2.0.0",
    "@types/jquery": "^3.5.32",
    "@types/js-yaml": "^4.0.9",
    "@types/lodash.throttle": "^4.1.9",
    "@types/mocha": "^10.0.7",
    "@types/node": "^20.14.15",
    "@types/pdf-parse": "^1.1.5",
    "@types/react": "^19.0.8",
    "@types/react-dom": "^19.0.3",
    "@types/showdown": "^2.0.6",
    "@types/vscode": "^1.95.0",
    "@typescript-eslint/eslint-plugin": "^8.36.0",
    "@typescript-eslint/parser": "^8.36.0",
    "@vscode/test-cli": "^0.0.9",
    "@vscode/test-electron": "^2.4.0",
    "@vscode/vsce": "^3.5.0",
    "copy-webpack-plugin": "^12.0.2",
    "eslint": "^8.57.1",
    "eslint-config-prettier": "^9.1.0",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^30.0.4",
    "prettier": "^3.4.1",
    "rollup": "^4.44.1",
    "ts-jest": "^29.4.0",
    "ts-loader": "^9.5.2",
    "ts-node": "^10.9.2",
    "ts-patch": "^3.3.0",
    "typedoc": "^0.28.9",
    "typedoc-plugin-markdown": "^4.8.0",
    "typescript": "^5.8.3",
    "typescript-transform-paths": "^3.5.5",
    "webpack": "^5.93.0",
    "webpack-cli": "^5.1.4"
  },
  "dependencies": {
    "@ai-sdk/anthropic": "^2.0.2",
    "@ai-sdk/azure": "^2.0.11",
    "@ai-sdk/google": "^2.0.5",
    "@ai-sdk/openai": "^2.0.11",
    "@azure-rest/ai-inference": "^1.0.0-beta.5",
    "@azure/core-sse": "^2.1.3",
    "@vscode/codicons": "^0.0.36",
    "@vscode/extension-telemetry": "^0.9.8",
    "@xml-tools/ast": "^5.0.5",
    "@xml-tools/content-assist": "^3.1.11",
    "@xml-tools/parser": "^1.0.11",
    "ai": "^5.0.11",
    "cheerio": "^1.0.0",
    "closest-match": "^1.3.3",
    "d3-dsv": "~2.0.0",
    "jquery": "^3.7.1",
    "js-tiktoken": "^1.0.20",
    "js-yaml": "^4.1.0",
    "json-schema-to-zod": "^2.6.1",
    "lodash.throttle": "^4.1.1",
    "mammoth": "^1.9.0",
    "pdf-parse": "^1.1.1",
    "pdfjs-dist": "^3.11.174",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-is": "^19.0.0",
    "react-keyed-flatten-children": "^5.0.0",
    "sharp": "^0.33.5",
    "showdown": "^2.1.0",
    "vscode-languageclient": "^9.0.1",
    "vscode-languageserver": "^9.0.1",
    "vscode-languageserver-textdocument": "^1.0.12",
    "xlsx": "^0.18.5",
    "xmlbuilder2": "^3.1.1",
    "yargs": "^17.7.2",
    "zod": "^4.0.17"
  },
  "overrides": {
    "jest-environment-jsdom": {
      "canvas": "^2.11.2"
    },
    "zod": "^4.0.17"
  }
}



================================================
FILE: poml.tmLanguage.json
================================================
{
  "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
  "name": "POML",
  "fileTypes": ["poml"],
  "patterns": [
    {
      "begin": "(<\\?)\\s*([-_a-zA-Z0-9]+)",
      "captures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "entity.name.tag.xml"
        }
      },
      "end": "(\\?>)",
      "name": "meta.tag.preprocessor.xml",
      "patterns": [
        {
          "match": " ([a-zA-Z-]+)",
          "name": "entity.other.attribute-name.xml"
        },
        {
          "include": "#doublequotedString"
        },
        {
          "include": "#singlequotedString"
        }
      ]
    },
    {
      "begin": "(<!)(DOCTYPE)\\s+([:a-zA-Z_][:a-zA-Z0-9_.-]*)",
      "captures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "keyword.other.doctype.xml"
        },
        "3": {
          "name": "variable.language.documentroot.xml"
        }
      },
      "end": "\\s*(>)",
      "name": "meta.tag.sgml.doctype.xml",
      "patterns": [
        {
          "include": "#internalSubset"
        }
      ]
    },
    {
      "include": "#comments"
    },
    {
      "begin": "(<)((?:([-_a-zA-Z0-9]+)(:))?([-_a-zA-Z0-9:]+))(?=(\\s[^>]*)?></\\2>)",
      "beginCaptures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "entity.name.tag.xml"
        },
        "3": {
          "name": "entity.name.tag.namespace.xml"
        },
        "4": {
          "name": "punctuation.separator.namespace.xml"
        },
        "5": {
          "name": "entity.name.tag.localname.xml"
        }
      },
      "end": "(>)(</)((?:([-_a-zA-Z0-9]+)(:))?([-_a-zA-Z0-9:]+))(>)",
      "endCaptures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "punctuation.definition.tag.xml"
        },
        "3": {
          "name": "entity.name.tag.xml"
        },
        "4": {
          "name": "entity.name.tag.namespace.xml"
        },
        "5": {
          "name": "punctuation.separator.namespace.xml"
        },
        "6": {
          "name": "entity.name.tag.localname.xml"
        },
        "7": {
          "name": "punctuation.definition.tag.xml"
        }
      },
      "name": "meta.tag.no-content.xml",
      "patterns": [
        {
          "include": "#tagStuff"
        }
      ]
    },
    {
      "begin": "(</?)(?:([-\\w\\.]+)((:)))?([-\\w\\.:]+)",
      "captures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "entity.name.tag.namespace.xml"
        },
        "3": {
          "name": "entity.name.tag.xml"
        },
        "4": {
          "name": "punctuation.separator.namespace.xml"
        },
        "5": {
          "name": "entity.name.tag.localname.xml"
        }
      },
      "end": "(/?>)",
      "name": "meta.tag.xml",
      "patterns": [
        {
          "include": "#tagStuff"
        }
      ]
    },
    {
      "include": "#entity"
    },
    {
      "include": "#bare-ampersand"
    },
    {
      "begin": "<%@",
      "beginCaptures": {
        "0": {
          "name": "punctuation.section.embedded.begin.xml"
        }
      },
      "end": "%>",
      "endCaptures": {
        "0": {
          "name": "punctuation.section.embedded.end.xml"
        }
      },
      "name": "source.java-props.embedded.xml",
      "patterns": [
        {
          "match": "page|include|taglib",
          "name": "keyword.other.page-props.xml"
        }
      ]
    },
    {
      "begin": "<%[!=]?(?!--)",
      "beginCaptures": {
        "0": {
          "name": "punctuation.section.embedded.begin.xml"
        }
      },
      "end": "(?!--)%>",
      "endCaptures": {
        "0": {
          "name": "punctuation.section.embedded.end.xml"
        }
      },
      "name": "source.java.embedded.xml",
      "patterns": [
        {
          "include": "source.java"
        }
      ]
    },
    {
      "begin": "<!\\[CDATA\\[",
      "beginCaptures": {
        "0": {
          "name": "punctuation.definition.string.begin.xml"
        }
      },
      "end": "]]>",
      "endCaptures": {
        "0": {
          "name": "punctuation.definition.string.end.xml"
        }
      },
      "name": "string.unquoted.cdata.xml"
    }
  ],
  "repository": {
    "EntityDecl": {
      "begin": "(<!)(ENTITY)\\s+(%\\s+)?([:a-zA-Z_][:a-zA-Z0-9_.-]*)(\\s+(?:SYSTEM|PUBLIC)\\s+)?",
      "captures": {
        "1": {
          "name": "punctuation.definition.tag.xml"
        },
        "2": {
          "name": "keyword.other.entity.xml"
        },
        "3": {
          "name": "punctuation.definition.entity.xml"
        },
        "4": {
          "name": "variable.language.entity.xml"
        },
        "5": {
          "name": "keyword.other.entitytype.xml"
        }
      },
      "end": "(>)",
      "patterns": [
        {
          "include": "#doublequotedString"
        },
        {
          "include": "#singlequotedString"
        }
      ]
    },
    "bare-ampersand": {
      "match": "&",
      "name": "invalid.illegal.bad-ampersand.xml"
    },
    "doublequotedString": {
      "begin": "\"",
      "beginCaptures": {
        "0": {
          "name": "punctuation.definition.string.begin.xml"
        }
      },
      "end": "\"",
      "endCaptures": {
        "0": {
          "name": "punctuation.definition.string.end.xml"
        }
      },
      "name": "string.quoted.double.xml",
      "patterns": [
        {
          "include": "#entity"
        },
        {
          "include": "#bare-ampersand"
        }
      ]
    },
    "entity": {
      "captures": {
        "1": {
          "name": "punctuation.definition.constant.xml"
        },
        "3": {
          "name": "punctuation.definition.constant.xml"
        }
      },
      "match": "(&)([:a-zA-Z_][:a-zA-Z0-9_.-]*|#[0-9]+|#x[0-9a-fA-F]+)(;)",
      "name": "constant.character.entity.xml"
    },
    "internalSubset": {
      "begin": "(\\[)",
      "captures": {
        "1": {
          "name": "punctuation.definition.constant.xml"
        }
      },
      "end": "(\\])",
      "name": "meta.internalsubset.xml",
      "patterns": [
        {
          "include": "#EntityDecl"
        },
        {
          "include": "#parameterEntity"
        },
        {
          "include": "#comments"
        }
      ]
    },
    "parameterEntity": {
      "captures": {
        "1": {
          "name": "punctuation.definition.constant.xml"
        },
        "3": {
          "name": "punctuation.definition.constant.xml"
        }
      },
      "match": "(%)([:a-zA-Z_][:a-zA-Z0-9_.-]*)(;)",
      "name": "constant.character.parameter-entity.xml"
    },
    "singlequotedString": {
      "begin": "'",
      "beginCaptures": {
        "0": {
          "name": "punctuation.definition.string.begin.xml"
        }
      },
      "end": "'",
      "endCaptures": {
        "0": {
          "name": "punctuation.definition.string.end.xml"
        }
      },
      "name": "string.quoted.single.xml",
      "patterns": [
        {
          "include": "#entity"
        },
        {
          "include": "#bare-ampersand"
        }
      ]
    },
    "tagStuff": {
      "patterns": [
        {
          "captures": {
            "1": {
              "name": "entity.other.attribute-name.namespace.xml"
            },
            "2": {
              "name": "entity.other.attribute-name.xml"
            },
            "3": {
              "name": "punctuation.separator.namespace.xml"
            },
            "4": {
              "name": "entity.other.attribute-name.localname.xml"
            }
          },
          "match": "(?:^|\\s+)(?:([-\\w.]+)((:)))?([-\\w.:]+)="
        },
        {
          "include": "#doublequotedString"
        },
        {
          "include": "#singlequotedString"
        }
      ]
    },
    "comments": {
      "begin": "<[!%]--",
      "captures": {
        "0": {
          "name": "punctuation.definition.comment.xml"
        }
      },
      "end": "--%?>",
      "name": "comment.block.xml"
    }
  },
  "scopeName": "source.poml"
}



================================================
FILE: pyproject.toml
================================================
[project]
name = "poml"
version = "0.0.8"
description = "Prompt Orchestration Markup Language"
readme = "README.md"
requires-python = ">=3.9"
license = {file = "LICENSE"}
dependencies = [
  "nodejs-wheel",
  "pydantic",
]

[project.optional-dependencies]
dev = [
  "black",
  "flake8",
  "pytest",
  "hatch",
  "twine",
  "mkdocs",
  "mkdocs-material",
  "mkdocstrings[python]",
  "mike",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["python/poml"]
include = [
  # Include the bundled CLI file
  "/python/poml/js/cli.js",
]

# Use the 'force-include' table to explicitly add node_modules, bypassing the default excludes.
[tool.hatch.build.targets.wheel.force-include]
# This line tells hatch:
# 1. Source: Find the directory at 'python/poml/node_modules' in your project.
# 2. Destination: Place its contents at the path 'poml/node_modules' inside the built wheel.
"python/poml/node_modules" = "/poml/node_modules"

[project.scripts]
poml-cli = "poml.cli:entrypoint"



================================================
FILE: RAI_README.md
================================================
# POML: Prompt Orchestration Markup Language

Version 0.1. Updated on 2025-03-27. Please see [README](README.md) for latest info.

## Overview

POML (Prompt Orchestration Markup Language) is a markup language designed for crafting prompts for Large Language Models (LLMs). It provides a structured, reusable, and maintainable way to interact with AI, similar to how HTML is used for building web pages. POML allows you to build clear, modular prompts using components, making prompt creation easier and more efficient.

## What Can POML Do

POML was developed to streamline the process of creating and managing prompts for LLMs. It solves the problem of messy, hard-to-manage prompts by introducing a structured, component-based approach. This makes prompts easier to read, understand, modify, and reuse. POML also offers a modern developer experience with features like syntax highlighting, auto-completion, and live preview in VSCode.

## Intended Uses

POML is best suited for researchers, developers, and anyone who frequently interacts with LLMs and needs a more efficient way to manage their prompts.

POML is being shared with the research community to facilitate the development of advanced prompting techniques and foster further research in this area.

POML is intended to be used by domain experts who are independently capable of evaluating the quality of prompts before acting on them.

## Out-of-Scope Uses

POML is not well suited for directly crafting production-ready prompts without further testing.

We do not recommend using POML in commercial or real-world applications without further testing and development. It is being released for research purposes.

POML was not designed or evaluated for all possible downstream purposes. Developers should consider its inherent limitations as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness concerns specific to each intended downstream use.

POML should not be used in highly regulated domains where inaccurate outputs could suggest actions that lead to injury or negatively impact an individual's legal, financial, or life opportunities.

We do not recommend using POML in the context of high-risk decision making (e.g. in law enforcement, legal, finance, or healthcare).

## How to Get Started

To begin using POML:

* Install the VS Code Extension: Search for "POML" in the VS Code Extensions marketplace and install it. This gives you all the awesome editor features!
* Create a .poml file: Start writing your prompts using POML's intuitive syntax.
* Explore the Documentation: Dive deeper into all the available components and features. You can find the documentation in the extension or on the GitHub page.

## Evaluation

POML has undergone rigorous evaluation through both controlled experiments and real-world application testing. The system demonstrates effectiveness in structuring prompts, handling diverse data formats, and providing consistent styling across different LLMs. User studies confirm its utility in practical scenarios while identifying areas for improvement. The evaluation validates POML's core design goals:

* Creating reusable and maintainable prompt markup
* Providing comprehensive data handling capabilities
* Decoupling content from presentation
* Enhancing tooling for development and collaboration

### Evaluation Methods

1.  **Case Studies**
    * TableQA: Systematic testing of 27,223 unique style configurations across 7 different LLMs using WikiTableQuestions dataset
    * PomLink: RAG application development integrating POML for document, image, table, and web content processing (another project, not included in this release)
2.  **User Study**
    * A within-group user study featuring 10 participants completing 5 different tasks
    * Tasks included prompt rewriting, document processing, data analysis, programming, and subtitle translation
    * Qualitative feedback collection through think-aloud protocols
    * Performance metrics tracking (task completion times, success rates)
3.  **Technical Testing**
    * 10 test suites with 115 test cases
    * Coverage from basic tag parsing to complex multi-modal data integration
    * Testing of error handling and recovery mechanisms

### Evaluation Results

1.  **TableQA Case Study**
    * Confirmed that simple stylesheet adjustments could dramatically improve performance without changing core content
    * Confirmed that POML is robust under all the prompt contents and stylings involved in the study.
2.  **PomLink Case Study**
    * Successfully integrated POML into a large application
    * Demonstrated effective handling of diverse data formats (documents, images, tables, webpages)
    * Showed benefits of centralized stylesheet management and component reuse
3.  **User Study Results**
    * Task completion rates varied by complexity (simpler tasks like document processing had higher success rates)
    * Users found POML particularly valuable for handling multiple file formats and structured prompts
    * Challenges identified included learning curve, file format issues, and desire for multi-turn interactions
    * Users appreciated the clear structure and data integration capabilities
    * Users have identified a series of bugs within POML. They have been resolved quickly in the last development cycle.

## Limitations

POML was developed for research and experimental purposes. Further testing and validation are needed before considering its application in commercial or real-world scenarios.

POML was designed and tested using the English language. Performance in other languages may vary and should be assessed by someone who is both an expert in the expected outputs and a native speaker of that language.

POML was designed to optimize the user’s prompt and does nothing to alter the underlying structure/function of the user’s chosen LLM. Users are reminded that all outputs generated by AI may include factual errors, fabrication, or bias. Users are responsible for assessing the accuracy of generated content. All decisions leveraging outputs of the system should be made with human oversight and not be based solely on system outputs.

## Best Practices

Better performance can be achieved by utilizing POML's features such as reusable components, stylesheets, and the template engine to create clear, concise, and adaptable prompts.

We strongly encourage users to use LLMs/MLLMs that support robust Responsible AI mitigations, such as Azure Open AI (AOAI) services. Such services continually update their safety and RAI mitigations with the latest industry standards for responsible use. For more on AOAI’s best practices when employing foundations models for scripts and applications:

* [Blog post on responsible AI features in AOAI that were presented at Ignite 2023](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/announcing-new-ai-safety-amp-responsible-ai-features-in-azure/ba-p/3983686)
* [Overview of Responsible AI practices for Azure OpenAI models](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview)
* [Azure OpenAI Transparency Note](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note)
* [OpenAI’s Usage policies](https://openai.com/policies/usage-policies)
* [Azure OpenAI’s Code of Conduct](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/code-of-conduct)

## Contact

We welcome feedback and collaboration from our audience. If you have suggestions, questions, or observe unexpected/offensive behavior in our technology, please contact us at Yuge.Zhang@microsoft.com.

If the team receives reports of undesired behavior or identifies issues independently, we will update this repository with appropriate mitigations.


================================================
FILE: SECURITY.md
================================================
<!-- BEGIN MICROSOFT SECURITY.MD V0.0.9 BLOCK -->

## Security

Microsoft takes the security of our software products and services seriously, which includes all source code repositories managed through our GitHub organizations, which include [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) and [Xamarin](https://github.com/xamarin).

If you believe you have found a security vulnerability in any Microsoft-owned repository that meets [Microsoft's definition of a security vulnerability](https://aka.ms/security.md/definition), please report it to us as described below.

## Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them to the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report).

If you prefer to submit without logging in, send email to [secure@microsoft.com](mailto:secure@microsoft.com).  If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page](https://aka.ms/security.md/msrc/pgp).

You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Additional information can be found at [microsoft.com/msrc](https://www.microsoft.com/msrc). 

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

  * Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
  * Full paths of source file(s) related to the manifestation of the issue
  * The location of the affected source code (tag/branch/commit or direct URL)
  * Any special configuration required to reproduce the issue
  * Step-by-step instructions to reproduce the issue
  * Proof-of-concept or exploit code (if possible)
  * Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

If you are reporting for a bug bounty, more complete reports can contribute to a higher bounty award. Please visit our [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) page for more details about our active programs.

## Preferred Languages

We prefer all communications to be in English.

## Policy

Microsoft follows the principle of [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd).

<!-- END MICROSOFT SECURITY.MD BLOCK -->



================================================
FILE: SUPPORT.md
================================================
# TODO: The maintainer of this repo has not yet edited this file

**REPO OWNER**: Do you want Customer Service & Support (CSS) support for this product/project?

- **No CSS support:** Fill out this template with information about how to file issues and get help.
- **Yes CSS support:** Fill out an intake form at [aka.ms/onboardsupport](https://aka.ms/onboardsupport). CSS will work with/help you to determine next steps.
- **Not sure?** Fill out an intake as though the answer were "Yes". CSS will help you decide.

*Then remove this first heading from this SUPPORT.MD file before publishing your repo.*

# Support

## How to file issues and get help  

This project uses GitHub Issues to track bugs and feature requests. Please search the existing 
issues before filing new issues to avoid duplicates.  For new issues, file your bug or 
feature request as a new Issue.

For help and questions about using this project, please **REPO MAINTAINER: INSERT INSTRUCTIONS HERE 
FOR HOW TO ENGAGE REPO OWNERS OR COMMUNITY FOR HELP. COULD BE A STACK OVERFLOW TAG OR OTHER
CHANNEL. WHERE WILL YOU HELP PEOPLE?**.

## Microsoft Support Policy  

Support for this **PROJECT or PRODUCT** is limited to the resources listed above.



================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "module": "NodeNext",
    "target": "ES2022",
    "outDir": "out",
    "lib": ["ES2022", "DOM"],
    "sourceMap": true,
    "baseUrl": "./",
    "rootDir": "packages",
    "jsx": "react",
    "allowJs": true,
    "strict": true, /* enable all strict type-checking options */
    "isolatedModules": true,
    /* Additional Checks */
    // "noImplicitReturns": true, /* Report error when not all code paths in function return a value. */
    // "noFallthroughCasesInSwitch": true, /* Report errors for fallthrough cases in switch statement. */
    // "noUnusedParameters": true,  /* Report errors on unused parameters. */
    "paths": {
      "poml": ["packages/poml"],
      "poml/*": ["packages/poml/*"],
      "poml-vscode": ["packages/poml-vscode"],
      "poml-vscode/*": ["packages/poml-vscode/*"]
    },
    "plugins": [
      { "transform": "typescript-transform-paths" }
    ],
    "resolveJsonModule": true,
    "esModuleInterop": true
  },
  "include": ["packages/**/*"]
}



================================================
FILE: typedoc.json
================================================
{
  "entryPoints": [
    "packages/poml/index.ts",
    "packages/poml/base.tsx", 
    "packages/poml/cli.ts",
    "packages/poml/essentials.tsx",
    "packages/poml/file.tsx",
    "packages/poml/writer.ts",
    "packages/poml/components/index.ts"
  ],
  "out": "docs/typescript/reference",
  "plugin": ["typedoc-plugin-markdown"],
  "readme": "none",
  "githubPages": false,
  "hideGenerator": true,
  "excludePrivate": true,
  "excludeInternal": true,
  "disableSources": false,
  "includeVersion": false,
  "categorizeByGroup": false,
  "tsconfig": "tsconfig.json",
  "name": "POML TypeScript API",
  "hideBreadcrumbs": true,
  "hidePageTitle": true,
  "cleanOutputDir": false,
  "outputFileStrategy": "modules",
  "mergeReadme": false,
  "indexFormat": "table",
  "excludeReferences": true,
  "skipErrorChecking": true,
  "treatWarningsAsErrors": false
}


================================================
FILE: vscodeignore.js
================================================
// This script generates a .vscodeignore file based on the package-lock.json.

const fs = require('fs');
const path = require('path');

// --- Configuration ---
// Add the names of the packages you need to ship in node_modules.
// For example:
// const rootPackages = ['sharp', 'pdf-parse', 'pdfjs-dist'];
// pdf-parse and pdfjs-dist are already manually handled.
const rootPackages = ['sharp'];
// -------------------

console.log('Generating .vscodeignore from package-lock.json...');

try {
  const lockfilePath = path.join(__dirname, 'package-lock.json');
  if (!fs.existsSync(lockfilePath)) {
    throw new Error('package-lock.json not found. Please run "npm install" first.');
  }

  const lockfileContent = fs.readFileSync(lockfilePath, 'utf-8');
  const lockfile = JSON.parse(lockfileContent);

  // Ensure we are working with a v2/v3 lockfile which has the 'packages' map
  if (!lockfile.packages) {
    throw new Error('This script requires a lockfile version 2 or 3 (npm v7+). Please update npm or adjust the script.');
  }

  const allDependencies = new Set(['@img']);
  const ignoredDependencies = ['@img', ...rootPackages]; // Add any other dependencies you want to ignore
  const queue = [...rootPackages]; // Start with our root packages

  // Add root packages to the set initially
  rootPackages.forEach(pkg => allDependencies.add(pkg));

  while (queue.length > 0) {
    const currentPackage = queue.shift();
    const packageKey = `node_modules/${currentPackage}`;
    
    const packageInfo = lockfile.packages[packageKey];

    if (packageInfo) {
      // Combine production and optional dependencies
      const dependencies = {
        ...(packageInfo.dependencies || {}),
        ...(packageInfo.optionalDependencies || {}),
      };

      for (const depName in dependencies) {
        if (!allDependencies.has(depName)) {
          allDependencies.add(depName);
          queue.push(depName);
        }
      }
    }
  }

  console.log(`Found ${allDependencies.size} unique dependencies.`);

  const ignoreHeader = `# This file is auto-generated by vscodeignore.js. DO NOT EDIT MANUALLY.
# It ensures that only necessary production dependencies are packaged with the extension.

.vscode/**
.vscode-test/**
out/**
packages/**
python/**
examples/**
.gitignore
.yarnrc
vsc-extension-quickstart.md
**/tsconfig.json
**/.eslintrc.json
**/*.map
**/*.ts
**/.vscode-test.*
webpack.config.*
.pytest_cache/**

# Hard coded ignore and unignore
node_modules/**
dist/**/node_modules/**
!node_modules/@img/**
!node_modules/sharp/install
!node_modules/sharp/lib
!node_modules/sharp/package.json
!node_modules/pdfjs-dist/**

# But, do NOT ignore the following required modules:
`;

  const ignoreRules = Array.from(allDependencies)
    .sort()
    .filter(depName => ignoredDependencies.every(ignored => !depName.startsWith(ignored)))
    .map(depName => `!node_modules/${depName}/**`);

  const ignoreContent = ignoreHeader + ignoreRules.join('\n');

  const outputPath = path.join(__dirname, '.vscodeignore');
  fs.writeFileSync(outputPath, ignoreContent);

  console.log(`.vscodeignore has been successfully generated at: ${outputPath}`);

} catch (error) {
  console.error('Failed to generate .vscodeignore file.');
  console.error('Original error:', error);
  process.exit(1);
}



================================================
FILE: webpack.config.cli.js
================================================
const path = require('path');
const fs = require('fs');
const CopyPlugin = require('copy-webpack-plugin');

const vscodeignorePath = path.resolve(__dirname, '.vscodeignore');
// The destination for our new node_modules folder
const outputNodeModulesPath = path.resolve(__dirname, 'python', 'poml', 'node_modules');
// The source of all node_modules
const sourceNodeModulesPath = path.resolve(__dirname, 'node_modules');

let copyPatterns = [];
try {
  const vscodeignoreContent = fs.readFileSync(vscodeignorePath, 'utf8');
  const lines = vscodeignoreContent.split('\n');

  copyPatterns = lines
    .map(line => line.trim())
    .filter(line => line.startsWith('!node_modules/'))
    .map(line => {
      // 1. Get the path relative to node_modules
      // e.g., '!node_modules/sharp/package.json' becomes 'sharp/package.json'
      let subPath = line.substring('!node_modules/'.length);

      // 2. Check if the path points to a directory (and isn't already a glob)
      const absolutePath = path.join(sourceNodeModulesPath, subPath);
      if (fs.existsSync(absolutePath) && fs.lstatSync(absolutePath).isDirectory() && !subPath.endsWith('/**')) {
        // If it's a directory, append `/**` to copy its contents recursively
        // while preserving the parent directory name.
        subPath = `${subPath}/**`;
      }

      // 3. Return the corrected pattern object for the plugin
      return {
        // 'from' is now relative to the context (the root node_modules)
        from: subPath,
        // The destination is the new node_modules folder we want to create
        to: outputNodeModulesPath,
        // The context tells the plugin where to find the 'from' files
        context: sourceNodeModulesPath,
        noErrorOnMissing: true,
        // Add this to preserve the directory structure for individual files
        ...(subPath.includes('/') && !subPath.endsWith('/**') ? {
          // For individual files, we need to preserve the full path structure
          to: path.join(outputNodeModulesPath, path.dirname(subPath))
        } : {})
      };
    });

  console.log(`[Webpack] Found ${copyPatterns.length} patterns to copy from .vscodeignore.`);

} catch (error) {
  console.error('[Webpack] Could not read or parse .vscodeignore file. No dependencies will be copied.', error);
}

module.exports = {
  mode: 'development',
  entry: {
    cli: './packages/poml/cli.ts'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  plugins: [
    new CopyPlugin({
      patterns: copyPatterns,
    }),
  ],
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
    alias: {
      poml: path.resolve(__dirname, 'packages/poml'),
    }
  },
  externals: {
    'sharp': 'commonjs sharp',
    'pdf-parse': 'commonjs pdf-parse',
    'pdfjs-dist': 'commonjs pdfjs-dist',
    'canvas': 'commonjs canvas',
  },
  devtool: 'inline-source-map',
  target: 'node',
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'python', 'poml', 'js')
  }
};



================================================
FILE: webpack.config.extension.js
================================================
const path = require('path');
const webpack = require('webpack');

module.exports = [
  // Main extension bundle
  {
    name: 'extension',
    mode: 'production',
    target: 'node',
    entry: './packages/poml-vscode/extension.ts',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'extension.js',
      libraryTarget: 'commonjs2'
    },
    externals: {
      vscode: 'commonjs vscode', // the vscode-module is created on-the-fly and must be excluded
    },
    resolve: {
      extensions: ['.ts', '.tsx', '.js'],
      alias: {
        'poml': path.resolve(__dirname, 'packages/poml'),
        'poml-vscode': path.resolve(__dirname, 'packages/poml-vscode')
      }
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          exclude: /node_modules/,
          use: [
            {
              loader: 'ts-loader',
              options: {
                configFile: path.resolve(__dirname, 'tsconfig.json'),
                transpileOnly: true
              }
            }
          ]
        }
      ]
    },
    plugins: [],
    optimization: {
      minimize: false // Keep readable for debugging
    },
    devtool: 'source-map'
  },
  
  // LSP Server bundle
  {
    name: 'server',
    mode: 'production',
    target: 'node',
    entry: './packages/poml-vscode/lsp/server.ts',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'server.js',
      libraryTarget: 'commonjs2'
    },
    externals: {
      vscode: 'commonjs vscode',
      sharp: 'commonjs sharp',
      'pdf-parse': 'commonjs pdf-parse',
      'pdfjs-dist': 'commonjs pdfjs-dist',
      'canvas': 'commonjs canvas',
    },
    resolve: {
      extensions: ['.ts', '.tsx', '.js'],
      alias: {
        'poml': path.resolve(__dirname, 'packages/poml'),
        'poml-vscode': path.resolve(__dirname, 'packages/poml-vscode')
      }
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          exclude: /node_modules/,
          use: [
            {
              loader: 'ts-loader',
              options: {
                configFile: path.resolve(__dirname, 'tsconfig.json'),
                transpileOnly: true
              }
            }
          ]
        }
      ]
    },
    plugins: [],
    optimization: {
      minimize: false // Keep readable for debugging
    },
    devtool: 'source-map'
  }
];



================================================
FILE: webpack.config.webview.js
================================================
const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: {
    index: './packages/poml-vscode-webview/index.ts'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js']
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, 'node_modules/@vscode/codicons/dist'),
          to: path.resolve(__dirname, 'media/codicons/[name][ext]')
        }
      ]
    })
  ],
  devtool: 'inline-source-map',
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'media')
  }
};



================================================
FILE: .env.azure-pipelines
================================================
# Get the token from https://dev.azure.com/yugzhan/_usersSettings/tokens
# Tick the "Marketplace (manage)" scope
VSCE_PAT=

# Get the token from https://github.com/settings/personal-access-tokens
# Use read-only under Microsoft
GITHUB_PAT=

# Get the token from https://pypi.org/manage/account/token/
PYPI_TOKEN=



================================================
FILE: .eslintrc.js
================================================
const a11yInsights = require('@accessibility-insights/eslint-plugin');

module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 6,
    sourceType: 'module',
  },
  plugins: [
    '@typescript-eslint',
    '@accessibility-insights',
  ],
  extends: [
    'prettier',
    'plugin:@typescript-eslint/recommended',
    'plugin:@accessibility-insights/recommended',
  ],
  rules: {
    ...a11yInsights.configs.recommended.rules,
    '@typescript-eslint/naming-convention': [
      'warn',
      {
        selector: 'import',
        format: ['camelCase', 'PascalCase'],
      },
    ],
    'curly': 'warn',
    // '@typescript-eslint/semi': 'warn',
    // 'eqeqeq': 'warn',
    // 'no-throw-literal': 'warn',
    // 'semi': ['warn', 'always'],
    // 'comma-dangle': ['warn', 'never'],
    // 'quotes': ['warn', 'single'],
    // 'max-len': ['warn', { code: 100 }],
    // 'indent': ['warn', 2],
    // Disabled rules as requested
    '@typescript-eslint/no-explicit-any': 'off',
    'max-len': 'off',
    'quotes': 'off',
    'indent': 'off',
    '@typescript-eslint/no-unused-vars': 'off',
    '@typescript-eslint/semi': 'off',
    'semi': 'off',
    'eqeqeq': 'off',
    'prefer-const': 'off',
    '@typescript-eslint/no-var-requires': 'off',
    '@typescript-eslint/no-namespace': 'off',
  },
  ignorePatterns: ['out', 'dist', '**/*.d.ts'],
  settings: {
    '@accessibility-insights': {
      disableTelemetry: true,
    },
  },
};


================================================
FILE: .npmrc
================================================
@accessibility-insights:registry=https://pkgs.dev.azure.com/accessibility-insights/accessibility-insights-linter/_packaging/accessibility-insights-linter-feed/npm/registry/



================================================
FILE: .prettierrc
================================================
{
  "semi": true,
  "trailingComma": "none",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}



================================================
FILE: .vscode-test.mjs
================================================
import { defineConfig } from '@vscode/test-cli';

export default defineConfig({
  files: 'out/poml-vscode/tests/**/*.test.js'
});



================================================
FILE: .vscodeignore
================================================
# This file is auto-generated by vscodeignore.js. DO NOT EDIT MANUALLY.
# It ensures that only necessary production dependencies are packaged with the extension.

.vscode/**
.vscode-test/**
out/**
packages/**
python/**
examples/**
.gitignore
.yarnrc
vsc-extension-quickstart.md
**/tsconfig.json
**/.eslintrc.json
**/*.map
**/*.ts
**/.vscode-test.*
webpack.config.*
.pytest_cache/**

# Hard coded ignore and unignore
node_modules/**
dist/**/node_modules/**
!node_modules/@img/**
!node_modules/sharp/install
!node_modules/sharp/lib
!node_modules/sharp/package.json
!node_modules/pdfjs-dist/**

# But, do NOT ignore the following required modules:
!node_modules/@emnapi/runtime/**
!node_modules/color/**
!node_modules/color-convert/**
!node_modules/color-name/**
!node_modules/color-string/**
!node_modules/detect-libc/**
!node_modules/is-arrayish/**
!node_modules/semver/**
!node_modules/simple-swizzle/**
!node_modules/tslib/**


================================================
FILE: docs/index.md
================================================
# POML Documentation

Welcome to the Prompt Orchestration Markup Language (POML) documentation.

**POML (Prompt Orchestration Markup Language)** is a novel markup language designed to bring structure, maintainability, and versatility to advanced prompt engineering for Large Language Models (LLMs). It addresses common challenges in prompt development, such as lack of structure, complex data integration, format sensitivity, and inadequate tooling. POML provides a systematic way to organize prompt components, integrate diverse data types seamlessly, and manage presentation variations, empowering developers to create more sophisticated and reliable LLM applications.


## Key Features

* **Structured Prompting Markup**: Employs an HTML-like syntax with semantic components such as `<role>`, `<task>`, and `<example>` to encourage modular design, enhancing prompt readability, reusability, and maintainability.
* **Comprehensive Data Handling**: Incorporates specialized data components (e.g., `<document>`, `<table>`, `<img>`) that seamlessly embed or reference external data sources like text files, spreadsheets, and images, with customizable formatting options.
* **Decoupled Presentation Styling**: Features a CSS-like styling system that separates content from presentation. This allows developers to modify styling (e.g., verbosity, syntax format) via `<stylesheet>` definitions or inline attributes without altering core prompt logic, mitigating LLM format sensitivity.
* **Integrated Templating Engine**: Includes a built-in templating engine with support for variables (`{{ }}`), loops (`for`), conditionals (`if`), and variable definitions (`<let>`) for dynamically generating complex, data-driven prompts.
* **Rich Development Toolkit**:
  * **IDE Extension (Visual Studio Code)**: Provides essential development aids like syntax highlighting, context-aware auto-completion, hover documentation, real-time previews, inline diagnostics for error checking, and integrated interactive testing.
  * **Software Development Kits (SDKs)**: Offers SDKs for Node.js (JavaScript/TypeScript) and Python for seamless integration into various application workflows and popular LLM frameworks.

## Sitemap

- [Language Basics](./language/quickstart.md): Get started with POML syntax and structure.
- [Write .poml Files](./language/standalone.md): Learn how to create
- [VS Code Extension](./vscode/index.md): Enhance your development experience with the POML Visual Studio Code extension.
- [TypeScript SDK](./typescript/index.md): Use the POML TypeScript API for building applications.
- [Python SDK](./python/index.md): Integrate POML into your Python projects.

## Community

Join our Discord community: Connect with the team and other users on our [Discord server](https://discord.gg/FhMCqWzAn6).



================================================
FILE: docs/language/components.md
================================================
# Components

## Basic Components

### Audio

Audio (`<audio>`) embeds an audio file in the content.

Accepts either a file path (`src`) or base64-encoded audio data (`base64`).
The MIME type can be provided via `type` or will be inferred from the file extension.

#### Usages

```xml
<Audio src="path/to/audio.mp3" />
```

#### Parameters

- **src**: Path to the audio file. If provided, the file will be read and encoded as base64.
- **base64**: Base64-encoded audio data. Cannot be used together with `src`.
- **alt**: The alternative text to show when the image cannot be displayed.
- **type**: The MIME type of the audio (e.g., audio/mpeg, audio/wav). If not specified, it will be inferred from the file extension.
    The type must be consistent with the real type of the file. The consistency will NOT be checked or converted.
    The type can be specified with or without the `audio/` prefix.
- **position**: Can be one of: top, bottom, here. The position of the image. Default is `here`.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, multimedia. Only when specified as `multimedia`, the image will be shown.
    Otherwise, the alt text will be shown. By default, it's `multimedia` when `alt` is not specified. Otherwise, it's undefined (inherit from parent).

### Bold

Bold (`<b>`) emphasizes text in a bold style when using markup syntaxes.

#### Usages

```xml
<p><b>Task:</b> Do something.</p>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### CaptionedParagraph

CaptionedParagraph (`<cp>` for short) creates a paragraph with a customized caption title.

#### Usages

```xml
<cp caption="Constraints">
  <list>
    <item>Do not exceed 1000 tokens.</item>
    <item>Please use simple words.</item>
  </list>
</cp>
```

#### Parameters

- **caption**: The title or label for the paragraph. Required.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes.
    By default, it's same as `caption`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Code

Code is used to represent code snippets or inline code in markup syntaxes.

#### Usages

```xml
<code inline="true">const x = 42;</code>
```

```xml
<code lang="javascript">
const x = 42;
</code>
```

#### Parameters

- **inline**: Boolean. Whether to render code inline or as a block. Default is `true`.
- **lang**: The language of the code snippet.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Header

Header (`<h>`) renders headings in markup syntaxes.
It's commonly used to highlight titles or section headings.
The header level will be automatically computed based on the context.
Use SubContent (`<section>`) for nested content.

#### Usages

```xml
<Header syntax="markdown">Section Title</Header>
```

#### Parameters

- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Inline

Inline (`<span>`) is a container for inline content.
When used with markup syntaxes, it wraps text in an inline style, without any preceding or following blank characters.
In serializer syntaxes, it's treated as a generic value.
Inline elements are not designed to be used alone (especially in serializer syntaxes).
One might notice problematic renderings (e.g., speaker not applied) when using it alone.

#### Usages

```xml
<p>I'm listening to <span>music</span> right now.</p>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Italic

Italic (`<i>`) emphasizes text in an italic style when using markup syntaxes.

#### Usages

```xml
Your <i>italicized</i> text.
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### List

List (`<list>`) is a container for multiple ListItem (`<item>`) elements.
When used with markup syntaxes, a bullet or numbering is added.

#### Usages

```xml
<list listStyle="decimal">
  <item>Item 1</item>
  <item>Item 2</item>
</list>
```

#### Parameters

- **listStyle**: Can be one of: star, dash, plus, decimal, latin. The style for the list marker, such as dash or star. Default is `dash`.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### ListItem

ListItem (`<item>`) is an item within a List component.
In markup mode, it is rendered with the specified bullet or numbering style.

#### Usages

```xml
<list listStyle="decimal">
  <item blankLine="true">Item 1</item>
  <item>Item 2</item>
</list>
```

#### Parameters

- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Newline

Newline (`<br>`) explicitly adds a line break, primarily in markup syntaxes.
In serializer syntaxes, it's ignored.

#### Usages

```xml
<br />
```

#### Parameters

- **newLineCount**: Number. The number of linebreaks to add.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Paragraph

Paragraph (`<p>`) is a standalone section preceded by and followed by two blank lines in markup syntaxes.
It's mostly used for text contents.

#### Usages

```xml
<p>Contents of the paragraph.</p>
```

#### Parameters

- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Strikethrough

Strikethrough (`<s>`, `<strike>`) indicates removed or invalid text in markup syntaxes.

#### Usages

```xml
<s>This messages is removed.</s>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### SubContent

SubContent (`<section>`) renders nested content, often following a header.
The headers within the section will be automatically adjusted to a lower level.

#### Usages

```xml
<h>Section Title</h>
<section>
  <h>Sub-section Title</h>  <!-- Nested header -->
  <p>Sub-section details</p>
</section>
```

#### Parameters

- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Text

Text (`<text>`, `<poml>`) is a wrapper for any contents.
By default, it uses `markdown` syntax and writes the contents within it directly to the output.
When used with "markup" syntaxes, it renders a standalone section preceded and followed by one blank line.
It's mostly used in the root element of a prompt, but it should also work in any other places.
This component will be automatically added as a wrapping root element if it's not provided:
1. If the first element is pure text contents, `<poml syntax="text">` will be added.
2. If the first element is a POML component, `<poml syntax="markdown">` will be added.

#### Usages

```xml
<poml syntax="text">
Contents of the whole prompt.

1. Your customized list.
2. You don't need to know anything about POML.
</poml>
```

To render the whole prompt in markdown syntax with a "human" speaker:

```xml
<poml syntax="markdown" speaker="human">
  <p>You are a helpful assistant.</p>
  <p>What is the capital of France?</p>
</poml>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Underline

Underline (`<u>`) draws a line beneath text in markup syntaxes.

#### Usages

```xml
This text is <u>underlined</u>.
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

## Intentions

### Example

Example is useful for providing a context, helping the model to understand what kind of inputs and outputs are expected.
It can also be used to demonstrate the desired output style, clarifying the structure, tone, or level of detail in the response.

#### Usages

```xml
<example>
  <input>What is the capital of France?</input>
  <output>Paris</output>
</example>
```

```xml
<task>Summarize the following passage in a single sentence.</task>
<example>
  <input caption="Passage">The sun provides energy for life on Earth through processes like photosynthesis.</input>
  <output caption="Summary">The sun is essential for energy and life processes on Earth.</output>
</example>
```

#### Parameters

- **caption**: The title or label for the example paragraph. Default is `Example`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `example`.
- **captionStyle**: Determines the style of the caption, applicable only for "markup" syntaxes. Default is `hidden`.
  Options include `header`, `bold`, `plain`, or `hidden`.
- **chat**: Boolean. Indicates whether the example should be rendered in chat format.
  When used in a example set (`<examples>`), this is inherited from the example set.
  Otherwise, it defaults to `false` for "serializer" syntaxes and `true` for "markup" syntaxes.
- **captionTextTransform**: Specifies text transformation for the caption, applicable only for "markup" syntaxes.
  Options are `upper`, `lower`, `capitalize`, or `none`. Default is `none`.
- **captionColon**: Boolean. Indicates whether to append a colon after the caption.
  By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### ExampleInput

ExampleInput (`<input>`) is a paragraph that represents an example input.
By default, it's spoken by a human speaker in a chat context, but you can manually specify the speaker.

#### Usages

```xml
<input>What is the capital of France?</input>
```

When used with a template:

```xml
<input>What is the capital of {{country}}?</input>
```

#### Parameters

- **caption**: The title or label for the example input paragraph. Default is `Input`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `input`.
- **speaker**: The speaker for the example input. Default is `human` if chat context is enabled (see `<example>`).
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `hidden` if chat context is enabled. Otherwise, it's `bold`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionColon**: Boolean. Indicates whether to append a colon after the caption.
  By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### ExampleOutput

ExampleOutput (`<output>`) is a paragraph that represents an example output.
By default, it's spoken by a AI speaker in a chat context, but you can manually specify the speaker.

#### Usages

```xml
<output>The capital of France is Paris.</output>
```

When used with a template:

```xml
<output>The capital of {{country}} is {{capital}}.</output>
```

#### Parameters

- **caption**: The title or label for the example output paragraph. Default is `Output`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `output`.
- **speaker**: The speaker for the example output. Default is `ai` if chat context is enabled (see `<example>`).
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `hidden` if chat context is enabled. Otherwise, it's `bold`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionColon**: Boolean. Indicates whether to append a colon after the caption.
  By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### ExampleSet

Example set (`<examples>`) is a collection of examples that are usually presented in a list.
With the example set, you can manage multiple examples under a single title and optionally an introducer,
as well as the same `chat` format.
You can also choose to use `<example>` purely without example set.

#### Usages

```xml
<examples chat={{true}}>
  <example>
    <input>What is the capital of France?</input>
    <output>Paris</output>
  </example>
  <example>
    <input>What is the capital of Germany?</input>
    <output>Berlin</output>
  </example>
</examples>
```

#### Parameters

- **caption**: The title or label for the example set paragraph. Default is `Examples`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `examples`.
- **chat**: Boolean. Indicates whether the examples should be rendered in chat format.
  By default, it's `true` for "markup" syntaxes and `false` for "serializer" syntaxes.
- **introducer**: An optional introducer text to be displayed before the examples.
  For example, `Here are some examples:`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Hint

Hint can be used anywhere in the prompt where you want to provide a helpful tip or explanation.
It is usually a short and concise statement that guides the LLM in the right direction.

#### Usages

```xml
<hint>Alice first purchased 4 apples and then 3 more, so she has 7 apples in total.</hint>
```

#### Parameters

- **caption**: The title or label for the hint paragraph. Default is `Hint`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `hint`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `bold`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionColon**: Boolean. Indicates whether to append a colon after the caption.
  By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Introducer

Introducer is a paragraph before a long paragraph (usually a list of examples, steps, or instructions).
It serves as a context introducing what is expected to follow.

#### Usages

```xml
<introducer>Here are some examples.</introducer>
```

#### Parameters

- **caption**: The title or label for the introducer paragraph. Default is `Introducer`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `introducer`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `hidden`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### OutputFormat

Output format deals with the format in which the model should provide the output.
It can be a specific format such as JSON, XML, or CSV, or a general format such as a story,
a diagram or steps of instructions.
Please refrain from specifying too complex formats that the model may not be able to generate,
such as a PDF file or a video.

#### Usages

```xml
<output-format>Respond with a JSON without additional characters or punctuations.</output-format>
```

#### Parameters

- **caption**: The title or label for the output format paragraph. Default is `Output Format`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `outputFormat`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Question

Question (`<qa>`) is actually a combination of a question and a prompt for the answer.
It's usually used at the end of a prompt to ask a question.
The question is followed by a prompt for answer (e.g., `Answer:`) to guide the model to respond.

#### Usages

```xml
<qa>What is the capital of France?</qa>
```

#### Parameters

- **questionCaption**: The title or label for the question paragraph. Default is `Question`.
- **answerCaption**: The title or label for the answer paragraph. Default is `Answer`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `question`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `bold`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Role

Specifies the role you want the language model to assume when responding.
Defining a role provides the model with a perspective or context,
such as a scientist, poet, child, or any other persona you choose.

#### Usages

```xml
<role>You are a data scientist.</role>
```

#### Parameters

- **caption**: The title or label for the role paragraph. Default is `Role`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `role`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### StepwiseInstructions

StepwiseInstructions that elaborates the task by providing a list of steps or instructions.
Each step should be concise and clear, and the list should be easy to follow.

#### Usages

```xml
<stepwise-instructions>
  <list>
    <item>Interpret and rewrite user's query.</item>
    <item>Think of a plan to solve the query.</item>
    <item>Generate a response based on the plan.</item>
  </list>
</stepwise-instructions>
```

#### Parameters

- **caption**: The title or label for the stepwise instructions paragraph. Default is `Stepwise Instructions`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `stepwiseInstructions`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Task

Task represents the action you want the language model to perform.
It is a directive or instruction that you want the model to follow.
Task is usually not long, but rather a concise and clear statement.
Users can also include a list of steps or instructions to complete the task.

#### Usages

```xml
<task>Cook a recipe on how to prepare a beef dish.</task>
```

When including a list of steps:
```xml
<task>
  Planning a schedule for a travel.
  <list>
    <item>Decide on the destination and plan the duration.</item>
    <item>Find useful information about the destination.</item>
    <item>Write down the schedule for each day.</item>
  </list>
</task>
```

#### Parameters

- **caption**: The title or label for the task paragraph. Default is `Task`.
- **captionSerialized**: The serialized version of the caption when using "serializer" syntaxes. Default is `task`.
- **captionStyle**: Can be one of: header, bold, plain, hidden. Determines the style of the caption,
  applicable only for "markup" syntaxes. Default is `header`.
- **captionTextTransform**: Can be one of: upper, level, capitalize, none. Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
- **captionEnding**: Can be one of: colon, newline, colon-newline, none. A caption can ends with a colon, a newline or simply nothing.
  If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
- **blankLine**: Boolean. Whether to add one more blank line (2 in total) before and after the paragraph.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

## Data Displays

### Document

Displaying an external document like PDF, TXT or DOCX.

#### Usages

To display a Word document without including the real multimedia:
```xml
<Document src="sample.docx" multimedia="false"/>
```

#### Parameters

- **src**: The source file to read the data from. This must be provided if records is not provided.
- **buffer**: Buffer. Document data buffer. Recommended to use `src` instead unless you want to use a string.
- **base64**: Base64 encoded string of the document data. Mutually exclusive with `src` and `buffer`.
- **parser**: Can be one of: auto, pdf, docx, txt. The parser to use for reading the data. If not provided, it will be inferred from the file extension.
- **multimedia**: Boolean. If true, the multimedias will be displayed. If false, the alt strings will be displayed at best effort. Default is `true`.
- **selectedPages**: The pages to be selected. This is only available **for PDF documents**. If not provided, all pages will be selected.
  You can use a string like `2` to specify a single page, or slice like `2:4` to specify a range of pages (2 inclusive, 4 exclusive).
  The pages selected are **0-indexed**. Negative indexes like `-1` is not supported here.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Image

Image (`<img>`) displays an image in the content.
Alternatively, it can also be shown as an alt text by specifying the `syntax` prop.
Note that syntax must be specified as `multimedia` to show the image.

#### Usages

```xml
<Image src="path/to/image.jpg" alt="Image description" position="bottom" />
```

#### Parameters

- **src**: The path to the image file.
- **alt**: The alternative text to show when the image cannot be displayed.
- **base64**: The base64 encoded image data. It can not be specified together with `src`.
- **type**: The MIME type of the image **to be shown**. If not specified, it will be inferred from the file extension.
    If specified, the image will be converted to the specified type. Can be `image/jpeg`, `image/png`, etc., or without the `image/` prefix.
- **position**: Can be one of: top, bottom, here. The position of the image. Default is `here`.
- **maxWidth**: Number. The maximum width of the image to be shown.
- **maxHeight**: Number. The maximum height of the image to be shown.
- **resize**: Number. The ratio to resize the image to to be shown.
- **syntax**: Can be one of: markdown, html, json, yaml, xml, multimedia. Only when specified as `multimedia`, the image will be shown.
    Otherwise, the alt text will be shown. By default, it's `multimedia` when `alt` is not specified. Otherwise, it's undefined (inherit from parent).
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Object

Object (`<obj>`, `<dataObj>`) displays external data or object content.
When in serialize mode, it's serialized according to the given serializer.

#### Usages

```xml
<Object syntax="json" data="{ key: 'value' }" />
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml. The syntax or serializer of the content. Default is `json`.
- **data**: Object. The data object to render.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Table

Displaying a table with records and columns.

#### Usages

```xml
<table records="{{[{ name: 'Alice', age: 20 }, { name: 'Bob', age: 30 }]}}" />
```

To import an excel file, and display the first 10 records in csv syntax:

```xml
<table src="data.xlsx" parser="excel" maxRecords="10" syntax="csv" />
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, text, csv, tsv, xml. The output syntax of the content.
- **records**: Object. A list, each element is an object / dictionary / list of elements. The keys are the fields and the values are the data in cells.
- **columns**: Object. A list of column definitions. Each column definition is an object with keys "field", "header", and "description".
  The field is the key in the record object, the header is displayed in the top row, and the description is meant to be an explanation.
  Columns are optional. If not provided, the columns are inferred from the records.
- **src**: The source file to read the data from. This must be provided if records is not provided.
- **parser**: Can be one of: auto, csv, tsv, excel, json, jsonl. The parser to use for reading the data. If not provided, it will be inferred from the file extension.
- **selectedColumns**: Object. The selected columns to display. If not provided, all columns will be displayed.
  It should be an array of column field names, e.g. `["name", "age"]`; or a string like `2:4` to select columns 2 (inclusive) to 4 (exclusive).
  There is a special column name called `index` which is the enumeration of the records starting from 0.
  You can also use a special value called `+index` to add the index column to the original table.
- **selectedRecords**: Object. The selected records to display. If not provided, all records will be displayed.
  It should be an array of record indices, e.g. `[0, 1]`; or a string like `2:4` to select records 2 (inclusive) to 4 (exclusive).
- **maxRecords**: Number. The maximum number of records to display. If not provided, all records will be displayed.
- **maxColumns**: Number. The maximum number of columns to display. If not provided, all columns will be displayed.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

## Utilities

### AiMessage

Wrap the contents in a AI message.

#### Usages

```xml
<ai-msg>Paris</ai-msg>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Conversation

Display a conversation between system, human and AI.

#### Usages

```xml
<conversation messages="{{[{ speaker: 'human', content: 'What is the capital of France?' }, { speaker: 'ai', content: 'Paris' }]}}" />
```

#### Parameters

- **messages**: Object. A list of message. Each message should have a `speaker` and a `content` field.
- **selectedMessages**: The messages to be selected. If not provided, all messages will be selected.
  You can use a string like `2` to specify a single message, or slice like `2:4` to specify a range of messages (2 inclusive, 4 exclusive).
  Or use `-6:` to select the last 6 messages.

### Folder

Displays a directory structure as a tree.

#### Usages

To display a directory structure with a filter for Python files:
```xml
<folder src="project_dir" filter=".*\.py$" maxDepth="3" />
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, text, xml. The output syntax of the content.
- **src**: The source directory path to display.
- **data**: TreeItemData[]. Alternative to src, directly provide tree data structure.
- **filter**: RegExp. A regular expression to filter files.
    The regex is applied to the folder names and file names (not the full path).
    Directories are included by default unless all of their nested content is filtered out.
    When filter is on, empty directories will not be shown.
- **maxDepth**: Number. Maximum depth of directory traversal. Default is 3.
- **showContent**: Boolean. Whether to show file contents. Default is false.

### HumanMessage

Wrap the contents in a user message.

#### Usages

```xml
<user-msg>What is the capital of France?</user-msg>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### MessageContent

Display a message content.

#### Usages

```xml
<msg-content content="What is the capital of France?" />
```

#### Parameters

- **content**: Object. The content of the message. It can be a string, or an array of strings and multimedia content.

### SystemMessage

Wrap the contents in a system message.

#### Usages

```xml
<system-msg>Answer concisely.</system-msg>
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **name**: The name of the content, used in serialization.
- **type**: The type of the content, used in serialization.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.

### Tree

Renders a tree structure in various formats.

#### Usages

```xml
<Tree items={treeData} syntax="markdown" showContent={true} />
```

#### Parameters

- **syntax**: Can be one of: markdown, html, json, yaml, text, xml. The output syntax to use for rendering the tree
- **items**: TreeItemData[]. Array of tree items to render
- **showContent**: Boolean. Whether to show content values of tree items

### Webpage

Displays content from a webpage.

#### Usages

Display content from a URL:
```xml
<webpage url="https://example.com" />
```

Extract only specific content using a selector:
```xml
<webpage url="https://example.com" selector="main article" />
```

Convert HTML to structured POML components:
```xml
<webpage url="https://example.com" extractText="false" />
```

#### Parameters

- **url**: The URL of the webpage to fetch and display.
- **src**: Local file path to an HTML file to display.
- **buffer**: Buffer. HTML content as string or buffer.
- **base64**: Base64 encoded HTML content.
- **extractText**: Boolean. Whether to extract plain text content (true) or convert HTML to structured POML (false). Default is false.
- **selector**: CSS selector to extract specific content from the page (e.g., "article", ".content", "#main"). Default is "body".
- **syntax**: Can be one of: markdown, html, json, yaml, xml, text. The syntax of the content.
- **className**: A class name for quickly styling the current block with stylesheets.
- **speaker**: Can be one of: human, ai, system. The speaker of the content. By default, it's determined by the context and the content.
- **writerOptions**: Object. An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.


================================================
FILE: docs/language/ir.md
================================================
# Intermediate Representation

**Attributes Applicable to All Tags:**
* speaker (ai/human/system) - The speaker of the current content
* original-start-index (integer) - The start offset of the element corresponding to the current one in the original document
* original-end-index (integer) - The end offset of the element corresponding to the current one in the original document

- **any** - Represents a generic container for arbitrary data values. Useful for storing dynamic or unstructured content.
  * type (string) - The data type of the value ('string', 'integer', 'float', 'boolean', 'array', 'object', 'buffer', 'null', or 'undefined').
  * name (string) - An optional identifier for the data.

- **b** - Represents text that should be displayed in boldface. Useful for highlighting important words or phrases.

- **code** - Represents a block or inline fragment of code. It can optionally include language and formatting attributes.
  * inline (boolean) - Indicates whether the code is inline (true) or a block element (false).
  * lang (string) - Specifies the programming language or syntax highlighting mode.
  * blank-line (boolean) - Inserts a blank line before and after the code block if inline = false.

- **env** - Represents a formatting environment or container to specify how nested content should be output.
  * presentation (string) - The output style or format mode ('markup', 'serialize', 'free', or 'multimedia').
  * markup-lang (string) - The specific markup language, required only if presentation = 'markup'.
  * serializer (string) - The name of the serializer, required only if presentation = 'serialize'.
  * writer-options (object) - Optional parameters passed to the writer constructor for customizing output.

- **h** - Represents a heading element.
  * level (integer) - Indicates the heading level. Typically ranges from 1 (highest level) to 6 (lowest level).

- **i** - Represents text that should be displayed in italics. Useful for emphasizing words or phrases.

- **img** - Represents an image element.
  * base64 (string) - The base64-encoded image data.
  * alt (string) - Alternative text describing the image.
  * position (string) - The placement of the image relative to text, such as 'here', 'top', or 'bottom'.
  * type (string) - The image MIME type (e.g., 'image/jpeg', 'image/png').

- **item** - Represents a single item within a list. Typically used as a child element of "list".

- **list** - Represents an ordered or unordered list of items.
  * list-style (string) - The style of the list bullets or enumeration (e.g., 'star', 'dash', 'decimal').

- **nl** - Inserts newline characters.
  * count (integer) - Specifies how many newline characters to insert.

- **obj** - Represents a data object, typically stored in JSON format.
  * data (object) - A valid JSON object containing the structured data.

- **p** - Represents a paragraph of text. Useful for dividing content into readable blocks.
  * blank-line (boolean) - Inserts a blank line before and after the paragraph when true.

- **s** - Represents text that should be displayed with a strikethrough style.

- **span** - Represents an inline container for text without additional formatting. Useful for applying attributes without changing display structure.

- **table** - Represents a table structure containing rows and cells.

- **tbody** - Represents the body section of a table, containing the majority of data rows.

- **tcell** - Represents a single cell within a table row.

- **text** - Represents raw or unformatted text content.

- **thead** - Represents the header section of a table, typically containing column headings.

- **trow** - Represents a single row within a table, containing one or more cells.

- **u** - Represents text that should be displayed with an underline.



================================================
FILE: docs/language/meta.md
================================================
# Meta

The `<meta>` element provides metadata and configuration for POML documents. It allows you to specify version requirements, disable/enable components, define response schemas, register tools, and set runtime parameters.

## Basic Usage

Meta elements are typically placed at the beginning of a POML document and don't produce any visible output. One POML file can have multiple `<meta>` elements at any position, but they should be used carefully to avoid conflicts.

```xml
<poml>
  <meta minVersion="1.0.0" />
  <p>Your content here</p>
</poml>
```

### Meta Element Types

Meta elements fall into two categories based on whether they include a `type` attribute:

**Without type attribute** - Used for general document configuration:
- Version control (`minVersion`, `maxVersion`)
- Component management (`components`)

**With type attribute** - Used for specific functionalities:
- `type="responseSchema"` - Defines structured output format for AI responses
- `type="tool"` - Registers callable functions for AI models
- `type="runtime"` - Sets language model execution parameters

## Response Schema

Response schemas define the expected structure of AI-generated responses, ensuring that language models return data in a predictable, parsable format. This transforms free-form text generation into structured data generation.

### JSON Schema Format

Use the `lang="json"` attribute to specify JSON Schema format:

```xml
<meta type="responseSchema" lang="json">
  {
    "type": "object",
    "properties": {
      "name": { "type": "string" },
      "age": { "type": "number" }
    },
    "required": ["name"]
  }
</meta>
```

### Expression Format

Use the `lang="expr"` attribute (or omit it for auto-detection) to evaluate JavaScript expressions that return schemas:

```xml
<meta type="responseSchema" lang="expr">
  z.object({
    name: z.string(),
    age: z.number().optional()
  })
</meta>
```

When `lang` is omitted, POML auto-detects the format:
- If the content starts with `{`, it's treated as JSON
- Otherwise, it's treated as an expression

### Expression Evaluation in Schemas

#### JSON Schema with Template Expressions

JSON schemas support template expressions using `{{ }}` syntax:

```xml
<let name="maxAge" value="100" />
<meta type="responseSchema" lang="json">
  {
    "type": "object",
    "properties": {
      "name": { "type": "string" },
      "age": { 
        "type": "number",
        "minimum": 0,
        "maximum": {{ maxAge }}
      }
    }
  }
</meta>
```

#### Expression Format with JavaScript Evaluation

Expression schemas are evaluated as JavaScript code with access to context variables and the `z` (Zod) variable:

```xml
<let name="fields" value='["name", "email", "age"]' />
<meta type="responseSchema" lang="expr">
  z.object(
    Object.fromEntries(fields.map(f => [f, z.string()]))
  )
</meta>
```

The expression can return either:
- A Zod schema object (detected by the presence of `_def` property)
- A plain JavaScript object treated as JSON Schema

**Important limitations:**
- Only one `responseSchema` meta element is allowed per document. Multiple response schemas will result in an error.
- Response schemas cannot be used together with tool definitions in the same document. You must choose between structured responses or tool calling capabilities.

## Tool Registration

Tool registration enables AI models to interact with external functions during conversation. Tools are function definitions that tell the AI model what functions are available, what parameters they expect, and what they do.

**Important:** Tools and response schemas are mutually exclusive. You cannot use both `responseSchema` and `tool` meta elements in the same POML document.

### JSON Schema Format

```xml
<meta type="tool" name="getWeather" description="Get weather information">
  {
    "type": "object",
    "properties": {
      "location": { "type": "string" },
      "unit": { 
        "type": "string", 
        "enum": ["celsius", "fahrenheit"] 
      }
    },
    "required": ["location"]
  }
</meta>
```

### Expression Format

```xml
<meta type="tool" name="calculate" description="Perform calculation" lang="expr">
  z.object({
    operation: z.enum(['add', 'subtract', 'multiply', 'divide']),
    a: z.number(),
    b: z.number()
  })
</meta>
```

### Expression Evaluation in Tool Schemas

Tool schemas support the same evaluation modes as response schemas:

#### JSON with Template Expressions

```xml
<let name="maxValue" value="1000" />
<meta type="tool" name="calculator" description="Calculate values" lang="json">
  {
    "type": "object",
    "properties": {
      "value": { 
        "type": "number",
        "maximum": {{ maxValue }}
      }
    }
  }
</meta>
```

#### Expression Format

```xml
<let name="supportedOperations" value='["add", "subtract", "multiply", "divide"]' />
<meta type="tool" name="calculator" description="Perform mathematical operations" lang="expr">
  z.object({
    operation: z.enum(supportedOperations),
    a: z.number(),
    b: z.number()
  })
</meta>
```

In expression mode, the `z` variable is automatically available for constructing Zod schemas, and you have direct access to all context variables.

**Required attributes for tools:**
- **name**: Tool identifier (required)
- **description**: Tool description (optional but recommended)
- **lang**: Schema language, either "json" or "expr" (optional, auto-detected based on content)

You can define multiple tools in a single document.

## Runtime Parameters

Runtime parameters configure the language model's behavior during execution. These parameters are automatically used in [VSCode's test command](../vscode/features.md) functionality, which is based on the [Vercel AI SDK](https://ai-sdk.dev/).

```xml
<meta type="runtime" 
      temperature="0.7" 
      maxOutputTokens="1000" 
      model="gpt-5"
      topP="0.9" />
```

All attributes except `type` are passed as runtime parameters. Common parameters include:

- **temperature**: Controls randomness (0-2, typically 0.3-0.7 for balanced output)
- **maxOutputTokens**: Maximum response length in tokens
- **model**: Model identifier (e.g., "gpt-5", "claude-4-sonnet")
- **topP**: Nucleus sampling threshold (0-1, typically 0.9-0.95)
- **frequencyPenalty**: Reduces token repetition based on frequency (-2 to 2)
- **presencePenalty**: Reduces repetition based on presence (-2 to 2)
- **seed**: For deterministic outputs (integer value)

The full parameter list depends on whether you're using standard text generation or structured data generation:
- [Text generation parameters](https://ai-sdk.dev/docs/ai-sdk-core/generating-text) - Standard text generation
- [Structured data parameters](https://ai-sdk.dev/docs/ai-sdk-core/generating-structured-data) - When using response schemas

The [Vercel AI SDK](https://ai-sdk.dev/) automatically handles parameter validation and conversion for different model providers.

## Version Control

Version requirements ensure compatibility between documents and the POML runtime. This prevents runtime errors when documents require specific POML features.

```xml
<meta minVersion="0.5.0" maxVersion="2.0.0" />
```

- **minVersion**: Minimum required POML version. If the current version is lower, an error is thrown.
- **maxVersion**: Maximum supported POML version. Documents may not work correctly with newer versions.

Version checking uses semantic versioning (MAJOR.MINOR.PATCH) and occurs during document parsing.

## Component Control

The `components` attribute dynamically enables or disables POML components within a document. This is useful for conditional content, feature flags, or restricting elements in specific contexts.

### Disabling Components

Prefix component names with `-` to disable them:

```xml
<meta components="-table" />
<!-- Now <table> elements will throw an error -->
```

You can disable multiple components:

```xml
<meta components="-table,-image" />
```

### Re-enabling Components

Use `+` prefix to re-enable previously disabled components:

```xml
<meta components="-table" />
<!-- table is disabled -->
<meta components="+table" />
<!-- table is re-enabled -->
```

Component aliases can be disabled independently of the main component name. For example, if a component has both a main name and aliases, you can disable just the alias while keeping the main component available.



================================================
FILE: docs/language/quickstart.md
================================================
# Quick Start

Here's a very simple POML example. Please put it in a file named `example.poml`. Make sure it resides in the same directory as the `photosynthesis_diagram.png` image file.

```xml
<poml>
  <role>You are a patient teacher explaining concepts to a 10-year-old.</role>
  <task>Explain the concept of photosynthesis using the provided image as a reference.</task>

  <img src="photosynthesis_diagram.png" alt="Diagram of photosynthesis" />

  <output-format>
    Keep the explanation simple, engaging, and under 100 words.
    Start with "Hey there, future scientist!".
  </output-format>
</poml>
```

This example defines a role and task for the LLM, includes an image for context, and specifies the desired output format. With the POML toolkit, the prompt can be easily rendered with a flexible format, and tested with a vision LLM.

## YouTube Video

We also recommend watching our [YouTube video](https://youtu.be/b9WDcFsKixo) for a quick introduction to POML and how to get started.

## Next Steps

- [Learn POML Syntax](./standalone.md): Understand the structure and syntax of POML files.
- [Explore Components](./components.md): Discover the available components and how to use them.
- [Install VS Code Extension](../vscode/index.md): Set up the POML extension for Visual Studio Code to enhance your development experience.
- [Configure Python SDK](../python/index.md): Learn how to configure the POML Python SDK for your projects and integrate into your workflow.



================================================
FILE: docs/language/standalone.md
================================================
# POML Standalone File Mode

## Introduction to Standalone File Mode

POML (Prompting Markup Language) provides a convenient way to create prompts using a markup language that is easy to read and write. The standalone file mode is the most commonly used approach, where you create a file with a `.poml` extension. This file contains XML-like syntax that POML renders into a prompt. This mode is particularly useful for creating reusable templates and managing complex prompts without embedding POML directly in JSX files or using a Python SDK.

In this mode, you wrap your content with a top-level `<poml>` tag, allowing POML to parse and render your markup correctly. Below is a guide on how to effectively use the standalone file mode.

## Basic Usage

To create a POML file, simply create a file with the `.poml` extension and wrap your content within the `<poml>` tag:

```xml
<poml>
  <p>Hello, world!</p>
</poml>
```

You can also type anything without a `poml` tag, and it will be treated as a string. It's called "free text mode" in POML. However, it has several limitations currently, including unabling to render any XML tags wrapped with `<>`, unabling to use many special characters, and unabling to use all the wonderful features of POML. So, it's always recommended to use the `poml` tag before everything.

**Tip: Glossary for Beginners:**

- **Tag:** A tag is a fundamental building block in XML (and POML). It's used to mark the beginning and end of an element. Tags are enclosed in angle brackets (`<` and `>`). For example, `<p>` is an opening tag, and `</p>` is a closing tag. Everything between the opening and closing tags is considered part of that element.
- **Attribute:** An attribute provides additional information about an element. Attributes are placed inside the opening tag, and they consist of a name and a value (enclosed in double quotes). For example, in `<p speaker="human">`, `speaker` is the attribute name, and `"human"` is the attribute value.
- **Content:** The content is the text or other elements that appear between the opening and closing tags of an element. For example, in `<p>Hello, world!</p>`, "Hello, world!" is the content of the `<p>` element.

**Escape Characters:** In POML, you can use escape characters to include special characters in your content and attribute values. Due to an implementation issue, the escape syntax in POML is slightly different from what you would know in HTML or XML. For example, to include a double quote (`"`) in your content, you can use `#quot;` (rather than `&quot;`). Here are some common escape characters:

1. `#quot;` for `"`
2. `#apos;` for `'`
3. `#amp;` for `&`
4. `#lt;` for `<`
5. `#gt;` for `>`
6. `#hash;` for `#`
7. `#lbrace;` for `{`
8. `#rbrace;` for `}`

It's not necessary to use the escape characters for most cases, but they can be helpful when you are having trouble displaying those characters in certain cases.

## Template Engine

The template engine of POML allows you to incorporate dynamic content and control structures. Here are some key features.

### Expressions

You can use expressions enclosed in double curly brackets (`{{` `}}`) to evaluate variables or expressions dynamically:

```xml
<poml>
  <p>Hello, {{name}}!</p>
</poml>
```

In this example, if `name` is set to "Alice" (e.g., using a `<let>` tag, described below), the output will be "Hello, Alice!".

#### Usage in Attributes

Expressions can also be used within attribute values:

```xml
<poml>
  <task caption="Task #{{index}}">This is task No. {{index}}.</p>
</poml>
```

This renders to the following when `index` is set to 1.

```
# Task #1

This is task No. 1.
```

#### Expression Usages

POML supports various JavaScript expressions within the double curly brackets. This includes but is not limited to:

- **Variables:**  `{{variableName}}`
- **Arithmetic:** `{{a + b}}`, `{{x * y}}`, `{{count / total}}`
- **String Concatenation:** `{{firstName + " " + lastName}}`
- **Array Access:** `{{myArray[0]}}`
- **Object Property Access:** `{{myObject.propertyName}}`
- **Function Calls:** `{{myFunction(arg1, arg2)}}` (if `myFunction` is defined in the context)
- **Ternary Operators:** `{{condition ? valueIfTrue : valueIfFalse}}`
- **Accessing loop variables:** `{{loop.index}}` (explained in the "For Attribute" section)

### Let Expressions

The `<let>` tag allows you to define variables, import data from external files, and set values within your POML template.

#### Syntax 1: Setting a variable from a value

```xml
<poml>
  <let name="greeting" value="Hello, world!" />
  <p>{{greeting}}</p>
</poml>
```

This will output "Hello, world!".  The `value` attribute can contain a string, number, or a POML expression.

#### Syntax 2: Importing data from a file

```xml
<poml>
  <let name="users" src="users.json" />
  <p>First user: {{users[0].name}}</p>
</poml>
```

This imports the contents of `users.json` and assigns it to the `users` variable.  The `src` attribute specifies the path to the file (relative to the POML file). The optional `type` attribute can specify the file type (e.g., "json", "text", "csv"). If not provided, POML attempts to infer it from the file extension.

#### Syntax 3: Importing data from a file without a name

```xml
<poml>
  <let src="config.json" />
  <p>API Key: {{apiKey}}</p>
</poml>
```
If `config.json` contains `{ "apiKey": "your_api_key" }`, this will output "API Key: your_api_key". When you use `src` without `name`, and the file content is a JSON object, the properties of that object are directly added to the context.

#### Syntax 4: Setting a variable using inline JSON

```xml
<poml>
  <let name="person">
    {
      "name": "Alice",
      "age": 30
    }
  </let>
  <p>Name: {{person.name}}, Age: {{person.age}}</p>
</poml>
```

This defines a `person` variable with the given JSON object. You can also specify the `type` attribute:

```xml
<poml>
  <let name="count" type="integer">5</let>
  <p>Count: {{count}}</p>
</poml>
```

#### Syntax 5: Setting a variable from an expression

```xml
<poml>
  <let name="base" value="10" />
  <let name="increment" value="5" />
  <let name="total" value="{{ base + increment }}" />
  <p>Total: {{ total }}</p>  <!-- Output: Total: 15 -->
</poml>
```

### Type-Autocasting in Attributes

The attributes of components will be automatically cast based on their defined types in the component documentation. This means you don't have to worry about manually converting types in many cases.

- **Boolean:** If an attribute is defined as a boolean, values like `"true"`, `1`, `"1"`, or `{{true}}` will be cast to the boolean value `true`. Similarly, `"false"`, `0`, `"0"`, or `{{false}}` will be cast to `false`.
- **Number:** If an attribute is defined as a number, values like `"123"`, `45.6`, `{{anyNumber}}` or `{{myNumber+1.3}}` will be cast to their corresponding numeric values.
- **Object:** If an attribute is defined as an object, POML will attempt to parse the attribute value as a JSON string. For example, `data="{{{name: 'John', age: 30}}}"` or `data='{"name":"John","age":30}'` will be parsed into the corresponding JavaScript object.
* **String:** If an attribute is a string, no casting is performed.

In the following example, the first auto-casting happened at let, where `true` is converted to boolean at `let` expression.

```xml
<poml>
  <let name="boolVar" type="boolean" value="true"/>
  <let name="numVar" type="number" value="42"/>
  <let name="objVar" type="object" value="{{ { key: 'value' } }}"/>

  <MyComponent boolProp="{{boolVar}}" numProp="{{numVar}}" objProp="{{objVar}}" stringProp="hello"/>
</poml>
```

If MyComponent is defined with `boolProp` as boolean, `numProp` as number, `objProp` as object, and `stringProp` as string, the values will be interpreted and auto-casted again when `MyComponent` is used.

### For Attribute

To loop over a list, use the `for` attribute. The syntax is `for="itemName in listName"`.

```xml
<poml>
  <list>
    <item for="item in ['apple', 'banana', 'cherry']">{{item}}</item>
  </list>
</poml>
```

This will render a list with "apple", "banana", and "cherry".

#### Loop Variables

Inside the loop, you have access to special `loop` variables:

- `loop.index`: The current iteration index (starting from 0).
- `loop.length`: The total number of items in the list.
- `loop.first`: `true` if it's the first iteration, `false` otherwise.
- `loop.last`: `true` if it's the last iteration, `false` otherwise.

Example:

```xml
<poml>
<let name="all_demos" value='[
    { "input": "What is your name?", "output": "My name is POML." },
    { "input": "What can you do?", "output": "I can generate prompts." }
]'/>
  <examples>
    <example for="example in all_demos" chat="false" caption="Example {{ loop.index + 1 }}" captionStyle="header">
      <input>{{ example.input }}</input>
      <output>{{ example.output }}</output>
    </example>
  </examples>
</poml>
```

This will generate two examples, with captions "Example 1" and "Example 2", displaying the input and output from each demo in the `all_demos` array. Note that we use `loop.index + 1` because `loop.index` starts from 0.

### If Condition

You can conditionally render elements using the `if` attribute:

```xml
<poml>
  <let name="isVisible" value="true"/>
  <let name="isHidden" value="{{ !isVisible }}"/>
  <p if="isVisible">This paragraph is visible.</p>
  <p if="isHidden">This paragraph is hidden.</p>
</poml>
```

If `isVisible` is `true`, the first paragraph will be rendered. The second paragraph will not be rendered because isHidden is false. The value of `if` can be a simple variable name (which is treated as a boolean) or a POML expression.

### Include Files

You can split prompts into multiple files and include them using the `<include>` tag.

```xml
<poml>
  <include src="snippet.poml" />
</poml>
```

The file specified in `src` is read and its contents are injected as if they were written in place. Variables from the current context are available inside the included file. The `for` and `if` attributes work as expected:

```xml
<poml>
  <include src="row.poml" for="i in [1,2,3]" />
  <include src="footer.poml" if="showFooter" />
</poml>
```

## Stylesheet

POML allows you to define styles for your elements using the `<stylesheet>` tag.  This enables you to apply CSS-like styles (or, more generally, component attributes) to your markup.

### Using Stylesheet

You can define styles within a `<stylesheet>` tag. The stylesheet must be a valid JSON object and must be placed directly under the root `<poml>` element.

```xml
<poml>
  <stylesheet>
    {
      "p": {
        "syntax": "json"
      }
    }
  </stylesheet>
  <p>This text will be rendered as JSON.</p>
</poml>
```

In this example, all `<p>` elements will have their `syntax` attribute set to `"json"`. You can set any attribute of a component using the stylesheet.

### ClassName Attribute

Elements can be identified with a `className` attribute for styling.  The stylesheet can then target elements with specific class names using a CSS-like selector syntax (using a dot `.` before the class name).

```xml
<poml>
  <table className="csv" records="[[1,2,3],[4,5,6]]"/>
  <stylesheet>
    {
      ".csv": {
        "syntax": "csv",
        "writerOptions": "{\\"csvSeparator\\": \\";\\", \\"csvHeader\\": false}"
      }
    }
  </stylesheet>
</poml>
```

Here, the `<table>` element has the class name "csv".  The stylesheet targets elements with the class "csv" (using `.csv`) and sets their `syntax` to "csv" and `writerOptions` to a specific JSON string. Note the escaped backslashes (`\\`) in the `writerOptions` value, which are necessary because the stylesheet itself is a JSON string.  This example will render to:

```
1;2;3
4;5;6
```

**NOTE:** *The writerOptions API is experimental and is subject to change.*



================================================
FILE: docs/language/proposals/poml_extended.md
================================================
# Extended POML File Format Design Specification

> Status: Under implementation

## Overview

This document describes the design for an extended POML file format that supports mixed content files - files that can contain both pure text (e.g., Markdown) and POML markup elements seamlessly integrated together.

## Current Limitations

The current POML implementation requires files to be fully enclosed within `<poml>...</poml>` tags. Even though the outer level `<poml>...</poml>` can be optional, the markup file is always parsed with one single pass of XML parser. This creates friction when users want to:

1. Write primarily text-based documents (like Markdown or Jinja) with occasional POML components
2. Usually need to escape characters like `<` and `>` in text content
3. Gradually migrate existing text files to use POML features

## Design Goals

1. **Backward Compatibility**: Most of existing POML files should continue to work without changes
2. **Flexibility**: Support pure text files with embedded POML elements
3. **Seamless Integration**: Allow switching between text and POML modes within a single file
<!-- 4. **Component Discovery**: Automatically detect POML elements from `componentDocs.json` -->

## File Format Specification

### Extended POML Files

Extended POML files can contain:

1. **Pure Text Content**: Regular text content (Markdown, plain text, etc.)
2. **POML Element Pairs**: Any element pair defined in `componentDocs.json` (e.g., `<poml>...</poml>`, `<p>...</p>`, `<task>...</task>`)
3. **Mixed Content**: Combination of pure text and POML elements

### Element Detection

The system will assume the whole file is a pure text file and detects certain parts as POML elements based on the following:

1. Loading component definitions from `componentDocs.json` and extracting valid POML component names and their aliases.
2. Scanning for opening tags that match these components, and scanning until the corresponding closing tag is found.
3. If a special tag `<text>...</text>` is found within a POML segment, it will be treated as pure text content and processed following the rules above (step 1 and 2).

An example is shown below:

#### Example 1

```markdown
# My Analysis Document

This is a regular markdown document that explains the task.

<task>
  Analyze the following data and provide insights.
</task>

Here are some key points to consider:

- Data quality
- Statistical significance  
- Business impact

<examples>
  <example>
    <input>Sample data point 1</input>
    <output>Analysis result 1</output>
  </example>
</examples>

## Conclusion

The analysis shows...
```

#### Example 2

```xml
<poml>
  <task>Process the following data</task>
  <text>
    This is **markdown** content that will be processed as pure text.
    
    - Item 1
    - Item 2

    {{ VARIABLES_WILL_ALSO_SHOWN_AS_IS }}
    <cp caption="Nested POML">This is a nested POML component that will be processed as POML.</cp>

    No POML processing happens here.
  </text>
  <hint>Remember to check the format</hint>
</poml>

There can be some intervening text here as well.

<poml>
  <p>You can add another POML segment here: {{variable_will_be_substituted}}</p>
</poml>

<p>POML elements do not necessarily reside in a <text><poml> (the <poml> here is processed as is.)</text> element.</p>
```

**Escaping Note**: To directly show a POML tag in the text, users can use a `<text>` tag to wrap the content, as shown in the example above. If they want to escape a pair such as `<poml>...</poml>`, they can escape the opening tag and closing tag respectively, such as `<text><poml></text>...<text></poml></text>`.

### File-level Metadata

Metadatas are information that is useful when parsing and rendering the file, such as context variables, stylesheets, version information, file paths, etc.
File-level metadata can be included at any place of the file in a special `<meta>` tag. This metadata will be processed before any content parsing.

## Architecture Design

### High-level Processing Pipeline

The core of the new architecture is a three-pass process: Segmentation, Metadata Extraction, and Recursive Rendering.

#### I. Segmentation Pass

This initial pass is a crucial preprocessing step that scans the raw file content and partitions it into a hierarchical tree of segments. It does **not** parse the full XML structure of POML blocks; it only identifies their boundaries.

* **Objective**: To classify every part of the file as `META`, `POML`, or `TEXT` and build a nested structure.
* **Algorithm**:
  1. Load all valid POML component tag names (including aliases) from `componentDocs.json`. This set of tags will be used for detection.
  2. Initialize the root of the segment tree as a single, top-level `TEXT` segment spanning the entire file, unless the root segment is a single `<poml>...</poml>` block spanning the whole file (in which case it will be treated as a `POML` segment).
  3. Use a stack-based algorithm to scan the text.
    * When an opening tag (e.g., `<task>`) that matches a known POML component is found, push its name and start position onto the stack. This marks the beginning of a potential `POML` segment.
    * When a closing tag (e.g., `</task>`) is found that matches the tag at the top of the stack, pop the stack. This marks a complete `POML` segment. This new segment is added as a child to the current parent segment in the tree.
    * The special `<text>` tag is handled recursively. If a `<text>` tag is found *inside* a `POML` segment, the scanner will treat its content as a nested `TEXT` segment. This `TEXT` segment can, in turn, contain more `POML` children.
    * Any content not enclosed within identified `POML` tags remains part of its parent `TEXT` segment.
  4. `<meta>` tags are treated specially. They are identified and parsed into `META` segments at any level but are logically hoisted and processed first. They should not have children.
* **Output**: A `Segment` tree. For backward compatibility, if the root segment is a single `<poml>...</poml>` block spanning the whole file, the system can revert to the original, simpler parsing model.

**`Segment` Interface**: The `children` property is key to representing the nested structure of mixed-content files.

```typescript
interface Segment {
  id: string;                      // Unique ID for caching and React keys
  kind: 'META' | 'TEXT' | 'POML';
  start: number;
  end: number;
  content: string;                 // The raw string content of the segment
  parent?: Segment;                 // Reference to the parent segment
  children: Segment[];             // Nested segments (e.g., a POML block within text)
  tagName?: string;                 // For POML segments, the name of the root tag (e.g., 'task')
}
```

#### II. Metadata Processing

Once the segment tree is built, all `META` segments are processed.

  * **Extraction**: Traverse the tree to find all `META` segments.
  * **Population**: Parse the content of each `<meta>` tag and populate the global `PomlContext` object.
  * **Removal**: After processing, `META` segments are removed from the tree to prevent them from being rendered.

**`PomlContext` Interface**: This context object is the single source of truth for the entire file, passed through all readers. It's mutable, allowing stateful operations like `<let>` to have a file-wide effect.

```typescript
interface PomlContext {
  variables: { [key: string]: any }; // For {{ substitutions }} and <let> (Read/Write)
  texts: { [key: string]: React.ReactElement }; // Maps TEXT_ID to content for <text> replacement (Read/Write)
  stylesheet: { [key: string]: string }; // Merged styles from all <meta> tags (Read-Only during render)
  minimalPomlVersion?: string;      // From <meta> (Read-Only)
  sourcePath: string;                // File path for resolving includes (Read-Only)
}
```

#### III. Text/POML Dispatching (Recursive Rendering)

Rendering starts at the root of the segment tree and proceeds recursively. A controller dispatches segments to the appropriate reader.

* **`PureTextReader`**: Handles `TEXT` segments.

  * Currently we directly render the pure-text contents as a single React element. In future, we can:
    * Renders the text content, potentially using a Markdown processor.
    * Performs variable substitutions (`{{...}}`) using the `variables` from `PomlContext`. The logic from `handleText` in the original `PomlFile` should be extracted into a shared utility for this.
  * Iterates through its `children` segments. For each child `POML` segment, it calls the `PomlReader`.

* **`PomlReader`**: Handles `POML` segments.

  * **Pre-processing**: Before parsing, it replaces any direct child `<text>` regions with a self-closing placeholder tag containing a unique ID: `<text ref="TEXT_ID_123" />`. The original content of the `<text>` segment is stored in `context.texts`. This ensures the XML parser inside `PomlFile` doesn't fail on non-XML content (like Markdown).
  * **Delegation**: Instantiates a modified `PomlFile` class with the processed segment content and the shared `PomlContext`.
  * **Rendering**: Calls the `pomlFile.react(context)` method to render the segment.

* **`IntelliSense Layer`**: The segment tree makes it easy to provide context-aware IntelliSense. By checking the `kind` of the segment at the cursor's offset, the request can be routed to the correct provider—either the `PomlReader`'s XML-aware completion logic or a simpler text/variable completion provider for `TEXT` segments.

**`Reader` Interface**: This interface defines the contract for both `PureTextReader` and `PomlReader`.

```typescript
interface Reader {
  read(segment: Segment, context: PomlContext?): React.ReactElement;
  getHoverToken(segment: Segment, offset: number): PomlToken | undefined;
  getCompletions(offset: number): PomlToken[];
}
```

### Implementation & `PomlFile` Refactoring

To achieve this design, the existing `PomlFile` class needs significant refactoring. Its role changes from a file-level controller to a specialized parser for `POML` segments.

#### **Key Modifications to `PomlFile`**

1. **Constructor (`new PomlFile`)**:

  * **Remove Auto-Wrapping**: The `autoAddPoml` logic must be **removed**. The `PomlReader` will only pass it well-formed XML content corresponding to a single `POML` segment. The constructor will now assume the input `text` is a valid XML string.
  * **Receive Context**: The constructor should accept the `PomlContext` object to access shared state.

2. **State Management (`handleLet`)**:

  * The `<let>` tag's implementation must be modified to read from and write to the **shared `PomlContext.variables` object**, not a local context. This ensures that a variable defined in one POML block is available to subsequent POML blocks in the same file.

3. **Handling `<include>`**:

  * The `handleInclude` method should be **removed** from `PomlFile`. Inclusion is now handled at a higher level by the main processing pipeline. When the `PomlReader` encounters an `<include>` tag, it will invoke the entire pipeline (Segmentation, Metadata, Rendering) on the included file and insert the resulting React elements.

4. **Parsing `TEXT` Placeholders**:

  * The core `parseXmlElement` method needs a new branch to handle the `<text ref="..." />` placeholder.
  * When it encounters this element:
    1. It extracts the `ref` attribute (e.g., `"TEXT_ID_123"`).
    2. It looks up the corresponding raw text from `context.texts`.
    3. It fetches from the `context.texts` map and returns a React element containing the pure text content.



================================================
FILE: docs/python/core.md
================================================
# Python POML Core Reference

::: poml

::: poml.prompt



================================================
FILE: docs/python/index.md
================================================
# POML Python SDK

This documentation provides an overview of the POML Python SDK, which allows you to work with POML files and components in your Python projects.

## Installation

### Stable Release
```bash
pip install --upgrade poml
```

### Nightly Build
```bash
pip install --upgrade --pre --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ poml
```

## References

- [POML Core Reference](./core.md): Detailed reference for the core POML components and utilities.
- [POML Integration](./integration.md): Reference on how to integrate POML with your Python applications.



================================================
FILE: docs/python/integration.md
================================================
# POML Integrations

::: poml.integration.agentops

::: poml.integration.langchain

::: poml.integration.mlflow

::: poml.integration.weave



================================================
FILE: docs/typescript/index.md
================================================
# TypeScript API Reference

This documentation is auto-generated from the TypeScript source code using TypeDoc.

## Installation

### Stable Release
To use the POML TypeScript API, install the package via npm:

```bash
npm install pomljs
```

### Nightly Build
```bash
npm install pomljs@nightly
```

## Quick Start

```tsx
import { Paragraph, Image } from 'poml/essentials';
import { read, write } from 'poml';
const prompt = <Paragraph>
  Hello, world! Here is an image:
  <Image src="photo.jpg" alt="A beautiful scenery" />
</Paragraph>;

// Parse the prompt components into an intermediate representation (IR)
const ir = await read(prompt);

// Render it to different formats
const markdown = write(ir);
```

## Links

- [Components Documentation](../language/components.md): detailed component specifications with examples and parameters.
- [TypeScript API Reference](./reference/README.md): auto-generated API reference for TypeScript components and utilities.



================================================
FILE: docs/vscode/configuration.md
================================================
# Configuration

Configure POML in VS Code settings (`Ctrl+,` or `Cmd+,`).

## Example Complete Configuration

```json
{
  "poml.languageModel.provider": "openai",
  "poml.languageModel.model": "gpt-4o",
  "poml.languageModel.apiKey": "sk-your-api-key-here",
  "poml.languageModel.apiUrl": "https://api.openai.com/v1/",
  "poml.languageModel.temperature": 0.7,
  "poml.languageModel.maxTokens": 1500,
  "poml.scrollPreviewWithEditor": true,
  "poml.markEditorSelection": true,
  "poml.trace": "off"
}
```

## Language Model Configuration

The following settings mainly control the language model used for POML testing feature within VSCode.

### Language Model Provider

```json
{
  "poml.languageModel.provider": "openai"
}
```

**Options:** `openai`, `microsoft`, `anthropic`, `google`  
**Default:** `openai`

### Model Name

```json
{
  "poml.languageModel.model": "gpt-4o"
}
```
**Default:** `gpt-4o`  
For Azure OpenAI, use the deployment name. For other providers, use the model code name.

### Temperature

```json
{
  "poml.languageModel.temperature": 0.5
}
```
**Default:** `0.5`  
**Range:** `0.0` to `2.0`  
Controls randomness in responses. Lower values are more deterministic.

### Max Tokens

```json
{
  "poml.languageModel.maxTokens": 2000
}
```
**Default:** `0` (unlimited)  
Maximum number of completion tokens to generate.

### API Key

```json
{
  "poml.languageModel.apiKey": "your-api-key-here"
}
```
**Required** for most providers. Keep this secure and never commit to version control.

### API URL

```json
{
  "poml.languageModel.apiUrl": "https://api.openai.com/v1/"
}
```
**Examples:**
- OpenAI: `https://api.openai.com/v1/`
- Azure OpenAI: `https://westeurope.api.cognitive.microsoft.com/`
- Custom OpenAI-compatible: `https://api.example.com/v2/`

### API Version

```json
{
  "poml.languageModel.apiVersion": "2024-02-15-preview"
}
```
**Optional** - Mainly used for OpenAI and Azure OpenAI services.

### Provider-Specific Examples

#### Azure OpenAI
```json
{
  "poml.languageModel.provider": "microsoft",
  "poml.languageModel.model": "my-gpt4-deployment",
  "poml.languageModel.apiKey": "your-azure-api-key",
  "poml.languageModel.apiUrl": "https://your-resource.openai.azure.com/",
  "poml.languageModel.apiVersion": "2024-02-15-preview"
}
```

#### Anthropic Claude
```json
{
  "poml.languageModel.provider": "anthropic",
  "poml.languageModel.model": "claude-3-5-sonnet-20241022",
  "poml.languageModel.apiKey": "your-anthropic-api-key"
}
```

#### Google Gemini
```json
{
  "poml.languageModel.provider": "google",
  "poml.languageModel.model": "gemini-1.5-pro",
  "poml.languageModel.apiKey": "your-google-api-key"
}
```

## Preview & Editor Settings

> These features need further testing. Please report bugs if you need this feature but it does not work as expected.

### Scroll Synchronization

```json
{
  "poml.scrollPreviewWithEditor": true,
  "poml.scrollEditorWithPreview": true
}
```
**Default:** `true`  
Synchronize scrolling between editor and preview panes.

### Editor Selection

```json
{
  "poml.markEditorSelection": true,
  "poml.doubleClickToSwitchToEditor": true
}
```
**Default:** `true`  
Highlight current editor selection in preview and enable double-click navigation.

## Development Settings

### Debugging
```json
{
  "poml.trace": "verbose"
}
```
**Options:** `off`, `verbose`  
**Default:** `off`

Enable detailed tracing for troubleshooting.

### Telemetry

```json
{
  "poml.telemetry.connection": ""
}
```
**Default:** `""` (empty)  
Development setting for telemetry connection string.



================================================
FILE: docs/vscode/features.md
================================================
# VS Code IntelliSense Features

POML comes with features that enhance your editing experience in Visual Studio Code, offering a more interactive way to work with your prompt files. Here’s how to make the most of these features:

### Diagnostics

![VSCode Diagnostics](../media/vscode-diagnosis.png)

The POML extension provides real-time error detection and validation for your `.poml` files through VS Code's diagnostics system. This helps you catch syntax errors, invalid attributes, and other issues as you write your prompts.

#### Types of Diagnostics

The POML extension detects various types of issues:

- **Syntax Errors**: Invalid XML/POML syntax, unclosed tags, malformed attributes
- **Component Validation**: Unknown components or incorrect component usage
- **Attribute Errors**: Invalid attributes for specific components or incorrect attribute values
- **File Reference Issues**: Problems with referenced context files, stylesheets, or other external resources
- **Expression Evaluation Errors**: Issues with template expressions and variable references

#### Real-time Validation and Working with Multiple Files

Diagnostics are updated automatically as you edit:

1. **On File Save**: Complete validation is triggered when you save the file
2. **Incremental Updates**: Basic syntax checking happens as you type
3. **Context-aware**: Validation considers your context files and stylesheets for more accurate error reporting

The diagnostics system can validate references across multiple files. It vlidates that referenced `.context.json` files exist and are properly formatted. It also checks `.stylesheet.json` files for syntax and structure issues.

### Hover Tooltips

When you hover over tags, attributes, or expression parts in your `.poml` file, VSCode will display helpful tooltips.

- **Tags:** Hovering over a tag (e.g., `<p>`) will show you the documentation for that component (if available).
- **Attributes:** Hovering over an attribute (e.g., `speaker` in `<p speaker="human">`) will show you the documentation for that attribute, including its type and accepted values.
- **Errors:** Hovering over a problematic element, it will show you the error cause and reason, which will help you understand the issue and fix it.

To use it, simply open your `.poml` file in VSCode and hover over any token.

### Side Preview

The side preview feature shows a live rendering of your prompt. As you make changes, you can see how your prompt structure and styles are applied.

Install the POML VSCode extension, then open your `.poml` file. Activate the side preview panel by:

1. **Click Show Preview Button:** Click the show preview button at the top-right corner of active editor, or type "POML: Open POML Preview" in the command palette and select the command.
2. **Side-by-side:** The preview will update automatically as you edit.

### Auto-completion

Autocompletion assists you by suggesting component tags, attribute names, and possible attribute values. This helps ensure your syntax is correct and speeds up development.

While editing a `.poml` file in VSCode:

- **Tag Completion:** Start typing a tag name (e.g., `<p`). VSCode with the POML extension will offer completions, such as `<p>`, `<paragraph>`, or other available components. It also suggests closing tags.
- **Attribute Completion:** Inside an opening tag, type a space or start typing an attribute name (e.g., `class`).  You'll see suggestions for valid attributes for that component (e.g., `className`).
- **Attribute Value Completion:**  For some attributes, POML can suggest possible values. For example, if you type `<question speaker="`, you might see suggestions like `"human"` or `"ai"`.

This feature significantly improves the efficiency and accuracy of writing POML code.

### Expression Evaluation with CodeLens

![Expression Evaluation](../media/vscode-evaluate.png)

The POML extension provides CodeLens buttons that allow you to evaluate template variables directly in your editor. This powerful debugging feature helps you understand what values your expressions produce locally.

#### How to Use Expression Evaluation

1. **CodeLens Buttons**: When you open a `.poml` file, you'll see "▶️ Evaluate" buttons appearing above expressions and variables.
2. **Click to Evaluate**: Click any "▶️ Evaluate" button to execute the expression and see its result.
3. **View Output**: Go to View → Output in VS Code. Results are displayed in the **POML Language Server** output channel.

#### What Gets Evaluated

The CodeLens evaluation feature works with:

- **Template Expressions**: Any `{{ expression }}` in your POML content
- **Variable Definitions**: `<let>` element value attributes
- **Control Flow**: Expressions in `for` and `if` attributes
- **Schema Expressions**: Expressions in meta elements with `lang="expr"`

#### Example

```xml
<poml>
  <let name="items" value='["apple", "banana", "cherry"]' />
  <let name="count" value="items.length" />
  
  <p>We have {{ count }} items: {{ items.join(', ') }}</p>
  
  <meta type="responseSchema" lang="expr">
    z.object({
      total: z.number().max(count),
      items: z.array(z.enum(items))
    })
  </meta>
</poml>
```

In this example, you can evaluate:
- The `items` array definition to see `["apple", "banana", "cherry"]`
- The `count` calculation to see `3`
- The template expressions to see `"3"` and `"apple, banana, cherry"`
- The schema expression to see the generated Zod schema object

## Testing Prompts

![Testing Prompts](../media/vscode-test.png)

POML provides integrated testing capabilities that allow you to test your prompts directly within VS Code against various language models. This feature helps you validate your prompts and see their output without leaving the editor.

### Testing with Chat Models

Use the **Test current prompt on Chat Models** command to test your `.poml` file with chat-based language models. This sends your prompt to the configured language model and displays the response in VS Code's output panel.

### Testing with Text Completion Models  

For non-chat models, use the **Test current prompt on Text Completion Models** command. This is useful for testing prompts designed for text completion rather than conversational AI models.

### Rerunning Tests

The **Clear output and rerun last test** command allows you to quickly clear the previous output and rerun your last test, making it easy to iterate on your prompts.

### Aborting Tests

If a test is taking too long or you need to stop it, use the **Abort current prompt test** command to cancel the ongoing request.

Before testing prompts, make sure you have configured your [language model settings](./configuration.md):
- Set your model provider (OpenAI, Azure OpenAI, Anthropic, or Google GenAI)
- Configure your API key and endpoint URL
- Choose your preferred model name

## Prompt Gallery

The Prompt Gallery provides access to pre-built prompt templates and allows you to manage your own custom prompts. Access it from the POML activity bar in VS Code.

### Built-in Templates

The gallery includes several built-in prompt templates covering common use cases:
- **Ask**: General question-answering prompts
- **Chat**: Conversational prompts
- **Edit**: Text editing and revision prompts

Gallery prompts can be used with the POML chat participant by typing `@poml /<prompt-name>` in any VS Code chat interface, where `<prompt-name>` is the name of your gallery prompt.

### Managing Custom Prompts

You can add your own prompts to the gallery:

1. **Add Prompt**: Click the plus (+) icon in the gallery view to add a new prompt template
2. **Edit Prompt**: Use the pencil icon to modify existing user-created prompts
3. **Delete Prompt**: Remove prompts you no longer need with the trash icon

The usage of custom prompts are the same as built-in prompts. You can use them in the POML chat participant or test them directly.

## List of Available Commands

| Command | Description |
|---------|-------------|
| `poml.test` | Test current prompt on Chat Models |
| `poml.testNonChat` | Test current prompt on Text Completion Models |
| `poml.testRerun` | Clear output and rerun last test |
| `poml.testAbort` | Abort current prompt test |
| `poml.showPreview` | Open POML Preview |
| `poml.showPreviewToSide` | Open POML Preview to the Side |
| `poml.showLockedPreviewToSide` | Open Locked POML Preview |
| `poml.showSource` | Show Source File |
| `poml.addContextFile` | Add Context File |
| `poml.addStylesheetFile` | Add Stylesheet File |
| `poml.removeContextFile` | Remove Context File |
| `poml.removeStylesheetFile` | Remove Stylesheet File |
| `poml.gallery.addPrompt` | Add Prompt to Gallery |
| `poml.gallery.deletePrompt` | Delete Prompt from Gallery |
| `poml.gallery.editPrompt` | Edit Prompt in Gallery |
| `poml.telemetry.completion` | Telemetry: Completion |


================================================
FILE: docs/vscode/index.md
================================================
# POML Visual Code Extension

The POML Visual Studio Code extension provides comprehensive support for working with POML files.

## Features

- **Syntax Highlighting**: Full syntax highlighting for `.poml` files
- **IntelliSense**: Auto-completion and suggestions
- **Preview Panel**: Live preview of POML rendering
- **Model Testing**: Test prompts directly in VS Code
- **Gallery**: Built-in prompt gallery for common patterns

## Installation

### Stable Release

Install from [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=poml-team.poml).

You can also install the extension manually by downloading the `.vsix` file from our [GitHub releases page](https://github.com/microsoft/poml/releases) and installing it in VS Code via the Extensions view.

### Nightly Build

Download the nightly build from this [index](https://poml-vscode-nightly.scottyugochang.workers.dev/)

Install the downloaded `.vsix` file in VS Code via the Extensions view (thanks [stackoverflow](https://stackoverflow.com/questions/42017617/how-to-install-vs-code-extension-manually) for the image below).

![Manual installation instructions](../media/vscode-manual-install.png)

Before testing prompts with the POML toolkit, make sure you have configured your preferred LLM model, API key, and endpoint. If these are not set, prompt testing will not work. [Configuration instructions](./configuration.md).



================================================
FILE: examples/README.md
================================================
# POML Example Library

This directory contains example POML files demonstrating a variety of use cases. Examples are organized by difficulty:

- **Beginner:** Filenames start with `1XX_`
- **Intermediate:** Filenames start with `2XX_`
- **Advanced:** Filenames start with `3XX_`

Each example highlights different POML features, such as structured prompting, data handling, and templating.

Non-POML examples (e.g., Python or JavaScript scripts) are prefixed with `4XX_` and use appropriate file extensions. Inline comments explain their usage.

## Contributing

Contributions are welcome! To add or improve an example:

- Follow the naming conventions above.
- Include clear explanations and comments in your examples.
- Place any assets in an `assets/` subdirectory within the example's folder.
- If your example includes expected output, place it in an `expects/` subdirectory.

Submit your changes via pull request.



================================================
FILE: examples/101_explain_character.poml
================================================
<!-- POML should always start with a POML tag to harvest most of its features. -->
<poml>
  <role>You are a teacher explaining figures to kids.</role>
  <!-- Use components like role and task to help you organize your intentions. This also usually comes with better LLM performance. -->
  <task>Please describe the figure first and then provide background knowledge to help kids understand the figure.</task>
  <output-format>Please write your response in a friendly tone.</output-format>

  <!-- Use properties like captionStyle and caption to customize your prompt style. -->
  <hint captionStyle="header" caption="Background Knowledge">
    <!-- Document can be used to import a word document, a PDF or a pure text. -->
    <Document src="assets/101_tom_and_jerry.docx"/>
  </hint>

  <!-- Organize few-shot examples with example. This will automatically generates an interaction of human and AI messages. -->
  <example>
    <input>
      <!-- alt strings help models without vision capabilities to understand the images. -->
      <!-- Specify syntax = "multimedia" to send the image itself to the prompt. -->
      <img src="assets/101_tom_cat.jpg" alt="The image contains the Tom cat character." syntax="multimedia" />
    </input>
    <output>
      <!-- Import the results from a txt file. -->
      <Document src="assets/101_tom_introduction.txt"/>
    </output>
  </example>

  <!-- In this case, the input is inferred as a human message. -->
  <input><img src="assets/101_jerry_mouse.jpg" alt="The image contains the Jerry mouse character." syntax="multimedia" /></input>

</poml>


================================================
FILE: examples/102_render_xml.poml
================================================
<poml syntax="xml">
<role>Senior Systems Architecture Consultant</role>
<task>Legacy System Migration Analysis</task>

<cp caption="Context">
  <list>
    <item>Fortune 500 retail company</item>
    <item>Current system: 15-year-old monolithic application</item>
    <item>500+ daily users</item>
    <item>99.99% uptime requirement</item>
  </list>
</cp>

<cp caption="Required Analysis" captionSerialized="RequiredAnalysis">
  <list listStyle="decimal">
    <item>Migration risks and mitigation strategies</item>
    <item>Cloud vs hybrid options</item>
    <item>Cost-benefit analysis</item>
    <item>Implementation roadmap</item>
  </list>
</cp>

<output-format>
  <list>
    <item>Executive brief (250 words)</item>
    <item>Technical details (500 words)</item>
    <item>Risk matrix</item>
    <item>Timeline visualization</item>
    <item>Budget breakdown</item>
  </list>
</output-format>

<cp caption="Constraints">
  <list>
    <item>Must maintain operational continuity</item>
    <item>Compliance with GDPR and CCPA</item>
    <item>Maximum 18-month implementation window</item>
    </list>
  </cp>
</poml>


================================================
FILE: examples/103_word_todos.poml
================================================
<poml>
<Task>I developed a project called Prompt Wizard and I want to write a blog to publish on the company website. I have already written a draft of the blog. There has been figures, numbers in tables, the key challenges, motivations, as well as some titles and subtitles. I want you to complete the <code>[TODO]</code>s in the draft.</Task>

<OutputFormat>Your response should be in the following format:

<Code inline="false">
<List>
<ListItem>TODO 1: </ListItem>
<ListItem>TODO 2: </ListItem>
<ListItem>...</ListItem>
</List>
</Code>
</OutputFormat>

<input>
<Document src="assets/103_prompt_wizard.docx" />
</input>

<stylesheet>
{
    "image": {
        "maxWidth": 500,
        "maxHeight": 500
    }
}
</stylesheet>
</poml>


================================================
FILE: examples/104_financial_analysis.poml
================================================
<poml>
<SystemMessage>

<task>
Given the stock ticker, provide a full and up-to-date financial analysis covering the following aspects, cite sources.
</task>

<list listStyle="decimal">
<item>Current stock price, recent performance trends, and historical comparison.</item>
<item>Key financial ratios (e.g., P/E ratio, forward P/E, Price/Free cash flow, EPS growth this year, Return on equity, return on investment, current ratio, net profit margin, debt-to-equity ratio) and what they indicate about the company's financial health.</item>
<item>Support and resistance prices of the stock and how current indicators may drive the direction of the stock</item>
<item>Recent earnings reports, revenue growth or decline, and net income trends over the past quarter. Please also include if latest EPS report beat estimates.</item>
<item>Industry comparison to determine the company's standing relative to its peers.</item>
<item>Current analyst ratings, target price forecasts, and recent upgrades or downgrades.</item>
<item>Overall summary on whether the stock is considered a 'buy', 'hold', or 'sell' based on current financial data and market sentiment.</item>
</list>
</SystemMessage>

<HumanMessage>
<table src="assets/104_mag7.xlsx" selectedRecords=":-1" syntax="markdown" />

<p>The following two charts on a visualization of the table above. One of them shows the absolute price of the stocks, and the other one shows the price normalized by the price of the first day.</p>

<img src="assets/104_chart_price.png" syntax="multimedia" />

<img src="assets/104_chart_normalized_price.png" syntax="multimedia" />

<Hint>
The table contains stock tickers of 7 companies. Please analyze and give financial analysis and comparison for them.
</Hint>
</HumanMessage>

</poml>



================================================
FILE: examples/105_write_blog_post.poml
================================================
<poml>
<task className="instruction">Create a blog post with these specifications:</task>

<output-format className="instruction">
<list listStyle="decimal">
  <item>Title: [SEO-friendly title]</item>
  <item>Introduction (100 words)
  <list>
    <item>Hook statement</item>
    <item>Context setting</item>
    <item>Main points preview</item>
  </list>
  </item>
  <item>Main body (800 words)
  <list>
    <item>3-4 main points</item>
    <item>Each point: [subtitle + 200 words]</item>
    <item>Include real examples</item>
    <item>Add actionable tips</item>
  </list>
  </item>
  <item>Conclusion (100 words)
  <list>
    <item>Summary of key points</item>
    <item>Call to action</item>
  </list>
  </item>
</list>
</output-format>

<cp className="instruction" caption="Style" captionSerialized="style">
<list>
  <item>Tone: Professional but conversational</item>
  <item>Level: Intermediate audience</item>
  <item>Voice: Active, engaging</item>
  <item>Format: Scannable, with subheadings</item>
</list>
</cp>

<cp className="instruction" caption="Include" captionSerialized="include">
<list>
  <item>Practical examples</item>
  <item>Statistics or research</item>
  <item>Actionable takeaways</item>
  <item>Relevant analogies</item>
</list>
</cp>
</poml>


================================================
FILE: examples/106_research.poml
================================================
<poml>
<task>You are given various potential options or approaches for a project. Convert these into a well-structured research plan.</task>

<stepwise-instructions>
<list listStyle="decimal">
<item>Identifies Key Objectives
  <list listStyle="dash">
    <item>Clarify what questions each option aims to answer</item>
    <item>Detail the data/info needed for evaluation</item>
  </list>
</item>
<item>Describes Research Methods
  <list listStyle="dash">
    <item>Outline how you’ll gather and analyze data</item>
    <item>Mention tools or methodologies for each approach</item>
  </list>
</item>

<item>Provides Evaluation Criteria
  <list listStyle="dash">
    <item>Metrics, benchmarks, or qualitative factors to compare options  </item>
    <item>Criteria for success or viability</item>
  </list>
</item>

<item>Specifies Expected Outcomes
  <list listStyle="dash">
    <item>Possible findings or results  </item>
    <item>Next steps or actions following the research</item>
  </list>
</item>
</list>

Produce a methodical plan focusing on clear, practical steps.
</stepwise-instructions>
</poml>


================================================
FILE: examples/107_read_report_pdf.poml
================================================
<poml>
<p>Provide a concise executive summary of the following text, highlighting key points, objectives, and outcomes. Keep the summary under 150 words and ensure it is suitable for a professional audience.</p>
<Document syntax="text" src="assets/107_usenix_paper.pdf" selectedPages="1:3" />
</poml>



================================================
FILE: examples/201_orders_qa.poml
================================================
<poml>
  <role>You are a chatbot agent answering customer's questions in a chat.</role>

  <task>
    Your task is to answer the customer's question using the data provided in the data section.
    <!-- Use listStyle property to change the style of a list. -->
    <list listStyle="decimal">
      <item>You can access order history in the orders section including email id and order total with payment summary.</item>
      <item>Refer to orderlines for item level details within each order in orders.</item>
    </list>
  </task>

  <!-- cp means CaptionedParagraph, which is a paragraph with customized headings. -->
  <cp caption="Data">
    <cp caption="Orders">
      <!-- Use table to read a csv file. By default, it follows its parents' style (markdown in this case). -->
      <table src="assets/201_orders.csv" />
    </cp>

    <cp caption="Orderlines">
      <!-- Use syntax to specify its output format. -->
      <table src="assets/201_orderlines.csv" syntax="tsv" />
    </cp>
  </cp>

  <!-- This can also be stepwise-instructions, and it's case-insensitive. -->
  <StepwiseInstructions>
    <!-- Read a file and save it as instructions -->
    <let src="assets/201_order_instructions.json" name="instructions"/>
    <!-- Use a for loop to iterate over the instructions, use {{ }} to evaluate an expression -->
    <p for="ins in instructions">
      Instruction {{loop.index+1}}: {{ ins }}
    </p>
  </StepwiseInstructions>

  <!-- Specify the speaker of a block. -->
  <HumanMessage>
    <!-- Use a question-answer format. -->
    <qa>How much did I pay for my last order?</qa>
  </HumanMessage>

  <!-- Use stylesheet (a CSS-like JSON) to modify the style in a batch. -->
  <stylesheet>
    {
      "cp": {
        "captionTextTransform": "upper"
      }
    }
  </stylesheet>
</poml>



================================================
FILE: examples/202_arc_agi.poml
================================================
<poml>
<SystemMessage>Be brief and clear in your responses</SystemMessage>
<let src="assets/202_arc_agi_data.json"/>
<HumanMessage>
<p>Find the common rule that maps an input grid to an output grid, given the examples below.</p>
<examples>
  <example for="example in train" chat="false" caption="Example {{ loop.index }}" captionStyle="header">
    <input><table records="{{ example.input }}"/></input>
    <output><table records="{{ example.output }}"/></output>
  </example>
</examples>

<p>Below is a test input grid. Predict the corresponding output grid by applying the rule you found. Your final answer should just be the text output grid itself.</p>
<input><table records="{{ test[0].input }}"/></input>
</HumanMessage>

<stylesheet>
{
  "table": {
    "syntax": "csv",
    "writerOptions": {
        "csvHeader": false,
        "csvSeparator": " "
    }
  },
  "input": {
    "captionEnding": "colon-newline",
    "captionStyle": "plain"
  },
  "output": {
    "captionEnding": "colon-newline",
    "captionStyle": "plain"
  }
}
</stylesheet>
</poml>


================================================
FILE: examples/301_generate_poml.poml
================================================
<poml>
<let src="105_write_blog_post.poml" name="blog_post" />
<let src="106_research.poml" name="research" />
<let src="202_arc_agi.poml" name="arc_agi" />
<let src="107_read_report_pdf.poml" name="read_report" />
<p>
<span whiteSpace="trim">
// PromptLibrary.jsx

/* Create a blog post. The prompt contains very specific instructions around output format, styles, and what to include in the content. */
<span whiteSpace="trim">
function blog_post() {
  return {{blog_post.replace(/^/gm, '  ').trimStart()}};
}
</span>

/* Conduct in-depth research with AI, such as tackling academic papers, business analyses, or large investigative projects. */
<span whiteSpace="trim">
function research() {
  return {{research.replace(/^/gm, '  ').trimStart()}};
}
</span>

/* Test the ability of an LLM to perform a complex reasoning task -- ARC-AGI. The data is in `arc_agi_data.json`.
 */
<span whiteSpace="trim">
function arc_agi() {
  return {{arc_agi.replace(/^/gm, '  ').trimStart()}};
}
</span>

/* Summarize a report, such as a research paper or a business report. */
<span whiteSpace="trim">
function read_report() {
  return {{read_report.replace(/^/gm, '  ').trimStart()}};
}
</span>

/* Write a entertaining story that is engaging, imaginative and captivating for the audience. */
<span whiteSpace="trim">
function storyteller() {
  return
</span>
</span>
</p>
</poml>


================================================
FILE: examples/_generate_expects.py
================================================
import os
import poml
import io
import sys
from contextlib import redirect_stdout


def process_example(example_content, output_file):
    """
    Process the example content and return the expected output.
    """
    # Capture stdout
    poml.poml(example_content, format="raw", output_file=output_file, extra_args=["--prettyPrint", "true"])


def generate_expectations():
    """
    Generate the expected output files for the examples.
    """
    examples_dir = os.path.abspath(os.path.dirname(__file__))
    expect_dir = os.path.join(examples_dir, "expects")
    print("Generating expectations in:", expect_dir)

    for example_file in sorted(os.listdir(examples_dir)):
        if example_file.endswith(".poml"):
            print(f"Processing example: {example_file}")
            # Generate the expected output
            process_example(
                os.path.join(examples_dir, example_file),
                os.path.join(expect_dir, example_file.replace(".poml", ".txt")),
            )


if __name__ == "__main__":
    generate_expectations()



================================================
FILE: examples/assets/101_tom_and_jerry.docx
================================================
[Binary file]


================================================
FILE: examples/assets/101_tom_introduction.txt
================================================
Hello there! Let's take a look at this picture together. What do you see? That's right, it's Tom from the famous cartoon series "Tom and Jerry"!

Tom is a gray and white domestic shorthair cat. In this picture, he looks a bit worried or scared, doesn't he? You can tell by his big, wide eyes and the way his mouth is shaped. Maybe Jerry, the clever little mouse, has played another trick on him!

Now, let's talk a little more about Tom and Jerry so you can understand why Tom might look this way. "Tom and Jerry" is a fun cartoon that has been around since 1940. It was created by William Hanna and Joseph Barbera. The show is all about the funny and sometimes crazy adventures of Tom the cat and Jerry the mouse. Tom is always trying to catch Jerry, but Jerry is very smart and always finds a way to escape or trick Tom.

Even though Tom and Jerry are often seen fighting, they do care about each other and sometimes work together to solve problems. The cartoon is full of funny moments, and even though they play tricks on each other, it's all in good fun.

So, whenever you see Tom looking like this, you can imagine that he's probably just been outsmarted by Jerry once again! But don't worry, Tom never gives up and always comes back for more adventures.


================================================
FILE: examples/assets/104_mag7.xlsx
================================================
[Binary file]


================================================
FILE: examples/assets/201_order_instructions.json
================================================
[
    "If there is no data that can help answer the question, respond with \"I do not have this information. Please contact customer service\".",
    "You are allowed to ask a follow up question if it will help narrow down the data row customer may be referring to.",
    "You can only answer questions related to order history and amount charged for it. Include OrderId in the response, when applicable.",
    "For everything else, please redirect to the customer service agent.",
    "Answer in plain English and no sources are required."
]



================================================
FILE: examples/assets/201_orderlines.csv
================================================
OrderId,OrderLineId,CreatedTimestamp,ItemDescription,Quantity,FulfillmentStatus,ExpectedDeliveryDate,ActualDeliveryDate,ActualShipDate,ExpectedShipDate,TrackingInformation,ShipToAddress,CarrierCode,DeliveryMethod,UnitPrice,OrderLineSubTotal,LineShippingCharge,TotalTaxes,Payments
CC10182,1,,Shorts,0.0,unshipped,2024-01-31,2024-02-01,2024-01-30,2024-01-29,,,,ShipToAddress,115.99,0.0,0.0,0.0,


================================================
FILE: examples/assets/201_orders.csv
================================================
OrderId,CustomerEmail,CreatedTimestamp,IsCancelled,OrderTotal,PaymentSummary
CC10182,222larabrown@gmail.com,2024-01-19,true,0.0,Not available
CC10183,baklavainthebalkans@gmail.com,2024-01-19,true,0.0,Not available


================================================
FILE: examples/assets/202_arc_agi_data.json
================================================
{"train": [{"input": [[2, 2, 2], [2, 1, 8], [2, 8, 8]], "output": [[2, 2, 2], [2, 5, 5], [2, 5, 5]]}, {"input": [[1, 1, 1], [8, 1, 3], [8, 2, 2]], "output": [[1, 1, 1], [5, 1, 5], [5, 5, 5]]}, {"input": [[2, 2, 2], [8, 8, 2], [2, 2, 2]], "output": [[2, 2, 2], [5, 5, 2], [2, 2, 2]]}, {"input": [[3, 3, 8], [4, 4, 4], [8, 1, 1]], "output": [[5, 5, 5], [4, 4, 4], [5, 5, 5]]}], "test": [{"input": [[1, 3, 2], [3, 3, 2], [1, 3, 2]], "output": [[5, 3, 5], [3, 3, 5], [5, 3, 5]]}]}


================================================
FILE: examples/expects/101_explain_character.txt
================================================
===== system =====

# Role

You are a teacher explaining figures to kids.

# Task

Please describe the figure first and then provide background knowledge to help kids understand the figure.

# Output Format

Please write your response in a friendly tone.

# Background Knowledge

Tom and Jerry

Tom and Jerry is an American animated media franchise and series of comedy short films created in 1940 by William Hanna and Joseph Barbera. Best known for its 161 theatrical short films by Metro-Goldwyn-Mayer, the series centers on the enmity between the titular characters of a cat named Tom and a mouse named Jerry. Many shorts also feature several recurring characters.

In its original run, Hanna and Barbera produced 114 Tom and Jerry shorts for MGM from 1940 to 1958.[1] During this time, they won seven Academy Awards for Best Animated Short Film, tying for first place with Walt Disney's Silly Symphonies with the most awards in the category. After the MGM cartoon studio closed in 1957, MGM revived the series with Gene Deitch directing an additional 13 Tom and Jerry shorts for Rembrandt Films in Czechoslovakia from 1961 to 1962. Tom and Jerry became the highest-grossing animated short film series of that time, overtaking Looney Tunes. Chuck Jones produced another 34 shorts with Sib Tower 12 Productions between 1963 and 1967. Five more shorts have been produced since 2001, making a total of 166 shorts.

A number of spin-offs have been made, including the television series The Tom and Jerry Show (1975), The Tom and Jerry Comedy Show (1980–1982), Tom & Jerry Kids (1990–1993), Tom and Jerry Tales (2006–2008), and The Tom and Jerry Show (2014–2021). In 1992, the first feature-length film based on the series, Tom and Jerry: The Movie, was released. 13 direct-to-video films have been produced since 2002. In 2019, a musical adaptation of the series, titled Tom and Jerry: Purr-Chance to Dream, debuted in Japan, in advance of Tom and Jerry's 80th anniversary. In 2021, a live-action/animated hybrid film was released.

## Plot

The series features comic fights between an iconic set of adversaries, a house cat (Tom) and a house mouse (Jerry). The plots of many shorts are often set in the backdrop of a house, centering on Tom (who is often enlisted by a human) trying to capture Jerry, and the mayhem and destruction that follows. Tom rarely succeeds in catching Jerry, mainly because of Jerry's cleverness, cunning abilities, and luck. However, on several occasions, they have displayed genuine friendship and concern for each other's well-being. At other times, the pair set aside their rivalry in order to pursue a common goal, such as when a baby escapes the watch of a negligent babysitter, causing Tom and Jerry to pursue the baby and keep it away from danger, in the shorts Busy Buddies and Tot Watchers respectively. Despite their endless attacks on one another, they have saved each other's lives every time they were truly in danger, except in The Two Mouseketeers, which features an uncharacteristically morbid ending, and Blue Cat Blues, where both sit on a railroad track at the end after being jilted by girlfriends. The cartoon irises out with the whistle of an oncoming steam train.

The cartoons are known for some of the most violent cartoon gags ever devised in theatrical animation: Tom may use axes, hammers, firearms, firecrackers, explosives, traps and poison to kill Jerry. Jerry's methods of retaliation are far more violent, with frequent success, including slicing Tom in half, decapitating him, shutting his head or fingers in a window or a door, stuffing Tom's tail in a waffle iron or a mangle, kicking him into a refrigerator, getting him electrocuted, pounding him with a mace, club or mallet, letting a tree or electric pole drive him into the ground, sticking matches into his feet and lighting them, tying him to a firework and setting it off, and so on.[2] While Tom and Jerry has often been criticized as excessively violent, there is no blood or gore in any scene.[3]: 42 [4]: 134 

Music plays a very important part in the shorts, emphasizing the action, filling in for traditional sound effects, and lending emotion to the scenes. Musical director Scott Bradley created complex scores that combined elements of jazz, classical, and pop music. Bradley often used contemporary pop songs and songs from other films, including MGM films like The Wizard of Oz and Meet Me in St. Louis.

Even though Tom and Jerry almost never speak, the shorts also often had dialogue from other characters. Minor characters are not similarly limited, and the two lead characters speak English on rare occasions. For example, the character Mammy Two Shoes has lines in nearly every cartoon in which she appears. Most of the vocal effects used for Tom and Jerry are their high-pitched laughs and gasping screams.

## Characters

Tom and Jerry

Main articles: Tom Cat and Jerry Mouse

Tom, named "Jasper" in his debut appearance, is a gray and white domestic shorthair cat. "Tom" is a generic name for a male cat. He is usually but not always, portrayed as living a comfortable, or even pampered life, while Jerry, whose name is not explicitly mentioned in his debut appearance, is a small, brown house mouse who always lives in close proximity to Tom. Despite being very energetic, determined and much larger, Tom is no match for Jerry's wits. Jerry possesses surprising strength for his size, approximately the equivalent of Tom's, lifting items such as anvils with relative ease and withstanding considerable impacts.[5]

Although cats typically chase mice to eat them, it is quite rare for Tom to actually try to eat Jerry. He tries to hurt or compete with him just to taunt Jerry, even as revenge, or to obtain a reward from a human, including his owner(s)/master(s), for catching Jerry, or for generally doing his job well as a house cat. By the final "fade-out" of each cartoon, Jerry usually gets the best of Tom.

Other results may be reached. On rare occasions, Tom triumphs, usually when Jerry becomes the aggressor or he pushes Tom a little too far. In The Million Dollar Cat, Jerry learns that Tom will lose his newly acquired wealth if he harms any animal, especially mice. He then torments Tom a little too much until he retaliates. In Timid Tabby Tom's look-alike cousin pushes Jerry over the edge. Occasionally and usually ironically, they both lose, usually because Jerry's last trap or attack on Tom backfires on him or he overlooks something. In Chuck Jones' Filet Meow, Jerry orders a shark from the pet store to scare Tom away from eating a goldfish. Afterward, the shark scares Jerry away as well. They occasionally end up being friends, although there is often a last-minute event that ruins the truce. One cartoon that has a friendly ending is Snowbody Loves Me.

Both characters display sadistic tendencies, in that they are equally likely to take pleasure in tormenting each other, although it is often in response to a triggering event. However, when one character appears to truly be in mortal danger from an unplanned situation or due to actions by a third party, the other will develop a conscience and save him. Occasionally, they bond over a mutual sentiment towards an unpleasant experience and their attacking each other is more play than serious attacks. Multiple shorts show the two getting along with minimal difficulty, and they are more than capable of working together when the situation calls for it, usually against a third party who manages to torture and humiliate them both.

Sometimes this partnership is forgotten quickly when an unexpected event happens, or when one character feels that the other is no longer necessary. This is the case in Posse Cat, when they agree that Jerry will allow himself to be caught if Tom agrees to share his reward dinner, but Tom then reneges. Other times, Tom keeps his promise to Jerry and the partnerships are not quickly dissolved after the problem is solved.

Tom changes his love interest many times. The first love interest is Toots who appears in Puss n' Toots, and calls him "Tommy" in The Mouse Comes to Dinner. He is interested in a cat called Toots in The Zoot Cat although she has a different appearance to the original Toots. The most frequent love interest of Tom's is Toodles Galore, who never has any dialogue in the cartoons.

Despite five shorts ending with a depiction of Tom's apparent death, his demise is never permanent. He even reads about his own death in a flashback in Jerry's Diary. He appears to die in explosions in Mouse Trouble, after which he is seen in heaven, Yankee Doodle Mouse and in Safety Second, while in The Two Mouseketeers he is guillotined offscreen. The short Blue Cat Blues ends with both Tom and Jerry sitting on the railroad tracks with the intent of suicide while the whistle of an oncoming train is heard foreshadowing their imminent death.

Tom and Jerry speaking

Although many supporting and minor characters speak, Tom and Jerry rarely do so themselves. One exception is The Lonesome Mouse where they speak several times briefly, primarily Jerry, to contrive to get Tom back into the house. Tom more often sings while wooing female cats. For example, Tom sings Louis Jordan's "Is You Is or Is You Ain't My Baby" in the 1946 short Solid Serenade. In that short and Zoot Cat, Tom woos female cats using a deep, heavily French-accented voice in imitation of then-popular leading man, actor Charles Boyer.

At the end of The Million Dollar Cat, after beginning to antagonize Jerry he says, "Gee, I'm throwin' away a million dollars... BUT I'M HAPPY!". In Tom and Jerry: The Magic Ring, Jerry says, "No, no, no, no, no." when choosing the shop to remove his ring. In The Mouse Comes to Dinner, Tom speaks to his girlfriend Toots while inadvertently sitting on a stove: "Say, what's cookin'?", to which Toots replies "You are, stupid."

Another instance of speech comes in Solid Serenade and The Framed Cat, where Tom directs Spike through a few dog tricks in a dog-trainer manner. In Puss Gets the Boot, Jerry prays for his life when Tom catches him by the tail. Jerry has whispered in Tom's ear on several occasions. In Love Me, Love My Mouse, Jerry calls Toots "Mama".

Co-director William Hanna provided most of the squeaks, gasps, and other vocal effects for the pair, including the most famous sound effects from the series, Tom's leather-lunged scream, created by recording Hanna's scream and eliminating the beginning and ending of the recording, leaving only the strongest part of the scream on the soundtrack, and Jerry's nervous gulp.

The only other reasonably common vocalization is made by Tom when some external reference claims a certain scenario or eventuality to be impossible, which inevitably thwarts Tom's plans – at which point, a bedraggled and battered Tom appears and says in a haunting, echoing voice "Don't you believe it!", a reference to the then-popular 1940s radio show Don't You Believe It!.[6][7] In Mouse Trouble, Tom says "Don't you believe it!" after being beaten up by Jerry, which also happens in The Missing Mouse. In the 1946 short Trap Happy, Tom hires a cat disguised as a mouse exterminator who, after several failed attempts to dispatch Jerry and suffering a lot of accidents in the process, changes profession to Cat exterminator by crossing out the "Mouse" on his title and writing "CAT", resulting in Tom spelling out the word out loud before reluctantly pointing at himself.

One short, 1956's Blue Cat Blues, is narrated by Jerry in VoiceOver, voiced by Paul Frees, as they try to win back their ladyfriends. Jerry was voiced by Sara Berner during his appearance in the 1945 MGM musical Anchors Aweigh. Tom and Jerry: The Movie is the first, and so far only installment of the series where the famous cat-and-mouse duo regularly speaks or is able to be understood by humans. In that film, Tom was voiced by Richard Kind, and Jerry was voiced by Dana Hill.

Spike and Tyke

Main article: Spike and Tyke (characters)

In his attempts to catch Jerry, Tom often has to deal with Spike, known as "Killer" and "Butch" in some shorts, an angry, vicious but gullible bulldog who tries to attack Tom for bothering him or his son Tyke while trying to get Jerry. Originally, Spike was unnamed and mute, aside from howls and biting noises as well as attacking indiscriminately, not caring whether it was Tom or Jerry though usually attacking Tom. In later cartoons, Spike spoke often, using a voice and expressions, performed by Billy Bletcher and later Daws Butler, modeled after comedian Jimmy Durante. Spike's coat has altered throughout the years between gray and creamy tan. The addition of Spike's son Tyke in the late 1940s led to both a slight softening of Spike's character and a short-lived spin-off theatrical series called Spike and Tyke.

Most cartoons with Spike in them conform to a theme: usually, Spike is trying to accomplish something, such as building a dog house or sleeping, when Tom and Jerry's antics stop him doing it. Spike then presumably due to prejudice, singles out Tom as the culprit, and threatens him that if it ever happens again, he will do "something horrible" to him, effectively forcing Tom to take the blame, while Jerry overhears. Afterward, Jerry usually does anything he can to interrupt whatever Spike is doing, while Tom barely manages to stop him, usually getting injured in the process. Usually, Jerry eventually wrecks whatever Spike is doing in spectacular fashion, and leaves Tom to take the blame, forcing him to flee from Spike and inevitably lose.

Off-screen, Spike does something to Tom, and Tom is generally shown injured or in a bad situation while Jerry smugly cuddles up to Spike unscathed. Tom sometimes gets irritated with Spike. An example is in That's My Pup!, when Spike forces Tom to run up a tree every time his son barked, causing Tom to hang Tyke on a flag pole. At least once, Tom does something that benefits Spike, who promises not to interfere ever again, causing Jerry to frantically leave the house and run into the distance, in Hic-cup Pup. Spike is well known for his famous "Listen pussycat!" catchphrase when he threatens Tom, his other famous catchphrase is "That's my boy!" normally said when he supports or congratulates his son.

Tyke is described as a cute, sweet-looking, happy and lovable puppy. He is Spike's son. Unlike Spike, Tyke does not speak and only communicates, mostly towards his father, by barking, yapping, wagging his tail, whimpering and growling. Spike would always go out of his way to care and comfort his son and make sure that he is safe from Tom. Tyke loves his father and Spike loves his son and they get along like friends, although most of time they would be taking a nap or Spike would teach Tyke the main facts of life of being a dog. Like Spike, Tyke's appearance has altered throughout the years, from gray, with white paws, to creamy tan. When Tom & Jerry Kids first aired, this was the first time that viewers heard Tyke speak.

Butch and Toodles Galore

Butch is a black, cigar-smoking alley cat who also wants to eat Jerry. He is Tom's most frequent adversary. For most of the shorts he appears in, he is usually seen rivaling Tom over Toodles. Butch was Tom's chum as in some cartoons, where Butch is leader of Tom's alley cat buddies, who are mostly Lightning, Topsy, and Meathead. Butch talks more often than Tom or Jerry in most shorts.

Butch and Toodles were originally introduced in Hugh Harman's 1941 short The Alley Cat, but were integrated into Tom and Jerry rather than continuing in their own series.

Nibbles

Main article: Nibbles (Tom and Jerry)

Nibbles is a small gray mouse who often appears in shorts as an orphan mouse. He is a carefree individual who very rarely understands the danger of the situation, simply following instructions the best he can both to Jerry's command and his own innocent understanding of the situation. This can lead to such results as "getting the cheese" by simply asking Tom to pick it up for him, rather than following Jerry's example of outmaneuvering and sneaking around Tom. Many times Nibbles is an ally of Jerry in fights against Tom, including being the second Mouseketeer. He is given speaking roles in all his appearances as a Mouseketeer, often with a high-pitched French tone. However, during a short in which he rescued Robin Hood, his voice was instead more masculine, gruff, and cockney accented.

The Housekeeper

Main article: Mammy Two Shoes

The housekeeper, usually seen from the torso down, is a heavy-set, middle-aged black woman who often has to deal with the mayhem generated by the lead characters. Voiced by character actress Lillian Randolph, she is often seen as the owner of Tom, and perhaps the homeowner as well. Her face was only shown once, very briefly, in Saturday Evening Puss. Her appearances have often been edited out, dubbed, or re-animated as a slim white woman in later television showings, since her character is a mammy archetype that had been protested as racist by the NAACP and other civil rights groups since the 1940s.[8][9] In a 1975 article in Film Comment she was referred to as "Mammy Two Shoes," a moniker that has been inaccurately attributed to the character ever since, The name "Mammy Two-Shoes" was on the Disney model sheets for a character in a Silly Symphony cartoon, though the name was never spoken in the cartoon. A similar housekeeper then appeared in MGM Bokso cartoons by Harman and Ising, also without a name. At no time, ever, was the name used in any Tom and Jerry cartoon, The author of the 1975 later apologized, but too much time had established the incorrect information, including on the DVD release DVD releases of the cartoons, in which the script read by Whoopi Goldberg on the Tom and Jerry Spotlight Collection: Vol. 2 DVD set, while explaining the importance of African-American representation in the cartoon series, however stereotyped, mentions the incorrect name numerous times.[10]

===== human =====

{"type":"image/jpeg","base64":"/9j/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWI...

===== ai =====

Hello there! Let's take a look at this picture together. What do you see? That's right, it's Tom from the famous cartoon series "Tom and Jerry"!

Tom is a gray and white domestic shorthair cat. In this picture, he looks a bit worried or scared, doesn't he? You can tell by his big, wide eyes and the way his mouth is shaped. Maybe Jerry, the clever little mouse, has played another trick on him!

Now, let's talk a little more about Tom and Jerry so you can understand why Tom might look this way. "Tom and Jerry" is a fun cartoon that has been around since 1940. It was created by William Hanna and Joseph Barbera. The show is all about the funny and sometimes crazy adventures of Tom the cat and Jerry the mouse. Tom is always trying to catch Jerry, but Jerry is very smart and always finds a way to escape or trick Tom.

Even though Tom and Jerry are often seen fighting, they do care about each other and sometimes work together to solve problems. The cartoon is full of funny moments, and even though they play tricks on each other, it's all in good fun.

So, whenever you see Tom looking like this, you can imagine that he's probably just been outsmarted by Jerry once again! But don't worry, Tom never gives up and always comes back for more adventures.

===== human =====

{"type":"image/jpeg","base64":"/9j/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWI...


================================================
FILE: examples/expects/102_render_xml.txt
================================================
===== human =====

<role>Senior Systems Architecture Consultant</role>
<task>Legacy System Migration Analysis</task>
<Context>
  <item>Fortune 500 retail company</item>
  <item>Current system: 15-year-old monolithic application</item>
  <item>500+ daily users</item>
  <item>99.99% uptime requirement</item>
</Context>
<RequiredAnalysis>
  <item>Migration risks and mitigation strategies</item>
  <item>Cloud vs hybrid options</item>
  <item>Cost-benefit analysis</item>
  <item>Implementation roadmap</item>
</RequiredAnalysis>
<outputFormat>
  <item>Executive brief (250 words)</item>
  <item>Technical details (500 words)</item>
  <item>Risk matrix</item>
  <item>Timeline visualization</item>
  <item>Budget breakdown</item>
</outputFormat>
<Constraints>
  <item>Must maintain operational continuity</item>
  <item>Compliance with GDPR and CCPA</item>
  <item>Maximum 18-month implementation window</item>
</Constraints>


================================================
FILE: examples/expects/103_word_todos.txt
================================================
===== system =====

# Task

I developed a project called Prompt Wizard and I want to write a blog to publish on the company website. I have already written a draft of the blog. There has been figures, numbers in tables, the key challenges, motivations, as well as some titles and subtitles. I want you to complete the `[TODO]`s in the draft.

# Output Format

Your response should be in the following format: 

```
- TODO 1:
- TODO 2:
- ...
```

===== human =====

PromptWizard: The future of prompt optimization through feedback-driven self-evolving prompts

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAAAfQAAAEZCAYAAABhDNfWAAAACXBIWXMAAAsTAAALEwEAmp...

# The challenge of effective prompting

AI is reshaping industries—from education to healthcare—thanks to advancements in large language models (LLMs). These models rely on prompts, carefully crafted inputs that guide them to produce relevant and meaningful outputs. While the impact of prompts is profound, creating prompts that can help with complex tasks is a time-intensive and expertise-heavy process, often involving months of trial and error. 

This challenge grows as new tasks arise and models evolve rapidly, making manual methods for prompt engineering increasingly unsustainable. The question then becomes: How can we make prompt optimization faster, more accessible, and more adaptable across diverse tasks? 

To address this challenge, we developed PromptWizard (PW), a research framework that automates and streamlines the process of prompt optimization. We are open sourcing the PromptWizard codebase(opens in new tab) to foster collaboration and innovation within the research and development community.

# Introducing PromptWizard

PromptWizard (PW) is designed to automate and simplify prompt optimization. It combines iterative feedback from LLMs with efficient exploration and refinement techniques to create highly effective prompts within minutes.

PromptWizard optimizes both the instruction and the in-context learning examples. Central to PW is its self-evolving and self-adaptive mechanism, where the LLM iteratively generates, critiques, and refines prompts and examples in tandem. This process ensures continuous improvement through feedback and synthesis, achieving a holistic optimization tailored to the specific task at hand. By evolving both instructions and examples simultaneously, PW ensures significant gains in task performance. 

# Three key insights behind PromptWizard:

- Feedback-driven refinement: [TODO 1]
- Joint optimization and synthesis of diverse examples: [TODO 2]
- Self-generated chain-of-thought (CoT) steps: [TODO 3]

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAAAfQAAACcCAYAAACJBlkJAAAACXBIWXMAAAsTAAALEwEAmp...

Figure 1. Overview of PromptWizard

# How PromptWizard works

PromptWizard begins with a user input: a problem description, an initial prompt instruction, and a few training examples that serve as a foundation for the task at hand.

Its output is a refined, optimized set of prompt instructions paired with carefully curated in-context few-shot examples. These outputs are enriched with detailed reasoning chains, task intent, and an expert profile that bridges human-like reasoning with the AI’s responses. 

# Stage 1: Refinement of prompt instruction

[TODO 4]

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAAAfQAAAD4CAYAAAAaYxRFAAAACXBIWXMAAA7DAAAOwwHHb6...

Figure 2. Refinement of prompt instruction

# Stage 2: Joint optimization of instructions and examples

[TODO 5]

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAAAfQAAADfCAYAAAAAyiHLAAAACXBIWXMAAA7DAAAOwwHHb6...

Figure 3. Joint optimization of instructions and examples

# Results

PromptWizard stands out for its feedback-driven refinement and systematic exploration, delivering exceptional results across a wide variety of tasks while maintaining computational efficiency. 

# Comprehensive evaluation across tasks

PromptWizard was rigorously evaluated on over 45 tasks, spanning both general and domain-specific challenges. Benchmarked against state-of-the-art techniques—including Instinct, InstructZero, APE, PromptBreeder, EvoPrompt, DSPy, APO, and PromptAgent—PW consistently outperformed competitors in accuracy, efficiency, and adaptability. Please see detailed results in our paper. 

[TODO 6]

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAAAfQAAAFiCAIAAACPi72DAAAACXBIWXMAAAsTAAALEwEAmp...

Figure 4. Performance Profile curve on BBII dataset

| Methods       | API calls | Total tokens |
| ------------- | --------- | ------------ |
| Instinct      | 1730      | 115k         |
| PromptBreeder | 18600     | 1488k        |
| EvoPrompt     | 5000      | 400k         |
| PW            | 69        | 24k          |

Table 1. Cost analysis on BBII dataset

# Resilience with limited data

[TODO 7]

| Datasets | 5 Examples | 25 Examples |
| -------- | ---------- | ----------- |
| MMLU     | 80.4       | 89.5        |
| GSM8k    | 94         | 95.4        |
| Ethos    | 86.4       | 89.4        |
| PubMedQA | 68         | 78.2        |
| MedQA    | 80.4       | 82.9        |
| Average  | 81.9       | 87          |

Table 2. PW’s performance with varying number of examples

# Leveraging smaller models for optimization

[TODO 8]

| Dataset | Prompt Gen: Llama-70B | Prompt Gen: GPT4 |
| ------- | --------------------- | ---------------- |
| GSM8k   | 94.6                  | 95.4             |
| Ethos   | 89.2                  | 89.4             |
| Average | 91.9                  | 92.4             |

Table 3. Performance with smaller LLMs for prompt generation 

# Conclusion

Whether you are a researcher addressing cutting-edge challenges or an organization looking to streamline workflows, PromptWizard provides a practical, scalable, and impactful solution for enhancing model performance.


================================================
FILE: examples/expects/104_financial_analysis.txt
================================================
===== system =====

# Task

Given the stock ticker, provide a full and up-to-date financial analysis covering the following aspects, cite sources.

1. Current stock price, recent performance trends, and historical comparison.
2. Key financial ratios (e.g., P/E ratio, forward P/E, Price/Free cash flow, EPS growth this year, Return on equity, return on investment, current ratio, net profit margin, debt-to-equity ratio) and what they indicate about the company's financial health.
3. Support and resistance prices of the stock and how current indicators may drive the direction of the stock
4. Recent earnings reports, revenue growth or decline, and net income trends over the past quarter. Please also include if latest EPS report beat estimates.
5. Industry comparison to determine the company's standing relative to its peers.
6. Current analyst ratings, target price forecasts, and recent upgrades or downgrades.
7. Overall summary on whether the stock is considered a 'buy', 'hold', or 'sell' based on current financial data and market sentiment.

===== human =====

| Date       | MSFT   | AMZN   | META   | AAPL   | GOOG   | NVDA   | TSLA   |
| ---------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 2025-02-12 | 409.04 | 228.93 | 725.38 | 236.87 | 185.43 | 131.14 | 336.51 |
| 2025-02-11 | 411.44 | 232.76 | 719.8  | 232.62 | 187.07 | 132.8  | 328.5  |
| 2025-02-10 | 412.22 | 233.14 | 717.4  | 227.65 | 188.2  | 133.57 | 350.73 |
| 2025-02-07 | 409.75 | 229.15 | 714.52 | 227.63 | 187.14 | 129.84 | 361.62 |
| 2025-02-06 | 415.82 | 238.83 | 711.99 | 233.22 | 193.31 | 128.68 | 374.32 |
| 2025-02-05 | 413.29 | 236.17 | 704.87 | 232.47 | 193.3  | 124.83 | 378.17 |
| 2025-02-04 | 412.37 | 242.06 | 704.19 | 232.8  | 207.71 | 118.65 | 392.21 |
| 2025-02-03 | 410.92 | 237.42 | 697.46 | 228.01 | 202.64 | 116.66 | 383.68 |
| 2025-01-31 | 415.06 | 237.68 | 689.18 | 236    | 205.6  | 120.07 | 404.6  |
| 2025-01-30 | 414.99 | 234.64 | 687    | 237.59 | 202.63 | 124.65 | 400.28 |
| 2025-01-29 | 442.33 | 237.07 | 676.49 | 239.36 | 197.18 | 123.7  | 389.1  |
| 2025-01-28 | 447.2  | 238.15 | 674.33 | 238.26 | 197.07 | 128.99 | 398.09 |
| 2025-01-27 | 434.56 | 235.42 | 659.88 | 229.86 | 193.77 | 118.42 | 397.15 |
| 2025-01-24 | 444.06 | 234.85 | 647.49 | 222.78 | 201.9  | 142.62 | 406.58 |
| 2025-01-23 | 446.71 | 235.42 | 636.45 | 223.66 | 199.58 | 147.22 | 412.38 |
| 2025-01-22 | 446.2  | 235.01 | 623.5  | 223.83 | 200.03 | 147.07 | 415.11 |
| 2025-01-21 | 428.5  | 230.71 | 616.46 | 222.64 | 199.63 | 140.83 | 424.07 |
| 2025-01-17 | 429.03 | 225.94 | 612.77 | 229.98 | 197.55 | 137.71 | 426.5  |
| 2025-01-16 | 424.58 | 220.66 | 611.3  | 228.26 | 194.41 | 133.57 | 413.82 |
| 2025-01-15 | 426.31 | 223.35 | 617.12 | 237.87 | 196.98 | 136.24 | 428.22 |
| 2025-01-14 | 415.67 | 217.76 | 594.25 | 233.28 | 191.05 | 131.76 | 396.36 |
| 2025-01-13 | 417.19 | 218.46 | 608.33 | 234.4  | 192.29 | 133.23 | 403.31 |
| 2025-01-10 | 418.95 | 218.94 | 615.86 | 236.85 | 193.17 | 135.91 | 394.74 |
| 2025-01-08 | 424.56 | 222.13 | 610.72 | 242.7  | 195.39 | 140.11 | 394.94 |
| 2025-01-07 | 422.37 | 222.11 | 617.89 | 242.21 | 196.71 | 140.14 | 394.36 |
| 2025-01-06 | 427.85 | 227.61 | 630.2  | 245    | 197.96 | 149.43 | 411.05 |
| 2025-01-03 | 423.35 | 224.19 | 604.63 | 243.36 | 193.13 | 144.47 | 410.44 |
| 2025-01-02 | 418.58 | 220.22 | 599.24 | 243.85 | 190.63 | 138.31 | 379.28 |
| 2024-12-31 | 421.5  | 219.39 | 585.51 | 250.42 | 190.44 | 134.29 | 403.84 |
| 2024-12-30 | 424.83 | 221.3  | 591.24 | 252.2  | 192.69 | 137.49 | 417.41 |
| 2024-12-27 | 430.53 | 223.75 | 599.81 | 255.59 | 194.04 | 137.01 | 431.66 |
| 2024-12-26 | 438.11 | 227.05 | 603.35 | 259.02 | 197.1  | 139.93 | 454.13 |
| 2024-12-24 | 439.33 | 229.05 | 607.75 | 258.2  | 197.57 | 140.22 | 462.28 |
| 2024-12-23 | 435.25 | 225.06 | 599.85 | 255.27 | 195.99 | 139.67 | 430.6  |
| 2024-12-20 | 436.6  | 224.92 | 585.25 | 254.49 | 192.96 | 134.7  | 421.06 |
| 2024-12-19 | 437.03 | 223.29 | 595.57 | 249.79 | 189.7  | 130.68 | 436.17 |
| 2024-12-18 | 437.39 | 220.52 | 597.19 | 248.05 | 190.15 | 128.91 | 440.13 |
| 2024-12-17 | 454.46 | 231.15 | 619.44 | 253.48 | 197.12 | 130.39 | 479.86 |
| 2024-12-16 | 451.59 | 232.93 | 624.24 | 251.04 | 198.16 | 132    | 463.02 |
| 2024-12-13 | 447.27 | 227.46 | 620.35 | 248.13 | 191.38 | 134.25 | 436.23 |
| 2024-12-12 | 449.56 | 228.97 | 630.79 | 247.96 | 193.63 | 137.34 | 418.1  |
| 2024-12-11 | 448.99 | 230.26 | 632.68 | 246.49 | 196.71 | 139.31 | 424.77 |
| 2024-12-10 | 443.33 | 225.04 | 619.32 | 247.77 | 186.53 | 135.07 | 400.99 |
| 2024-12-09 | 446.02 | 226.09 | 613.57 | 246.75 | 177.1  | 138.81 | 389.79 |
| 2024-12-06 | 443.57 | 227.03 | 623.77 | 242.84 | 176.49 | 142.44 | 389.22 |
| 2024-12-05 | 442.62 | 220.55 | 608.93 | 243.04 | 174.31 | 145.06 | 369.49 |
| 2024-12-04 | 437.42 | 218.16 | 613.78 | 243.01 | 176.09 | 145.14 | 357.93 |
| 2024-12-03 | 431.2  | 213.44 | 613.65 | 242.65 | 173.02 | 140.26 | 351.42 |
| 2024-12-02 | 430.98 | 210.71 | 592.83 | 239.59 | 172.98 | 138.63 | 357.09 |
| 2024-11-29 | 423.46 | 207.89 | 574.32 | 237.33 | 170.49 | 138.25 | 345.16 |
| 2024-11-27 | 422.99 | 205.74 | 569.2  | 234.93 | 170.82 | 135.34 | 332.89 |
| 2024-11-26 | 427.99 | 207.86 | 573.54 | 235.06 | 170.62 | 136.92 | 338.23 |
| 2024-11-25 | 418.79 | 201.45 | 565.11 | 232.87 | 169.43 | 136.02 | 338.59 |
| 2024-11-22 | 417    | 197.12 | 559.14 | 229.87 | 166.57 | 141.95 | 352.56 |
| 2024-11-21 | 412.87 | 198.38 | 563.09 | 228.52 | 169.24 | 146.67 | 339.64 |
| 2024-11-20 | 415.49 | 202.88 | 565.52 | 229    | 177.33 | 145.89 | 342.03 |
| 2024-11-19 | 417.79 | 204.61 | 561.09 | 228.28 | 179.58 | 147.01 | 346    |
| 2024-11-18 | 415.76 | 201.7  | 554.4  | 228.02 | 176.8  | 140.15 | 338.74 |
| 2024-11-15 | 415    | 202.61 | 554.08 | 225    | 173.89 | 141.98 | 320.72 |
| 2024-11-14 | 426.89 | 211.48 | 577.16 | 228.22 | 177.35 | 146.76 | 311.18 |

The following two charts on a visualization of the table above. One of them shows the absolute price of the stocks, and the other one shows the price normalized by the price of the first day.

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAABxUAAAVWCAYAAABb2OdwAAAACXBIWXMAADLAAAAywAEoZF...

{"type":"image/png","base64":"iVBORw0KGgoAAAANSUhEUgAABxUAAAVWCAYAAABb2OdwAAAACXBIWXMAADLAAAAywAEoZF...

**Hint:** The table contains stock tickers of 7 companies. Please analyze and give financial analysis and comparison for them.



================================================
FILE: examples/expects/105_write_blog_post.txt
================================================
===== human =====

# Task

Create a blog post with these specifications:

# Output Format

1. Title: [SEO-friendly title]

2. Introduction (100 words) 

   - Hook statement
   - Context setting
   - Main points preview

3. Main body (800 words) 

   - 3-4 main points
   - Each point: [subtitle + 200 words]
   - Include real examples
   - Add actionable tips

4. Conclusion (100 words) 

   - Summary of key points
   - Call to action

# Style

- Tone: Professional but conversational
- Level: Intermediate audience
- Voice: Active, engaging
- Format: Scannable, with subheadings

# Include

- Practical examples
- Statistics or research
- Actionable takeaways
- Relevant analogies


================================================
FILE: examples/expects/106_research.txt
================================================
===== human =====

# Task

You are given various potential options or approaches for a project. Convert these into a well-structured research plan.

# Stepwise Instructions

1. Identifies Key Objectives 

   - Clarify what questions each option aims to answer
   - Detail the data/info needed for evaluation

2. Describes Research Methods 

   - Outline how you’ll gather and analyze data
   - Mention tools or methodologies for each approach

3. Provides Evaluation Criteria 

   - Metrics, benchmarks, or qualitative factors to compare options
   - Criteria for success or viability

4. Specifies Expected Outcomes 

   - Possible findings or results
   - Next steps or actions following the research

 Produce a methodical plan focusing on clear, practical steps.


================================================
FILE: examples/expects/107_read_report_pdf.txt
================================================
===== human =====

Provide a concise executive summary of the following text, highlighting key points, objectives, and outcomes. Keep the summary under 150 words and ensure it is suitable for a professional audience.



F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12Esc Power Sleep 
Wake
Up
Print
Scrn
SysRq
Scroll
Lock 
Pause
Break
Insert Home 
Page
Up
Delete End 
Page
Down
½ 1 
2 
3 4 5 6 7 8 9 0 + '
Q 
W 
E R T Y U I O P Å ^
A S D F G H J K L Æ Ø *
> Z 
X C V B N M ; : 
_
Num Lock Caps Lock Scroll Lock
Num
Lock 
/ 
* 
_
+
Enter
Ctrl Alt
Caps Lock
Alt Gr Ctrl
Web E-Mail +Volume-VolumeMutePrevious NextMenuTuner
< \
§ ! " # ¤ % & / ( ) = ? `
|
€
@ £ $ { [ ] }
" ~
'
-
.,
7 8 9
4 5 6
1 2 3
0
Home PgUp
End PgDn
Ins Del
,
Figure 2: This figure floats to the top of the page, spanning both columns.
3.1 HTML5
This template uses HTML5 elements to aid in rep-
resenting the document structure. The section
element is used to split the text into sections, and
the header element holds the headlines. The
figure element is used to include figures and
their corrensponding captions live inside the fig-
caption element. The cite element holds all ref-
erences.
A small microformat, based on a convention of
class names, is used to encode the name and affili-
ation of the authors.
3.2 CSS
A CSS style sheet describes how to format the
HTML document into a PDF file. CSS is a declar-
ative language which attaches property values to
HTML elements and documents. Many aspects of
CSS is used to achieve the presentation of USENIX
papers, including:
• multi-column layout
• footnotes
• page and column floats
• multi-level counters
Some commonly used features are absent from
the above list: page numbers and running headers
should not be specifed by USENIX authors, these
are added by those who compile the Proceedings.
3.3 JavaScript
This template uses JavaScript to process refer-
ences. References are added at the point where
they appear, and a script is later used to move the
references to the end of the paper, leaving behind
a numeric marker.
3.4 PDF
(This section has been added by Håkon Wium Lie)
In order to convert the document to PDF, a for-
matter is needed. Common browsers support
HTML and CSS, but they do not support all the CSS
functionality for page-based formatting. For ex-
ample, browsers do not support footnotes or page
floats. This paper has been formatted with
Prince,
[a] 
a purpose-built program for converting
HTML and XML documents into PDF by way of
CSS. Prince is a commercial product, but can be
downloaded and used for free for non-commercial
purposes.
In order for Prince to process the script includ-
ed in this template, a command line option must
be specified:
$ prince --javascript example.html
4 Tables
The table below lists recipients of the USENIX Life-
time Achievement Award in the 1900s. Notice how
notes inside the table are moved to the end of the
table.
Year Recipient
1999 X Window System*
1998 Tim Berners-Lee
1997 Brian W. Kernighan
[a] www.princexml.com

1996 The Software Tools Project
1995 The Creation of USENET **
1994 Networking Technologies
1993 Berkeley UNIX
* Given to the Community at Large
** Given to Jim Ellis and Tom Truscott
5 Conclusions
Each good paper concludes the most significant
findings in the end.
Acknowledgments
A polite author always includes acknowledgments.
Thank everyone, especially those who funded the
work.
Availability
Please include a section at the end of your paper
providing availability information. If the system
you describe is available to others, and if more in-
formation (reports, etc.) may be obtained, indicate
terms and contact information.
References
[1] STRUNK, W. JR., AND WHITE, E.B. The Elements
of Style, 4th Ed, Allyn and Bacon, August, 1999,
ISBN 020530902X
[2] ZOBEL, J. Writing for Computer Science,
Springer-Verlag, December 1997, ISBN
9813083220


================================================
FILE: examples/expects/201_orders_qa.txt
================================================
===== system =====

# ROLE

You are a chatbot agent answering customer's questions in a chat.

# TASK

Your task is to answer the customer's question using the data provided in the data section. 

1. You can access order history in the orders section including email id and order total with payment summary.
2. Refer to orderlines for item level details within each order in orders.

# DATA

## ORDERS

| OrderId | CustomerEmail                 | CreatedTimestamp | IsCancelled | OrderTotal | PaymentSummary |
| ------- | ----------------------------- | ---------------- | ----------- | ---------- | -------------- |
| CC10182 | 222larabrown@gmail.com        | 2024-01-19       |             | 0          | Not available  |
| CC10183 | baklavainthebalkans@gmail.com | 2024-01-19       |             | 0          | Not available  |

## ORDERLINES

OrderId	OrderLineId	CreatedTimestamp	ItemDescription	Quantity	FulfillmentStatus	ExpectedDeliveryDate	ActualDeliveryDate	ActualShipDate	ExpectedShipDate	TrackingInformation	ShipToAddress	CarrierCode	DeliveryMethod	UnitPrice	OrderLineSubTotal	LineShippingCharge	TotalTaxes	Payments
CC10182	1		Shorts	0	unshipped	2024-01-31	2024-02-01	2024-01-30	2024-01-29				ShipToAddress	115.99	0	0	0	

# STEPWISE INSTRUCTIONS

Instruction 1: If there is no data that can help answer the question, respond with "I do not have this information. Please contact customer service".

Instruction 2: You are allowed to ask a follow up question if it will help narrow down the data row customer may be referring to.

Instruction 3: You can only answer questions related to order history and amount charged for it. Include OrderId in the response, when applicable.

Instruction 4: For everything else, please redirect to the customer service agent.

Instruction 5: Answer in plain English and no sources are required.

===== human =====

**QUESTION:** How much did I pay for my last order?

**Answer:**



================================================
FILE: examples/expects/202_arc_agi.txt
================================================
===== system =====

Be brief and clear in your responses

===== human =====

Find the common rule that maps an input grid to an output grid, given the examples below.

# Examples

## Example 0

Input:
2 2 2
2 1 8
2 8 8

Output:
2 2 2
2 5 5
2 5 5

## Example 1

Input:
1 1 1
8 1 3
8 2 2

Output:
1 1 1
5 1 5
5 5 5

## Example 2

Input:
2 2 2
8 8 2
2 2 2

Output:
2 2 2
5 5 2
2 2 2

## Example 3

Input:
3 3 8
4 4 4
8 1 1

Output:
5 5 5
4 4 4
5 5 5

Below is a test input grid. Predict the corresponding output grid by applying the rule you found. Your final answer should just be the text output grid itself.

Input:
1 3 2
3 3 2
1 3 2


================================================
FILE: examples/expects/301_generate_poml.txt
================================================
===== human =====

// PromptLibrary.jsx

/* Create a blog post. The prompt contains very specific instructions around output format, styles, and what to include in the content. */
function blog_post() {
  return <poml>
  <task className="instruction">Create a blog post with these specifications:</task>
  
  <output-format className="instruction">
  <list listStyle="decimal">
    <item>Title: [SEO-friendly title]</item>
    <item>Introduction (100 words)
    <list>
      <item>Hook statement</item>
      <item>Context setting</item>
      <item>Main points preview</item>
    </list>
    </item>
    <item>Main body (800 words)
    <list>
      <item>3-4 main points</item>
      <item>Each point: [subtitle + 200 words]</item>
      <item>Include real examples</item>
      <item>Add actionable tips</item>
    </list>
    </item>
    <item>Conclusion (100 words)
    <list>
      <item>Summary of key points</item>
      <item>Call to action</item>
    </list>
    </item>
  </list>
  </output-format>
  
  <cp className="instruction" caption="Style" captionSerialized="style">
  <list>
    <item>Tone: Professional but conversational</item>
    <item>Level: Intermediate audience</item>
    <item>Voice: Active, engaging</item>
    <item>Format: Scannable, with subheadings</item>
  </list>
  </cp>
  
  <cp className="instruction" caption="Include" captionSerialized="include">
  <list>
    <item>Practical examples</item>
    <item>Statistics or research</item>
    <item>Actionable takeaways</item>
    <item>Relevant analogies</item>
  </list>
  </cp>
  </poml>;
}


/* Conduct in-depth research with AI, such as tackling academic papers, business analyses, or large investigative projects. */
function research() {
  return <poml>
  <task>You are given various potential options or approaches for a project. Convert these into a well-structured research plan.</task>
  
  <stepwise-instructions>
  <list listStyle="decimal">
  <item>Identifies Key Objectives
    <list listStyle="dash">
      <item>Clarify what questions each option aims to answer</item>
      <item>Detail the data/info needed for evaluation</item>
    </list>
  </item>
  <item>Describes Research Methods
    <list listStyle="dash">
      <item>Outline how you’ll gather and analyze data</item>
      <item>Mention tools or methodologies for each approach</item>
    </list>
  </item>
  
  <item>Provides Evaluation Criteria
    <list listStyle="dash">
      <item>Metrics, benchmarks, or qualitative factors to compare options  </item>
      <item>Criteria for success or viability</item>
    </list>
  </item>
  
  <item>Specifies Expected Outcomes
    <list listStyle="dash">
      <item>Possible findings or results  </item>
      <item>Next steps or actions following the research</item>
    </list>
  </item>
  </list>
  
  Produce a methodical plan focusing on clear, practical steps.
  </stepwise-instructions>
  </poml>;
}


/* Test the ability of an LLM to perform a complex reasoning task -- ARC-AGI. The data is in `arc_agi_data.json`.
 */
function arc_agi() {
  return <poml>
  <SystemMessage>Be brief and clear in your responses</SystemMessage>
  <let src="assets/202_arc_agi_data.json"/>
  <HumanMessage>
  <p>Find the common rule that maps an input grid to an output grid, given the examples below.</p>
  <examples>
    <example for="example in train" chat="false" caption="Example {{ loop.index }}" captionStyle="header">
      <input><table records="{{ example.input }}"/></input>
      <output><table records="{{ example.output }}"/></output>
    </example>
  </examples>
  
  <p>Below is a test input grid. Predict the corresponding output grid by applying the rule you found. Your final answer should just be the text output grid itself.</p>
  <input><table records="{{ test[0].input }}"/></input>
  </HumanMessage>
  
  <stylesheet>
  {
    "table": {
      "syntax": "csv",
      "writerOptions": {
          "csvHeader": false,
          "csvSeparator": " "
      }
    },
    "input": {
      "captionEnding": "colon-newline",
      "captionStyle": "plain"
    },
    "output": {
      "captionEnding": "colon-newline",
      "captionStyle": "plain"
    }
  }
  </stylesheet>
  </poml>;
}


/* Summarize a report, such as a research paper or a business report. */
function read_report() {
  return <poml>
  <p>Provide a concise executive summary of the following text, highlighting key points, objectives, and outcomes. Keep the summary under 150 words and ensure it is suitable for a professional audience.</p>
  <Document syntax="text" src="assets/107_usenix_paper.pdf" selectedPages="1:3" />
  </poml>
  ;
}


/* Write a entertaining story that is engaging, imaginative and captivating for the audience. */
function storyteller() {
  return



================================================
FILE: gallery/ask.poml
================================================
<poml>
<p>You are a specialized Code-QA assistant. Given a user's request and one or more code files, follow these steps without deviation:</p>

<list listStyle="decimal">
  <item>
    <b>Clarify Scope</b>
    <list listStyle="dash">
      <item>Restate the user's objective in your own words.</item>
      <item>Highlight any ambiguities and request clarification if needed.</item>
    </list>
  </item>
  <item>
    <b>Locate Relevant Code</b>
    <list listStyle="dash">
      <item>List the filenames and line ranges that pertain to the request.</item>
      <item>Do not modify code. Only reference locations.</item>
    </list>
  </item>
  <item>
    <b>Formulate Your Answer</b>
    <list listStyle="dash">
      <item>Provide a concise, accurate solution or explanation.</item>
      <item>Justify each step by citing the code context.</item>
      <item>If an assumption is required, state it explicitly.</item>
    </list>
  </item>
</list>

<p>---</p>

<cp caption="CODE FILES">
  <div for="file in files">
    <cp caption="FILENAME: {{file}}">
      <code inline="false"><document src="{{file}}" parser="txt" /></code>
    </cp>
  </div>
</cp>

<cp caption="USER REQUEST"><div whiteSpace="pre">{{ prompt }}</div></cp>

<p>---</p>

<p>Assistant, begin.</p>
</poml>



================================================
FILE: gallery/chat.poml
================================================
<poml>
  <task>{{ prompt }}</task>
  <cp caption="References">
    <document src="{{ file }}" parser="txt" for="file in files" />
  </cp>
</poml>



================================================
FILE: gallery/edit.poml
================================================
<poml>
<p>You are a senior engineer with deep experience building production-grade AI agents, automations, and workflow systems. Your task is code edit: fixing bugs, adding features and introducing refactors.</p>

<cp caption="PROCEDURE (MUST follow strictly)">
<list listStyle="decimal">
  <item>
    <b>Clarify Scope</b>
    <list listStyle="dash">
      <item>Restate the objective in your own words; if unclear, ask one concise question.</item>
      <item>Sketch a high-level plan of how to meet the objective.</item>
    </list>
  </item>
  <item>
    <b>Locate exact code edit point</b>
    <list listStyle="dash">
      <item>Work <b>only</b> inside the given code files.</item>
      <item>Quote the <b>smallest</b> relevant snippet (line numbers) you need to change.</item>
    </list>
  </item>
  <item>
    <b>Make minimal, contained changes</b>
    <list listStyle="dash">
      <item>Produce edited output.</item>
      <item>Do not add, rename, or delete any files.</item>
      <item>No logging, TODOs, tests, or refactors unless explicitly requested.</item>
    </list>
  </item>
  <item>
    <b>Deliver clearly</b>
    <list listStyle="dash">
      <item>Begin with <code>PLAN:</code> (1-3 bullet points).</item>
      <item>Then output the code edit.</item>
      <item>Finish with <code>SUMMARY:</code> (what changed and why).</item>
    </list>
  </item>
</list>
</cp>

<p>---</p>

<cp caption="CODE FILES">
  <div for="file in files">
    <cp caption="FILENAME: {{file}}">
      <code inline="false"><document src="{{file}}" parser="txt" /></code>
    </cp>
  </div>
</cp>

<cp caption="USER REQUEST"><div whiteSpace="pre">{{ prompt }}</div></cp>

<p>---</p>

<p>Assistant, begin.</p>
</poml>



================================================
FILE: gallery/latex_edit.poml
================================================
<poml>
  <role>You are a LaTeX expert revising documents.</role>
  <task>{{ prompt }}</task>
  <cp caption="LaTeX Source">
    <document src="{{ file }}" parser="txt" for="file in files" />
  </cp>
  <output-format>Return only the updated LaTeX code.</output-format>
</poml>



================================================
FILE: gallery/latex_write.poml
================================================
<poml>
  <role>Skilled LaTeX author creating new content.</role>
  <task>{{ prompt }}</task>
  <cp caption="References">
    <document src="{{ file }}" parser="txt" for="file in files" />
  </cp>
  <output-format>Provide valid LaTeX only.</output-format>
</poml>



================================================
FILE: gallery/pdf_understanding.poml
================================================
<poml>
  <role>You help summarize and analyze PDF documents.</role>
  <task>{{ prompt }}</task>
  <cp caption="PDF">
    <document src="{{ file }}" parser="pdf" for="file in files" />
  </cp>
</poml>



================================================
FILE: gallery/table_understanding.poml
================================================
<poml>
  <role>You are a data analyst interpreting tables.</role>
  <task>{{ prompt }}</task>
  <cp caption="Table">
    <table src="{{ file }}" parser="auto" for="file in files" />
  </cp>
</poml>



================================================
FILE: gallery/word_understanding.poml
================================================
<poml>
  <role>You help interpret Word documents.</role>
  <task>{{ prompt }}</task>
  <cp caption="Document">
    <document src="{{ file }}" parser="docx" for="file in files" />
  </cp>
</poml>



================================================
FILE: media/style.css
================================================
body {
  --poml-padding: calc(var(--vscode-editor-font-size) * 0.8);
  --poml-padding-02: calc(var(--poml-padding) * 0.2);
  --poml-padding-035: calc(var(--poml-padding) * 0.35);
  --poml-padding-05: calc(var(--poml-padding) * 0.5);
  --poml-padding-08: calc(var(--poml-padding) * 0.8);
  --poml-padding-15: calc(var(--poml-padding) * 1.5);

  --poml-font-family: var(--vscode-font-family);
  --poml-font-size: var(--vscode-editor-font-size);
  --poml-font-size-08: calc(var(--vscode-editor-font-size) * 0.8);
  --poml-font-size-09: calc(var(--vscode-editor-font-size) * 0.9);
  --poml-font-size-12: calc(var(--vscode-editor-font-size) * 1.2);
  --poml-font-size-15: calc(var(--vscode-editor-font-size) * 1.5);
  --poml-font-size-20: calc(var(--vscode-editor-font-size) * 2);

  --poml-color-border: var(--vscode-editorRuler-foreground);
  --poml-color-background: var(--vscode-editor-background);
  --poml-color-background-code: var(--vscode-textPreformat-background);
  --poml-color-text: var(--vscode-editor-foreground);

  font-size: var(--poml-font-size);
  line-height: var(--vscode-editor-line-height);
  color: var(--poml-color-text);
  padding-top: var(--poml-padding);
  padding-bottom: var(--poml-padding);
}

.vscode-body {
/*   position: fixed;
  width: 100%;
  height: 100%;
    */
  font-family: var(--poml-font-family);
  font-size: var(--poml-font-size);
  line-height: var(--vscode-editor-line-height);
  color: var(--poml-color-text);
  padding-top: var(--poml-padding);
  padding-bottom: var(--poml-padding);
  background: var(--poml-color-background);
}

.hidden {
  display: none;
}

/* toolbar */
.toolbar {
  display: flex;
  flex-direction: column;
  gap: var(--poml-padding);
}

.toolbar-buttons {
  display: flex;
  gap: var(--poml-padding);
  align-items: center;
}

.toolbar-files {
  display: flex;
  gap: var(--poml-padding-05);
  flex-wrap: wrap;
  align-items: center;
}

.chips.hidden {
  display: none;
}

.toolbar .button {
  align-items: center;
  display: flex;
  justify-content: space-between;
  position: relative;
  gap: var(--poml-padding-05);
  padding: var(--poml-padding-035) var(--poml-padding-05);
  cursor: default;
  font-size: var(--poml-font-size);
  border: 1px solid var(--vscode-editorWidget-border);
  border-radius: 3px;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.toolbar .button:hover, .toolbar .button.menu-selection.active {
  background: var(--vscode-toolbar-hoverBackground);
}

.toolbar .button:active {
  background: var(--vscode-toolbar-activeBackground);
}

.toolbar .button .avatar, .toolbar .button .expand {
  height: var(--poml-font-size-20);
  width: var(--poml-font-size-20);
  align-items: center;
  display: flex;
  justify-content: center;
}

.toolbar .button>.content {
  margin-right: var(--poml-padding-035);
}

.toolbar .button .expand {
  width: auto;
}

.toolbar .button .badge {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--vscode-badge-background);
  color: var(--vscode-badge-foreground);
  border-radius: 50%;
  width: var(--poml-font-size-15);
  height: var(--poml-font-size-15);
  line-height: var(--poml-font-size);
}

.toolbar .button .avatar .codicon {
  font-size: var(--poml-font-size-15);
}

.toolbar .button .expand .codicon {
  font-size: var(--poml-font-size);
}

.toolbar .button.onoff.active {
  border: 1px solid var(--vscode-focusBorder);
  background: var(--vscode-editor-selectionBackground);
}

.toolbar .button .menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  margin-top: var(--poml-padding-05);
  background: var(--vscode-editorWidget-background);
  border: 1px solid var(--vscode-editorWidget-border);
  border-radius: 4px;
  min-width: calc(var(--poml-font-size) * 15);
  box-shadow: 0 2px 8px var(--vscode-widget-shadow);
  z-index: 1000;
}

.toolbar .menu-selection.active .menu {
  display: block;
}

/* Menu item styles */
.toolbar .menu .item {
  display: flex;
  align-items: center;
  padding: var(--poml-padding-05);
  gap: var(--poml-padding-05);
  cursor: default;
}

.toolbar .menu .item:hover {
  background: var(--vscode-list-hoverBackground);
}

.chips {
  display: flex;
  gap: var(--poml-padding-05);
  flex-wrap: wrap;
  align-items: center;
}

.chip {
  position: relative;
  display: flex;
  align-items: center;
  padding: var(--poml-padding-02) var(--poml-padding-035);
  border: 1px solid var(--vscode-editorWidget-border);
  border-radius: 4px;
  font-size: var(--poml-font-size-08);
}

.chip .content {
  color: var(--vscode-editor-foreground);
  cursor: default;
}

.chip .codicon {
  padding: 0 var(--poml-padding-02);
  font-size: var(--poml-font-size) !important;
}

.chip .remove {
  margin-left: var(--poml-padding-02);
  padding-right: 0;
  cursor: pointer;
}

.chip .remove:hover {
  background: var(--vscode-toolbar-hoverBackground);
}

.chip.add {
  cursor: pointer;
}

.chip.add:hover {
  background: var(--vscode-toolbar-hoverBackground);
}

.menu .item .avatar {
  height: var(--poml-font-size-15);
  width: var(--poml-font-size-15);
  opacity: 0;
}

.menu .item.selected .avatar {
  opacity: 1;
}

select {
  background-color: var(--vscode-dropdown-background);
  border-radius: 0;
  color: var(--vscode-dropdown-foreground);
  border: var(--vscode-dropdown-border);
  padding: var(--poml-padding-05);
}

pre {
  font-family: var(--vscode-editor-font-family);
  background-color: var(--poml-color-background-code);
  white-space: pre-wrap;
  padding: var(--poml-padding-05);
  line-height: 1.2em;
  margin: 0;
}

pre code {
  background-color: transparent;
}

.vscode-form {
  display: flex;
}

.vscode-form-input {
  flex: 1;
  margin-right: var(--vscode-editor-font-size);
}

.font-weight-bold {
  font-weight: bold;
}

.code-non-chat {
  margin: var(--poml-padding) 0;
}

.chat-message {
  display: flex;
  flex-direction: column;
  gap: var(--poml-padding-08);
  padding: var(--poml-padding-15) 0;
}

.chat-message:not(:last-child) {
  border-bottom: 1px solid var(--poml-color-border);
}

.chat-message-header {
  align-items: center;
  display: flex;
  justify-content: space-between;
  position: relative;
}

.chat-message-header .content {
  align-items: center;
  display: flex;
  gap: var(--poml-padding);
}

.chat-message-header .content .avatar {
  align-items: center;
  border-radius: 50%;
  display: flex;
  height: var(--poml-font-size-20);
  width: var(--poml-font-size-20);
  justify-content: center;
  outline: 1px solid var(--poml-color-border);
}

.chat-message-header .content .avatar .codicon {
  color: var(--poml-color-text);
  font-size: var(--poml-font-size-12);
}

.chat-message-header .content .name {
  font-weight: bold;
  font-size: var(--poml-font-size-12);
  margin: 0;
}

.chat-message-header .token-count {
  margin-left: var(--poml-padding);
  font-weight: normal;
  font-size: var(--poml-font-size-09);
  color: var(--vscode-descriptionForeground);
}

.chat-message-toolbar {
  position: absolute;
  right: 0;
  gap: var(--poml-padding);
  align-items: center;
  display: flex;
  height: 100%;
  margin: 0 auto;
  padding: 0;
}

.chat-message-toolbar .toolbar-item {
  align-items: center;
  cursor: pointer;
  display: block;
  justify-content: center;
  position: relative;
}

.chat-message-toolbar .toolbar-item .codicon {
  position: relative;
  padding: var(--poml-padding-02);
  font-size: var(--poml-font-size-12);
  color: var(--vscode-editor-foreground);
  height: var(--poml-font-size-12);
  width: var(--poml-font-size-12);
  border: 1px solid transparent;
  border-radius: 50%;
}

.chat-message-toolbar .toolbar-item:hover {
  background-color: var(--vscode-toolbar-hoverBackground);
}

.main-container {
  padding: var(--poml-padding-15) 0;
}

.tooltip {
  visibility: hidden;
  width: auto;
  font-size: var(--poml-font-size-08);
  background-color: var(--poml-color-background);
  color: var(--poml-color-text);
  text-align: center;
  border: 1px solid var(--poml-color-border);
  border-radius: 3px;
  padding: var(--poml-padding-05);
  position: absolute;
  z-index: 1;
  top: 150%;
  left: 50%;
  margin-left: -50%;
}

.tooltip-long {
  word-wrap: break-word;
  text-align: left;
}

.tooltip-anchor:hover .tooltip {
  visibility: visible;
}

.chat-message-content {
  padding: 0 var(--poml-padding-02);
}

.token-total {
  text-align: right;
  font-size: var(--poml-font-size-09);
  color: var(--vscode-descriptionForeground);
}



================================================
FILE: packages/poml/base.tsx
================================================
/**
 * The very basic logics that drive "every" component in the system.
 * The "every" is the criteria whether the logic should serve as a base.
 * For example, the stylesheet is considered as a base, as it's supported in every component,
 * but markup presentation is not.
 */

import * as React from 'react';
import { distance } from 'closest-match';
import { deepMerge } from './util';
import componentDocs from './assets/componentDocs.json';
import path from 'path';
import flattenChildren from 'react-keyed-flatten-children';

export type Speaker = 'system' | 'human' | 'ai';
export const ValidSpeakers = ['system', 'human', 'ai'];

/**
 * This is to show in the final rendered prompt.
 */
export interface ContentMultiMedia {
  type: string; // image/png, image/jpeg, ...,
  base64: string;
  alt?: string;
}

export type RichContent = string | (string | ContentMultiMedia)[];

export interface Message {
  speaker: Speaker;
  content: RichContent;
}

export interface SourceMapRichContent {
  startIndex: number;
  endIndex: number;
  irStartIndex: number;
  irEndIndex: number;
  content: RichContent;
}

export interface SourceMapMessage {
  startIndex: number;
  endIndex: number;
  irStartIndex: number;
  irEndIndex: number;
  speaker: Speaker;
  content: SourceMapRichContent[];
}

export function richContentFromSourceMap(contents: SourceMapRichContent[]): RichContent {
  const parts: (string | ContentMultiMedia)[] = [];

  const append = (txt: string) => {
    if (parts.length > 0 && typeof parts[parts.length - 1] === 'string') {
      parts[parts.length - 1] = (parts[parts.length - 1] as string) + txt;
    } else if (txt.length > 0) {
      parts.push(txt);
    }
  };

  for (const seg of contents) {
    const c = seg.content as any;
    if (typeof c === 'string') {
      append(c);
    } else if (Array.isArray(c)) {
      for (const item of c) {
        if (typeof item === 'string') {
          append(item);
        } else {
          parts.push(item);
        }
      }
    } else {
      parts.push(c);
    }
  }

  if (parts.length === 1) {
    return typeof parts[0] === 'string' ? parts[0] : [parts[0]];
  }
  return parts;
}

/**
 * Props base serves the following props subclass, as far as I can now think of:
 * 1. Props for markup basic components
 * 2. Props for serialization basic components
 * 3. Props for essential general components
 *   3.1. Props for other high-level components
 */
export interface PropsBase {
  speaker?: Speaker;
  className?: string;

  // Record the original start and end index in the raw text file for debugging purposes.
  // Marked as "original" to distinguish from the index in writer.
  originalStartIndex?: number;
  originalEndIndex?: number;

  // Source path for diagnostics
  sourcePath?: string;

  // Experimental
  writerOptions?: object;
  whiteSpace?: 'pre' | 'filter' | 'trim';

  /** Soft character limit before truncation is applied. */
  charLimit?: number;
  /** Soft token limit before truncation is applied. */
  tokenLimit?: number;
  /** Priority used when truncating globally. Lower numbers are dropped first. */
  priority?: number;
}

/**
 * Create an element that will be visible in the IR.
 * Helper function for logging and debugging purposes.
 */
export const irElement = (type: string, props: any, ...children: React.ReactNode[]) => {
  if (props.speaker && !ValidSpeakers.includes(props.speaker)) {
    ErrorCollection.add(ReadError.fromProps(`"${props.speaker}" is not a valid speaker.`, props));
    props.speaker = undefined;
  }
  const propsWithoutUndefined = Object.fromEntries(
    Object.entries(props)
      .filter(([_, v]) => v !== undefined)
      .map(([k, v]) => {
        const hyphenCaseKey = k.replace(/[A-Z]/g, m => '-' + m.toLowerCase());
        if (typeof v === 'boolean') {
          return [hyphenCaseKey, v.toString()];
        } else if (typeof v === 'number') {
          return [hyphenCaseKey, v.toString()];
        } else if (typeof v === 'object') {
          return [hyphenCaseKey, JSON.stringify(v)];
        } else {
          return [hyphenCaseKey, v];
        }
      })
  );

  const trimmedChildren = trimChildrenWhiteSpace(children, props);
  return React.createElement(type, propsWithoutUndefined, ...trimmedChildren);
};

export function trimChildrenWhiteSpace(children: React.ReactNode, props: PropsBase) {
  // This is exposed for providers.
  // The children directly under a context provider also needs to be trimmed,
  // otherwise they do not have a chance to be trimmed.
  let flattenedChildren = flattenChildren(children);

  // Merge consecutive strings.
  if (props.whiteSpace !== 'pre') {
    const mergedChildren: React.ReactNode[] = [];
    let currentString: string = '';
    for (const child of flattenedChildren) {
      if (typeof child === 'string') {
        currentString += child;
      } else {
        if (currentString) {
          mergedChildren.push(currentString);
          currentString = '';
        }
        mergedChildren.push(child);
      }
    }
    if (currentString) {
      mergedChildren.push(currentString);
    }
    flattenedChildren = mergedChildren;
  }

  const trimmedChildren = flattenedChildren
    .map((child, index) => {
      if (typeof child === 'string') {
        if (props.whiteSpace === 'pre') {
          return child;
        } else if (props.whiteSpace === 'filter' || props.whiteSpace === undefined) {
          return trimText(child, index === 0, index === flattenedChildren.length - 1);
        } else if (props.whiteSpace === 'trim') {
          return index === 0
            ? child.trimStart()
            : index === flattenedChildren.length - 1
              ? child.trimEnd()
              : child;
        } else {
          ErrorCollection.add(
            ReadError.fromProps(`"${props.whiteSpace}" is not a valid whiteSpace option.`, props)
          );
          return child;
        }
      } else {
        return child;
      }
    })
    .filter(c => c !== '');
  return trimmedChildren;
}

/**
 * Trim the element tree following the CSS rules
 * https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Whitespace
 */
const trimText = (text: string, isFirst: boolean, isLast: boolean): string => {
  // 1. all spaces and tabs immediately before and after a line break are ignored
  text = text.replace(/[\t\n\r ]*\n[\t\n\r ]*/g, '\n');
  // 2. all tab characters and line breaks are handled as space characters
  text = text.replace(/[\t\n\r]/g, ' ');
  // 3. multiple space characters are handled as one space character
  text = text.replace(/ +/g, ' ');
  // 4. sequences of spaces at the beginning and end of an element are removed
  if (isFirst) {
    text = text.replace(/^ +/, '');
  }
  if (isLast) {
    text = text.replace(/ +$/, '');
  }
  return text;
};

/**
 * Error type.
 */

interface PomlErrorOptions extends ErrorOptions {
  severity?: 'error' | 'warning';
}

class PomlError extends Error {
  public severity: 'error' | 'warning' = 'error';

  constructor(message: string, options?: PomlErrorOptions) {
    super(message, options);
    this.name = 'PomlError';
    if (options?.severity) {
      this.severity = options.severity;
    }
  }
}

export class SystemError extends PomlError {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = 'SystemError';
  }
}

export class ReadError extends PomlError {
  constructor(
    message: string,
    public startIndex?: number,
    public endIndex?: number,
    public sourcePath?: string,
    options?: PomlErrorOptions
  ) {
    super(message, options);
    this.name = 'ReadError';
  }

  public static fromProps(message: string, props: PropsBase, options?: PomlErrorOptions) {
    return new ReadError(message, props.originalStartIndex, props.originalEndIndex, props.sourcePath, options);
  }
}

export class WriteError extends PomlError {
  constructor(
    message: string,
    public startIndex?: number,
    public endIndex?: number,
    public sourcePath?: string,
    public irStartIndex?: number,
    public irEndIndex?: number,
    public relatedIr?: string,
    options?: PomlErrorOptions
  ) {
    super(message, options);
    this.name = 'WriteError';
  }
}

/**
 * A can to hold all the errors.
 */

export class ErrorCollection {
  private errors: PomlError[] = [];

  private static _instance: ErrorCollection;

  private constructor() {}

  public static get instance() {
    if (!this._instance) {
      this._instance = new ErrorCollection();
    }
    return this._instance;
  }

  public static add(error: PomlError) {
    this.instance.errors.push(error);
  }

  public static first() {
    return this.instance.errors[0];
  }

  public static last() {
    return this.instance.errors[this.instance.errors.length - 1];
  }

  public static list() {
    return this.instance.errors;
  }

  public static empty() {
    return this.instance.errors.length === 0;
  }

  public static clear() {
    this.instance.errors = [];
  }
}

function calculateSize(value: any, visited = new Set<any>()): number {
  if (value === null || value === undefined) {
    return 0;
  }
  if (visited.has(value)) {
    return 0;
  }
  if (Buffer.isBuffer(value)) {
    return value.length;
  }
  const t = typeof value;
  if (t === 'string') {
    return Buffer.byteLength(value);
  }
  if (t === 'number' || t === 'boolean' || t === 'bigint') {
    return 8;
  }
  if (Array.isArray(value)) {
    visited.add(value);
    let size = 0;
    for (const item of value) {
      try {
        size += calculateSize(item, visited);
      } catch {
        // ignore
      }
    }
    visited.delete(value);
    return size;
  }
  if (t === 'object') {
    visited.add(value);
    let size = 0;
    for (const key in value) {
      try {
        size += calculateSize((value as any)[key], visited);
      } catch {
        // ignore
      }
    }
    visited.delete(value);
    return size;
  }
  return 0;
}

export class BufferCollection {
  private buffers: Map<string, { value: any; size: number }> = new Map();
  private totalSize = 0;
  private limit = 10 * 1024 * 1024; // 10MB default

  private static _instance: BufferCollection;

  private constructor() {}

  public static get instance() {
    if (!this._instance) {
      this._instance = new BufferCollection();
    }
    return this._instance;
  }

  private evict() {
    while (this.totalSize > this.limit && this.buffers.size > 0) {
      const oldestKey = this.buffers.keys().next().value as string;
      const entry = this.buffers.get(oldestKey);
      if (entry) {
        this.totalSize -= entry.size;
      }
      this.buffers.delete(oldestKey);
    }
  }

  public static get<T>(key: string): T | undefined {
    const entry = this.instance.buffers.get(key);
    return entry ? (entry.value as T) : undefined;
  }

  public static set(key: string, value: any) {
    const inst = this.instance;
    const prev = inst.buffers.get(key);
    if (prev) {
      inst.totalSize -= prev.size;
    }
    const entrySize = calculateSize(value);
    if (entrySize > inst.limit) {
      return;
    }
    inst.buffers.set(key, { value, size: entrySize });
    inst.totalSize += entrySize;
    inst.evict();
  }

  public static clear() {
    this.instance.buffers.clear();
    this.instance.totalSize = 0;
  }
}

export const useWithCatch = <T,>(promise: Promise<T>, props: PropsBase) => {
  const catchedPromise = promise.catch((err: any) => {
    if (err instanceof PomlError) {
      ErrorCollection.add(err);
    } else {
      ErrorCollection.add(
        ReadError.fromProps(
          err && err.message
            ? err.message
            : 'Unknown error happened during asynchroneous process of rendering.',
          props,
          { cause: err }
        )
      );
    }
  });
  return React.use(catchedPromise);
};

/**
 * Stylesheet is a way to configure the props to be used in the components globally.
 * It can be used to set multiple things, including markup syntax, presentation approach,
 * text formats, and more, as long as they are supported by the components' props.
 * If a globally set prop is not supported by a component, it will be ignored.
 *
 * The style can be set for all components or for a specific component type, such as:
 *
 * ```tsx
 * const stylesheet = {
 *   '*': {
 *     presentation: 'markup',
 *     markupLang: 'markdown',
 *     listStyle: 'unordered'
 *   },
 *   'table': {
 *     presentation: 'serialize',
 *     serializer: 'json'
 *   },
 *   Example: {
 *     messageInteraction: true
 *   },
 *   TaskDescription: {
 *     titleMarkupTransform: 'header',
 *     titleTextTransform: {
 *       case: 'upper'
 *     }
 *   }
 * }
 * ```
 *
 * The stylesheet can be then set via a `StyleSheetProvider` component:
 *
 * ```tsx
 * <StyleSheetProvider stylesheet={stylesheet}><MyPrompt /></StyleSheetProvider>
 * ```
 */
export interface StyleSheet {
  // Match can be a component name, a wildcard, or a class name.
  // One component can have multiple aliases, which are all valid for matching.
  [match: string]: AnyProps;
}

type AnyProps = { [x: string]: unknown };

const StyleSheetContext = React.createContext<StyleSheet>({});

export const StyleSheetProvider = ({
  stylesheet,
  children
}: React.PropsWithChildren<{ stylesheet: StyleSheet }>) => {
  const currentStylesheet = React.useContext(StyleSheetContext);
  // Deep merge stylesheet
  stylesheet = deepMerge(currentStylesheet, stylesheet);
  return <StyleSheetContext.Provider value={stylesheet}>{children}</StyleSheetContext.Provider>;
};

const useStyleSheet = () => React.useContext(StyleSheetContext);

const computeStyles = <T,>(
  currentProps: T,
  component: PomlComponent,
  _stylesheet?: StyleSheet
): T => {
  const stylesheet = _stylesheet !== undefined ? _stylesheet : useStyleSheet();

  // priority, order, props
  const matches: [number, number, AnyProps][] = [];
  Object.entries(stylesheet).forEach(([match, props], index) => {
    if (match === '*') {
      matches.push([0, index, props]);
    } else {
      const matchResult: number[] = match.split(/\s+/g).map(indiv => {
        // FIXME: this is different from css rule
        if (indiv.startsWith('.')) {
          const currentClassName: string | undefined = (currentProps as any)?.className;
          const currentClasses = currentClassName ? currentClassName.split(/\s+/g) : [];
          return currentClasses.includes(indiv.slice(1)) ? 2 : 0;
        } else {
          return component.getAliases().includes(indiv.toLowerCase()) ? 1 : 0;
        }
      });
      if (matchResult.every(r => r > 0)) {
        matches.push([matchResult.reduce((a, b) => a + b, 0), index, props]);
      }
    }
  });

  matches.sort((a, b) => (a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]));
  const { className, ...restProps } = currentProps as any;
  matches.push([999, -1, restProps]);

  let finalProps = {};
  matches.forEach(([, , props]) => {
    finalProps = deepMerge(finalProps, props);
  });
  return finalProps as T;
};

// Source provider provides a path to the source file.
// It's used to find related files specified in the source file.
// It's also used to locate the source file for debugging purposes.
const SourceContext = React.createContext<string>('');
export const SourceProvider = ({
  source,
  children
}: React.PropsWithChildren<{ source: string }>) => {
  return <SourceContext.Provider value={source}>{children}</SourceContext.Provider>;
};
export const expandRelative = (src: string) => {
  if (path.isAbsolute(src)) {
    return src;
  }
  const pomlSource = React.useContext(SourceContext);
  if (!pomlSource) {
    return src;
  }
  return path.resolve(path.dirname(pomlSource), src);
};

export interface Parameter {
  name: string;
  type: string;
  fallbackType: string | undefined;
  choices: string[];
  description: string;
  defaultValue: string | undefined;
  required: boolean;
}

export interface ComponentSpec {
  name?: string;
  description: string;
  params: Parameter[];
  baseComponents: string[];
  example: string;
}

interface ComponentOptions {
  aliases: string[];
  requiredProps: string[];
  unwantedProps: string[];
  applyStyleSheet: boolean;
  asynchorous: boolean;
}

interface NonStrictComponentOptions {
  aliases?: string[];
  requiredProps?: string[];
  unwantedProps?: string[];
  applyStyleSheet?: boolean;
  asynchorous?: boolean;
}

export class PomlComponent {
  private officialName: string;
  private componentFunc: any;
  private options: ComponentOptions;

  public constructor(officialName: string, componentFunc: any, options: ComponentOptions) {
    this.officialName = officialName;
    this.componentFunc = componentFunc;
    this.options = options;
  }

  public get name() {
    return this.officialName;
  }

  public getAliases(lower: boolean = true) {
    if (lower) {
      return this.options.aliases.map(alias => alias.toLowerCase());
    } else {
      return this.options.aliases;
    }
  }

  private warnsIfProvided(props: any) {
    if (!props) {
      return;
    }
    this.options.unwantedProps.forEach(key => {
      if (props[key] !== undefined) {
        ErrorCollection.add(
          ReadError.fromProps(
            `"${key}" is not supported (but provided) in ${this.officialName}.`,
            props,
            { severity: 'warning' }
          )
        );
      }
    });
  }

  private throwIfMissing(props: any) {
    this.options.requiredProps.forEach(key => {
      if (!props || props[key] === undefined) {
        throw ReadError.fromProps(
          `"${key}" is required but not provided for ${this.officialName}, available props are ${props ? Object.keys(props) : []}.`,
          props
        );
      }
    });
  }

  public isPublic(): boolean {
    return this.spec() !== undefined;
  }

  public static fromSpec(spec: ComponentSpec): PomlComponent {
    const found = findComponentByAliasOrUndefined(spec.name ?? '');
    if (found !== undefined) {
      return found;
    }
    throw new SystemError(`Component ${spec.name} not found.`);
  }

  public spec(): ComponentSpec | undefined {
    return (componentDocs as ComponentSpec[]).find(document => document.name === this.name);
  }

  public parameters(): Parameter[] {
    const spec = this.spec();
    if (!spec) {
      return [];
    }
    const bases = this.mro();
    const parameters = [...spec.params];
    for (const base of bases) {
      const baseSpec = base.spec();
      if (baseSpec) {
        parameters.push(
          ...baseSpec.params.filter(p => !parameters.map(p => p.name).includes(p.name))
        );
      }
    }
    return parameters;
  }

  public mro(): PomlComponent[] {
    const spec = this.spec();
    if (!spec) {
      return [];
    }

    const toSearch = [...spec.baseComponents];
    const result: PomlComponent[] = [];
    let searchPointer: number = 0;
    while (searchPointer < toSearch.length) {
      const component = findComponentByAliasOrUndefined(toSearch[searchPointer]);
      if (component !== undefined) {
        result.push(component);
        const componentSpec = component.spec();
        if (componentSpec) {
          for (const base of componentSpec.baseComponents) {
            if (!toSearch.includes(base) && !result.map(c => c.name).includes(base)) {
              toSearch.push(base);
            }
          }
        }
      }
      searchPointer++;
    }
    return result;
  }

  public style(props: any, stylesheet?: StyleSheet) {
    return computeStyles(props, this, stylesheet);
  }

  private preprocessProps<T>(props: any): any {
    const params = this.parameters();
    return Object.entries(props).reduce(
      (acc, [key, value]: [string, any]) => {
        const param = params.find(param => param.name.toLowerCase() === key.toLowerCase());
        if (!param) {
          // Keep it.
          acc[key] = value;
          return acc;
        }
        const formalKey = param.name;
        if (value === undefined) {
          // TODO: check required parameters
          acc[key] = value;
          return acc;
        }
        if (param.type === 'string') {
          if (typeof value !== 'string' && value !== undefined) {
            value = value.toString();
          }
        } else if (param.type === 'number') {
          if (typeof value !== 'number' && value !== undefined) {
            value = parseFloat(value);
          }
        } else if (param.type === 'boolean') {
          if (typeof value !== 'boolean') {
            const isTrue = ['1', 'true'].includes(value.toString().toLowerCase());
            const isFalse = ['0', 'false'].includes(value.toString().toLowerCase());
            if (!isTrue && !isFalse) {
              ErrorCollection.add(ReadError.fromProps(`"${key}" should be a boolean`, props));
              value = undefined;
            }
            value = isTrue;
          }
        } else if (param.type === 'object' || param.type === 'object|string') {
          if (typeof value === 'string') {
            try {
              value = JSON.parse(value);
            } catch (e) {
              if (param.fallbackType !== 'string') {
                ErrorCollection.add(
                  ReadError.fromProps(`Fail to parse \"${key}\" with JSON parser`, props)
                );
              }
            }
          }
        } else if (param.type === 'RegExp' || param.type === 'RegExp|string') {
          if (typeof value === 'string') {
            if (value.startsWith('/')) {
              // Extract flags if present
              const lastSlashIndex = value.lastIndexOf('/');
              if (lastSlashIndex > 0) {
                const pattern = value.substring(1, lastSlashIndex);
                const flags = value.substring(lastSlashIndex + 1);
                // Only create RegExp with flags if flags exist and are valid
                if (flags && /^[gimsuy]*$/.test(flags)) {
                  value = new RegExp(pattern, flags);
                } else if (lastSlashIndex === value.length - 1) {
                  // Format is /pattern/ with no flags
                  value = new RegExp(pattern);
                }
              }
            } else {
              // Default behavior for strings not in /pattern/ format
              value = new RegExp(value);
            }
          }
        } else {
          // Keep as is.
        }
        if (param.choices.length > 0) {
          if (!param.choices.includes(value)) {
            ErrorCollection.add(
              ReadError.fromProps(
                `"${key}" should be one of ${param.choices.join(', ')}, not ${value}`,
                props
              )
            );
          }
        }
        acc[formalKey] = value;
        return acc;
      },
      {} as { [key: string]: any }
    );
  }

  public render(props: any) {
    this.warnsIfProvided(props);
    try {
      // If one of the following steps has error, abort the process.
      this.throwIfMissing(props);
      if (this.options.applyStyleSheet) {
        props = this.style(props);
      }
      props = this.preprocessProps(props);
      if (this.options.asynchorous) {
        const msg =
          'This prompt is asynchorous and still loading. Users should not see this message. ' +
          'If you see this message, please report it to the developer.';
        return (
          <React.Suspense fallback={<div>{msg}</div>}>{this.componentFunc(props)}</React.Suspense>
        );
      } else {
        return this.componentFunc(props);
      }
    } catch (e) {
      if (
        e &&
        typeof (e as any).message === 'string' &&
        (e as any).message.startsWith('Suspense Exception:')
      ) {
        throw e;
      }
      if (e instanceof PomlError) {
        ErrorCollection.add(e);
      } else {
        ErrorCollection.add(
          ReadError.fromProps(`Error in component render of ${this.officialName}: ${e}`, props, {
            cause: e
          })
        );
      }
      return null;
    }
  }
}

class ComponentRegistry {
  private static _instance: ComponentRegistry;

  private components: PomlComponent[] = [];

  private constructor() {}

  public static get instance() {
    if (!this._instance) {
      this._instance = new ComponentRegistry();
    }
    return this._instance;
  }

  public registerComponent(officialName: string, component: any, options: ComponentOptions) {
    if (!options.aliases.includes(officialName)) {
      options.aliases = [officialName, ...options.aliases];
    }
    options.aliases.forEach(alias => {
      const aliasExisting = this.components.filter(c =>
        c.getAliases().includes(alias.toLowerCase())
      );
      if (aliasExisting.length > 0) {
        throw new SystemError(`Alias "${alias}" is already used by ${aliasExisting[0]}.`);
      }
    });
    const registered = new PomlComponent(officialName, component, options);
    this.components.push(registered);
    return registered;
  }

  public unregisterComponent(name: string) {
    const component = this.getComponent(name);
    this.components = this.components.filter(c => c !== component);
  }

  public listComponents() {
    return [...this.components];
  }

  public getComponent(name: string, disabled?: Set<string>): PomlComponent | undefined;
  public getComponent(name: string, returnReasonIfNotFound: true, disabled?: Set<string>): PomlComponent | string;
  public getComponent(
    name: string,
    returnReasonIfNotFound: boolean | Set<string> = false,
    disabled: Set<string> | undefined = undefined
  ): PomlComponent | string | undefined {
    if (returnReasonIfNotFound instanceof Set) {
      disabled = returnReasonIfNotFound;
      returnReasonIfNotFound = false;
    }

    const hyphenToCamelCase = (s: string) => {
      return s.toLowerCase().replace(/-([a-z])/g, g => g[1].toUpperCase());
    };

    const nameVariants = [name.toLowerCase(), hyphenToCamelCase(name).toLowerCase()];

    for (const variant of nameVariants) {
      for (const component of this.components) {
        const aliases = component.getAliases();
        if (!aliases.includes(variant)) {
          continue;
        }
        if (disabled?.has(variant)) {
          continue;
        }
        return component;
      }
    }

    if (!returnReasonIfNotFound) {
      return undefined;
    }

    const availableAliases = this.components
      .flatMap(c => c.getAliases())
      .filter(a => !disabled?.has(a));

    const distances = availableAliases.map(alias => {
      return {
        alias: alias,
        dist: distance(alias.toLowerCase(), name.toLowerCase())
      };
    });
    distances.sort((a, b) => a.dist - b.dist);
    const doYouMean = distances.filter((d, index) => index < 1 || d.dist <= 2);
    return `Component ${name} not found. Do you mean: ${doYouMean.map(d => d.alias).join(', ')}?`;
  }
}

/**
 * Usage:
 * 1. `component('my-component', ['mc'])(MyComponent)`
 * 2. `component('my-component', {
 *   aliases: ['mc'],
 *   requiredProps: ['requiredProp'],
 *   unwantedProps: ['unwantedProp'],
 *   applyStyleSheet: false
 * })(MyComponent)`
 */
export function component(name: string, options?: string[]): <T>(fn: T) => T;
export function component(name: string, options?: NonStrictComponentOptions): <T>(fn: T) => T;
export function component(name: string, options?: string[] | NonStrictComponentOptions) {
  return <T,>(target: T): T => {
    const registered = ComponentRegistry.instance.registerComponent(
      name,
      target,
      options
        ? Array.isArray(options)
          ? {
              aliases: options,
              requiredProps: [],
              unwantedProps: [],
              applyStyleSheet: true,
              asynchorous: false
            }
          : {
              aliases: options.aliases ?? [],
              requiredProps: options.requiredProps ?? [],
              unwantedProps: options.unwantedProps ?? [],
              applyStyleSheet: options.applyStyleSheet ?? true,
              asynchorous: options.asynchorous ?? false
            }
        : {
            aliases: [],
            requiredProps: [],
            unwantedProps: [],
            applyStyleSheet: true,
            asynchorous: false
          }
    );
    return registered.render.bind(registered) as T;
  };
}

export function unregisterComponent(alias: string) {
  ComponentRegistry.instance.unregisterComponent(alias);
}

/**
 * Find a component by its alias. If not found, return a string that suggests the closest match.
 * @param alias Alias or official name.
 */
export function findComponentByAlias(
  alias: string,
  disabled?: Set<string>
): PomlComponent | string {
  return ComponentRegistry.instance.getComponent(alias, true, disabled);
}

export function findComponentByAliasOrUndefined(
  alias: string,
  disabled?: Set<string>
): PomlComponent | undefined {
  return ComponentRegistry.instance.getComponent(alias, disabled);
}

export function listComponents() {
  return ComponentRegistry.instance.listComponents();
}



================================================
FILE: packages/poml/cli.ts
================================================
#!/usr/bin/env node

import yargs from 'yargs/yargs';
import { hideBin } from 'yargs/helpers';
import { commandLine } from './index';

const args = yargs(hideBin(process.argv)).options({
  input: { type: 'string', alias: 'i', description: 'Input string' },
  file: { type: 'string', alias: 'f', description: 'Path to input file' },
  output: { type: 'string', alias: 'o', description: 'Path to output file' },
  context: { type: 'string', array: true, alias: 'c', description: 'Context variables' },
  contextFile: { type: 'string', alias: 'context-file', description: 'Path to context JSON file' },
  stylesheet: { type: 'string', alias: 's', description: 'Path to stylesheet file' },
  stylesheetFile: { type: 'string', alias: 'stylesheet-file', description: 'Path to stylesheet JSON file' },
  trim: { type: 'boolean', alias: 't', description: 'Trim whitespace between elements when parsing the input', default: true },
  speakerMode: { type: 'boolean', alias: 'chat', description: 'Output in speaker mode (JSON)', default: true },
  prettyPrint: { type: 'boolean', alias: 'p', description: 'Pretty print the output', default: false },
  strict: { type: 'boolean', description: 'Strict mode', default: true },
  cwd: { type: 'string', description: 'Working directory (defaults to file location if file is specified, otherwise current directory)' },
  traceDir: { type: 'string', description: 'Enable tracing and dump files to this directory' },
}).parseSync();

commandLine(args);



================================================
FILE: packages/poml/essentials.tsx
================================================
import * as React from 'react';
import { component, expandRelative, PropsBase, ReadError, useWithCatch } from './base';
import {
  Markup,
  Serialize,
  InlineProps,
  PropsMarkupBase,
  PropsSerializeBase,
  PropsPresentationBase,
  Presentation,
  computePresentationOrUndefined,
  PropsFreeBase,
  Free,
  MultiMedia
} from './presentation';
import fs from './util/fs';
import { preprocessImage } from './util/image';
import { preprocessAudio } from './util/audio';

export interface PropsSyntaxBase extends PropsBase {
  syntax?: string;
}

export type PropsSyntaxAny = PropsSyntaxBase & Serialize.AnyProps;

const FREE_SYNTAXES = ['text'];

const MARKUP_SYNTAXES = ['markdown', 'html', 'csv', 'tsv'];

const SERIALIZE_SYNTAXES = ['json', 'yaml', 'xml'];

const MULTIMEDIA_SYNTAXES = ['multimedia'];

export const computeSyntaxContext = (
  props: PropsSyntaxBase,
  defaultSyntax?: string,
  invalidPresentations?: string[]
): Presentation => {
  const { syntax, ...others } = props;
  invalidPresentations = invalidPresentations ?? ['multimedia'];

  // 1. Create the full presentation style based on the syntax shortcut.
  // This is the case when syntax is explicity specified.
  let presentationStyle:
    | PropsMarkupBase
    | PropsSerializeBase
    | PropsFreeBase
    | PropsPresentationBase;
  if (!syntax) {
    presentationStyle = {};
  } else if (MARKUP_SYNTAXES.includes(syntax)) {
    if (invalidPresentations.includes('markup')) {
      throw ReadError.fromProps(`Markup syntax (${syntax}) is not supported here.`, others);
    }
    presentationStyle = { presentation: 'markup', markupLang: syntax };
  } else if (SERIALIZE_SYNTAXES.includes(syntax)) {
    if (invalidPresentations.includes('serialize')) {
      throw ReadError.fromProps(`Serialize syntax (${syntax}) is not supported here.`, others);
    }
    presentationStyle = { presentation: 'serialize', serializer: syntax };
  } else if (FREE_SYNTAXES.includes(syntax)) {
    if (invalidPresentations.includes('free')) {
      throw ReadError.fromProps(`Free syntax (${syntax}) is not supported here.`, others);
    }
    presentationStyle = { presentation: 'free' };
  } else if (MULTIMEDIA_SYNTAXES.includes(syntax)) {
    if (invalidPresentations.includes('multimedia')) {
      throw ReadError.fromProps(`Multimedia syntax (${syntax}) is not supported here.`, others);
    }
    presentationStyle = { presentation: 'multimedia' };
  } else {
    throw ReadError.fromProps(`Unsupported syntax: ${syntax}`, others);
  }

  // 2. Compute the presentation context.
  // Try to inherit presentation and syntax from parents.
  // There are two cases where the inherited presentation does not count.
  // (a) No presentation is found.
  // (b) The presentation is free and the syntax is not specified.
  const presentation = computePresentationOrUndefined(presentationStyle);
  if (!presentation || (presentation === 'free' && !syntax)) {
    if (syntax) {
      // This should not happen. Must be a bug.
      throw ReadError.fromProps(
        `Syntax is specified (${syntax}) but presentation method is not found. Something is wrong.`,
        others
      );
    }

    // Try again with a default syntax
    return computeSyntaxContext(
      { ...others, syntax: defaultSyntax || 'markdown' },
      defaultSyntax,
      invalidPresentations
    );
  }
  return presentation;
};

// Helper component for contents that are designed for markup, but also work in other syntaxes.
export const AnyOrFree = component('AnyOrFree')((
  props: React.PropsWithChildren<PropsSyntaxAny & { presentation: Presentation; asAny: boolean }>
) => {
  const { syntax, children, presentation, name, type, asAny, ...others } = props;
  if (presentation === 'serialize') {
    if (asAny) {
      return (
        <Serialize.Any serializer={syntax} name={name} type={type} {...others}>
          {children}
        </Serialize.Any>
      );
    } else {
      return (
        <Serialize.Environment serializer={syntax} {...others}>
          {children}
        </Serialize.Environment>
      );
    }
  } else if (presentation === 'free') {
    return <Free.Text {...others}>{children}</Free.Text>;
  } else {
    throw ReadError.fromProps(
      `This component is not designed for ${presentation} syntaxes.`,
      others
    );
  }
});

/**
 * Text (`<text>`, `<poml>`) is a wrapper for any contents.
 * By default, it uses `markdown` syntax and writes the contents within it directly to the output.
 * When used with "markup" syntaxes, it renders a standalone section preceded and followed by one blank line.
 * It's mostly used in the root element of a prompt, but it should also work in any other places.
 * This component will be automatically added as a wrapping root element if it's not provided:
 * 1. If the first element is pure text contents, `<poml syntax="text">` will be added.
 * 2. If the first element is a POML component, `<poml syntax="markdown">` will be added.
 *
 * @param {'markdown'|'html'|'json'|'yaml|'xml'|'text'} syntax - The syntax of the content.
 * @param className - A class name for quickly styling the current block with stylesheets.
 * @param {'human'|'ai'|'system'} speaker - The speaker of the content. By default, it's determined by the context and the content.
 * @param name - The name of the content, used in serialization.
 * @param type - The type of the content, used in serialization.
 * @param {object} writerOptions - An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.
 *
 * @example
 * ```xml
 * <poml syntax="text">
 * Contents of the whole prompt.
 *
 * 1. Your customized list.
 * 2. You don't need to know anything about POML.
 * </poml>
 * ```
 *
 * To render the whole prompt in markdown syntax with a "human" speaker:
 *
 * ```xml
 * <poml syntax="markdown" speaker="human">
 *   <p>You are a helpful assistant.</p>
 *   <p>What is the capital of France?</p>
 * </poml>
 * ```
 */
export const Text = component('Text', ['div', 'poml'])((
  props: React.PropsWithChildren<PropsSyntaxAny>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props, 'markdown');

  if (presentation === 'markup') {
    return (
      <Paragraph syntax={syntax} blankLine={false} {...others}>
        {children}
      </Paragraph>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

export const Poml = Text;

/**
 * Paragraph (`<p>`) is a standalone section preceded by and followed by two blank lines in markup syntaxes.
 * It's mostly used for text contents.
 *
 * @param {boolean} blankLine - Whether to add one more blank line (2 in total) before and after the paragraph.
 *
 * @see {@link Text} for other props available.
 *
 * @example
 * ```xml
 * <p>Contents of the paragraph.</p>
 * ```
 */
export const Paragraph = component('Paragraph', ['p'])((
  props: React.PropsWithChildren<PropsSyntaxAny & Markup.ParagraphProps>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Paragraph markupLang={syntax} {...others}>
        {children}
      </Markup.Paragraph>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Inline (`<span>`) is a container for inline content.
 * When used with markup syntaxes, it wraps text in an inline style, without any preceding or following blank characters.
 * In serializer syntaxes, it's treated as a generic value.
 * Inline elements are not designed to be used alone (especially in serializer syntaxes).
 * One might notice problematic renderings (e.g., speaker not applied) when using it alone.
 *
 * @param {'markdown'|'html'|'json'|'yaml'|'xml'|'text'} syntax - The syntax of the content.
 * @param className - A class name for quickly styling the current block with stylesheets.
 * @param {'human'|'ai'|'system'} speaker - The speaker of the content. By default, it's determined by the context and the content.
 * @param {object} writerOptions - An experimental optional JSON string to customize the format of markdown headers, JSON indents, etc.
 *
 * @example
 * ```xml
 * <p>I'm listening to <span>music</span> right now.</p>
 * ```
 */
export const Inline = component('Inline', ['span'])((
  props: React.PropsWithChildren<PropsSyntaxBase>
) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Inline markupLang={syntax} {...others}>
        {children}
      </Markup.Inline>
    );
  } else {
    return (
      <AnyOrFree syntax={syntax} presentation={presentation} asAny={false} {...others}>
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Newline (`<br>`) explicitly adds a line break, primarily in markup syntaxes.
 * In serializer syntaxes, it's ignored.
 *
 * @param {number} newLineCount - The number of linebreaks to add.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * <br />
 * ```
 */
export const Newline = component('Newline', ['br'])((
  props: PropsSyntaxBase & Markup.NewlineProps
) => {
  const { syntax, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return <Markup.Newline markupLang={syntax} {...others} />;
  } else {
    return null;
  }
});

/**
 * Header (`<h>`) renders headings in markup syntaxes.
 * It's commonly used to highlight titles or section headings.
 * The header level will be automatically computed based on the context.
 * Use SubContent (`<section>`) for nested content.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <Header syntax="markdown">Section Title</Header>
 * ```
 */
export const Header = component('Header', ['h'])((
  props: React.PropsWithChildren<PropsSyntaxAny & Markup.ParagraphProps>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Header markupLang={syntax} {...others}>
        {children}
      </Markup.Header>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * SubContent (`<section>`) renders nested content, often following a header.
 * The headers within the section will be automatically adjusted to a lower level.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <h>Section Title</h>
 * <section>
 *   <h>Sub-section Title</h>  <!-- Nested header -->
 *   <p>Sub-section details</p>
 * </section>
 * ```
 */
export const SubContent = component('SubContent', ['section'])((
  props: React.PropsWithChildren<PropsSyntaxAny & Markup.ParagraphProps>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.SubContent markupLang={syntax} {...others}>
        {children}
      </Markup.SubContent>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Bold (`<b>`) emphasizes text in a bold style when using markup syntaxes.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * <p><b>Task:</b> Do something.</p>
 * ```
 */
export const Bold = component('Bold', ['b'])((props: React.PropsWithChildren<PropsSyntaxBase>) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Bold markupLang={syntax} {...others}>
        {children}
      </Markup.Bold>
    );
  } else {
    return (
      <AnyOrFree syntax={syntax} presentation={presentation} asAny={false} {...others}>
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Italic (`<i>`) emphasizes text in an italic style when using markup syntaxes.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * Your <i>italicized</i> text.
 * ```
 */
export const Italic = component('Italic', ['i'])((
  props: React.PropsWithChildren<PropsSyntaxBase>
) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Italic markupLang={syntax} {...others}>
        {children}
      </Markup.Italic>
    );
  } else {
    return (
      <AnyOrFree syntax={syntax} presentation={presentation} asAny={false} {...others}>
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Strikethrough (`<s>`, `<strike>`) indicates removed or invalid text in markup syntaxes.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * <s>This messages is removed.</s>
 * ```
 */
export const Strikethrough = component('Strikethrough', ['s', 'strike'])((
  props: React.PropsWithChildren<PropsSyntaxBase>
) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Strikethrough markupLang={syntax} {...others}>
        {children}
      </Markup.Strikethrough>
    );
  } else {
    return (
      <AnyOrFree syntax={syntax} presentation={presentation} asAny={false} {...others}>
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Underline (`<u>`) draws a line beneath text in markup syntaxes.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * This text is <u>underlined</u>.
 * ```
 */
export const Underline = component('Underline', ['u'])((
  props: React.PropsWithChildren<PropsSyntaxBase>
) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Underline markupLang={syntax} {...others}>
        {children}
      </Markup.Underline>
    );
  } else {
    return (
      <AnyOrFree syntax={syntax} presentation={presentation} asAny={false} {...others}>
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Code is used to represent code snippets or inline code in markup syntaxes.
 *
 * @param {boolean} inline - Whether to render code inline or as a block. Default is `true`.
 * @param lang - The language of the code snippet.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <code inline="true">const x = 42;</code>
 * ```
 *
 * ```xml
 * <code lang="javascript">
 * const x = 42;
 * </code>
 * ```
 */
export const Code = component('Code')((
  props: React.PropsWithChildren<PropsSyntaxAny & InlineProps & Markup.CodeProps>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.Code markupLang={syntax} {...others}>
        {children}
      </Markup.Code>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * List (`<list>`) is a container for multiple ListItem (`<item>`) elements.
 * When used with markup syntaxes, a bullet or numbering is added.
 *
 * @param {'star'|'dash'|'plus'|'decimal'|'latin'} listStyle - The style for the list marker, such as dash or star. Default is `dash`.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <list listStyle="decimal">
 *   <item>Item 1</item>
 *   <item>Item 2</item>
 * </list>
 * ```
 */
export const List = component('List')((
  props: React.PropsWithChildren<PropsSyntaxAny & Markup.ListProps & Markup.ParagraphProps>
) => {
  const { syntax, children, listStyle, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.List markupLang={syntax} listStyle={listStyle} {...others}>
        {children}
      </Markup.List>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type ?? 'array'}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * ListItem (`<item>`) is an item within a List component.
 * In markup mode, it is rendered with the specified bullet or numbering style.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <list listStyle="decimal">
 *   <item blankLine="true">Item 1</item>
 *   <item>Item 2</item>
 * </list>
 * ```
 */
export const ListItem = component('ListItem', ['item'])((
  props: React.PropsWithChildren<PropsSyntaxAny & Markup.ParagraphProps>
) => {
  const { syntax, children, name, type, ...others } = props;
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    return (
      <Markup.ListItem markupLang={syntax} {...others}>
        {children}
      </Markup.ListItem>
    );
  } else {
    return (
      <AnyOrFree
        syntax={syntax}
        presentation={presentation}
        asAny={true}
        name={name}
        type={type}
        {...others}
      >
        {children}
      </AnyOrFree>
    );
  }
});

/**
 * Object (`<obj>`, `<dataObj>`) displays external data or object content.
 * When in serialize mode, it's serialized according to the given serializer.
 *
 * @param {'markdown'|'html'|'json'|'yaml'|'xml'} syntax - The syntax or serializer of the content. Default is `json`.
 * @param {object} data - The data object to render.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * <Object syntax="json" data="{ key: 'value' }" />
 * ```
 */
export const Object = component('Object', ['obj', 'dataObj'])((
  props: React.PropsWithChildren<PropsSyntaxBase & Serialize.ObjectProps>
) => {
  const { syntax, children, ...others } = props;
  const presentation = computeSyntaxContext(props, 'json');
  if (presentation === 'serialize') {
    return (
      <Serialize.Object serializer={syntax} {...others}>
        {children}
      </Serialize.Object>
    );
  } else {
    return <Text syntax={syntax}>{JSON.stringify(props.data)}</Text>;
  }
});

interface ImageProps extends PropsSyntaxBase, MultiMedia.ImageProps {
  src?: string;
  maxWidth?: number;
  maxHeight?: number;
  resize?: number;
}

/**
 * Image (`<img>`) displays an image in the content.
 * Alternatively, it can also be shown as an alt text by specifying the `syntax` prop.
 * Note that syntax must be specified as `multimedia` to show the image.
 *
 * @see {@link Inline} for other props available.
 *
 * @param {string} src - The path to the image file.
 * @param {string} alt - The alternative text to show when the image cannot be displayed.
 * @param {string} base64 - The base64 encoded image data. It can not be specified together with `src`.
 * @param {string} type - The MIME type of the image **to be shown**. If not specified, it will be inferred from the file extension.
 *   If specified, the image will be converted to the specified type. Can be `image/jpeg`, `image/png`, etc., or without the `image/` prefix.
 * @param {'top'|'bottom'|'here'} position - The position of the image. Default is `here`.
 * @param {number} maxWidth - The maximum width of the image to be shown.
 * @param {number} maxHeight - The maximum height of the image to be shown.
 * @param {number} resize - The ratio to resize the image to to be shown.
 * @param {'markdown'|'html'|'json'|'yaml'|'xml'|'multimedia'} syntax - Only when specified as `multimedia`, the image will be shown.
 *   Otherwise, the alt text will be shown. By default, it's `multimedia` when `alt` is not specified. Otherwise, it's undefined (inherit from parent).
 *
 * @example
 * ```xml
 * <Image src="path/to/image.jpg" alt="Image description" position="bottom" />
 * ```
 */
export const Image = component('Image', { aliases: ['img'], asynchorous: true })((
  props: ImageProps
) => {
  let { syntax, src, base64, alt, type, position, maxWidth, maxHeight, resize, ...others } = props;
  if (!alt) {
    syntax = syntax ?? 'multimedia';
  }
  const presentation = computeSyntaxContext({ ...props, syntax }, 'multimedia', []);
  if (presentation === 'multimedia') {
    if (src) {
      if (base64) {
        throw ReadError.fromProps('Cannot specify both `src` and `base64`.', others);
      }
      src = expandRelative(src);
      if (!fs.existsSync(src)) {
        throw ReadError.fromProps(`Image file not found: ${src}`, others);
      }
    } else if (!base64) {
      throw ReadError.fromProps('Either `src` or `base64` must be specified.', others);
    }
    const image = useWithCatch(
      preprocessImage({ src, base64, type, maxWidth, maxHeight, resize }),
      others
    );
    if (!image) {
      return null;
    }
    return (
      <MultiMedia.Image
        presentation={presentation}
        base64={image.base64}
        position={position}
        type={image.mimeType}
        alt={alt}
        {...others}
      />
    );
  } else {
    return <Inline syntax={syntax}>{alt}</Inline>;
  }
});

interface AudioProps extends PropsSyntaxBase, MultiMedia.AudioProps {
  src?: string;
}

/**
 * Audio (`<audio>`) embeds an audio file in the content.
 *
 * Accepts either a file path (`src`) or base64-encoded audio data (`base64`).
 * The MIME type can be provided via `type` or will be inferred from the file extension.
 *
 * @param {string} src - Path to the audio file. If provided, the file will be read and encoded as base64.
 * @param {string} base64 - Base64-encoded audio data. Cannot be used together with `src`.
 * @param {string} alt - The alternative text to show when the image cannot be displayed.
 * @param {string} type - The MIME type of the audio (e.g., audio/mpeg, audio/wav). If not specified, it will be inferred from the file extension.
 *   The type must be consistent with the real type of the file. The consistency will NOT be checked or converted.
 *   The type can be specified with or without the `audio/` prefix.
 * @param {'top'|'bottom'|'here'} position - The position of the image. Default is `here`.
 * @param {'markdown'|'html'|'json'|'yaml'|'xml'|'multimedia'} syntax - Only when specified as `multimedia`, the image will be shown.
 *   Otherwise, the alt text will be shown. By default, it's `multimedia` when `alt` is not specified. Otherwise, it's undefined (inherit from parent).
 *
 * @example
 * ```xml
 * <Audio src="path/to/audio.mp3" />
 * ```
 * @example
 * ```xml
 * <Audio base64="..." type="audio/wav" />
 * ```
 */
export const Audio = component('Audio', { aliases: ['audio'], asynchorous: true })((
  props: AudioProps
) => {
  let { syntax, src, base64, type, ...others } = props;
  const presentation = computeSyntaxContext(props, 'multimedia', []);
  if (presentation === 'multimedia') {
    if (src) {
      if (base64) {
        throw ReadError.fromProps('Cannot specify both `src` and `base64`.', others);
      }
      src = expandRelative(src);
      if (!fs.existsSync(src)) {
        throw ReadError.fromProps(`Audio file not found: ${src}`, others);
      }
    } else if (!base64) {
      throw ReadError.fromProps('Either `src` or `base64` must be specified.', others);
    }
    const audio = useWithCatch(
      preprocessAudio({ src, base64, type }),
      others
    );
    if (!audio) {
      return null;
    }
    return (
      <MultiMedia.Audio
        presentation={presentation}
        base64={audio.base64}
        type={audio.mimeType}
        {...others}
      />
    );
  } else {
    return null;
  }
});



================================================
FILE: packages/poml/file.tsx
================================================
/**
 * Handles the files (with .poml extension).
 */

import { IToken, CstNode } from 'chevrotain';
import { DocumentCstNode, parse as parseXML } from '@xml-tools/parser';
import { buildAst, XMLAttribute, XMLDocument, XMLElement, XMLTextContent } from '@xml-tools/ast';
import * as React from 'react';
import {
  ComponentSpec,
  PomlComponent,
  ReadError,
  SourceProvider,
  findComponentByAlias,
  findComponentByAliasOrUndefined,
  listComponents
} from './base';
import { AnyValue, deepMerge, parseText, readSource } from './util';
import { StyleSheetProvider, ErrorCollection } from './base';
import { getSuggestions } from './util/xmlContentAssist';
import { existsSync, readFileSync } from './util/fs';
import path from 'path';
import { POML_VERSION } from './version';
import { Schema, ToolsSchema } from './util/schema';
import { z } from 'zod';

export interface PomlReaderOptions {
  trim?: boolean;
  autoAddPoml?: boolean;
  crlfToLf?: boolean;
}

interface PomlReaderConfig {
  trim: boolean;
  autoAddPoml: boolean;
  crlfToLf: boolean;
}

export interface PomlToken {
  type: 'element' | 'attribute' | 'attributeValue' | 'expression';
  range: Range;
  element?: string;
  attribute?: string; // specified only if it's an attribute
  value?: string; // specified only if it's an attribute value
  expression?: string; // specified only if it's an expression
}

/**
 * Temporarily used for document range and positional range.
 */
interface Range {
  start: number;
  end: number;
}

export class PomlFile {
  private text: string;
  private sourcePath: string | undefined;
  private config: PomlReaderConfig;
  private ast: XMLDocument | undefined;
  private cst: CstNode;
  private tokenVector: IToken[];
  private documentRange: Range;
  private disabledComponents: Set<string> = new Set();
  private expressionTokens: PomlToken[] = [];
  private expressionEvaluations: Map<string, any[]> = new Map();
  private responseSchema: Schema | undefined;
  private toolsSchema: ToolsSchema | undefined;
  private runtimeParameters: { [key: string]: any } | undefined;

  constructor(text: string, options?: PomlReaderOptions, sourcePath?: string) {
    this.config = {
      trim: options?.trim ?? true,
      autoAddPoml: options?.autoAddPoml ?? true,
      crlfToLf: options?.crlfToLf ?? true
    };
    this.text = this.config.crlfToLf ? text.replace(/\r\n/g, '\n') : text;
    this.sourcePath = sourcePath;
    if (this.sourcePath) {
      const envFile = this.sourcePath.replace(/(source\.)?\.poml$/i, '.env');
      if (existsSync(envFile)) {
        try {
          const envText = readFileSync(envFile, 'utf8');
          const match = envText.match(/^SOURCE_PATH=(.*)$/m);
          if (match) {
            // The real source path is specified in the .env file.
            this.sourcePath = match[1];
          }
        } catch {
          /* ignore */
        }
      }
    }

    this.documentRange = { start: 0, end: text.length - 1 };
    let { ast, cst, tokenVector, errors } = this.readXml(text);

    let addPoml: string | undefined = undefined;
    if (this.config.autoAddPoml && text.slice(5).toLowerCase() !== '<poml') {
      if (!ast || !ast.rootElement) {
        // Invalid XML. Treating it as a free text.
        addPoml = '<poml syntax="text" whiteSpace="pre">';
      } else if (
        // Valid XML, but contains e.g., multiple root elements.
        (ast.rootElement.position.startOffset > 0 &&
          !this.testAllCommentsAndSpace(
            0,
            ast.rootElement.position.startOffset - 1,
            tokenVector
          )) ||
        (ast.rootElement.position.endOffset + 1 < text.length &&
          !this.testAllCommentsAndSpace(
            ast.rootElement.position.endOffset + 1,
            text.length - 1,
            tokenVector
          ))
      ) {
        addPoml = '<poml syntax="markdown">';
      }
    }

    if (addPoml) {
      this.documentRange = { start: addPoml.length, end: text.length - 1 + addPoml.length };
      this.config.trim = options?.trim ?? false; // TODO: this is an ad-hoc fix.
      let { ast, cst, tokenVector, errors } = this.readXml(addPoml + text + '</poml>');
      this.ast = ast;
      this.cst = cst;
      this.tokenVector = tokenVector;
      // Report errors
      for (const error of errors) {
        ErrorCollection.add(error);
      }
    } else {
      this.ast = ast;
      this.cst = cst;
      this.tokenVector = tokenVector;
      for (const error of errors) {
        ErrorCollection.add(error);
      }
    }
  }

  private readXml(text: string) {
    const { cst, tokenVector, lexErrors, parseErrors } = parseXML(text);
    const errors: ReadError[] = [];

    for (const lexError of lexErrors) {
      errors.push(
        this.formatError(
          lexError.message,
          {
            start: this.ensureRange(lexError.offset),
            end: this.ensureRange(lexError.offset)
          },
          lexErrors
        )
      );
    }

    for (const parseError of parseErrors) {
      let startOffset = parseError.token.startOffset;
      let endOffset = parseError.token.endOffset;
      if (
        isNaN(startOffset) &&
        (endOffset === undefined || isNaN(endOffset)) &&
        (parseError as any).previousToken
      ) {
        startOffset = (parseError as any).previousToken.endOffset;
        endOffset = (parseError as any).previousToken.endOffset;
      }
      errors.push(
        this.formatError(
          parseError.message,
          {
            start: this.ensureRange(startOffset),
            end: endOffset ? this.ensureRange(endOffset) : this.ensureRange(startOffset)
          },
          parseError
        )
      );
    }

    let ast: XMLDocument | undefined = undefined;
    try {
      ast = buildAst(cst as any, tokenVector);
    } catch (e) {
      errors.push(
        this.formatError(
          'Error building AST',
          {
            start: this.ensureRange(0),
            end: this.ensureRange(text.length)
          },
          e
        )
      );
    }

    return { ast, cst, tokenVector, errors };
  }

  private testAllCommentsAndSpace(
    startOffset: number,
    endOffset: number,
    tokens: IToken[]
  ): boolean {
    // start to end, inclusive. It must not be in the middle of a token.
    const tokensFiltered = tokens.filter(
      (token: IToken) =>
        token.startOffset >= startOffset && (token.endOffset ?? token.startOffset) <= endOffset
    );
    return tokensFiltered.every((token: IToken) => {
      if (token.tokenType.name === 'SEA_WS' || token.tokenType.name === 'Comment') {
        return true;
      } else if (/^\s*$/.test(token.image)) {
        return true;
      }
      return false;
    });
  }

  private readJsonElement(parent: XMLElement, tagName: string): any | undefined {
    const element = xmlElementContents(parent).filter(
      i => i.type === 'XMLElement' && i.name?.toLowerCase() === tagName.toLowerCase()
    ) as XMLElement[];
    if (element.length === 0) {
      return undefined;
    }

    if (element.length > 1) {
      this.reportError(`Multiple ${tagName} element found.`, {
        start: this.ensureRange(element[0].position.startOffset),
        end: this.ensureRange(element[element.length - 1].position.endOffset)
      });
      return undefined;
    }

    const text = xmlElementText(element[0]);
    try {
      return JSON.parse(text);
    } catch (e) {
      this.reportError(
        e !== undefined && (e as Error).message
          ? (e as Error).message
          : `Error parsing JSON: ${text}`,
        this.xmlElementRange(element[0]),
        e
      );
      return undefined;
    }
  }

  public getResponseSchema(): Schema | undefined {
    return this.responseSchema;
  }

  public getToolsSchema(): ToolsSchema | undefined {
    return this.toolsSchema;
  }

  public getRuntimeParameters(): { [key: string]: any } | undefined {
    return this.runtimeParameters;
  }

  public xmlRootElement(): XMLElement | undefined {
    if (!this.ast || !this.ast.rootElement) {
      this.reportError('Root element is invalid.', {
        start: this.ensureRange(this.documentRange.start),
        end: this.ensureRange(this.documentRange.end)
      });
      return undefined;
    } else {
      return this.ast.rootElement;
    }
  }

  public react(context?: { [key: string]: any }): React.ReactElement {
    this.expressionTokens = [];
    this.expressionEvaluations.clear();
    const rootElement = this.xmlRootElement();

    if (rootElement) {
      // See whether stylesheet and context is available
      const stylesheet = this.readJsonElement(rootElement, 'stylesheet');
      context = deepMerge(context || {}, this.readJsonElement(rootElement, 'context') || {});

      let parsedElement = this.parseXmlElement(rootElement, context || {}, {});
      if (stylesheet) {
        parsedElement = React.createElement(StyleSheetProvider, { stylesheet }, parsedElement);
      }
      if (this.sourcePath) {
        parsedElement = React.createElement(
          SourceProvider,
          { source: this.sourcePath },
          parsedElement
        );
      }
      return parsedElement;
    } else {
      return <></>;
    }
  }

  public getHoverToken(offset: number): PomlToken | undefined {
    const realOffset = this.recoverPosition(offset);
    if (!this.ast || !this.ast.rootElement) {
      return undefined;
    }
    return this.findTokenInElement(this.ast.rootElement, realOffset);
  }

  public getCompletions(offset: number): PomlToken[] {
    const realOffset = this.recoverPosition(offset);
    if (!this.ast || !this.ast.rootElement) {
      return [];
    }

    return getSuggestions({
      ast: this.ast,
      cst: this.cst as DocumentCstNode,
      tokenVector: this.tokenVector,
      offset: realOffset,
      providers: {
        // 1. There are more types(scenarios) of suggestions providers (see api.d.ts)
        // 2. Multiple providers may be supplied for a single scenario.
        elementName: [this.handleElementNameCompletion(realOffset)],
        elementNameClose: [this.handleElementNameCloseCompletion(realOffset)],
        attributeName: [this.handleAttributeNameCompletion(realOffset)],
        attributeValue: [this.handleAttributeValueCompletion(realOffset)]
      }
    });
  }

  public getExpressionTokens(): PomlToken[] {
    if (this.expressionTokens.length > 0) {
      return this.expressionTokens;
    }
    if (!this.ast || !this.ast.rootElement) {
      return [];
    }
    const tokens: PomlToken[] = [];
    const regex = /{{\s*(.+?)\s*}}(?!})/gm;

    const visit = (element: XMLElement) => {
      // Special handling for meta elements with lang="expr"
      if (element.name?.toLowerCase() === 'meta') {
        const langAttr = xmlAttribute(element, 'lang');
        const typeAttr = xmlAttribute(element, 'type');
        const isSchemaType = typeAttr?.value === 'responseSchema' || typeAttr?.value === 'tool';
        const text = xmlElementText(element).trim();

        // Check if it's an expression (either explicit lang="expr" or auto-detected)
        if (isSchemaType && (langAttr?.value === 'expr' || (!langAttr && !text.trim().startsWith('{')))) {
          const position = this.xmlElementRange(element.textContents[0]);
          tokens.push({
            type: 'expression',
            range: position,
            expression: text.trim(),
          });
          return;
        }
      }

      // attributes
      for (const attr of element.attributes) {
        if (!attr.value) {
          continue;
        }
        if (attr.key?.toLowerCase() === 'if' || attr.key?.toLowerCase() === 'for') {
          tokens.push({
            type: 'expression',
            range: this.xmlAttributeValueRange(attr),
            expression: attr.value
          });
          continue;
        }
        if (element.name?.toLowerCase() === 'let' && attr.key?.toLowerCase() === 'value') {
          tokens.push({
            type: 'expression',
            range: this.xmlAttributeValueRange(attr),
            expression: attr.value
          });
          continue;
        }
        const range = this.xmlAttributeValueRange(attr);
        regex.lastIndex = 0;
        let match: RegExpExecArray | null;
        while ((match = regex.exec(attr.value))) {
          tokens.push({
            type: 'expression',
            range: {
              start: range.start + match.index,
              end: range.start + match.index + match[0].length - 1,
            },
            expression: match[1],
          });
        }
      }

      // text contents
      for (const tc of element.textContents) {
        const text = tc.text || '';
        const pos = this.xmlElementRange(tc);

        // Regular template expression handling for other elements and JSON
        regex.lastIndex = 0;
        let match: RegExpExecArray | null;
        while ((match = regex.exec(text))) {
          tokens.push({
            type: 'expression',
            range: {
              start: pos.start + match.index,
              end: pos.start + match.index + match[0].length - 1,
            },
            expression: match[1],
          });
        }
      }

      for (const child of element.subElements) {
        visit(child);
      }
    };

    visit(this.ast.rootElement);
    return tokens;
  }

  public getExpressionEvaluations(range: Range): any[] {
    const key = `${range.start}:${range.end}`;
    return this.expressionEvaluations.get(key) ?? [];
  }

  private recordEvaluation(range: Range, output: any) {
    const key = `${range.start}:${range.end}`;
    const evaluationList = this.expressionEvaluations.get(key) ?? [];
    evaluationList.push(output);
    this.expressionEvaluations.set(key, evaluationList);
  }

  private formatError(msg: string, range?: Range, cause?: any): ReadError {
    return ReadError.fromProps(
      msg,
      {
        originalStartIndex: range?.start,
        originalEndIndex: range?.end,
        sourcePath: this.sourcePath
      },
      { cause: cause }
    );
  }

  private reportError(msg: string, range?: Range, cause?: any): void {
    ErrorCollection.add(this.formatError(msg, range, cause));
  }

  /**
   * Template related functions only usable in standalone poml files.
   * It's not available for POML expressed with JSX or Python SDK.
   */

  private handleForLoop(
    element: XMLElement,
    context: { [key: string]: any }
  ): { [key: string]: any }[] {
    const forLoop = element.attributes.find(attr => attr.key?.toLowerCase() === 'for');
    if (!forLoop) {
      // No for loop found.
      return [];
    }
    const forLoopValue = forLoop.value;
    if (!forLoopValue) {
      this.reportError('for attribute value is expected.', this.xmlElementRange(element));
      return [];
    }
    const [itemName, listName] = forLoopValue.match(/(.+)\s+in\s+(.+)/)?.slice(1) || [null, null];
    if (!itemName || !listName) {
      this.reportError(
        'item in list syntax is expected in for attribute.',
        this.xmlAttributeValueRange(forLoop)
      );
      return [];
    }

    const list = this.evaluateExpression(listName, context, this.xmlAttributeValueRange(forLoop));
    if (!Array.isArray(list)) {
      this.reportError('List is expected in for attribute.', this.xmlAttributeValueRange(forLoop));
      return [];
    }
    return list.map((item: any, index: number) => {
      const loop = {
        index: index,
        length: list.length,
        first: index === 0,
        last: index === list.length - 1
      };
      return { loop: loop, [itemName]: item };
    });
  }

  private handleIfCondition = (element: XMLElement, context: { [key: string]: any }): boolean => {
    const ifCondition = element.attributes.find(attr => attr.key?.toLowerCase() === 'if');
    if (!ifCondition) {
      // No if condition found.
      return true;
    }
    const ifConditionValue = ifCondition.value;
    if (!ifConditionValue) {
      this.reportError('if attribute value is expected.', this.xmlAttributeValueRange(ifCondition));
      return false;
    }
    const condition = this.evaluateExpression(
      ifConditionValue,
      context,
      this.xmlAttributeValueRange(ifCondition),
      true
    );
    if (condition) {
      return true;
    } else {
      return false;
    }
  };

  private handleLet = (element: XMLElement, context: { [key: string]: any }): boolean => {
    if (element.name?.toLowerCase() !== 'let') {
      return false;
    }
    const source = xmlAttribute(element, 'src')?.value;
    const type = xmlAttribute(element, 'type')?.value;
    const name = xmlAttribute(element, 'name')?.value;
    const value = xmlAttribute(element, 'value')?.value;

    // Case 1: <let name="var1" src="/path/to/file" />, case insensitive
    // or <let src="/path/to/file" />, case insensitive
    if (source) {
      let content: any;
      try {
        content = readSource(
          source,
          this.sourcePath ? path.dirname(this.sourcePath) : undefined,
          type as AnyValue | undefined
        );
      } catch (e) {
        this.reportError(
          e !== undefined && (e as Error).message
            ? (e as Error).message
            : `Error reading source: ${source}`,
          this.xmlAttributeValueRange(xmlAttribute(element, 'src')!),
          e
        );
        return true;
      }
      if (!name) {
        if (content && typeof content === 'object') {
          Object.assign(context, content);
        } else {
          this.reportError(
            'name attribute is expected when the source is not an object.',
            this.xmlElementRange(element)
          );
        }
      } else {
        context[name] = content;
      }
      return true;
    }

    // Case 2: <let name="var1" value="{{ expression }}" />, case insensitive
    if (value) {
      if (!name) {
        this.reportError(
          'name attribute is expected when <let> contains two attributes.',
          this.xmlElementRange(element)
        );
        return true;
      }
      const evaluated = this.evaluateExpression(
        value,
        context,
        this.xmlAttributeValueRange(xmlAttribute(element, 'value')!),
        true
      );
      context[name] = evaluated;
      return true;
    }

    // Case 3: <let>{ JSON }</let>
    // or <let name="var1" type="number">{ JSON }</let>
    if (element.textContents.length > 0) {
      const text = xmlElementText(element);
      let content: any;
      try {
        content = parseText(text, type as AnyValue | undefined);
      } catch (e) {
        this.reportError(
          e !== undefined && (e as Error).message
            ? (e as Error).message
            : `Error parsing text as type ${type}: ${text}`,
          this.xmlElementRange(element),
          e
        );
        return true;
      }
      if (!name) {
        if (content && typeof content === 'object') {
          Object.assign(context, content);
        } else {
          this.reportError(
            'name attribute is expected when the source is not an object.',
            this.xmlElementRange(element)
          );
        }
      } else {
        context[name] = content;
      }

      return true;
    }

    this.reportError('Invalid <let> element.', this.xmlElementRange(element));
    return true;
  };

  private handleAttribute = (
    attribute: XMLAttribute,
    context: { [key: string]: any }
  ): [string, any] | undefined => {
    if (!attribute.key || !attribute.value) {
      return;
    }
    if (attribute.key.toLowerCase() === 'for' || attribute.key.toLowerCase() === 'if') {
      return;
    }
    const key = hyphenToCamelCase(attribute.key);
    const value = this.handleText(attribute.value, context, this.xmlAttributeValueRange(attribute));
    if (value.length === 1) {
      return [key, value[0]];
    } else {
      return [key, value];
    }
  };

  private handleInclude = (
    element: XMLElement,
    context: { [key: string]: any }
  ): React.ReactElement | undefined => {
    if (element.name?.toLowerCase() !== 'include') {
      return undefined;
    }

    const src = xmlAttribute(element, 'src');
    if (!src || !src.value) {
      this.reportError('src attribute is expected.', this.xmlElementRange(element));
      return <></>;
    }

    const source = src.value;

    let text: string;
    try {
      text = readSource(
        source,
        this.sourcePath ? path.dirname(this.sourcePath) : undefined,
        'string'
      );
    } catch (e) {
      this.reportError(
        e !== undefined && (e as Error).message
          ? (e as Error).message
          : `Error reading source: ${source}`,
        this.xmlAttributeValueRange(src),
        e
      );
      return <></>;
    }

    const includePath =
      this.sourcePath && !path.isAbsolute(source)
        ? path.join(path.dirname(this.sourcePath), source)
        : source;

    const included = new PomlFile(text, this.config, includePath);
    const root = included.xmlRootElement();
    if (!root) {
      return <></>;
    }

    let contents: (XMLElement | XMLTextContent)[] = [];
    if (root.name?.toLowerCase() === 'poml') {
      contents = xmlElementContents(root);
    } else {
      contents = [root];
    }
    const resultNodes: any[] = [];

    contents.forEach((el, idx) => {
      if (el.type === 'XMLTextContent') {
        resultNodes.push(
          ...included
            .handleText(el.text ?? '', context, included.xmlElementRange(el))
            .map(v =>
              typeof v === 'object' && v !== null && !React.isValidElement(v)
                ? JSON.stringify(v)
                : v
            )
        );
      } else if (el.type === 'XMLElement') {
        const child = included.parseXmlElement(el as XMLElement, context, {});
        resultNodes.push(
          React.isValidElement(child) ? React.cloneElement(child, { key: `child-${idx}` }) : child
        );
      }
    });

    if (resultNodes.length === 1) {
      return <>{resultNodes[0]}</>;
    }
    return <>{resultNodes}</>;
  };

  private handleSchema = (element: XMLElement, context?: { [key: string]: any }): Schema | undefined => {
    let lang: 'json' | 'expr' | undefined = xmlAttribute(element, 'lang')?.value as any;
    const text = xmlElementText(element).trim();
    
    // Get the range for the text content (if available)
    const textRange = element.textContents.length > 0 
      ? this.xmlElementRange(element.textContents[0])
      : this.xmlElementRange(element);
    
    // Auto-detect language if not specified
    if (!lang) {
      if (text.startsWith('{')) {
        lang = 'json';
      } else {
        lang = 'expr';
      }
    } else if (lang !== 'json' && lang !== 'expr') {
      this.reportError(
        `Invalid lang attribute: ${lang}. Expected "json" or "expr"`,
        this.xmlAttributeValueRange(xmlAttribute(element, 'lang')!)
      );
      return undefined;
    }
    
    try {
      if (lang === 'json') {
        // Process template expressions in JSON text
        const processedText = this.handleText(text, context || {}, textRange);
        // handleText returns an array, join if all strings
        const jsonText = processedText.length === 1 && typeof processedText[0] === 'string'
          ? processedText[0]
          : processedText.map(p => typeof p === 'string' ? p : JSON.stringify(p)).join('');
        const jsonSchema = JSON.parse(jsonText);
        return Schema.fromOpenAPI(jsonSchema);
      } else if (lang === 'expr') {
        // Evaluate expression directly with z in context
        const contextWithZ = { z, ...context };
        const result = this.evaluateExpression(text, contextWithZ, textRange);
        
        // If evaluation failed, result will be empty string
        if (!result) {
          return undefined;
        }
        
        // Determine if result is a Zod schema or JSON schema
        if (result && typeof result === 'object' && result._def) {
          // It's a Zod schema
          return Schema.fromZod(result);
        } else {
          // Treat as JSON schema
          return Schema.fromOpenAPI(result);
        }
      }
    } catch (e) {
      this.reportError(
        e instanceof Error ? e.message : 'Error parsing schema',
        this.xmlElementRange(element),
        e
      );
    }
    return undefined;
  }

  private handleMeta = (element: XMLElement, context?: { [key: string]: any }): boolean => {
    if (element.name?.toLowerCase() !== 'meta') {
      return false;
    }
    const metaType = xmlAttribute(element, 'type')?.value;
    if (metaType === 'responseSchema') {
      if (this.responseSchema) {
        this.reportError(
          'Multiple responseSchema meta elements found. Only one is allowed.',
          this.xmlElementRange(element)
        );
        return true;
      }
      const schema = this.handleSchema(element, context);
      if (schema) {
        this.responseSchema = schema;
      }
      return true;
    }

    if (metaType === 'tool') {
      const name = xmlAttribute(element, 'name')?.value;
      if (!name) {
        this.reportError(
          'name attribute is required for tool meta type',
          this.xmlElementRange(element)
        );
        return true;
      }
      const description = xmlAttribute(element, 'description')?.value;
      const inputSchema = this.handleSchema(element, context);
      if (inputSchema) {
        if (!this.toolsSchema) {
          this.toolsSchema = new ToolsSchema();
        }
        try {
          this.toolsSchema.addTool(name, description || undefined, inputSchema);
        } catch (e) {
          this.reportError(
            e instanceof Error ? e.message : 'Error adding tool to tools schema',
            this.xmlElementRange(element),
            e
          );
        }
      }
      return true;
    }

    if (metaType === 'runtime') {
      // Extra runtime parameters sending to LLM.
      const runtimeParams: any = {};
      for (const attribute of element.attributes) {
        if (attribute.key && attribute.value && attribute.key?.toLowerCase() !== 'type') {
          runtimeParams[attribute.key] = attribute.value;
        }
      }
      this.runtimeParameters = runtimeParams;
      return true;
    }

    const minVersion = xmlAttribute(element, 'minVersion')?.value;
    if (minVersion && compareVersions(POML_VERSION, minVersion) < 0) {
      this.reportError(
        `POML version ${minVersion} or higher is required`,
        this.xmlAttributeValueRange(xmlAttribute(element, 'minVersion')!)
      );
    }
    const maxVersion = xmlAttribute(element, 'maxVersion')?.value;
    if (maxVersion && compareVersions(POML_VERSION, maxVersion) > 0) {
      this.reportError(
        `POML version ${maxVersion} or lower is required`,
        this.xmlAttributeValueRange(xmlAttribute(element, 'maxVersion')!)
      );
    }

    const comps = xmlAttribute(element, 'components')?.value;
    if (comps) {
      comps.split(/[,\s]+/).forEach(token => {
        token = token.trim();
        if (!token) {
          return;
        }
        const op = token[0];
        const name = token.slice(1).toLowerCase().trim();
        if (!name) {
          return;
        }
        if (op === '+') {
          this.disabledComponents.delete(name);
        } else if (op === '-') {
          this.disabledComponents.add(name);
        } else {
          this.reportError(
            `Invalid component operation: ${op}. Use + to enable or - to disable.`,
            this.xmlAttributeValueRange(xmlAttribute(element, 'components')!)
          );
        }
      });
    }
    return true;
  };

  private unescapeText = (text: string): string => {
    return text
      .replace(/#lt;/g, '<')
      .replace(/#gt;/g, '>')
      .replace(/#amp;/g, '&')
      .replace(/#quot;/g, '"')
      .replace(/#apos;/g, "'")
      .replace(/#hash;/g, '#')
      .replace(/#lbrace;/g, '{')
      .replace(/#rbrace;/g, '}');
  };

  private handleText = (text: string, context: { [key: string]: any }, position?: Range): any[] => {
    let curlyMatch;
    let replacedPrefixLength: number = 0;
    let results: any[] = [];
    const regex = /{{\s*(.+?)\s*}}(?!})/gm;

    while ((curlyMatch = regex.exec(text))) {
      const curlyExpression = curlyMatch[1];
      const value = this.evaluateExpression(
        curlyExpression,
        context,
        position
          ? {
            start: position.start + curlyMatch.index,
            end: position.start + curlyMatch.index + curlyMatch[0].length - 1
          }
          : undefined
      );
      if (this.config.trim && curlyMatch[0] === text.trim()) {
        return [value];
      }

      if (curlyMatch.index > replacedPrefixLength) {
        results.push(this.unescapeText(text.slice(replacedPrefixLength, curlyMatch.index)));
      }
      results.push(value);
      replacedPrefixLength = curlyMatch.index + curlyMatch[0].length;
    }

    if (text.length > replacedPrefixLength) {
      results.push(this.unescapeText(text.slice(replacedPrefixLength)));
    }

    if (results.length > 0 && results.every(r => typeof r === 'string' || typeof r === 'number')) {
      return [results.map(r => r.toString()).join('')];
    }

    return results;
  };

  private evaluateExpression(
    expression: string,
    context: { [key: string]: any },
    range?: Range,
    stripCurlyBrackets: boolean = false
  ) {
    try {
      if (stripCurlyBrackets) {
        const curlyMatch = expression.match(/^\s*{{\s*(.+?)\s*}}\s*$/m);
        if (curlyMatch) {
          expression = curlyMatch[1];
        }
      }
      const result = evalWithVariables(expression, context || {});
      if (range) {
        this.recordEvaluation(range, result);
      }
      return result;
    } catch (e) {
      const errMessage = e !== undefined && (e as Error).message
        ? (e as Error).message
        : `Error evaluating expression: ${expression}`;
      if (range) {
        this.recordEvaluation(range, errMessage);
      }
      this.reportError(errMessage, range, e);
      return '';
    }
  }

  /**
   * Parse the XML element and return the corresponding React element.
   *
   * @param element The element to be converted.
   * @param globalContext The context can be carried over when the function returns.
   * @param localContext The context that is only available in the current element and its children.
   */
  private parseXmlElement(
    element: XMLElement,
    globalContext: { [key: string]: any },
    localContext: { [key: string]: any }
  ): React.ReactElement {
    // Let. Always set the global.
    if (this.handleLet(element, globalContext)) {
      return <></>;
    }

    const tagName = element.name;
    if (!tagName) {
      // Probably already had an invalid syntax error.
      return <></>;
    }
    const isMeta = tagName.toLowerCase() === 'meta';
    const isInclude = tagName.toLowerCase() === 'include';

    // Common logic for handling for-loops
    const forLoops = this.handleForLoop(element, globalContext);
    const forLoopedContext = forLoops.length > 0 ? forLoops : [{}];
    const resultElements: React.ReactElement[] = [];

    for (let i = 0; i < forLoopedContext.length; i++) {
      const currentLocal = { ...localContext, ...forLoopedContext[i] };
      const context = { ...globalContext, ...currentLocal };

      // Common logic for handling if-conditions
      if (!this.handleIfCondition(element, context)) {
        continue;
      }
      // Common logic for handling meta elements
      if (isMeta && this.handleMeta(element, context)) {
        // If it's a meta element, we don't render anything.
        continue;
      }

      let elementToAdd: React.ReactElement | null = null;

      if (isInclude) {
        // Logic for <include> tags
        const included = this.handleInclude(element, context);
        if (included) {
          // Add a key if we are in a loop with multiple items
          if (forLoopedContext.length > 1) {
            elementToAdd = <React.Fragment key={`include-${i}`}>{included}</React.Fragment>;
          } else {
            elementToAdd = included;
          }
        }
      } else {
        // Logic for all other components
        const component = findComponentByAlias(tagName, this.disabledComponents);
        if (typeof component === 'string') {
          // Add a read error
          this.reportError(component, this.xmlOpenNameRange(element));
          // Return empty fragment to prevent rendering this element
          // You might want to 'continue' the loop as well.
          return <></>;
        }

        const attrib: any = element.attributes.reduce(
          (acc, attribute) => {
            const [key, value] = this.handleAttribute(attribute, context) || [null, null];
            if (key && value !== null) {
              acc[key] = value;
            }
            return acc;
          },
          {} as { [key: string]: any }
        );

        // Retain the position of current element for future diagnostics
        const range = this.xmlElementRange(element);
        attrib.originalStartIndex = range.start;
        attrib.originalEndIndex = range.end;

        // Add key attribute for react
        if (!attrib.key && forLoopedContext.length > 1) {
          attrib.key = `key-${i}`;
        }

        const contents = xmlElementContents(element).filter(el => {
          // Filter out stylesheet and context element in the root poml element
          if (
            tagName === 'poml' &&
            el.type === 'XMLElement' &&
            ['context', 'stylesheet'].includes((el as XMLElement).name?.toLowerCase() ?? '')
          ) {
            return false;
          } else {
            return true;
          }
        });

        const avoidObject = (el: any) => {
          if (typeof el === 'object' && el !== null && !React.isValidElement(el)) {
            return JSON.stringify(el);
          }
          return el;
        };

        const processedContents = contents.reduce((acc, el, i) => {
          if (el.type === 'XMLTextContent') {
            // const isFirst = i === 0,
            //   isLast = i === contents.length - 1;
            // const text = this.config.trim ? trimText(el.text || '', isFirst, isLast) : el.text || '';
            acc.push(
              ...this.handleText(
                el.text ?? '',
                { ...globalContext, ...currentLocal },
                this.xmlElementRange(el)
              ).map(avoidObject)
            );
          } else if (el.type === 'XMLElement') {
            acc.push(this.parseXmlElement(el, globalContext, currentLocal));
          }
          return acc;
        }, [] as any[]);

        elementToAdd = React.createElement(
          component.render.bind(component),
          attrib,
          ...processedContents
        );
      }
      if (elementToAdd) {
        // If we have an element to add, push it to the result elements.
        resultElements.push(elementToAdd);
      }
    }

    // Common logic for returning the final result
    if (resultElements.length === 1) {
      return resultElements[0];
    } else {
      // Cases where there are multiple elements or zero elements.
      return <>{resultElements}</>;
    }
  }

  private recoverPosition(position: number): number {
    return position + this.documentRange.start;
  }

  private ensureRange(position: number): number {
    return Math.max(Math.min(position, this.documentRange.end) - this.documentRange.start, 0);
  }

  private xmlElementRange(element: XMLElement | XMLTextContent | XMLAttribute): Range {
    return {
      start: this.ensureRange(element.position.startOffset),
      end: this.ensureRange(element.position.endOffset)
    };
  }

  private xmlOpenNameRange(element: XMLElement): Range {
    if (element.syntax.openName) {
      return {
        start: this.ensureRange(element.syntax.openName.startOffset),
        end: this.ensureRange(element.syntax.openName.endOffset)
      };
    } else {
      return this.xmlElementRange(element);
    }
  }

  private xmlCloseNameRange(element: XMLElement): Range {
    if (element.syntax.closeName) {
      return {
        start: this.ensureRange(element.syntax.closeName.startOffset),
        end: this.ensureRange(element.syntax.closeName.endOffset)
      };
    } else {
      return this.xmlElementRange(element);
    }
  }

  private xmlAttributeKeyRange(element: XMLAttribute): Range {
    if (element.syntax.key) {
      return {
        start: this.ensureRange(element.syntax.key.startOffset),
        end: this.ensureRange(element.syntax.key.endOffset)
      };
    } else {
      return this.xmlElementRange(element);
    }
  }

  private xmlAttributeValueRange(element: XMLAttribute): Range {
    if (element.syntax.value) {
      return {
        start: this.ensureRange(element.syntax.value.startOffset),
        end: this.ensureRange(element.syntax.value.endOffset)
      };
    } else {
      return this.xmlElementRange(element);
    }
  }

  private findTokenInElement(element: XMLElement, offset: number): PomlToken | undefined {
    if (element.name) {
      if (
        element.syntax.openName &&
        element.syntax.openName.startOffset <= offset &&
        offset <= element.syntax.openName.endOffset
      ) {
        return {
          type: 'element',
          range: this.xmlOpenNameRange(element),
          element: element.name
        };
      }
      if (
        element.syntax.closeName &&
        element.syntax.closeName.startOffset <= offset &&
        offset <= element.syntax.closeName.endOffset
      ) {
        return {
          type: 'element',
          range: this.xmlCloseNameRange(element),
          element: element.name
        };
      }
      for (const attrib of element.attributes) {
        if (
          attrib.key &&
          attrib.syntax.key &&
          attrib.syntax.key.startOffset <= offset &&
          offset <= attrib.syntax.key.endOffset
        ) {
          return {
            type: 'attribute',
            range: this.xmlAttributeKeyRange(attrib),
            element: element.name,
            attribute: attrib.key
          };
        }
      }
    }

    for (const child of element.subElements) {
      const result = this.findTokenInElement(child, offset);
      if (result) {
        return result;
      }
    }
  }

  private handleElementNameCompletion(offset: number) {
    return ({ element, prefix }: { element: XMLElement; prefix?: string }): PomlToken[] => {
      const candidates = this.findComponentWithPrefix(prefix, true);
      return candidates.map(candidate => {
        return {
          type: 'element',
          range: {
            start: this.ensureRange(offset - (prefix ? prefix.length : 0)),
            end: this.ensureRange(offset - 1)
          },
          element: candidate
        };
      });
    };
  }

  private handleElementNameCloseCompletion(offset: number) {
    return ({ element, prefix }: { element: XMLElement; prefix?: string }): PomlToken[] => {
      const candidates: string[] = [];
      const excludedComponents: string[] = [];
      if (element.name) {
        candidates.push(element.name);
        const component = findComponentByAliasOrUndefined(
          element.name,
          this.disabledComponents
        );
        if (component !== undefined) {
          excludedComponents.push(component.name);
        }
      }
      if (prefix) {
        candidates.push(...this.findComponentWithPrefix(prefix, true, excludedComponents));
      }
      return candidates.map(candidate => {
        return {
          type: 'element',
          range: {
            start: this.ensureRange(offset - (prefix ? prefix.length : 0)),
            end: this.ensureRange(offset - 1)
          },
          element: candidate
        };
      });
    };
  }

  private handleAttributeNameCompletion(offset: number) {
    return ({
      element,
      prefix
    }: {
      element: XMLElement;
      attribute?: XMLAttribute;
      prefix?: string;
    }): PomlToken[] => {
      if (!element.name) {
        return [];
      }
      const component = findComponentByAliasOrUndefined(
        element.name,
        this.disabledComponents
      );
      const parameters = component?.parameters();
      if (!component || !parameters) {
        return [];
      }
      const candidates: PomlToken[] = [];
      for (const parameter of parameters) {
        if (parameter.name.toLowerCase().startsWith(prefix?.toLowerCase() ?? '')) {
          candidates.push({
            type: 'attribute',
            range: {
              start: this.ensureRange(offset - (prefix ? prefix.length : 0)),
              end: this.ensureRange(offset - 1)
            },
            element: component.name,
            attribute: parameter.name
          });
        }
      }
      return candidates;
    };
  }

  private handleAttributeValueCompletion(offset: number) {
    return ({
      element,
      attribute,
      prefix
    }: {
      element: XMLElement;
      attribute: XMLAttribute;
      prefix?: string;
    }): PomlToken[] => {
      if (!element.name) {
        return [];
      }
      const component = findComponentByAliasOrUndefined(
        element.name,
        this.disabledComponents
      );
      const parameters = component?.parameters();
      if (!component || !parameters) {
        return [];
      }
      const candidates: PomlToken[] = [];
      for (const parameter of parameters) {
        if (parameter.name.toLowerCase() === attribute.key?.toLowerCase()) {
          for (const choice of parameter.choices) {
            if (choice.toLowerCase().startsWith(prefix?.toLowerCase() ?? '')) {
              candidates.push({
                type: 'attributeValue',
                range: {
                  start: this.ensureRange(offset - (prefix ? prefix.length : 0)),
                  end: this.ensureRange(offset - 1)
                },
                element: component.name,
                attribute: parameter.name,
                value: choice
              });
            }
          }
        }
      }
      return candidates;
    };
  }

  private findComponentWithPrefix(
    prefix: string | undefined,
    publicOnly: boolean,
    excludedComponents?: string[]
  ): string[] {
    const candidates: string[] = [];
    for (const component of listComponents()) {
      if (publicOnly && !component.isPublic()) {
        continue;
      }
      if (excludedComponents && excludedComponents.includes(component.name)) {
        continue;
      }
      let nameMatch: string | undefined = undefined;
      if (!prefix || component.name.toLowerCase().startsWith(prefix.toLowerCase())) {
        nameMatch = component.name;
      } else {
        const candidates: string[] = [];
        for (const alias of component.getAliases()) {
          if (alias.toLowerCase().startsWith(prefix.toLowerCase())) {
            candidates.push(alias);
            // One component can have at most one alias match.
            break;
          }
        }
        // Match hyphen case.
        for (const alias of component.getAliases(false)) {
          const aliasHyphen = camelToHyphenCase(alias);
          if (aliasHyphen.startsWith(prefix.toLowerCase())) {
            candidates.push(aliasHyphen);
            break;
          }
        }

        // Try to see if there is a match in the exact case.
        for (const candidate of candidates) {
          if (candidate.startsWith(prefix)) {
            nameMatch = candidate;
            break;
          }
        }
        if (!nameMatch && candidates) {
          nameMatch = candidates[0];
        }
      }
      if (nameMatch) {
        candidates.push(nameMatch);
      }
    }
    return candidates;
  }
}

/**
 * XML utility functions.
 */
const evalWithVariables = (text: string, context: { [key: string]: any }): any => {
  const variableNames = Object.keys(context);
  const variableValues = Object.values(context);
  const fn = new Function(...variableNames, `return ${text}`);
  return fn(...variableValues);
};

const hyphenToCamelCase = (text: string): string => {
  return text.replace(/-([a-z])/g, g => g[1].toUpperCase());
};

const camelToHyphenCase = (text: string): string => {
  return text.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
};

/**
 * Compares two version strings supporting semantic versioning with nightly/dev suffixes.
 * Supports formats: "x.y.z", "x.y.z-nightly.timestamp", "x.y.z.devtimestamp"
 * 
 * @param a - The first version string.
 * @param b - The second version string.
 * @returns -1 if `a` is less than `b`, 1 if `a` is greater than `b`, and 0 if they are equal.
 */
const compareVersions = (a: string, b: string): number => {
  const parseVersion = (version: string) => {
    // Handle nightly versions: "1.2.3-nightly.202508120345"
    const nightlyMatch = version.match(/^(\d+\.\d+\.\d+)-nightly\.(\d+)$/);
    if (nightlyMatch) {
      const [, baseVersion, timestamp] = nightlyMatch;
      const parts = baseVersion.split('.').map(n => parseInt(n, 10));
      return { parts, isPrerelease: true, timestamp: parseInt(timestamp, 10) };
    }

    // Handle regular semantic versions: "1.2.3"
    const parts = version.split('.').map(n => parseInt(n, 10));
    return { parts, isPrerelease: false, timestamp: 0 };
  };

  const versionA = parseVersion(a);
  const versionB = parseVersion(b);

  // Compare base version parts first
  for (let i = 0; i < Math.max(versionA.parts.length, versionB.parts.length); i++) {
    const na = versionA.parts[i] || 0;
    const nb = versionB.parts[i] || 0;
    if (na > nb) return 1;
    if (na < nb) return -1;
  }

  // If base versions are equal, handle prerelease comparison
  if (versionA.isPrerelease && !versionB.isPrerelease) {
    return -1; // Prerelease is less than release
  }
  if (!versionA.isPrerelease && versionB.isPrerelease) {
    return 1; // Release is greater than prerelease
  }
  if (versionA.isPrerelease && versionB.isPrerelease) {
    // Both are prereleases, compare timestamps
    if (versionA.timestamp > versionB.timestamp) return 1;
    if (versionA.timestamp < versionB.timestamp) return -1;
  }

  return 0;
};

const xmlAttribute = (element: XMLElement, key: string): XMLAttribute | undefined => {
  return element.attributes.find(attr => attr.key?.toLowerCase() === key.toLowerCase());
};

const xmlElementContents = (element: XMLElement): (XMLElement | XMLTextContent)[] => {
  return [...element.subElements, ...element.textContents].sort(
    (i, j) => i.position.startOffset - j.position.startOffset
  );
};

const xmlElementText = (element: XMLElement): string => {
  return element.textContents.map(content => content.text || '').join(' ');
};



================================================
FILE: packages/poml/index.ts
================================================
import * as React from 'react';
import { readFileSync, writeFileSync } from './util/fs';
import { renderToString } from "react-dom/server";
import path from 'path';
import { EnvironmentDispatcher } from "./writer";
import { ErrorCollection, Message, RichContent, StyleSheetProvider, SystemError, SourceMapRichContent, SourceMapMessage, richContentFromSourceMap } from './base';
import { PomlFile, PomlReaderOptions } from './file';
import './presentation';
import './essentials';
import "./components";
import { reactRender } from './util/reactRender';
import { dumpTrace, setTrace, clearTrace, isTracing, parseJsonWithBuffers } from './util/trace';

export type { RichContent, Message, SourceMapRichContent, SourceMapMessage };
export { richContentFromSourceMap };

export const read = async (
  element: React.ReactElement | string,
  options?: PomlReaderOptions,
  context?: { [key: string]: any },
  stylesheet?: { [key: string]: any },
  sourcePath?: string,
): Promise<string> => {
  let readElement: React.ReactElement;
  if (typeof element === 'string') {
    readElement = new PomlFile(element, options, sourcePath).react(context);
  } else {
    if (options || context) {
      console.warn('Options and context are ignored when element is React.ReactElement');
    }
    readElement = element;
  }
  if (stylesheet) {
    readElement = React.createElement(StyleSheetProvider, { stylesheet }, readElement);
  }
  return await reactRender(readElement);
};

// Read and also returning the POML file
// A hacky way to get the POML file from the React element
// Do not use it in production code
export const _readWithFile = async (
  element: React.ReactElement | string,
  options?: PomlReaderOptions,
  context?: { [key: string]: any },
  stylesheet?: { [key: string]: any },
  sourcePath?: string,
): Promise<[string, PomlFile | undefined]> => {
  let readElement: React.ReactElement;
  let pomlFile: PomlFile | undefined;
  if (typeof element === 'string') {
    pomlFile = new PomlFile(element, options, sourcePath);
    readElement = pomlFile.react(context);
  } else {
    if (options || context) {
      console.warn('Options and context are ignored when element is React.ReactElement');
    }
    readElement = element;
  }
  if (stylesheet) {
    readElement = React.createElement(StyleSheetProvider, { stylesheet }, readElement);
  }
  return [
    await reactRender(readElement),
    pomlFile
  ];
};

interface WriteOptions {
  speaker?: boolean;
}

interface WriteOptionsNoSpeakerMode extends WriteOptions {
  speaker?: false;
}

interface WriteOptionsSpeakerMode extends WriteOptions {
  speaker: true;
}


export function write(ir: string, options?: WriteOptionsNoSpeakerMode): RichContent;
export function write(ir: string, options: WriteOptionsSpeakerMode): Message[];
export function write(ir: string, options?: WriteOptions): RichContent | Message[];
/**
 * Entry point for turning a parsed IR string into rich content or a list of
 * speaker messages. The heavy lifting is done by `EnvironmentDispatcher`.
 */
export function write(ir: string, options?: WriteOptions): RichContent | Message[] {
  const writer = new EnvironmentDispatcher();
  if (options?.speaker) {
    return writer.writeMessages(ir);
  } else {
    return writer.write(ir);
  }
};

export function writeWithSourceMap(ir: string, options?: WriteOptionsNoSpeakerMode): SourceMapRichContent[];
export function writeWithSourceMap(ir: string, options: WriteOptionsSpeakerMode): SourceMapMessage[];
export function writeWithSourceMap(ir: string, options?: WriteOptions): SourceMapRichContent[] | SourceMapMessage[];
/**
 * Variant of {@link write} that also exposes a source map describing the
 * mapping between input indices and output content.
 */
export function writeWithSourceMap(ir: string, options?: WriteOptions): SourceMapRichContent[] | SourceMapMessage[] {
  const writer = new EnvironmentDispatcher();
  if (options?.speaker) {
    return writer.writeMessagesWithSourceMap(ir);
  } else {
    return writer.writeWithSourceMap(ir);
  }
};

export const poml = async (element: React.ReactElement | string): Promise<RichContent> => {
  ErrorCollection.clear();
  const readResult = await read(element);
  const result = write(readResult);
  if (!ErrorCollection.empty()) {
    throw ErrorCollection.first();
  }
  return result;
}

interface CliArgs {
  input?: string;
  file?: string;
  output?: string;
  context?: string[];
  contextFile?: string;
  stylesheet?: string;
  stylesheetFile?: string;
  trim?: boolean;
  speakerMode?: boolean;
  prettyPrint?: boolean;
  strict?: boolean;
  cwd?: string;
  traceDir?: string;
}

interface CliResult {
  messages: Message[] | RichContent;
  responseSchema?: { [key: string]: any };
  tools?: { [key: string]: any }[];
  runtime?: { [key: string]: any };
}

export async function commandLine(args: CliArgs) {
  const readOptions = {
    trim: args.trim,
  };

  if (args.traceDir) {
    setTrace(true, args.traceDir);
  }

  // Determine the working directory
  let workingDirectory: string;
  if (args.cwd) {
    workingDirectory = path.resolve(args.cwd);
  } else {
    workingDirectory = process.cwd();
  }

  let input: string;
  let sourcePath: string | undefined;
  if (args.input && args.file) {
    throw new Error('Cannot specify both input and file');
  } else if (args.input) {
    input = args.input;
  } else if (args.file) {
    const filePath = path.resolve(workingDirectory, args.file);
    input = readFileSync(filePath, { encoding: 'utf8' });
    sourcePath = filePath;
  } else {
    throw new Error('Must specify either input or file');
  }

  let context: { [key: string]: any } = {};
  if (args.context) {
    for (const pair of args.context) {
      if (!pair.includes('=')) {
        throw new Error(`Invalid context variable, must include one '=': ${pair}`);
      }
      const [key, value] = pair.split('=', 2);
      context[key] = value;
    }
  } else if (args.contextFile) {
    const contextFilePath = path.resolve(workingDirectory, args.contextFile);
    const contextFromFile = parseJsonWithBuffers(readFileSync(contextFilePath, { encoding: 'utf8' }));
    context = { ...context, ...contextFromFile };
  }

  let stylesheet: { [key: string]: any } = {};
  if (args.stylesheetFile) {
    const stylesheetFilePath = path.resolve(workingDirectory, args.stylesheetFile);
    stylesheet = { ...stylesheet, ...parseJsonWithBuffers(readFileSync(stylesheetFilePath, { encoding: 'utf8' })) };
  }
  if (args.stylesheet) {
    stylesheet = { ...stylesheet, ...JSON.parse(args.stylesheet) };
  }

  ErrorCollection.clear();

  const pomlFile = new PomlFile(input, readOptions, sourcePath);
  let reactElement = pomlFile.react(context);
  reactElement = React.createElement(StyleSheetProvider, { stylesheet }, reactElement);

  const ir = await read(input, readOptions, context, stylesheet, sourcePath);

  const speakerMode = args.speakerMode === true || args.speakerMode === undefined;
  const prettyPrint = args.prettyPrint === true;
  let resultMessages = write(ir, { speaker: speakerMode });
  const prettyOutput = speakerMode
    ? (resultMessages as Message[]).map((message) => `===== ${message.speaker} =====\n\n${renderContent(message.content)}`).join('\n\n')
    : renderContent(resultMessages as RichContent);
  const result: CliResult = {
    messages: resultMessages,
    responseSchema: pomlFile.getResponseSchema()?.toOpenAPI(),
    tools: pomlFile.getToolsSchema()?.toOpenAI(),
    runtime: pomlFile.getRuntimeParameters(),
  }
  const output = prettyPrint ? prettyOutput : JSON.stringify(result);

  if (isTracing()) {
    try {
      dumpTrace(input, context, stylesheet, result, sourcePath, prettyOutput);
    } catch (err: any) {
      ErrorCollection.add(new SystemError('Failed to dump trace', { cause: err }));
    }
  }

  if (args.strict === true || args.strict === undefined) {
    if (!ErrorCollection.empty()) {
      throw ErrorCollection.first();
    }
  }

  if (args.output) {
    const outputPath = path.resolve(workingDirectory, args.output);
    writeFileSync(outputPath, output);
  } else {
    process.stdout.write(output);
  }
}

const renderContent = (content: RichContent) => {
  if (typeof content === 'string') {
    return content;
  }
  const outputs: string[] = content.map((part) => {
    if (typeof part === 'string') {
      return part;
    } else {
      const media = JSON.stringify(part);
      if (media.length > 100) {
        return media.slice(0, 100) + '...';
      } else {
        return media;
      }
    }
  });
  return outputs.join('\n\n');
}

export { setTrace, clearTrace, parseJsonWithBuffers, dumpTrace };



================================================
FILE: packages/poml/presentation.tsx
================================================
/**
 * NOTE: The components in this file are the lowest-level APIs and for internal use only.
 *
 * There are two main ways to present data: as markup or as serialized data.
 * 1. Markup is to be rendered as markup languages like Markdown, Wikitext, etc.
 * 2. Serialized data is to be rendered as JSON, XML, etc.
 *
 * When rendered as serialized data, the framework will output key-value pairs,
 * objects, arrays, etc. instead of bolds, italics, headers that are considered
 * helpful for human readers in markup texts.
 *
 * HTML is a special case. It can be considered as a markup language because it
 * has the tags that are used to format the text. However, it can also be considered
 * as serialized data when using its tags to represent key-value pairs.
 *
 * Presentation can be configured in stylesheet, but it's a special style that can
 * be propagated down to the children components. All other styles are only set for
 * current active component, including the serializer language, which only affects
 * the enclosing environment of the markup/serialized.
 */

import * as React from 'react';

import { component, PropsBase, irElement, ReadError, trimChildrenWhiteSpace } from './base';
import { AnyValue } from './util';

export type Presentation = 'markup' | 'serialize' | 'free' | 'multimedia';
export const DefaultMarkupLang = 'markdown';
export const DefaultSerializer = 'json';
export type Position = 'top' | 'bottom' | 'here';

export interface PropsPresentationBase extends PropsBase {
  presentation?: Presentation;
}

export interface PropsMarkupBase extends PropsPresentationBase {
  presentation?: 'markup';
  markupLang?: string;
}

export interface PropsSerializeBase extends PropsPresentationBase {
  presentation?: 'serialize';
  serializer?: string;
}

export interface PropsFreeBase extends PropsPresentationBase {
  presentation?: 'free';
}

export interface PropsMultiMediaBase extends PropsPresentationBase {
  presentation?: 'multimedia';
}

export interface InlineProps {
  inline?: boolean;
}

// The context that stores the current presentation appraoch.
// The language is preserved in the context,
// because we need to know whether to create a environment with a different lang.
const PresentationApproach = React.createContext<
  PropsMarkupBase | PropsSerializeBase | PropsFreeBase | PropsMultiMediaBase | undefined
>(undefined);

/**
 * Get the current presentation approach.
 * Used by components to determine how to render themselves.
 */
export const computePresentation = (
  props:
    | PropsMarkupBase
    | PropsSerializeBase
    | PropsFreeBase
    | PropsMultiMediaBase
    | PropsPresentationBase
): Presentation => {
  const result = computePresentationOrUndefined(props);
  if (!result) {
    throw ReadError.fromProps(
      `No presentation approach found in context or currently: ${props}`,
      props
    );
  }
  return result;
};

export const computePresentationOrUndefined = (
  props:
    | PropsMarkupBase
    | PropsSerializeBase
    | PropsFreeBase
    | PropsMultiMediaBase
    | PropsPresentationBase
): Presentation | undefined => {
  if (
    props.presentation === 'markup' ||
    props.presentation === 'serialize' ||
    props.presentation === 'free' ||
    props.presentation === 'multimedia'
  ) {
    return props.presentation;
  } else if ((props as any).presentation) {
    throw ReadError.fromProps(`Invalid presentation: ${(props as any).presentation}`, props);
  }
  const presentation = React.useContext(PresentationApproach);
  return presentation?.presentation;
};

export namespace Markup {
  /**
   * Encloses a markup component.
   * It could produce nothing if it's not necessary to wrap the component.
   */
  export const Environment = component('Markup.Environment')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const parentPresentation = React.useContext(PresentationApproach);

    // presentation is extracted but not used here. We are already in markup mode.
    let {
      presentation,
      markupLang,
      children,
      originalStartIndex,
      originalEndIndex,
      writerOptions,
      sourcePath
    } = props;

    if (!markupLang) {
      if (parentPresentation?.presentation === 'markup') {
        markupLang = (parentPresentation as PropsMarkupBase).markupLang;
      } else {
        markupLang = DefaultMarkupLang;
      }
    }

    return parentPresentation?.presentation === 'markup' &&
      (parentPresentation as PropsMarkupBase).markupLang === markupLang &&
      (!writerOptions ||
        (parentPresentation as PropsMarkupBase).writerOptions === writerOptions) ? (
      <>{children}</>
    ) : (
      irElement(
        'env',
        { presentation: 'markup', markupLang, writerOptions, originalStartIndex, originalEndIndex, sourcePath },
        <PresentationApproach.Provider
          value={{
            presentation: 'markup',
            markupLang: markupLang,
            writerOptions: writerOptions
          }}
        >
          {trimChildrenWhiteSpace(children, props)}
        </PresentationApproach.Provider>
      )
    );
  });

  export const EncloseSerialize = component('Markup.EncloseSerialize')((
    props: React.PropsWithChildren<InlineProps & CodeProps>
  ) => {
    const { children, inline = false, ...others } = props;
    return (
      <Markup.Code inline={inline} {...others}>
        {children}
      </Markup.Code>
    );
  });

  const SimpleMarkupComponent = (
    props: React.PropsWithChildren<PropsMarkupBase & { tagName: string }>
  ) => {
    // Sometimes it helps to extract attributes like markupLang to avoid too many props sent to IR.
    // But this is not necessary.
    const { children, tagName, markupLang, presentation, ...others } = props;
    return (
      <Markup.Environment markupLang={markupLang} presentation={presentation} {...others}>
        {irElement(tagName, others, children)}
      </Markup.Environment>
    );
  };

  const HeaderLevel = React.createContext(1);

  export interface ParagraphProps {
    blankLine?: boolean; // whether to add 1 more blank line before and after paragraph.
  }

  // Paragraph is a block preceded by a newline and followed by a newline.
  // The paragraph in our context is the most common block element.
  // It can be nested, and represent complex sections and rich texts.
  export const Paragraph = component('Markup.Paragraph')((
    props: React.PropsWithChildren<PropsMarkupBase & ParagraphProps>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="p">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // Inline is a light-weight element that is wrapped by two spaces.
  export const Inline = component('Markup.Inline')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="span">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // NewLine explicitly adds newlines (vertical spaces).
  export interface NewlineProps {
    newlineCount?: number;
  }

  export const Newline = component('Markup.Newline')((props: PropsMarkupBase & NewlineProps) => {
    const { newlineCount, ...others } = props;
    return (
      <Markup.Environment {...others}>
        {irElement('nl', { count: newlineCount, ...others })}
      </Markup.Environment>
    );
  });

  // Header is a block that is usually used to emphasize the title of a section.
  export const Header = component('Markup.Header')((
    props: React.PropsWithChildren<PropsMarkupBase & ParagraphProps>
  ) => {
    const ctxLevel = React.useContext(HeaderLevel);
    const { children, ...others } = props;
    return (
      <Markup.Environment {...others}>
        {irElement(
          'h',
          {
            level: ctxLevel,
            ...others
          },
          children
        )}
      </Markup.Environment>
    );
  });

  // SubContent usually follows a header and states that the headers inside it are sub-headers.
  // It's same as a paragraph in all other aspects.
  export const SubContent = component('Markup.SubContent')((
    props: React.PropsWithChildren<PropsMarkupBase & Markup.ParagraphProps>
  ) => {
    const { children, ...others } = props;
    const ctxLevel = React.useContext(HeaderLevel);
    // needn't trim here.
    return (
      <HeaderLevel.Provider value={ctxLevel + 1}>
        <Markup.Paragraph {...others}>{children}</Markup.Paragraph>
      </HeaderLevel.Provider>
    );
  });

  // Bold is a Inline element that is used to emphasize the text.
  export const Bold = component('Markup.Bold')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="b">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // Italic is a Inline element that is used to emphasize the text.
  export const Italic = component('Markup.Italic')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="i">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // Strikethrough is a Inline element that is used to represent deleted text.
  export const Strikethrough = component('Markup.Strikethrough')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="s">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // Underline is a Inline element that is used to represent underlined text.
  export const Underline = component('Markup.Underline')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="u">
        {children}
      </SimpleMarkupComponent>
    );
  });

  // Code is a Inline element that is used to represent code snippets.
  export interface CodeProps {
    lang?: string;
  }

  export const Code = component('Markup.Code')((
    props: React.PropsWithChildren<PropsMarkupBase & InlineProps & CodeProps>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="code">
        {children}
      </SimpleMarkupComponent>
    );
  });

  export interface ListProps {
    listStyle?: 'star' | 'dash' | 'plus' | 'decimal' | 'latin';
  }

  export const ListContext = React.createContext<ListProps | undefined>(undefined);
  export const ListItemIndexContext = React.createContext<number>(0);

  export const List = component('Markup.List')((
    props: React.PropsWithChildren<PropsMarkupBase & ListProps & ParagraphProps>
  ) => {
    const { children, listStyle = 'dash', ...others } = props;
    if (!['star', 'dash', 'plus', 'decimal', 'latin'].includes(listStyle)) {
      throw ReadError.fromProps(`Invalid list style: ${listStyle}`, others);
    }
    return (
      <Markup.Environment {...others}>
        {irElement('list', { listStyle, ...others }, children)}
      </Markup.Environment>
    );
  });

  export const ListItem = component('Markup.ListItem')((
    props: React.PropsWithChildren<PropsMarkupBase & ParagraphProps>
  ) => {
    const { children, ...others } = props;
    return irElement('item', { ...others }, children);
  });

  export const TableContainer = component('Markup.TableContainer')((
    props: React.PropsWithChildren<PropsMarkupBase & ParagraphProps>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="table">
        {children}
      </SimpleMarkupComponent>
    );
  });

  export const TableHead = component('Markup.TableHead')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="thead">
        {children}
      </SimpleMarkupComponent>
    );
  });

  export const TableBody = component('Markup.TableBody')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="tbody">
        {children}
      </SimpleMarkupComponent>
    );
  });

  export const TableRow = component('Markup.TableRow')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="trow">
        {children}
      </SimpleMarkupComponent>
    );
  });

  export const TableCell = component('Markup.TableCell')((
    props: React.PropsWithChildren<PropsMarkupBase>
  ) => {
    const { children, ...others } = props;
    return (
      <SimpleMarkupComponent {...others} tagName="tcell">
        {children}
      </SimpleMarkupComponent>
    );
  });
}

export namespace Serialize {
  /**
   * Encloses a serialize component.
   * It becomes transparent when already in a serialized environment.
   *
   * When environment exists, the writer does things to render the environment.
   * How environment handles its child elements is very similar to the Any component,
   * except when the environment only contains a single element, in which case it will be directly returned
   * if it's unnamed.
   */
  export const Environment = component('Serialize.Environment')((
    props: React.PropsWithChildren<PropsSerializeBase>
  ) => {
    const parentPresentation = React.useContext(PresentationApproach);

    // presentation is extracted but not used here. We are already in serialize mode.
    // The env IR element only accepts a limited subset. Make sure others is not used here.
    let {
      presentation,
      serializer,
      children,
      originalStartIndex,
      originalEndIndex,
      writerOptions,
      sourcePath,
      ...others
    } = props;

    if (!serializer) {
      if (parentPresentation?.presentation === 'serialize') {
        serializer = (parentPresentation as PropsSerializeBase).serializer;
      } else {
        serializer = DefaultSerializer;
      }
    }

    let elem =
      parentPresentation?.presentation === 'serialize' &&
      parentPresentation?.serializer === serializer &&
      (!writerOptions || parentPresentation?.writerOptions === writerOptions) ? (
        <>{children}</>
      ) : (
        irElement(
          'env',
          {
            presentation: 'serialize',
            serializer,
            originalStartIndex,
            originalEndIndex,
            writerOptions,
            sourcePath
          },
          <PresentationApproach.Provider
            value={{
              presentation: 'serialize',
              serializer: serializer,
              writerOptions: writerOptions
            }}
          >
            {trimChildrenWhiteSpace(children, props)}
          </PresentationApproach.Provider>
        )
      );
    if (parentPresentation?.presentation === 'markup') {
      // If the parent is in markup mode, we need a wrapper (e.g., ```json...```).
      // TODO: support inline = true
      elem = (
        <Markup.EncloseSerialize inline={false} lang={serializer} {...others}>
          {elem}
        </Markup.EncloseSerialize>
      );
    }
    return elem;
  });

  export interface AnyProps {
    name?: string; // using name because key is reserved in react.
    type?: AnyValue;
  }

  /**
   * Value is a single value or (usually) a pair of key and value. The behavior is as follows:
   * 1. If the inner children are one single text element, it renders as a single value with the specified type.
   * 2. Otherwise, it can be either a list or an object depending on its children.
   *
   * Detailed implementation might differ between different writers, but generally:
   * 1. When the children contain all named values and type is not array, it presents as an object.
   * 2. When the children contain unnamed values, it presents as a list.
   * 3. When the children contain multiple elements including text elements, they are concatenated into a list.
   */
  export const Any = component('Serialize.Any')((
    props: React.PropsWithChildren<AnyProps & PropsSerializeBase>
  ) => {
    const { name, type, children, ...others } = props;
    const attrs: { [key: string]: any } = {};
    if (name !== undefined) {
      attrs.name = name;
    }
    if (type === undefined) {
      if (typeof children === 'string') {
        attrs.type = 'string';
      } else if (typeof children === 'number') {
        attrs.type = Number.isInteger(children) ? 'integer' : 'float';
      } else if (typeof children === 'boolean') {
        attrs.type = 'boolean';
      } else if (children === null || children === undefined) {
        attrs.type = 'null';
      }
    } else {
      attrs.type = type;
    }
    return (
      <Serialize.Environment {...others}>
        {irElement('any', { name, type, ...others }, children)}
      </Serialize.Environment>
    );
  });

  export interface ObjectProps {
    data: any;
  }

  // Object is to quickly insert an external data into the current document.
  export const Object = component('Serialize.Object')((
    props: React.PropsWithChildren<ObjectProps & PropsSerializeBase>
  ) => {
    const { data, ...others } = props;

    return (
      <Serialize.Environment {...others}>
        {irElement('obj', { data: JSON.stringify(data), ...others })}
      </Serialize.Environment>
    );
  });
}

export namespace Free {
  /**
   * The free environment marks the content as free-form text,
   * which will be kept as is without any processing.
   */
  export const Environment = component('Free.Environment')((
    props: React.PropsWithChildren<PropsFreeBase>
  ) => {
    const parentPresentation = React.useContext(PresentationApproach);

    // presentation is extracted but not used here. We are already in serialize mode.
    // The env IR element only accepts a limited subset. Make sure others is not used here.
    const {
      presentation,
      children,
      originalStartIndex,
      originalEndIndex,
      writerOptions,
      sourcePath,
      whiteSpace = 'pre',
      ...others
    } = props;

    let elem =
      parentPresentation?.presentation === 'free' &&
      (!writerOptions || parentPresentation?.writerOptions === writerOptions) ? (
        <>{children}</>
      ) : (
        irElement(
          'env',
          { presentation: 'free', originalStartIndex, originalEndIndex, writerOptions, whiteSpace, sourcePath },
          <PresentationApproach.Provider
            value={{
              presentation: 'free',
              writerOptions: writerOptions
            }}
          >
            {trimChildrenWhiteSpace(children, { ...props, whiteSpace })}
          </PresentationApproach.Provider>
        )
      );
    if (parentPresentation?.presentation === 'markup') {
      // If the parent is in markup mode, we need a wrapper (e.g., ```...```).
      // TODO: support inline = true
      elem = (
        <Markup.EncloseSerialize inline={false} {...others}>
          {elem}
        </Markup.EncloseSerialize>
      );
    } else if (parentPresentation?.presentation === 'serialize') {
      // Make it a string
      elem = <Serialize.Any {...others}>{elem}</Serialize.Any>;
    }
    return elem;
  });

  // This exists only because sometimes we needs to set attributes on free text.
  // For example, class names and speakers.
  export const Text = component('Free.Text')((props: React.PropsWithChildren<PropsFreeBase>) => {
    const { children, whiteSpace = 'pre', ...others } = props;
    return (
      <Free.Environment whiteSpace={whiteSpace} {...others}>
        {irElement('text', { whiteSpace, ...others }, children)}
      </Free.Environment>
    );
  });
}

export namespace MultiMedia {
  export interface ImageProps {
    type?: string; // image/png, image/jpeg, etc.
    base64?: string; // Used for models that does support image.
    alt?: string; // Used for models that does not support image.
    position?: Position; // Only applicable when the image is shown as image (not as text).
  }

  export interface AudioProps {
    type?: string; // audio/mpeg, audio/wav, etc.
    base64?: string; // Used for models that does support audio.
    alt?: string; // Used for models that does not support audio.
    position?: Position; // Only applicable when the audio is shown as audio (not as text).
  }

  export const Environment = component('MultiMedia.Environment')((
    props: React.PropsWithChildren<PropsMultiMediaBase>
  ) => {
    const parentPresentation = React.useContext(PresentationApproach);

    const {
      presentation,
      children,
      originalStartIndex,
      originalEndIndex,
      writerOptions,
      sourcePath,
      ...others
    } = props;

    return parentPresentation?.presentation === 'multimedia' &&
      (!writerOptions || parentPresentation?.writerOptions === writerOptions) ? (
      <>{children}</>
    ) : (
      irElement(
        'env',
        { presentation: 'multimedia', originalStartIndex, originalEndIndex, writerOptions, sourcePath },
        <PresentationApproach.Provider
          value={{
            presentation: 'multimedia',
            writerOptions: writerOptions
          }}
        >
          {trimChildrenWhiteSpace(children, props)}
        </PresentationApproach.Provider>
      )
    );
  });

  export const Image = component('MultiMedia.Image')((props: PropsMultiMediaBase & ImageProps) => {
    const { ...others } = props;
    return (
      <MultiMedia.Environment {...others}>{irElement('img', { ...others })}</MultiMedia.Environment>
    );
  });

  export const Audio = component('MultiMedia.Audio')((props: PropsMultiMediaBase & AudioProps) => {
    const { ...others } = props;
    return (
      <MultiMedia.Environment {...others}>
        {irElement('audio', { ...others })}
      </MultiMedia.Environment>
    );
  });
}



================================================
FILE: packages/poml/version.ts
================================================
export const POML_VERSION = "0.0.8";



================================================
FILE: packages/poml/components/document.tsx
================================================
import * as React from 'react';
import fs from '../util/fs';
import * as mammoth from 'mammoth';
import * as cheerio from 'cheerio';

import { Header, Newline, Text, Image, Paragraph, PropsSyntaxBase, List, ListItem, Bold, Italic } from 'poml/essentials';
// import pdf from 'pdf-parse';
import { pdfParse, getNumPages } from 'poml/util/pdf';
import { component, expandRelative, useWithCatch, BufferCollection } from 'poml/base';
import { Table } from './table';
import { parsePythonStyleSlice } from './utils';

function readBufferCached(filePath: string): Buffer {
  const abs = expandRelative(filePath);
  const key = `content://${abs}`;
  const stat = fs.statSync(abs);
  const cached = BufferCollection.get<{ value: Buffer; mtime: number }>(key);
  if (cached && cached.mtime === stat.mtimeMs) {
    return cached.value;
  }
  const buf = fs.readFileSync(abs);
  BufferCollection.set(key, { value: buf, mtime: stat.mtimeMs });
  return buf;
}

async function parsePdfWithPageLimit(dataBuffer: Buffer, startPage: number, endPage: number) {
  // This is a workaround for pdf-parse not supporting a range.
  const data = await pdfParse(dataBuffer, endPage + 1);
  if (startPage <= 0) {
    return data;
  }
  const minusData = await pdfParse(dataBuffer, startPage);
  return data.slice(minusData.length);
}

export async function readPdf(
  dataBuffer: Buffer,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const { selectedPages } = options || {};
  const numPages = await getNumPages(dataBuffer);
  if (selectedPages) {
    const [start, end] = parsePythonStyleSlice(selectedPages, numPages);
    const result = await parsePdfWithPageLimit(dataBuffer, start, end);
    return <Text whiteSpace='pre'>{result}</Text>;
  } else {
    return <Text whiteSpace='pre'>{await pdfParse(dataBuffer)}</Text>;
  }
}

export async function readPdfFromPath(
  filePath: string,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const dataBuffer = readBufferCached(filePath);
  return readPdf(dataBuffer, options);
}

function htmlContentsToPoml(
  element: cheerio.Cheerio<any>,
  $: cheerio.CheerioAPI,
  options?: DocumentProps
): React.ReactNode[] {
  const children = element
    .contents()
    .toArray()
    .map((child, index) => {
      if (child.type === 'text') {
        return <React.Fragment key={index}>{child.data}</React.Fragment>;
      } else {
        return <React.Fragment key={index}>{htmlToPoml($(child), $, options)}</React.Fragment>;
      }
    });
  return children;
}

function convertTableFromHtml(
  element: cheerio.Cheerio<any>,
  $: cheerio.CheerioAPI,
  options?: DocumentProps
): React.ReactElement {
  const body = element
    .find('tr')
    .toArray()
    .map(tr =>
      $(tr)
        .find('td, th')
        .toArray()
        .map(td => $(td).text())
    );
  const header = body.shift() || [];

  if (header.length === 0) {
    return <></>;
  }
  const maxColumns = Math.max(...body.map(row => row.length), header.length);
  if (header.length < maxColumns) {
    header.push(
      ...Array(maxColumns - header.length).map(i => `Unnamed Column ${i + header.length}`)
    );
  }
  const rows = body.map(row => {
    return Object.fromEntries(
      header.map((column, index) => {
        return [column, index < row.length ? row[index] : ''];
      })
    );
  });
  return (
    <Table records={rows} columns={header.map(column => ({ field: column, header: column }))} />
  );
}

export function htmlToPoml(
  element: cheerio.Cheerio<any>,
  $: cheerio.CheerioAPI,
  options?: DocumentProps
): React.ReactElement {
  if (element.is('style') || element.is('script')) {
    return <></>;
  } else if (
    element.is('h1') ||
    element.is('h2') ||
    element.is('h3') ||
    element.is('h4') ||
    element.is('h5') ||
    element.is('h6')
  ) {
    return <Header whiteSpace='pre'>{htmlContentsToPoml(element, $, options)}</Header>;
  } else if (element.is('p') || element.is('div')) {
    return <Paragraph whiteSpace='pre'>{htmlContentsToPoml(element, $, options)}</Paragraph>;
  } else if (element.is('br')) {
    return <Newline />;
  } else if (element.is('ol')) {
    return <List listStyle='decimal'>{htmlContentsToPoml(element, $, options)}</List>;
  } else if (element.is('ul')) {
    return <List>{htmlContentsToPoml(element, $, options)}</List>;
  } else if (element.is('li')) {
    return <ListItem>{htmlContentsToPoml(element, $, options)}</ListItem>;
  } else if (element.is('b')) {
    return <Bold>{htmlContentsToPoml(element, $, options)}</Bold>;
  } else if (element.is('i')) {
    return <Italic>{htmlContentsToPoml(element, $, options)}</Italic>;
  } else if (element.is('img')) {
    // src is in the format of data:image/png;base64, so we can't use it directly
    const src = element.attr('src')!;
    // check whether src is in the format of data:type;base64
    if (src.startsWith('data:') && src.includes(';base64')) {
      const base64 = src.split(',')[1];
      if (options?.multimedia || options?.multimedia === undefined) {
        return <Image syntax="multimedia" base64={base64} alt={element.attr('alt')} />;
      } else {
        return <Image base64={base64} alt={element.attr('alt')} />;
      }
    } else {
      // TODO: Probably needs to fetch a file or URL
      return <></>;
    }
  } else if (element.is('table')) {
    return convertTableFromHtml(element, $, options);
  } else {
    return <>{htmlContentsToPoml(element, $, options)}</>;
  }
}

export async function readDocx(
  dataBuffer: Buffer,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const result = await mammoth.convertToHtml({ buffer: dataBuffer });
  const $ = cheerio.load(result.value);
  return <Text syntax="markdown">{htmlContentsToPoml($('body'), $, options)}</Text>;
}

export async function readDocxFromPath(
  filePath: string,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const dataBuffer = readBufferCached(filePath);
  return readDocx(dataBuffer, options);
}

export async function readTxt(
  dataBuffer: Buffer,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const text = dataBuffer.toString();
  return <Text whiteSpace='pre'>{text}</Text>;
}

export async function readTxtFromPath(
  filePath: string,
  options?: DocumentProps
): Promise<React.ReactElement> {
  const dataBuffer = readBufferCached(filePath);
  return readTxt(dataBuffer, options);
}

type DocumentParser = 'pdf' | 'docx' | 'txt' | 'auto';

interface DocumentProps extends PropsSyntaxBase {
  src?: string;
  parser?: DocumentParser;
  buffer?: string | Buffer;
  base64?: string;
  multimedia?: boolean;
  selectedPages?: string;
}

function determineParser(src: string): DocumentParser {
  src = src.toLowerCase();
  if (src.endsWith('.docx') || src.endsWith('.doc')) {
    return 'docx';
  } else if (src.endsWith('.pdf')) {
    return 'pdf';
  } else if (src.endsWith('.txt')) {
    return 'txt';
  } else {
    throw new Error('Cannot determine parser for ' + src + '. Please manually specify a parser.');
  }
}

async function autoParseDocument(
  props: DocumentProps & { buffer?: Buffer }
): Promise<React.ReactElement> {
  let { parser, src, buffer } = props;
  if (parser === 'auto' || parser === undefined) {
    if (!src) {
      throw new Error('Cannot determine parser without source file provided.');
    }
    parser = determineParser(src);
  }
  if (src) {
    buffer = readBufferCached(src);
  } else if (!buffer) {
    throw new Error('Either buffer or src must be provided');
  }

  switch (parser) {
    case 'pdf':
      return await readPdf(buffer, props);
    case 'docx':
      return await readDocx(buffer, props);
    case 'txt':
      return await readTxt(buffer, props);
    default:
      throw new Error('Unsupported parser: ' + parser);
  }
}

/**
 * Displaying an external document like PDF, TXT or DOCX.
 *
 * @param {string} src - The source file to read the data from. This must be provided if records is not provided.
 * @param {Buffer|string} buffer - Document data buffer. Recommended to use `src` instead unless you want to use a string.
 * @param {string} base64 - Base64 encoded string of the document data. Mutually exclusive with `src` and `buffer`.
 * @param {'auto'|'pdf'|'docx'|'txt'} parser - The parser to use for reading the data. If not provided, it will be inferred from the file extension.
 * @param {boolean} multimedia - If true, the multimedias will be displayed. If false, the alt strings will be displayed at best effort. Default is `true`.
 * @param {string} selectedPages - The pages to be selected. This is only available **for PDF documents**. If not provided, all pages will be selected.
 * You can use a string like `2` to specify a single page, or slice like `2:4` to specify a range of pages (2 inclusive, 4 exclusive).
 * The pages selected are **0-indexed**. Negative indexes like `-1` is not supported here.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * To display a Word document without including the real multimedia:
 * ```xml
 * <Document src="sample.docx" multimedia="false"/>
 * ```
 */
export const Document = component('Document', { aliases: ['doc'], asynchorous: true })((
  props: DocumentProps
) => {
  let { buffer, parser, base64, ...others } = props;
  let parsedBuffer: Buffer | undefined;
  if (base64) {
    if (buffer !== undefined) {
      throw new Error('Either buffer or base64 should be provided, not both.');
    }
    parsedBuffer = Buffer.from(base64, 'base64');
  } else {
    if (typeof buffer === 'string') {
      parsedBuffer = Buffer.from(buffer, 'utf-8');
      if (parser === undefined || parser === 'auto') {
        parser = 'txt';
      }
    } else {
      parsedBuffer = buffer;
    }
  }
  const document = useWithCatch(
    autoParseDocument({ buffer: parsedBuffer, parser, ...others }),
    others
  );
  return <>{document ?? null}</>;
});



================================================
FILE: packages/poml/components/index.ts
================================================
export * from "./table";
export * from "./instructions";
export * from "./utils";
export * from "./document";
export * from "./message";
export * from "./tree";
export * from "./webpage";



================================================
FILE: packages/poml/components/instructions.tsx
================================================
import * as React from 'react';
import { component, trimChildrenWhiteSpace } from 'poml/base';
import { computeSyntaxContext, Paragraph, Text } from 'poml/essentials';
import { BaseCaptionedParagraphProps, Caption, CaptionedParagraph } from './utils';

interface CustomizableCaptionParagraphProps extends BaseCaptionedParagraphProps {
  caption?: string;
}

/**
 * Specifies the role you want the language model to assume when responding.
 * Defining a role provides the model with a perspective or context,
 * such as a scientist, poet, child, or any other persona you choose.
 *
 * @param caption - The title or label for the role paragraph. Default is `Role`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `role`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 * 
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <role>You are a data scientist.</role>
 * ```
 */
export const Role = component('Role')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const { children, caption = 'Role', captionSerialized = 'role', ...others } = props;
  return (
    <CaptionedParagraph caption={caption} captionSerialized={captionSerialized} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

/**
 * Task represents the action you want the language model to perform.
 * It is a directive or instruction that you want the model to follow.
 * Task is usually not long, but rather a concise and clear statement.
 * Users can also include a list of steps or instructions to complete the task.
 *
 * @param caption - The title or label for the task paragraph. Default is `Task`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `task`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <task>Cook a recipe on how to prepare a beef dish.</task>
 * ```
 * 
 * When including a list of steps:
 * ```xml
 * <task>
 *   Planning a schedule for a travel.
 *   <list>
 *     <item>Decide on the destination and plan the duration.</item>
 *     <item>Find useful information about the destination.</item>
 *     <item>Write down the schedule for each day.</item>
 *   </list>
 * </task>
 * ```
 */
export const Task = component('Task')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const { children, caption = 'Task', captionSerialized = 'task', ...others } = props;
  return (
    <CaptionedParagraph caption={caption} captionSerialized={captionSerialized} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

/**
 * Output format deals with the format in which the model should provide the output.
 * It can be a specific format such as JSON, XML, or CSV, or a general format such as a story,
 * a diagram or steps of instructions.
 * Please refrain from specifying too complex formats that the model may not be able to generate,
 * such as a PDF file or a video.
 *
 * @param caption - The title or label for the output format paragraph. Default is `Output Format`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `outputFormat`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <output-format>Respond with a JSON without additional characters or punctuations.</output-format>
 * ```
 */
export const OutputFormat = component('OutputFormat')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Output Format',
    captionSerialized = 'outputFormat',
    ...others
  } = props;
  return (
    <CaptionedParagraph caption={caption} captionSerialized={captionSerialized} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

/**
 * StepwiseInstructions that elaborates the task by providing a list of steps or instructions.
 * Each step should be concise and clear, and the list should be easy to follow.
 *
 * @param caption - The title or label for the stepwise instructions paragraph. Default is `Stepwise Instructions`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `stepwiseInstructions`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <stepwise-instructions>
 *   <list>
 *     <item>Interpret and rewrite user's query.</item>
 *     <item>Think of a plan to solve the query.</item>
 *     <item>Generate a response based on the plan.</item>
 *   </list>
 * </stepwise-instructions>
 * ```
 */
export const StepwiseInstructions = component('StepwiseInstructions')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Stepwise Instructions',
    captionSerialized = 'stepwiseInstructions',
    ...others
  } = props;
  return (
    <CaptionedParagraph caption={caption} captionSerialized={captionSerialized} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

/**
 * Hint can be used anywhere in the prompt where you want to provide a helpful tip or explanation.
 * It is usually a short and concise statement that guides the LLM in the right direction.
 *
 * @param caption - The title or label for the hint paragraph. Default is `Hint`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `hint`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `bold`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {boolean} captionColon - Indicates whether to append a colon after the caption.
 * By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <hint>Alice first purchased 4 apples and then 3 more, so she has 7 apples in total.</hint>
 * ```
 */
export const Hint = component('Hint')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Hint',
    captionStyle = 'bold',
    captionSerialized = 'hint',
    ...others
  } = props;
  return (
    <CaptionedParagraph caption={caption} captionStyle={captionStyle} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

/**
 * Introducer is a paragraph before a long paragraph (usually a list of examples, steps, or instructions).
 * It serves as a context introducing what is expected to follow.
 *
 * @param caption - The title or label for the introducer paragraph. Default is `Introducer`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `introducer`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `hidden`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <introducer>Here are some examples.</introducer>
 * ```
 */
export const Introducer = component('Introducer')((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Introducer',
    captionStyle = 'hidden',
    captionSerialized = 'introducer',
    ...others
  } = props;
  return (
    <CaptionedParagraph caption={caption} captionStyle={captionStyle} {...others}>
      {children}
    </CaptionedParagraph>
  );
});

interface ExampleSetProps extends CustomizableCaptionParagraphProps {
  chat?: boolean;
  introducer?: string;
}

const ChatRenderedExampleContext = React.createContext(true);

/**
 * Example set (`<examples>`) is a collection of examples that are usually presented in a list.
 * With the example set, you can manage multiple examples under a single title and optionally an introducer,
 * as well as the same `chat` format.
 * You can also choose to use `<example>` purely without example set.
 *
 * @param caption - The title or label for the example set paragraph. Default is `Examples`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `examples`.
 * @param {boolean} chat - Indicates whether the examples should be rendered in chat format.
 * By default, it's `true` for "markup" syntaxes and `false` for "serializer" syntaxes.
 * @param introducer - An optional introducer text to be displayed before the examples.
 * For example, `Here are some examples:`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <examples chat={{true}}>
 *   <example>
 *     <input>What is the capital of France?</input>
 *     <output>Paris</output>
 *   </example>
 *   <example>
 *     <input>What is the capital of Germany?</input>
 *     <output>Berlin</output>
 *   </example>
 * </examples>
 * ```
 */
export const ExampleSet = component('ExampleSet', ['examples'])((
  props: React.PropsWithChildren<ExampleSetProps>
) => {
  const {
    children,
    caption = 'Examples',
    captionSerialized = 'examples',
    chat,
    introducer,
    ...others
  } = props;
  const presentation = computeSyntaxContext(props);
  const chatComputed = chat ?? (presentation === 'markup');
  const examples = (
    <ChatRenderedExampleContext.Provider value={chatComputed}>
      {trimChildrenWhiteSpace(children, props)}
    </ChatRenderedExampleContext.Provider>
  );
  return (
    <CaptionedParagraph caption={caption} captionSerialized={captionSerialized} {...others}>
      {introducer && presentation === 'markup' ? <Introducer>{introducer}</Introducer> : null}
      {examples}
    </CaptionedParagraph>
  );
});

interface ExampleProps extends CustomizableCaptionParagraphProps {
  chat?: boolean;
}

/**
 * Example is useful for providing a context, helping the model to understand what kind of inputs and outputs are expected.
 * It can also be used to demonstrate the desired output style, clarifying the structure, tone, or level of detail in the response.
 *
 * @param caption - The title or label for the example paragraph. Default is `Example`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `example`.
 * @param captionStyle - Determines the style of the caption, applicable only for "markup" syntaxes. Default is `hidden`.
 * Options include `header`, `bold`, `plain`, or `hidden`.
 * @param {boolean} chat - Indicates whether the example should be rendered in chat format.
 * When used in a example set (`<examples>`), this is inherited from the example set.
 * Otherwise, it defaults to `false` for "serializer" syntaxes and `true` for "markup" syntaxes.
 * @param captionTextTransform - Specifies text transformation for the caption, applicable only for "markup" syntaxes.
 * Options are `upper`, `lower`, `capitalize`, or `none`. Default is `none`.
 * @param {boolean} captionColon - Indicates whether to append a colon after the caption.
 * By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <example>
 *   <input>What is the capital of France?</input>
 *   <output>Paris</output>
 * </example>
 * ```
 * 
 * ```xml
 * <task>Summarize the following passage in a single sentence.</task>
 * <example>
 *   <input caption="Passage">The sun provides energy for life on Earth through processes like photosynthesis.</input>
 *   <output caption="Summary">The sun is essential for energy and life processes on Earth.</output>
 * </example>
 * ```
 */
export const Example = component('Example')((props: React.PropsWithChildren<ExampleProps>) => {
  const presentation = computeSyntaxContext(props);
  const {
    children,
    caption = 'Example',
    captionSerialized = 'example',
    captionStyle = 'hidden',
    chat,
    ...others
  } = props;
  if (presentation === 'markup') {
    return (
      <CaptionedParagraph
        caption={caption}
        captionSerialized={captionSerialized}
        captionStyle={captionStyle}
        {...others}
      >
        {chat !== undefined ? (
          <ChatRenderedExampleContext.Provider value={chat}>
            {trimChildrenWhiteSpace(children, props)}
          </ChatRenderedExampleContext.Provider>
        ) : (
          children
        )}
      </CaptionedParagraph>
    );
  } else {
    return <Text {...others}>{children}</Text>;
  }
});

/**
 * ExampleInput (`<input>`) is a paragraph that represents an example input.
 * By default, it's spoken by a human speaker in a chat context, but you can manually specify the speaker.
 *
 * @param caption - The title or label for the example input paragraph. Default is `Input`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `input`.
 * @param speaker - The speaker for the example input. Default is `human` if chat context is enabled (see `<example>`).
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `hidden` if chat context is enabled. Otherwise, it's `bold`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {boolean} captionColon - Indicates whether to append a colon after the caption.
 * By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <input>What is the capital of France?</input>
 * ```
 * 
 * When used with a template:
 * 
 * ```xml
 * <input>What is the capital of {{country}}?</input>
 * ```
 */
export const ExampleInput = component('ExampleInput', ['input'])((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Input',
    captionSerialized = 'input',
    captionStyle,
    speaker,
    ...others
  } = props;
  const speakerFromContext =
    speaker || (React.useContext(ChatRenderedExampleContext) ? 'human' : undefined);
  const captionStyleForContext =
    captionStyle || (React.useContext(ChatRenderedExampleContext) ? 'hidden' : 'bold');
  return (
    <CaptionedParagraph
      caption={caption}
      captionSerialized={captionSerialized}
      captionStyle={captionStyleForContext}
      speaker={speakerFromContext}
      {...others}
    >
      {children}
    </CaptionedParagraph>
  );
});

/**
 * ExampleOutput (`<output>`) is a paragraph that represents an example output.
 * By default, it's spoken by a AI speaker in a chat context, but you can manually specify the speaker.
 *
 * @param caption - The title or label for the example output paragraph. Default is `Output`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `output`.
 * @param speaker - The speaker for the example output. Default is `ai` if chat context is enabled (see `<example>`).
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `hidden` if chat context is enabled. Otherwise, it's `bold`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {boolean} captionColon - Indicates whether to append a colon after the caption.
 * By default, this is true for `bold` or `plain` captionStyle, and false otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <output>The capital of France is Paris.</output>
 * ```
 * 
 * When used with a template:
 * 
 * ```xml
 * <output>The capital of {{country}} is {{capital}}.</output>
 * ```
 */
export const ExampleOutput = component('ExampleOutput', ['output'])((
  props: React.PropsWithChildren<CustomizableCaptionParagraphProps>
) => {
  const {
    children,
    caption = 'Output',
    captionSerialized = 'output',
    captionStyle,
    speaker,
    ...others
  } = props;
  const speakerFromContext =
    speaker || (React.useContext(ChatRenderedExampleContext) ? 'ai' : undefined);
  const captionStyleForContext =
    captionStyle || (React.useContext(ChatRenderedExampleContext) ? 'hidden' : 'bold');
  return (
    <CaptionedParagraph
      caption={caption}
      captionSerialized={captionSerialized}
      captionStyle={captionStyleForContext}
      speaker={speakerFromContext}
      {...others}
    >
      {children}
    </CaptionedParagraph>
  );
});

interface QuestionProps extends BaseCaptionedParagraphProps {
  questionCaption?: string;
  answerCaption?: string;
}

/**
 * Question (`<qa>`) is actually a combination of a question and a prompt for the answer.
 * It's usually used at the end of a prompt to ask a question.
 * The question is followed by a prompt for answer (e.g., `Answer:`) to guide the model to respond.
 *
 * @param questionCaption - The title or label for the question paragraph. Default is `Question`.
 * @param answerCaption - The title or label for the answer paragraph. Default is `Answer`.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes. Default is `question`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `bold`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <qa>What is the capital of France?</qa>
 * ```
 */
export const Question = component('Question', ['qa'])((
  props: React.PropsWithChildren<QuestionProps>
) => {
  const presentation = computeSyntaxContext(props);
  const {
    children,
    questionCaption = 'Question',
    answerCaption = 'Answer',
    captionSerialized = 'question',
    captionStyle = 'bold',
    ...others
  } = props;
  return (
    <Paragraph>
      <CaptionedParagraph
        caption={questionCaption}
        captionSerialized={captionSerialized}
        captionStyle={captionStyle}
        {...others}
      >
        {children}
      </CaptionedParagraph>
      {answerCaption && presentation === 'markup' ? (
        <Caption
          caption={answerCaption}
          captionStyle={captionStyle}
          captionTailingSpace={false}
          {...others}
        />
      ) : null}
    </Paragraph>
  );
});



================================================
FILE: packages/poml/components/message.tsx
================================================
import { component, ContentMultiMedia, RichContent } from 'poml/base';
import { Text, Image } from 'poml/essentials';
import * as React from 'react';
import { Message } from 'poml/base';
import { parsePythonStyleSlice } from './utils';

/**
 * Wrap the contents in a system message.
 *
 * @see {@link Text} for other props available.
 *
 * @example
 * ```xml
 * <system-msg>Answer concisely.</system-msg>
 * ```
 */
export const SystemMessage = component('SystemMessage', ['system-msg'])((
  props: React.PropsWithChildren
) => {
  const { children, ...others } = props;
  return (
    <Text speaker="system" {...others}>
      {children}
    </Text>
  );
});

/**
 * Wrap the contents in a user message.
 *
 * @see {@link Text} for other props available.
 *
 * @example
 * ```xml
 * <user-msg>What is the capital of France?</user-msg>
 * ```
 */
export const HumanMessage = component('HumanMessage', ['human-msg'])((
  props: React.PropsWithChildren
) => {
  const { children, ...others } = props;
  return (
    <Text speaker="human" {...others}>
      {children}
    </Text>
  );
});

/**
 * Wrap the contents in a AI message.
 *
 * @see {@link Text} for other props available.
 *
 * @example
 * ```xml
 * <ai-msg>Paris</ai-msg>
 * ```
 */
export const AiMessage = component('AiMessage', ['ai-msg'])((props: React.PropsWithChildren) => {
  const { children, ...others } = props;
  return (
    <Text speaker="ai" {...others}>
      {children}
    </Text>
  );
});

interface MessageContentProps {
  content: RichContent;
}

/**
 * Display a message content.
 * 
 * @param {object|string} content - The content of the message. It can be a string, or an array of strings and multimedia content.
 * 
 * @example
 * ```xml
 * <msg-content content="What is the capital of France?" />
 * ```
 */
export const MessageContent = component('MessageContent', ['msg-content'])((
  props: React.PropsWithChildren<MessageContentProps>
) => {
  const { children, content, ...others } = props;

  const displayStringOrMultimedia = (media: ContentMultiMedia | string, key?: string) => {
    if (typeof media === 'string') {
      return (
        <Text key={key} {...others}>
          {media}
        </Text>
      );
    } else if (media.type.startsWith('image/')) {
      return (
        <Image key={key} base64={media.base64} alt={media.alt} type={media.type} {...others} />
      );
    } else {
      throw new Error(`Unsupported media type: ${media.type}`);
    }
  };

  if (typeof content === 'string') {
    return displayStringOrMultimedia(content);
  } else if (Array.isArray(content)) {
    return <>{content.map((item, index) => displayStringOrMultimedia(item, `content-${index}`))}</>;
  }
});

interface ConversationProps {
  messages: Message[];
  selectedMessages?: string;
}

/**
 * Display a conversation between system, human and AI.
 *
 * @param {object} messages - A list of message. Each message should have a `speaker` and a `content` field.
 * @param {string} selectedMessages - The messages to be selected. If not provided, all messages will be selected.
 * You can use a string like `2` to specify a single message, or slice like `2:4` to specify a range of messages (2 inclusive, 4 exclusive).
 * Or use `-6:` to select the last 6 messages.
 *
 * @example
 * ```xml
 * <conversation messages="{{[{ speaker: 'human', content: 'What is the capital of France?' }, { speaker: 'ai', content: 'Paris' }]}}" />
 * ```
 */
export const Conversation = component('Conversation', ['conversation'])((
  props: React.PropsWithChildren<ConversationProps>
) => {
  let { children, messages, selectedMessages, ...others } = props;
  if (selectedMessages) {
    const [start, end] = parsePythonStyleSlice(selectedMessages, messages.length);
    messages = messages.slice(start, end);
  }
  return (
    <>
      {messages.map((message, index) => (
        <Text key={`message-${index}`} speaker={message.speaker} {...others}>
          <MessageContent content={message.content} {...others} />
        </Text>
      ))}
    </>
  );
});



================================================
FILE: packages/poml/components/table.tsx
================================================
import * as React from 'react';
import { Markup, Serialize } from 'poml/presentation';
import { PropsSyntaxBase, computeSyntaxContext } from 'poml/essentials';
import { component, expandRelative } from 'poml/base';
import { parseText, guessStringType, AnyValue } from 'poml/util';
import { csvParse, tsvParse, DSVRowArray } from 'd3-dsv';
import { readFileSync } from '../util/fs';
import * as XLSX from 'xlsx';
import { parsePythonStyleSlice } from './utils';

interface ColumnDefinition {
  field: string;
  header: string;
  description?: string;
}

export interface RecordColumns {
  records: any[];
  columns?: ColumnDefinition[];
}

type TableParser = 'auto' | 'csv' | 'tsv' | 'excel' | 'json' | 'jsonl';

export interface TableProps extends PropsSyntaxBase {
  records?: any[] | string;
  columns?: ColumnDefinition[];
  src?: string;
  parser?: TableParser;
  selectedColumns?: string | string[];
  selectedRecords?: string | number[];
  maxRecords?: number;
  maxColumns?: number;
}

function determineParser(src: string): TableParser {
  src = src.toLowerCase();
  if (src.endsWith('.csv')) {
    return 'csv';
  } else if (src.endsWith('.tsv')) {
    return 'tsv';
  } else if (src.endsWith('.xls') || src.endsWith('.xlsx')) {
    return 'excel';
  } else if (src.endsWith('.jsonl')) {
    return 'jsonl';
  } else if (src.endsWith('.json')) {
    return 'json';
  } else {
    throw new Error('Cannot determine parser for ' + src);
  }
}

function parseTableData(data: Buffer, parser: TableParser): RecordColumns {
  switch (parser) {
    case 'csv':
      return parseCsv(data);
    case 'tsv':
      return parseTsv(data);
    case 'excel':
      return parseExcel(data);
    case 'json':
      return parseJson(data);
    case 'jsonl':
      return parseJsonl(data);
    default:
      throw new Error('Unsupported parser: ' + parser);
  }
}

function postProcessD3Records(records: DSVRowArray<string>): RecordColumns {
  if (records.length === 0 && records.columns === undefined) {
    throw new Error('No records found and no headers provided');
  }
  const columns = records.columns.map((column: string) => ({ field: column, header: column }));
  const columnTypes = records.columns.reduce(
    (prev, column) => {
      prev[column] = 'string';
      if (records.length > 0) {
        const types = records.map(record => guessStringType(record[column])[1]);
        if (types.every(type => type === 'boolean')) {
          prev[column] = 'boolean';
        } else if (types.every(type => type === 'integer' || type === 'boolean')) {
          prev[column] = 'integer';
        } else if (
          types.every(type => type === 'float' || type === 'integer' || type === 'boolean')
        ) {
          prev[column] = 'float';
        } else if (types.every(type => type === 'array' || type === 'object')) {
          prev[column] = 'object';
        }
      }
      return prev;
    },
    {} as Record<string, AnyValue>
  );

  return {
    records: [
      ...records.map((record: any) => {
        return Object.entries(record).reduce((prev, [key, value]) => {
          if (typeof value === 'string') {
            prev[key] = parseText(value, columnTypes[key]);
          } else {
            prev[key] = value;
          }
          return prev;
        }, {} as any);
      })
    ],
    columns: columns
  };
}

function parseCsv(data: Buffer): RecordColumns {
  const records = csvParse(data.toString('utf-8'));
  return postProcessD3Records(records);
}

function parseTsv(data: Buffer): RecordColumns {
  const records = tsvParse(data.toString('utf-8'));
  return postProcessD3Records(records);
}

function parseExcel(data: Buffer): RecordColumns {
  const workbook = XLSX.read(data, { type: 'buffer' });
  const sheetName = workbook.SheetNames[0];
  if (!sheetName) {
    throw new Error('No sheet found in Excel file');
  }
  const sheet = workbook.Sheets[sheetName];
  const rawData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
  if (rawData.length === 0) {
    return { records: [] };
  }
  const headers = rawData[0] as string[];
  const columns = headers.map(header => ({ field: header, header }));
  const records = rawData.slice(1).map((row: any) => {
    const record: Record<string, any> = {};
    headers.forEach((header, index) => {
      record[header] = row[index];
    });
    return record;
  });
  return { records, columns };
}

function parseJson(data: Buffer): RecordColumns {
  return { records: JSON.parse(data.toString('utf-8')) };
}

function parseJsonl(data: Buffer): RecordColumns {
  return {
    records: data
      .toString('utf-8')
      .trim()
      .split('\n')
      .map(line => JSON.parse(line))
  };
}

function columnRecordsSelector(
  records: any[],
  columns: ColumnDefinition[] | undefined,
  props: TableProps
): RecordColumns {
  const { selectedColumns, selectedRecords, maxRecords, maxColumns } = props;
  if (!selectedColumns && !selectedRecords && !maxRecords && !maxColumns) {
    return { records, columns };
  }
  if (selectedColumns && columns) {
    let newColumns: ColumnDefinition[];
    if (Array.isArray(selectedColumns)) {
      newColumns = selectedColumns.map(columnName => {
        const found = columns!.find(column => column.field === columnName);
        if (found) {
          return found;
        }
        if (columnName === 'index') {
          return { field: 'index', header: 'Index' };
        }
        throw new Error('Column ' + columnName + 'is selected but not found');
      });
    } else if (typeof selectedColumns === 'string') {
      if (selectedColumns === '+index') {
        newColumns = [{ field: 'index', header: 'Index' }, ...columns];
      } else {
        const [start, end] = parsePythonStyleSlice(selectedColumns, columns.length);
        newColumns = columns.slice(start, end);
      }
    } else {
      throw new Error('Invalid selectedColumns format');
    }
    columns = newColumns;
    records = records.map((record, loopIndex) => {
      return newColumns.reduce((prev, column) => {
        if (column.field === 'index' && record.index === undefined) {
          prev['index'] = loopIndex;
        } else {
          prev[column.field] = record[column.field];
        }
        return prev;
      }, {} as any);
    });
  }
  if (selectedRecords) {
    if (Array.isArray(selectedRecords)) {
      records = selectedRecords.map(index => records[index]);
    } else if (typeof selectedRecords === 'string') {
      const [start, end] = parsePythonStyleSlice(selectedRecords, records.length);
      records = records.slice(start, end);
    } else {
      throw new Error('Invalid selectedRecords format');
    }
  }
  if (maxRecords && records.length > maxRecords) {
    const topRows = Math.ceil(maxRecords / 2);
    const bottomRows = Math.floor(maxRecords / 2);
    const ellipseRecord = (
      columns ? columns.map(column => column.field) : Object.keys(records[0])
    ).reduce((prev, column) => {
      prev[column] = '...';
      return prev;
    }, {} as any);
    records = [
      ...records.slice(0, topRows),
      ellipseRecord,
      ...records.slice(-bottomRows)
    ];
  }
  if (maxColumns && columns && columns.length > maxColumns) {
    const leftColumns = Math.ceil(maxColumns / 2);
    const rightColumns = Math.floor(maxColumns / 2);
    const newColumns = [
      ...columns.slice(0, leftColumns),
      { field: '...', header: '...' },
      ...columns.slice(-rightColumns)
    ];
    records = records.map(record => {
      return newColumns.reduce((prev, column) => {
        prev[column.field] = column.field === '...' ? '...' : record[column.field];
        return prev;
      }, {} as any);
    });
    columns = newColumns;
  }
  return { records, columns };
}

export function toRecordColumns(props: TableProps): RecordColumns {
  let { records, columns, src, parser } = props;
  if (records !== undefined && typeof records !== 'string') {
    if (!Array.isArray(records)) {
      throw new Error('Records must be an array for table');
    }
    if (records.length > 0 && Array.isArray(records[0])) {
      // Converting to object records
      const maxColumns = Math.max(...records.map(record => record.length));
      const columns = Array.from({ length: maxColumns }, (_, i) => ({
        field: i.toString(),
        header: 'Column ' + i.toString()
      }));
      records = records.map((record: any) => {
        return columns.reduce((prev, column, index) => {
          prev[column.field] = index < record.length ? record[index] : undefined;
          return prev;
        }, {} as any);
      });
      return { records, columns };
    }
    return { records, columns };
  }
  // Need to read data from src / parse data from string
  if (parser === 'auto' || parser === undefined) {
    if (!src) {
      throw new Error('Cannot determine parser without source file provided.');
    }
    parser = determineParser(src);
  }
  let data: Buffer;
  if (src) {
    data = readFileSync(expandRelative(src));
  } else if (records) {
    data = Buffer.from(records, 'utf-8');
  } else {
    throw new Error('Either records data or src must be provided');
  }

  const result = parseTableData(data, parser);
  if (!result.columns && columns) {
    result.columns = columns;
  }
  return result;
}

const TableMarkup = component('TableMarkup')(({
  columns,
  records,
  syntax,
  ...others
}: RecordColumns & PropsSyntaxBase) => {
  if (columns === undefined) {
    const keys = Object.keys(records[0]);
    records.forEach(record => {
      Object.keys(record).forEach((key: any) => {
        if (!keys.includes(key)) {
          keys.push(key);
        }
      });
    });
    columns = keys.map(key => ({ field: key, header: key }));
  }
  return (
    <Markup.TableContainer markupLang={syntax} {...others}>
      <Markup.TableHead>
        <Markup.TableRow>
          {columns.map((column, index) => (
            <Markup.TableCell key={index}>{column.header}</Markup.TableCell>
          ))}
        </Markup.TableRow>
      </Markup.TableHead>
      <Markup.TableBody>
        {records.map((record, index) => (
          <Markup.TableRow key={index}>
            {columns.map((column, index) => (
              <Markup.TableCell key={index}>{record[column.field]}</Markup.TableCell>
            ))}
          </Markup.TableRow>
        ))}
      </Markup.TableBody>
    </Markup.TableContainer>
  );
});

const TableSerialize = component('TableSerialize')(({
  columns,
  records,
  syntax,
  ...others
}: RecordColumns & PropsSyntaxBase) => {
  if (columns === undefined) {
    return <Serialize.Object data={records} serializer={syntax} {...others} />;
  } else {
    return (
      <Serialize.Object
        data={{
          columns: columns,
          records: records
        }}
        serializer={syntax}
        {...others}
      />
    );
  }
});

/**
 * Displaying a table with records and columns.
 *
 * @param {'markdown'|'html'|'json'|'text'|'csv'|'tsv'|'xml'} syntax - The output syntax of the content.
 * @param {object|string} records - A list, each element is an object / dictionary / list of elements. The keys are the fields and the values are the data in cells.
 * @param {object} columns - A list of column definitions. Each column definition is an object with keys "field", "header", and "description".
 * The field is the key in the record object, the header is displayed in the top row, and the description is meant to be an explanation.
 * Columns are optional. If not provided, the columns are inferred from the records.
 * @param {string} src - The source file to read the data from. This must be provided if records is not provided.
 * @param {'auto'|'csv'|'tsv'|'excel'|'json'|'jsonl'} parser - The parser to use for reading the data. If not provided, it will be inferred from the file extension.
 * @param {object|string} selectedColumns - The selected columns to display. If not provided, all columns will be displayed.
 * It should be an array of column field names, e.g. `["name", "age"]`; or a string like `2:4` to select columns 2 (inclusive) to 4 (exclusive).
 * There is a special column name called `index` which is the enumeration of the records starting from 0.
 * You can also use a special value called `+index` to add the index column to the original table.
 * @param {object|string} selectedRecords - The selected records to display. If not provided, all records will be displayed.
 * It should be an array of record indices, e.g. `[0, 1]`; or a string like `2:4` to select records 2 (inclusive) to 4 (exclusive).
 * @param {number} maxRecords - The maximum number of records to display. If not provided, all records will be displayed.
 * @param {number} maxColumns - The maximum number of columns to display. If not provided, all columns will be displayed.
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * ```xml
 * <table records="{{[{ name: 'Alice', age: 20 }, { name: 'Bob', age: 30 }]}}" />
 * ```
 * 
 * To import an excel file, and display the first 10 records in csv syntax:
 * 
 * ```xml
 * <table src="data.xlsx" parser="excel" maxRecords="10" syntax="csv" />
 * ```
 */
export const Table = component('Table')((props: TableProps) => {
  const presentation = computeSyntaxContext(props);
  const { records, columns, src, parser, ...others } = props;
  const data = toRecordColumns(props);
  const selectedData = columnRecordsSelector(data.records, data.columns, props);
  if (presentation === 'markup') {
    return <TableMarkup {...selectedData} {...others} />;
  } else if (presentation === 'serialize') {
    return <TableSerialize {...selectedData} {...others} />;
  }
});



================================================
FILE: packages/poml/components/tree.tsx
================================================
import * as React from 'react';
import fs from '../util/fs';
import * as path from 'path';
import {
  PropsSyntaxBase,
  computeSyntaxContext,
  List,
  ListItem,
  Text,
  Header,
  Code,
  SubContent,
  Object
} from 'poml/essentials';
import { component, expandRelative } from 'poml/base';

export interface TreeItemData {
  name: string;
  value?: string; // Content value for the item
  children?: TreeItemData[];
}

export interface TreeProps extends PropsSyntaxBase {
  items: TreeItemData[];
  showContent?: boolean;
}

// FIXME: The comment is not in the right format due to the parser limitation
/*
 * # Project
 *
 * ## Project/src
 *
 * ###  Project/src/index.js
 *
 * ```js
 * console.log("hello")
 * ```
 *
 * ### Project/package.json
 *
 * ```json
 * { "name": "project" }
 * ```
 **/
function treeToHeaderContentTree(
  items: TreeItemData[],
  parentPath = '',
  showContent: boolean = false
): React.ReactNode[] {
  return items.map((item, index) => {
    const currentPath = parentPath ? `${parentPath}/${item.name}` : item.name;
    const hasContent = item.value && showContent;

    const elements: React.ReactNode[] = [<Header key={`header-${index}`}>{currentPath}</Header>];

    if (hasContent) {
      const pathExtension = path.extname(item.name).toLowerCase();
      const lang = pathExtension.length > 0 ? pathExtension.slice(1) : undefined;
      elements.push(
        <Code key={`content-${index}`} lang={lang} inline={false} whiteSpace="pre">
          {item.value}
        </Code>
      );
    }

    if (item.children && item.children.length > 0) {
      elements.push(
        <SubContent>{treeToHeaderContentTree(item.children, currentPath, showContent)}</SubContent>
      );
    }

    return elements;
  });
}

/*
 * Example:
 * - Project
 *   - src
 *     - index.js
 *   - package.json
 **/
function treeToNestedList(items: TreeItemData[], depth = 0): React.ReactNode {
  return (
    <List blankLine={false}>
      {items.map((item, index) => (
        <ListItem key={`item-${index}`}>
          {item.name}
          {item.children && item.children.length > 0 && treeToNestedList(item.children, depth + 1)}
        </ListItem>
      ))}
    </List>
  );
}

/*
 * Example:
 * .git/
 * .git/branches/
 * .git/config
 * ==> start .git/config <==
 * [core]
 *         repositoryformatversion = 0
 *         filemode = true
 *         bare = false
 *         logallrefupdates = true
 * ==> end .git/config <==
 *
 * Reference: https://askubuntu.com/questions/1095947/show-tree-of-directory-with-files-content
 */
function treeToPureTextContents(items: TreeItemData[], parentPath = ''): string {
  return items
    .map(item => {
      const currentPath = parentPath ? `${parentPath}/${item.name}` : item.name;
      const result: string[] = [];

      // Always output path
      result.push(currentPath);

      // If the item has content, format with start/end markers
      if (item.value) {
        result.push(`==> start ${currentPath} <==`);
        result.push(item.value);
        result.push(`==> end ${currentPath} <==`);
        result.push(''); // Add an extra blank line after content
      }

      if (item.children && item.children.length > 0) {
        result.push(treeToPureTextContents(item.children, currentPath));
      }

      return result;
    })
    .flat(Infinity)
    .join('\n');
}

/*
 * Example:
 * Project
 * ├── src
 * │   └── index.js
 * └── package.json
 **/
function treeToBoxDrawings(items: TreeItemData[], prefix = '', isRoot = true): string {
  const lines: string[] = [];

  items.forEach((item, index) => {
    const isLast = index === items.length - 1;

    if (isRoot && !item.children) {
      // This is a root-level item without children (category header)
      lines.push(`${item.name}`);
    } else if (isRoot) {
      // This is a root-level item with children (category header)
      lines.push(`${item.name}`);

      if (item.children && item.children.length > 0) {
        // Process children with box drawing characters
        const childPrefix = '';
        lines.push(treeToBoxDrawings(item.children, childPrefix, false));
      }
    } else {
      // This is a non-root item, add box drawing characters
      lines.push(`${prefix}${isLast ? '└── ' : '├── '}${item.name}`);

      if (item.children && item.children.length > 0) {
        // Calculate new prefix for children
        const childPrefix = prefix + (isLast ? '    ' : '│   ');
        lines.push(treeToBoxDrawings(item.children, childPrefix, false));
      }
    }
  });

  return lines.join('\n');
}

// Function to convert tree items to a nested object for JSON/YAML output
function treeItemsToObject(items: TreeItemData[], showContent: boolean = false): any {
  return items.reduce((obj, item) => {
    if (item.children && item.children.length > 0) {
      obj[item.name] = treeItemsToObject(item.children, showContent);
    } else if (item.value && showContent) {
      obj[item.name] = item.value;
    } else {
      obj[item.name] = null;
    }
    return obj;
  }, {} as any);
}

/**
 * Renders a tree structure in various formats.
 *
 * @param {'markdown'|'html'|'json'|'yaml'|'text'|'xml'} syntax - The output syntax to use for rendering the tree
 * @param {TreeItemData[]} items - Array of tree items to render
 * @param {boolean} showContent - Whether to show content values of tree items
 *
 * @example
 * ```xml
 * <Tree items={treeData} syntax="markdown" showContent={true} />
 * ```
 */
export const Tree = component('Tree')((props: TreeProps) => {
  const presentation = computeSyntaxContext(props);
  const { items, showContent, ...others } = props;
  if (presentation === 'serialize') {
    const object = treeItemsToObject(items, showContent);
    return <Object data={object} {...others} />;
  } else if (presentation === 'free') {
    if (showContent) {
      const pureText = treeToPureTextContents(items);
      return (
        <Text whiteSpace="pre" {...others}>
          {pureText}
        </Text>
      );
    } else {
      const boxDrawings = treeToBoxDrawings(items);
      return (
        <Text whiteSpace="pre" {...others}>
          {boxDrawings}
        </Text>
      );
    }
  } else {
    if (showContent) {
      return <Text {...others}>{treeToHeaderContentTree(items, '', showContent)}</Text>;
    } else {
      return <List {...others}>{treeToNestedList(items)}</List>;
    }
  }
});

function readDirectoryToTreeItems(
  dirPath: string,
  maxDepth: number,
  currentDepth: number,
  showContent: boolean,
  filter?: RegExp
): TreeItemData | null {
  const name = path.basename(dirPath);

  if (currentDepth >= maxDepth) {
    return { name };
  }

  try {
    const stats = fs.statSync(dirPath);

    if (!stats.isDirectory()) {
      // For files, apply filter immediately
      if (filter && !filter.test(name)) {
        return null;
      }
      return { name };
    }

    // For directories, process children first
    const children: TreeItemData[] = [];
    const entries = fs.readdirSync(dirPath, { withFileTypes: true }).sort((a, b) => {
      // Directories first, then files
      if (a.isDirectory() && !b.isDirectory()) {
        return -1;
      }
      if (!a.isDirectory() && b.isDirectory()) {
        return 1;
      }
      return a.name.localeCompare(b.name);
    });

    for (const entry of entries) {
      const entryPath = path.join(dirPath, entry.name);
      
      if (entry.isDirectory()) {
        // For directories, recursively process and check if it has any matching children
        const directoryItem = readDirectoryToTreeItems(entryPath, maxDepth, currentDepth + 1, showContent, filter);
        if (directoryItem && (directoryItem.children || !filter)) {
          children.push(directoryItem);
        }
      } else {
        // For files, check if they match the filter
        if (filter && !filter.test(entry.name)) {
          continue;
        }
        
        if (showContent) {
          // TODO: support other file types.
          const content = fs.readFileSync(entryPath, 'utf-8');
          children.push({ name: entry.name, value: content });
        } else {
          children.push({ name: entry.name });
        }
      }
    }

    // If we have a filter and no children matched, return null
    if (filter && children.length === 0) {
      return null;
    }

    return {
      name,
      children: children.length > 0 ? children : undefined
    };
  } catch (error) {
    throw new Error(`Error reading directory ${dirPath}: ${error}`);
  }
}

export interface FolderProps extends PropsSyntaxBase {
  src?: string;
  data?: TreeItemData[];
  filter?: string | RegExp;
  maxDepth?: number;
  showContent?: boolean;
}

/**
 * Displays a directory structure as a tree.
 *
 * @param {'markdown'|'html'|'json'|'yaml'|'text'|'xml'} syntax - The output syntax of the content.
 * @param {string} src - The source directory path to display.
 * @param {TreeItemData[]} data - Alternative to src, directly provide tree data structure.
 * @param {RegExp|string} filter - A regular expression to filter files.
 *   The regex is applied to the folder names and file names (not the full path).
 *   Directories are included by default unless all of their nested content is filtered out.
 *   When filter is on, empty directories will not be shown.
 * @param {number} maxDepth - Maximum depth of directory traversal. Default is 3.
 * @param {boolean} showContent - Whether to show file contents. Default is false.
 *
 * @example
 * To display a directory structure with a filter for Python files:
 * ```xml
 * <folder src="project_dir" filter=".*\.py$" maxDepth="3" />
 * ```
 */
export const Folder = component('Folder')((props: FolderProps) => {
  const { src, data, filter, showContent, maxDepth = 3, ...others } = props;

  let treeData: TreeItemData[] = [];

  if (data) {
    treeData = data;
  } else if (src) {
    const resolvedPath = expandRelative(src);
    const filterRegex = filter
      ? typeof filter === 'string'
        ? new RegExp(filter)
        : filter
      : undefined;

    try {
      const folderData = readDirectoryToTreeItems(
        resolvedPath,
        maxDepth ?? 3,
        0,
        showContent ?? false,
        filterRegex
      );
      
      if (folderData) {
        // If we got results, add them to the tree
        treeData = folderData.children || [];
        // Add the root name as the first item
        treeData = [{ name: path.basename(resolvedPath), children: treeData }];
      } else {
        // If we got null result (everything was filtered out), return empty tree
        treeData = [{ name: path.basename(resolvedPath) }];
      }
    } catch (error) {
      throw new Error(`Error processing folder ${src}: ${error}`);
    }
  } else {
    throw new Error('Either src or data must be provided');
  }

  return <Tree items={treeData} showContent={showContent} {...others} />;
});



================================================
FILE: packages/poml/components/utils.tsx
================================================
import * as React from 'react';
import { component, ReadError, trimChildrenWhiteSpace } from 'poml/base';
import {
  PropsSyntaxAny,
  Text,
  Paragraph,
  Header,
  Bold,
  computeSyntaxContext,
  SubContent,
  Newline,
  Inline
} from 'poml/essentials';

export interface BaseCaptionedParagraphProps extends PropsSyntaxAny {
  captionSerialized?: string;
  captionStyle?: 'header' | 'bold' | 'plain' | 'hidden';
  captionTextTransform?: 'upper' | 'lower' | 'capitalize' | 'none';
  captionEnding?: 'colon' | 'newline' | 'colon-newline' | 'none';
  captionTailingSpace?: boolean;
}

interface CaptionedParagraphProps extends BaseCaptionedParagraphProps {
  caption: string;
}

// Helper components for caption text.
// Try not to use it in syntaxes other than markup.
const CaptionText = component('CaptionText')((props: CaptionedParagraphProps) => {
  const {
    caption,
    captionTextTransform = 'none',
    captionStyle = 'header',
    captionEnding,
    ...others
  } = props;
  let captionText = caption;
  switch (captionTextTransform) {
    case 'upper':
      captionText = captionText.toUpperCase();
      break;
    case 'lower':
      captionText = captionText.toLowerCase();
      break;
    case 'capitalize':
      captionText =
        captionText.length >= 1
          ? captionText.charAt(0).toUpperCase() + captionText.slice(1)
          : captionText;
      break;
    case 'none':
      break;
    default:
      throw ReadError.fromProps(
        `Unsupported caption text transform: ${captionTextTransform}`,
        others
      );
  }
  const computedCaptionEnding =
    captionEnding === undefined
      ? captionStyle === 'bold' || captionStyle === 'plain'
        ? 'colon'
        : 'none'
      : captionEnding;
  if (computedCaptionEnding.includes('colon')) {
    return <>{captionText}:</>;
  } else {
    return <>{captionText}</>;
  }
});

export const Caption = component('Caption', {
  requiredProps: ['caption']
})((props: CaptionedParagraphProps) => {
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    const {
      caption,
      captionStyle = 'header',
      captionEnding,
      captionTailingSpace,
      ...others
    } = props;
    if (captionStyle === 'header') {
      return (
        <Header {...others}>
          <CaptionText
            caption={caption}
            captionStyle={captionStyle}
            captionEnding={captionEnding}
            {...others}
          />
        </Header>
      );
    } else if (captionStyle === 'bold') {
      const result = (
        <Bold {...others}>
          <CaptionText
            caption={caption}
            captionStyle={captionStyle}
            captionEnding={captionEnding}
            {...others}
          />
        </Bold>
      );
      if (captionTailingSpace === undefined || captionTailingSpace) {
        if (captionEnding?.includes('newline')) {
          return (
            <>
              {result}
              <Newline />
            </>
          );
        } else {
          return <>{result} </>;
        }
      } else {
        return result;
      }
    } else if (captionStyle === 'plain') {
      const result = (
        <Inline>
          <CaptionText
            caption={caption}
            captionStyle={captionStyle}
            captionEnding={captionEnding}
            {...others}
          />
        </Inline>
      );
      if (captionTailingSpace === undefined || captionTailingSpace) {
        if (captionEnding?.includes('newline')) {
          return (
            <>
              {result}
              <Newline />
            </>
          );
        } else {
          return <>{result} </>;
        }
      } else {
        return result;
      }
    } else {
      return null;
    }
  } else {
    // this should seldom happen
    const { caption, captionSerialized, name, type, ...others } = props;
    if (presentation === 'serialize') {
      return (
        <Text name={name} type={type} {...others}>
          {captionSerialized}
        </Text>
      );
    } else {
      return <Text>{caption}</Text>;
    }
  }
});

/**
 * CaptionedParagraph (`<cp>` for short) creates a paragraph with a customized caption title.
 *
 * @param caption - The title or label for the paragraph. Required.
 * @param captionSerialized - The serialized version of the caption when using "serializer" syntaxes.
 *   By default, it's same as `caption`.
 * @param {'header'|'bold'|'plain'|'hidden'} captionStyle - Determines the style of the caption,
 * applicable only for "markup" syntaxes. Default is `header`.
 * @param {'upper'|'level'|'capitalize'|'none'} captionTextTransform -
 * Specifies text transformation for the caption, applicable only for "markup" syntaxes. Default is `none`.
 * @param {'colon'|'newline'|'colon-newline'|'none'} captionEnding - A caption can ends with a colon, a newline or simply nothing.
 * If not specified, it defaults to `colon` for `bold` or `plain` captionStyle, and `none` otherwise.
 *
 * @see {@link Paragraph} for other props available.
 *
 * @example
 * ```xml
 * <cp caption="Constraints">
 *   <list>
 *     <item>Do not exceed 1000 tokens.</item>
 *     <item>Please use simple words.</item>
 *   </list>
 * </cp>
 * ```
 */
export const CaptionedParagraph = component('CaptionedParagraph', {
  aliases: ['cp'],
  requiredProps: ['caption']
})((props: React.PropsWithChildren<CaptionedParagraphProps>) => {
  const presentation = computeSyntaxContext(props);
  if (presentation === 'markup') {
    const { captionStyle = 'header', children, ...others } = props;
    const trimmedChildren = trimChildrenWhiteSpace(children, props);
    const hasContent = React.Children.count(trimmedChildren) > 0;
    if (captionStyle === 'header') {
      return (
        <Paragraph {...others}>
          <Caption captionStyle={captionStyle} captionTailingSpace={hasContent} {...others} />
          <SubContent>{trimmedChildren}</SubContent>
        </Paragraph>
      );
    } else if (captionStyle === 'bold' || captionStyle === 'plain') {
      return (
        <Paragraph {...others}>
          <Caption captionStyle={captionStyle} captionTailingSpace={hasContent} {...others} />
          {trimmedChildren}
        </Paragraph>
      );
    } else if (captionStyle === 'hidden') {
      return <Paragraph {...others}>{trimmedChildren}</Paragraph>;
    } else {
      throw ReadError.fromProps(`Unsupported caption style: ${captionStyle}`, props);
    }
  } else if (presentation === 'serialize') {
    const { children, captionSerialized, caption, ...others } = props;
    return (
      <Text name={captionSerialized || caption} {...others}>
        {children}
      </Text>
    );
  } else {
    const { children } = props;
    return <Text>{children}</Text>;
  }
});

export const parsePythonStyleSlice = (slice: string, totalLength: number): [number, number] => {
  // slices could be like :3, 3:5, 5:, 5:-1
  if (slice === ':') {
    return [0, totalLength];
  } else if (slice.endsWith(':')) {
    return [parseInt(slice.slice(0, -1)), totalLength];
  } else if (slice.startsWith(':')) {
    return [0, parseInt(slice.slice(1))];
  } else if (slice.includes(':')) {
    const [start, end] = slice.split(':').map(Number);
    return [start, end];
  } else {
    const index = parseInt(slice);
    return [index, index + 1];
  }
};



================================================
FILE: packages/poml/components/webpage.tsx
================================================
import { PropsSyntaxBase } from 'poml/essentials';
import * as React from 'react';
import fs from '../util/fs';
import { component, expandRelative, useWithCatch } from 'poml/base';
import { Text } from 'poml/essentials';
import * as cheerio from 'cheerio';
import { htmlToPoml } from './document';

export interface WebpageProps extends PropsSyntaxBase {
  src?: string;
  url?: string;
  buffer?: string | Buffer;
  base64?: string;
  extractText?: boolean;
  selector?: string;
}

async function fetchWebpage(url: string): Promise<string> {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.text();
  } catch (error) {
    throw new Error(`Error fetching webpage from ${url}: ${error}`);
  }
}

async function extractTextFromHtml(html: string, selector?: string): Promise<string> {
  const $ = cheerio.load(html);

  // Remove scripts and styles
  $('script').remove();
  $('style').remove();

  // If selector is provided, extract content from matching elements
  if (selector) {
    try {
      const elements = $(selector);
      if (elements.length === 0) {
        return `No elements found matching selector: ${selector}`;
      }

      return elements
        .map((_, el) => $(el).text())
        .get()
        .join('\n\n');
    } catch (error) {
      throw new Error(`Error with selector "${selector}": ${error}`);
    }
  }

  // Get text from body, preserving some structure
  return $('body').text().trim() || '';
}

async function processWebpage(props: WebpageProps): Promise<React.ReactElement> {
  const { src, url, buffer, extractText = false, selector } = props;

  let html: string;

  if (url) {
    html = await fetchWebpage(url);
  } else if (src) {
    const filePath = expandRelative(src);
    html = fs.readFileSync(filePath, 'utf-8');
  } else if (buffer) {
    if (typeof buffer === 'string') {
      html = buffer;
    } else {
      html = buffer.toString('utf-8');
    }
  } else {
    throw new Error('Either url, src, or buffer must be provided');
  }

  if (extractText) {
    const text = await extractTextFromHtml(html, selector);
    return <Text whiteSpace="pre">{text}</Text>;
  } else {
    // Use the htmlToPoml function to convert HTML to POML components
    const $ = cheerio.load(html);
    let content: React.ReactElement;

    if (selector) {
      const selected = $(selector);
      if (selected.length === 0) {
        return <Text>No elements found matching selector: {selector}</Text>;
      }
      content = htmlToPoml(selected, $, props);
    } else {
      content = htmlToPoml($('body'), $, props);
    }

    return content;
  }
}

/**
 * Displays content from a webpage.
 *
 * @param {string} url - The URL of the webpage to fetch and display.
 * @param {string} src - Local file path to an HTML file to display.
 * @param {string|Buffer} buffer - HTML content as string or buffer.
 * @param {string} base64 - Base64 encoded HTML content.
 * @param {boolean} extractText - Whether to extract plain text content (true) or convert HTML to structured POML (false). Default is false.
 * @param {string} selector - CSS selector to extract specific content from the page (e.g., "article", ".content", "#main"). Default is "body".
 *
 * @see {@link Inline} for other props available.
 *
 * @example
 * Display content from a URL:
 * ```xml
 * <webpage url="https://example.com" />
 * ```
 *
 * Extract only specific content using a selector:
 * ```xml
 * <webpage url="https://example.com" selector="main article" />
 * ```
 *
 * Convert HTML to structured POML components:
 * ```xml
 * <webpage url="https://example.com" extractText="false" />
 * ```
 */
export const Webpage = component('Webpage', { asynchorous: true })((
  props: WebpageProps
) => {
  let { src, url, buffer, base64, extractText, selector, ...others } = props;
  if (base64) {
    if (buffer !== undefined) {
      throw new Error('Either buffer or base64 should be provided, not both.');
    }
    buffer = Buffer.from(base64, 'base64');
  }
  const content = useWithCatch(processWebpage({ ...props, buffer: buffer }), others);
  return <Text {...others}>{content ?? null}</Text>;
});



================================================
FILE: packages/poml/reader/base.tsx
================================================
import * as React from 'react';

import { Segment } from './segment';
import { PomlToken } from 'poml/file';

export interface ReaderOptions {
  trim?: boolean;
  autoAddPoml?: boolean;
  crlfToLf?: boolean;
}

export interface PomlContext {
  variables: { [key: string]: any }; // For {{ substitutions }} and <let> (Read/Write)
  texts: { [key: string]: React.ReactElement }; // Maps TEXT_ID to content for <text> replacement (Read/Write)
  stylesheet: { [key: string]: string }; // Merged styles from all <meta> tags (Read-Only during render)
  minimalPomlVersion?: string;      // From <meta> (Read-Only)
  sourcePath: string;                // File path for resolving includes (Read-Only)
}

export class Reader {
  private segment: Segment;
  private options: ReaderOptions;

  constructor(segment: Segment, options?: ReaderOptions) {
    this.segment = segment;
    this.options = options || {};
  }

  public react(context?: PomlContext): React.ReactElement {
    throw new Error('Method react() not implemented');
  }

  public getHoverToken(offset: number): PomlToken | undefined {
    throw new Error('Method getHoverToken() not implemented');
  }

  public getCompletions(offset: number): PomlToken[] {
    throw new Error('Method getCompletions() not implemented');
  }
}



================================================
FILE: packages/poml/reader/index.tsx
================================================
import { Reader } from './base';

class DispatchReader extends Reader {
}



================================================
FILE: packages/poml/reader/meta.ts
================================================
import { Reader } from './base';

class MetaReader extends Reader {
}


================================================
FILE: packages/poml/reader/poml.tsx
================================================
import { Reader } from './base';

export class PomlReader extends Reader {
}


================================================
FILE: packages/poml/reader/segment.ts
================================================
export interface Segment {
  // Unique ID for caching and React keys
  id: string;
  kind: 'META' | 'TEXT' | 'POML';
  start: number;
  end: number;
  // The raw string content of the segment
  content: string;
  // The path to the file or resource this segment belongs to
  path?: string;
  // Reference to the parent segment
  parent?: Segment;
  // Nested segments (e.g., a POML block within text)
  children: Segment[];
  // For POML segments, the name of the root tag (e.g., 'task')
  tagName?: string;
}

export function createSegments(content: string, path?: string): Segment[] {
  throw new Error('createSegments is not implemented yet');
}



================================================
FILE: packages/poml/reader/text.tsx
================================================
import { Reader } from './base';

export class PureTextReader extends Reader {
}



================================================
FILE: packages/poml/tests/base.test.tsx
================================================
import * as React from 'react';
import {
  component,
  StyleSheetProvider,
  PomlComponent,
  unregisterComponent,
  listComponents,
  findComponentByAlias,
  findComponentByAliasOrUndefined,
  BufferCollection
} from 'poml/base';
import { read } from 'poml';
import { describe, expect, test } from '@jest/globals';

test('component', async () => {
  const App = component('App', ['app1'])(() => {
    return <div>123</div>;
  });
  expect(await read(<App />)).toBe('<div>123</div>');
  unregisterComponent('App');
});

test('parameters', () => {
  expect(
    findComponentByAliasOrUndefined('question')!
      .mro()
      .map(c => c.name)
  ).toEqual(['Paragraph', 'Text']);

  expect(
    findComponentByAliasOrUndefined('table')!
      .parameters()
      .map(p => p.name)
  ).toEqual([
    'syntax',
    'records',
    'columns',
    'src',
    'parser',
    'selectedColumns',
    'selectedRecords',
    'maxRecords',
    'maxColumns',
    'className',
    'speaker',
    'writerOptions'
  ]);
});

test('computeStylesLegacy', () => {
  const AppInner = (props: any) => {
    const { component, customStyle, expectStyle, children } = props;
    const fakeComponent = new PomlComponent(component, undefined, {
      aliases: [component],
      unwantedProps: [],
      requiredProps: [],
      applyStyleSheet: true,
      asynchorous: false
    });
    const style = fakeComponent.style(customStyle);
    expect(style).toEqual(expectStyle);
    if (children) {
      return <>{children}</>;
    } else {
      return <p>hahaha</p>;
    }
  };
  const App = ({ component, customStyle, expectStyle, children }: any) => {
    const stylesheet = {
      '*': {
        color: 'red'
      },
      table: {
        color: 'blue',
        header: {
          color: 'green'
        }
      }
    };
    if (children) {
      return (
        <StyleSheetProvider stylesheet={stylesheet}>
          <AppInner component={component} customStyle={customStyle} expectStyle={expectStyle}>
            {children}
          </AppInner>
        </StyleSheetProvider>
      );
    } else {
      return (
        <StyleSheetProvider stylesheet={stylesheet}>
          <AppInner component={component} customStyle={customStyle} expectStyle={expectStyle} />
        </StyleSheetProvider>
      );
    }
  };

  read(
    <App
      component="table"
      customStyle={{ padding: 10 }}
      expectStyle={{ color: 'blue', padding: 10, header: { color: 'green' } }}
    />
  );
  read(
    <App
      component="header"
      customStyle={{ padding: 10 }}
      expectStyle={{ color: 'red', padding: 10 }}
    />
  );
  read(
    <App
      component="table"
      customStyle={{ color: 'white' }}
      expectStyle={{ color: 'white', header: { color: 'green' } }}
    />
  );
  read(
    <App
      component="base"
      customStyle={{ padding: 10 }}
      expectStyle={{ color: 'red', padding: 10 }}
    />
  );

  read(
    <App
      component="table"
      customStyle={{ padding: 10 }}
      expectStyle={{ color: 'blue', padding: 10, header: { color: 'green' } }}
    >
      <App
        component="header"
        customStyle={{ padding: 20 }}
        expectStyle={{ color: 'red', padding: 20 }}
      />
    </App>
  );
});

test('computeStylesNew', () => {
  const component = new PomlComponent('table', undefined, {
    aliases: ['table'],
    unwantedProps: [],
    requiredProps: [],
    applyStyleSheet: true,
    asynchorous: false
  });
  const stylesheet = {
    '*': {
      padding: 20
    },
    '.layout': {
      padding: 30,
      margin: 5
    },
    '.layout2': {
      padding: 40
    },
    '.layout .layout2': {
      margin: 10,
      color: 'blue'
    },
    table: {
      color: 'red',
      margin: 20
    },
    'table .layout': {
      color: 'green'
    }
  };
  expect(component.style({ className: 'layout', padding: 10 }, stylesheet)).toEqual({
    padding: 10,
    margin: 5,
    color: 'green'
  });
  expect(component.style({ className: 'layout layout2', padding: 10 }, stylesheet)).toEqual({
    padding: 10,
    margin: 10,
    color: 'blue'
  });
  expect(component.style({ padding: 10 }, stylesheet)).toEqual({
    padding: 10,
    margin: 20,
    color: 'red'
  });
  expect(component.style({ children: component }, stylesheet)).toEqual({
    children: component,
    padding: 20,
    margin: 20,
    color: 'red'
  });
});

test('calculateSize recursive', () => {
  BufferCollection.clear();
  const obj = { data: { arr: [1, 2, 'abc'] }, extra: Buffer.alloc(4) };
  BufferCollection.set('obj', obj);
  const inst = (BufferCollection as any).instance as any;
  const size = inst.buffers.get('obj').size;
  expect(size).toBe(23);
});



================================================
FILE: packages/poml/tests/components.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test, beforeAll } from '@jest/globals';

import { poml, read, write } from 'poml';
import { readDocx, readDocxFromPath, readPdfFromPath, readTxtFromPath, Document } from 'poml/components/document';
import { Tree, TreeItemData, Folder } from 'poml/components/tree';
import { Webpage } from 'poml/components/webpage';
import { readFileSync, mkdirSync, existsSync } from '../util/fs';
import { ErrorCollection, BufferCollection } from 'poml/base';
import * as path from 'path';

describe('document', () => {
  test('pdf', async () => {
    const document = await readPdfFromPath(__dirname + '/assets/pdfLatexImage.pdf');
    expect((document.props as any).children).toMatch(/1 Your Chapter\nLorem ipsum dolor sit amet/g);

    const document2 = await readPdfFromPath(__dirname + '/assets/pdfLatexImage.pdf', {
      selectedPages: '1:'
    });
    expect((document2.props as any).children).toMatch('');

    const document3 = await readPdfFromPath(__dirname + '/assets/pdfLatexImage.pdf', {
      selectedPages: ':1'
    });
    expect((document3.props as any).children).toMatch('1 Your Chapter\nLorem ipsum dolor sit amet');
  });

  test('docx', async () => {
    const document = await readDocxFromPath(__dirname + '/assets/sampleWord.docx');
    expect((document.props as any).children.length).toEqual(26);
  });

  test('txt', async () => {
    const document = await poml(<Document buffer={'123\n456'} />);
    expect(document).toBe('123\n456');

    const documentJson = await poml(
      <Document src={__dirname + '/assets/peopleList.json'} parser="txt" />
    );
    expect(documentJson).toBe(readFileSync(__dirname + '/assets/peopleList.json', 'utf-8'));
  });

  test('write result', async () => {
    const result = await poml(<Document src={__dirname + '/assets/sampleWord.docx'} />);
    expect(result.length).toEqual(5);
    expect((result[3] as any).base64).toBeTruthy();
    expect(result[4]).toMatch(
      /without any merged cells:\n\n\| Screen Reader \| Responses \| Share \|\n/g
    );
  });

  test('docx from base64', async () => {
    const buffer = readFileSync(__dirname + '/assets/sampleWord.docx');
    const base64 = buffer.toString('base64');
    const result = await poml(<Document base64={base64} parser="docx" />);
    expect(result[4]).toMatch(
      /without any merged cells:\n\n\| Screen Reader \| Responses \| Share \|\n/g
    );
  });

  test('buffer caching', async () => {
    const filePath = path.join(__dirname, 'assets', 'peopleList.json');
    BufferCollection.clear();
    await readTxtFromPath(filePath);
    const key = `content://${path.resolve(filePath)}`;
    const first = BufferCollection.get<{ value: Buffer; mtime: number }>(key);
    expect(first?.value).toBeInstanceOf(Buffer);

    await readTxtFromPath(filePath);
    const second = BufferCollection.get<{ value: Buffer; mtime: number }>(key);
    expect(second?.mtime).toBe(first?.mtime);
    expect(second?.value).toBe(first?.value);
  });

  test('skip cache when over limit', () => {
    BufferCollection.clear();
    const inst = (BufferCollection as any).instance as any;
    const originalLimit = inst.limit;
    inst.limit = 10;
    BufferCollection.set('big', { data: 'a'.repeat(50) });
    expect(BufferCollection.get('big')).toBeUndefined();
    inst.limit = originalLimit;
  });
});

describe('message', () => {
  test('msg', async () => {
    const text =
      "<poml><system-msg>start</system-msg><ai-msg>hello</ai-msg><human-msg speaker='human'>yes</human-msg></poml>";
    const element = await read(text);
    expect(write(element, { speaker: true })).toStrictEqual([
      { speaker: 'system', content: 'start' },
      { speaker: 'ai', content: 'hello' },
      { speaker: 'human', content: 'yes' }
    ]);
  });

  test('conversation', async () => {
    const text = `<poml>
      <conversation messages="{{[{ speaker: 'human', content: 'What is the capital of France?' }, { speaker: 'ai', content: 'Paris' }]}}" />
    </poml>`;
    const element = await read(text);
    expect(write(element, { speaker: true })).toStrictEqual([
      { speaker: 'human', content: 'What is the capital of France?' },
      { speaker: 'ai', content: 'Paris' }
    ]);
  });

  test('conversation selected', async () => {
    const text = `<poml>
      <conversation messages="{{[{ speaker: 'system', content: 'Be brief and clear in your responses' }, { speaker: 'human', content: 'What is the capital of France?' }, { speaker: 'ai', content: 'Paris' }]}}" selectedMessages="-1:" />
    </poml>`;
    const element = await read(text);
    expect(write(element, { speaker: true })).toStrictEqual([{ speaker: 'ai', content: 'Paris' }]);
  });

  test('conversation with image', async () => {
    const imagePath = __dirname + '/assets/tomCat.jpg';
    const text = `<poml>
      <let name="imagedata" src="${imagePath}" type="buffer" />
      <conversation messages='{{[{"speaker":"human","content":[{"type":"image/jpg","base64":imagedata.toString("base64")}]}]}}' />
    </poml>`;
    ErrorCollection.clear();
    const element = await read(text);
    expect(ErrorCollection.empty()).toBe(true);
    const result = write(element, { speaker: true });
    expect(result.length).toBe(1);
    expect((result[0].content as any)[0].type).toBe('image/jpg');
    expect((result[0].content as any)[0].base64).toBeTruthy();
  });
});

describe('tree', () => {
  const treeData: TreeItemData[] = [
    {
      name: 'Data Grid',
      children: [
        { name: 'data-grid' },
        { name: 'data-grid-pro', value: 'Content Grid Pro' },
        { name: 'data-grid-premium' }
      ]
    },
    {
      name: 'Date and Time Pickers',
      children: [
        { name: 'date-pickers', value: 'Content Date Pickers' },
        { name: 'date-pickers-pro' }
      ]
    },
    {
      name: 'Tree.view',
      value: 'Content Tree View'
    }
  ];

  const backticks = '```';

  const treeMarkdownWithContent = `# Data Grid

## Data Grid/data-grid

## Data Grid/data-grid-pro

${backticks}
Content Grid Pro
${backticks}

## Data Grid/data-grid-premium

# Date and Time Pickers

## Date and Time Pickers/date-pickers

${backticks}
Content Date Pickers
${backticks}

## Date and Time Pickers/date-pickers-pro

# Tree.view

${backticks}view
Content Tree View
${backticks}`;

  const treeMarkdownWithoutContent = `- Data Grid
  - data-grid
  - data-grid-pro
  - data-grid-premium
- Date and Time Pickers
  - date-pickers
  - date-pickers-pro
- Tree.view`;

  const treeTextWithContent = `Data Grid
Data Grid/data-grid
Data Grid/data-grid-pro
==> start Data Grid/data-grid-pro <==
Content Grid Pro
==> end Data Grid/data-grid-pro <==

Data Grid/data-grid-premium
Date and Time Pickers
Date and Time Pickers/date-pickers
==> start Date and Time Pickers/date-pickers <==
Content Date Pickers
==> end Date and Time Pickers/date-pickers <==

Date and Time Pickers/date-pickers-pro
Tree.view
==> start Tree.view <==
Content Tree View
==> end Tree.view <==
`;

  // with box drawings
  const treeTextWithoutContent = `Data Grid
├── data-grid
├── data-grid-pro
└── data-grid-premium
Date and Time Pickers
├── date-pickers
└── date-pickers-pro
Tree.view`;

  const treeYamlWithoutContent = `Data Grid:
  data-grid: null
  data-grid-pro: null
  data-grid-premium: null
Date and Time Pickers:
  date-pickers: null
  date-pickers-pro: null
Tree.view: null`;

  const testJsonWithContent = `{
  "Data Grid": {
    "data-grid": null,
    "data-grid-pro": "Content Grid Pro",
    "data-grid-premium": null
  },
  "Date and Time Pickers": {
    "date-pickers": "Content Date Pickers",
    "date-pickers-pro": null
  },
  "Tree.view": "Content Tree View"
}`;

  test('tree markdown with content', async () => {
    const markup = <Tree items={treeData} syntax="markdown" showContent={true} />;
    const result = await poml(markup);
    expect(result).toBe(treeMarkdownWithContent);
  });

  test('tree markdown without content', async () => {
    const markup = <Tree items={treeData} syntax="markdown" />;
    const result = await poml(markup);
    expect(result).toBe(treeMarkdownWithoutContent);
  });

  test('tree text with content', async () => {
    const markup = <Tree items={treeData} syntax="text" showContent={true} />;
    const result = await poml(markup);
    expect(result).toBe(treeTextWithContent);
  });

  test('tree text without content', async () => {
    const markup = <Tree items={treeData} syntax="text" />;
    const result = await poml(markup);
    expect(result).toBe(treeTextWithoutContent);
  });

  test('tree yaml without content', async () => {
    const markup = <Tree items={treeData} syntax="yaml" />;
    const result = await poml(markup);
    expect(result).toBe(treeYamlWithoutContent);
  });

  test('tree json with content', async () => {
    const markup = <Tree items={treeData} syntax="json" showContent={true} />;
    const result = await poml(markup);
    expect(result).toBe(testJsonWithContent);
  });
});

describe('folder', () => {
  const directory = __dirname + '/assets/directory';
  const content123jsx = readFileSync(directory + '/anotherdirectory/123.jsx', 'utf-8');
  const content456cpp = readFileSync(directory + '/anotherdirectory/456.cpp', 'utf-8');
  const contentNestedFileTxt = readFileSync(
    directory + '/nested1/nested2/nested3/nested5/nestedFile.txt',
    'utf-8'
  );
  const contentIgnoreplease = readFileSync(
    directory + '/nested1/nested2/nested4/.ignoreplease',
    'utf-8'
  );
  const contentIgnoremeplease = readFileSync(directory + '/.ignoremeplease', 'utf-8');

  // Create directory structure if it doesn't exist
  beforeAll(() => {
    const directories = [
      directory,
      path.join(directory, 'anotherdirectory'),
      path.join(directory, 'nested1'),
      path.join(directory, 'nested1', 'nested2'),
      path.join(directory, 'nested1', 'nested2', 'nested3'),
      path.join(directory, 'nested1', 'nested2', 'nested3', 'nested5'),
      path.join(directory, 'nested1', 'nested2', 'nested4'),
      path.join(directory, 'nested1', 'nested6')
    ];

    // Create each directory if it doesn't exist
    directories.forEach(dir => {
      if (!existsSync(dir)) {
        mkdirSync(dir, { recursive: true });
      }
    });
  });

  test('basic folder structure', async () => {
    const markup = <Folder src={directory} syntax="text" maxDepth={10} />;
    const result = await poml(markup);

    expect(result).toBe(`directory
├── anotherdirectory
│   ├── 123.jsx
│   └── 456.cpp
├── nested1
│   ├── nested2
│   │   ├── nested3
│   │   │   └── nested5
│   │   │       └── nestedFile.txt
│   │   └── nested4
│   │       └── .ignoreplease
│   └── nested6
└── .ignoremeplease`);
  });

  test('test file contents', async () => {
    const markup = <Folder src={directory} syntax="json" maxDepth={10} showContent={true} />;
    const result = await poml(markup);
    expect(JSON.parse(result as string)).toStrictEqual({
      directory: {
        anotherdirectory: {
          '123.jsx': content123jsx,
          '456.cpp': content456cpp
        },
        nested1: {
          nested2: {
            nested3: {
              nested5: {
                'nestedFile.txt': contentNestedFileTxt,
              }
            },
            nested4: {
              '.ignoreplease': contentIgnoreplease
            }
          },
          nested6: null
        },
        '.ignoremeplease': contentIgnoremeplease
      }
    });
  });

  test('folder with maxDepth=1', async () => {
    const markup = <Folder src={directory} maxDepth={1} syntax="markdown" showContent={true} />;
    const result = await poml(markup);

    const backticks = '```';
    expect((result as string).replace(/\r\n/g, '\n')).toBe(`# directory

## directory/anotherdirectory

## directory/nested1

## directory/.ignoremeplease

${backticks}
abcde
fhijk
${backticks}`.replace(/\r\n/g, '\n'));
  });

  test('folder with maxDepth=2', async () => {
    const markup = <Folder src={directory} maxDepth={2} syntax="xml" showContent={false} />;
    const result = await poml(markup);

    expect(result).toBe(`<directory>
  <anotherdirectory>
    <_123.jsx/>
    <_456.cpp/>
  </anotherdirectory>
  <nested1>
    <nested2/>
    <nested6/>
  </nested1>
  <_.ignoremeplease/>
</directory>`);
  });

  test('folder with filter=jsx', async () => {
    const markup = <Folder src={directory} filter={/.*\.jsx$/} syntax="text" maxDepth={4} />;
    const result = await poml(markup);

    // Using full text match with JSX filter
    expect(result).toBe(`directory
└── anotherdirectory
    └── 123.jsx`);
  });

  test('folder with filter not starting with dot', async () => {
    const markup = <Folder src={directory} filter={/^[^.].*$/} syntax="text" maxDepth={10} />;
    const result = await poml(markup);

    // Using a filter that excludes files starting with dot
    expect(result).toBe(`directory
├── anotherdirectory
│   ├── 123.jsx
│   └── 456.cpp
└── nested1
    └── nested2
        └── nested3
            └── nested5
                └── nestedFile.txt`);
  });

  test('folder with filter and maxDepth combined', async () => {
    const markup = <Folder src={directory} filter={/.*\.txt$/} maxDepth={3} syntax="text" />;
    const result = await poml(markup);

    expect(result).toBe(`directory`);
  });

  test('folder with different syntax (markdown)', async () => {
    const markup = <Folder src={directory} maxDepth={2} syntax="markdown" />;
    const result = await poml(markup);

    // Using full text match with markdown syntax
    expect(result).toBe(`- directory
  - anotherdirectory
    - 123.jsx
    - 456.cpp
  - nested1
    - nested2
    - nested6
  - .ignoremeplease`);
  });
});

describe('webpage', () => {
  const webpagePath = __dirname + '/assets/sampleWebpage.html';
  
  test('extracting text from HTML', async () => {
    const markup = <Webpage src={webpagePath} />;
    const result = await poml(markup);
    expect(result).toBe(`# Enter the main heading, usually the same as the title.

Be **bold** in stating your key points. Put them in a list: 

- The first item in your list
- The second item; *italicize* key words

Improve your image by including an image. 

Add a link to your favorite Web site.
Break up your page with a horizontal rule or two. 

Finally, link to another page in your own Web site.

© Wiley Publishing, 2011`);
  });
  
  test('using selector to extract specific content', async () => {
    const markup = <Webpage src={webpagePath} selector="ul" />;
    const result = await poml(markup);
    expect(result).toBe(`- The first item in your list
- The second item; *italicize* key words`);
  });
  
  test('selector with no matches', async () => {
    const markup = <Webpage src={webpagePath} selector=".non-existent-class" />;
    const result = await poml(markup);
    
    expect(result).toContain('No elements found matching selector: .non-existent-class');
  });
  
  test('extract text from HTML', async () => {
    const markup = <Webpage src={webpagePath} extractText={true} />;
    const result = await poml(markup);

    expect(result).toBe(`Enter the main heading, usually the same as the title.
Be bold in stating your key points. Put them in a list: 

The first item in your list
The second item; italicize key words

Improve your image by including an image. 

Add a link to your favorite Web site.
Break up your page with a horizontal rule or two. 

Finally, link to another page in your own Web site.

© Wiley Publishing, 2011`);
  });
  
  test('loading HTML from buffer', async () => {
    const htmlContent = readFileSync(webpagePath, 'utf-8');
    const markup = <Webpage buffer={htmlContent} selector="h1" syntax="html" />;
    const result = await poml(markup);

    expect(result).toContain('<h1>Enter the main heading, usually the same as the title.</h1>');
  });

  test('loading HTML from base64', async () => {
    const htmlContent = readFileSync(webpagePath, 'utf-8');
    const base64Content = Buffer.from(htmlContent).toString('base64');
    const markup = <Webpage base64={base64Content} selector="h1" syntax="html" />;
    const result = await poml(markup);

    expect(result).toContain('<h1>Enter the main heading, usually the same as the title.</h1>');
  });
});



================================================
FILE: packages/poml/tests/essentials.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test } from '@jest/globals';
import * as essentials from 'poml/essentials';
import { poml } from 'poml';

describe('essentials', () => {
  test('endToEnd', async () => {
    const markup = (
      <essentials.Text syntax="markdown">
        <essentials.Paragraph>Hello, world!</essentials.Paragraph>
        <essentials.Code inline={false}>c += 1</essentials.Code>
      </essentials.Text>
    );
    const result = await poml(markup);
    expect(result).toBe('Hello, world!\n\n```\nc += 1\n```');
  });

  test('data-obj', async () => {
    const markup = <essentials.Object data={{ name: 'world' }} />;
    const result = await poml(markup);
    expect(result).toBe('{\n  "name": "world"\n}');
  });

  test('image', async () => {
    const imagePath = __dirname + '/assets/tomCat.jpg';

    const markup = <essentials.Image src={imagePath} alt="example" />;
    const result = await poml(markup);
    expect(result.length).toBe(1);
    expect((result[0] as any).type).toBe('image/jpeg');
    expect((result[0] as any).base64).toBeTruthy();
    expect((result[0] as any).alt).toBe('example');

    const markupInsideText = (
      <essentials.Text syntax="markdown">
        <essentials.Image src={imagePath} />
      </essentials.Text>
    );
    const result2 = await poml(markupInsideText);
    expect(result2.length).toBe(1);
    expect((result2[0] as any).type).toBe('image/jpeg');
    expect((result2[0] as any).base64).toBeTruthy();
  });

  test('image markdown', async () => {
    const imagePath = __dirname + '/assets/tomCat.jpg';

    const markup = (
      <essentials.Text syntax="markdown">
        <essentials.Image src={imagePath} alt="example" syntax="markdown" />
      </essentials.Text>
    );
    const result = await poml(markup);
    expect(result).toBe('example');

    const syntaxViaStylesheet = `<poml><img src="${imagePath}" alt="example" /><stylesheet>{"image":{"syntax":"markdown"}}</stylesheet></poml>`;
    const result2 = await poml(syntaxViaStylesheet);
    expect(result2).toBe('example');
  });

  test('audio', async () => {
    const audioPath = __dirname + '/assets/audioThreeSeconds.mp3';
    const markup = <essentials.Audio src={audioPath} />;
    const result = await poml(markup);
    expect(result.length).toBe(1);
    expect((result[0] as any).type).toBe('audio/mpeg');
    expect((result[0] as any).base64).toBeTruthy();
  });

  test('writer options', async () => {
    const header = (
      <essentials.Header writerOptions={{ markdownBaseHeaderLevel: 3 }}>Header</essentials.Header>
    );
    const result = await poml(header);
    expect(result).toBe('### Header');
  });
});



================================================
FILE: packages/poml/tests/file.test.tsx
================================================
import { describe, expect, test } from '@jest/globals';
import { PomlFile } from 'poml/file';
import { read, write, poml } from 'poml';
import { ErrorCollection } from 'poml/base';

describe('stringToElement', () => {
  test('simple', async () => {
    const text = '<Markup.Paragraph>Hello, world!</Markup.Paragraph>';
    const element = new PomlFile(text).react();
    expect(await read(element)).toBe(
      '<env presentation=\"markup\" markup-lang=\"markdown\" original-start-index=\"0\" original-end-index=\"49\"><p original-start-index=\"0\" original-end-index=\"49\">Hello, world!</p></env>'
    );
  });

  test('space', async () => {
    const text =
      '<markup.paragraph><markup.header>hello\n\n</markup.header>\n\n\n<markup.bold>world</markup.bold>\n  </markup.paragraph>';
    const element = new PomlFile(text).react();
    expect((element.props as any).children.length).toBe(4);
    expect(await read(element)).toBe(
      '<env presentation=\"markup\" markup-lang=\"markdown\" original-start-index=\"0\" original-end-index=\"112\"><p original-start-index=\"0\" original-end-index=\"112\"><h level=\"1\" original-start-index=\"18\" original-end-index=\"55\">hello</h> <b original-start-index=\"59\" original-end-index=\"90\">world</b></p></env>'
    );
    expect(await read(element)).toBe(await read(text));
    expect(write(await read(element))).toBe('# hello\n\n**world**');
  });

  test('variable', async () => {
    const text = '<Markup.Paragraph> {{name}} </Markup.Paragraph>';
    const element = new PomlFile(text).react({ name: 'world' });
    expect(await read(element)).toBe(
      '<env presentation=\"markup\" markup-lang=\"markdown\" original-start-index=\"0\" original-end-index=\"46\"><p original-start-index=\"0\" original-end-index=\"46\">world</p></env>'
    );
  });

  test('list', async () => {
    ErrorCollection.clear();
    const text = '<list listStyle="decimal"><item>Do not have</item></list>';
    const element = new PomlFile(text).react();
    expect(write(await read(element))).toBe('1. Do not have');
  
    const textComplex = `<list listStyle="decimal">
    <item>Do not have</item>
    <item>true</item>
    <item><code inline="false" lang="cpp">world</code></item>
</list>`;
    const elementComplex = new PomlFile(textComplex).react();
    expect(write(await read(elementComplex))).toBe('1. Do not have\n2. true\n\n3. ```cpp\n   world\n   ```');
    expect(ErrorCollection.empty()).toBe(true);
  });

  test('variableObject', () => {
    const text = '<Markup.Header writerOptions="{{{markdownBaseHeaderLevel: 3}}}">hello</Markup.Header>';
    const element = new PomlFile(text).react();
    expect((element.props as any).writerOptions).toStrictEqual({ markdownBaseHeaderLevel: 3 });
  })

  test('attrVariable', () => {
    const text = '<Markup.Paragraph blankLine="{{true}}">hello</Markup.Paragraph>';
    const element = new PomlFile(text).react();
    expect((element.props as any).blankLine).toBe(true);
  });

  test('inEssentials', async () => {
    const markup = '<p syntax="html">hello</p>';
    const element = new PomlFile(markup).react();
    expect(await read(element)).toBe(
      '<env presentation=\"markup\" markup-lang=\"html\" original-start-index=\"0\" original-end-index=\"25\"><p original-start-index=\"0\" original-end-index=\"25\">hello</p></env>'
    );

    const markupHyphen = '<serialize.object syntax="json" data="{{myData}}"/>';
    const elementHyphen = new PomlFile(markupHyphen).react({
      myData: {
        name: 'world'
      }
    });
    expect(await poml(elementHyphen)).toBe('{\n  "name": "world"\n}');
  });

  test('inplaceContextStylesheet', async () => {
    const text =
      '<poml><p>{{name}}</p><stylesheet>{"p": {"speaker": "ai"}}</stylesheet><context>{"name": "world"}</context></poml>';
    const element = new PomlFile(text).react();
    expect(write(await read(element), { speaker: true })).toStrictEqual([
      { speaker: 'ai', content: 'world' }
    ]);

    const text2 = `<poml><p>hello world<p speaker="human">{{name}}</p></p>
<stylesheet>
{
    "p": {
        "speaker": "human"
    }
}
</stylesheet>
<context>
{
    "name": "world"
}
</context></poml>`;
    const element2 = new PomlFile(text2).react();
    expect(write(await read(element2), { speaker: true })).toStrictEqual([
      { speaker: 'human', content: 'hello world\n\nworld' }
    ]);
  });

  test('emptyLine', async () => {
    const text = '<poml>\n\n<examples>\n\nhello\n\n</examples>\n\n</poml>';
    const element = await read(text);
    expect(element).toMatch('Examples</h><p>hello</p></p></p>');
  });

  test('yaml', async () => {
    const text = `<poml syntax='yaml'>
<role>Senior Systems Architecture Consultant</role>
<task>Legacy System Migration Analysis</task>
</poml>`;
    const element = write(await read(text));
    expect(element).toBe('role: Senior Systems Architecture Consultant\ntask: Legacy System Migration Analysis');
  });

  test('xml', async () => {
    const text = `<poml syntax='xml'>
<role>Senior Systems Architecture Consultant</role>
<task>Legacy System Migration Analysis</task>
</poml>`;
    const element = write(await read(text));
    expect(element).toBe('<role>Senior Systems Architecture Consultant</role>\n<task>Legacy System Migration Analysis</task>');
  });

  test('escape', async () => {
    // const text = '<poml><p>hello <sp value="&"/> world</p> <sp value="&lt;" />end<sp value=">"/></poml>';
    // FIXME: extra space is not allowed here
    // const text = '<poml><p>hello #amp; world</p>   #lt;end#gt;</poml>';
    const text = '<poml><p>hello #amp; world</p>#lt;end#gt;</poml>';
    const element = write(await read(text));
    expect(element).toBe('hello & world\n\n<end>');
  });
});

describe('autoAddPoml', () => {
  test('freeText', async () => {
    const text = `My home\n\n1. The  house is big\n2. The house is small\n\nMy car\n\n1. The car is red\n    2. The car is blue`;
    const result = await poml(text);
    expect(result).toBe(text);
  });

  test('emptySpaceBeforeAfter', async () => {
    const text = '    <poml><p>hello</p>\n\n\n\n\n<p>hello</p></poml>    ';
    const result = await poml(text);
    expect(result).toBe('hello\n\nhello');
  });

  test('commentBefore', async () => {
    const text = '<!-- hello -->  \n  <poml syntax="json">hello</poml>';
    const readResult = await read(text);
    expect(readResult).toMatch(/^<env presentation="serialize" serializer="json"/);
    const writeResult = write(readResult);
    expect(writeResult).toBe('"hello"');
  });

  test('commentBetween', async () => {
    const text = `<poml>  
    <!-- hello1 -->
    <p> <!-- something -->  hello  </p>
    <!-- hello2 -->
    </poml>`;
    const readResult = await read(text);
    expect(readResult).toMatch(/>hello<\/p><\/p><\/env>$/);
    expect(readResult).toMatch(/><p /);
  });
});

describe('templateEngine', () => {
  test('forLoop', async () => {
    const text = '<p><p for="i in [1,2,3]">{{i}}</p></p>';
    expect(await poml(text)).toBe('1\n\n2\n\n3');
    expect(ErrorCollection.empty()).toBe(true);
  });

  test('forLoopNested', async () => {
    const text = '<p><p for="i in [1,2,3]"><p>{{i}}</p></p></p>';
    expect(await poml(text)).toBe('1\n\n2\n\n3');
  })

  test('forLoopIf', async () => {
    const text = '<p><p for="i in [0,1,2]" if="i % 2 == 0">{{i}}</p></p>';
    expect(await poml(text)).toBe('0\n\n2');
  });

  test('forLoopIfLoopIndex', async () => {
    const text = '<p><p for="i in [1,2]" if="loop.index == 1">{{i}}</p></p>';
    expect(await poml(text)).toBe('2');
  });

  test('ifCondition', async () => {
    const text =
      '<p><p if="true">hello</p><p if="i == 0">world</p><p if="{{ i == 1 }}">foo</p></p>';
    expect(write(await read(text, undefined, { i: 0 }))).toBe('hello\n\nworld');
    expect(ErrorCollection.empty()).toBe(true);
    expect(write(await read(text, undefined, { i: 1 }))).toBe('hello\n\nfoo');
    expect(ErrorCollection.empty()).toBe(true);
  });

  test('let', async () => {
    const text = '<p><let name="i" value="1"/><p>{{i}}</p></p>';
    expect(await poml(text)).toBe('1');
    expect(ErrorCollection.empty()).toBe(true);
  });

  test('letFileError', () => {
    const text1 =
      '<let src="assets/peopleList.json" name="people" /><p>hello {{people[0].name.first}}</p>';
    read(text1, undefined, undefined, undefined, __filename);
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    expect(error.message).toMatch(/Cannot read properties of undefined \(reading 'first'\)/);
    expect((error as any).startIndex).toBe(59);
    expect((error as any).endIndex).toBe(82);
    ErrorCollection.clear();

    const text2 = '<let src="assets/people.json" name="people" />';
    read(text2, undefined, undefined, undefined, __filename);
    expect(ErrorCollection.empty()).toBe(false);
    const error2 = ErrorCollection.first();
    expect(error2.message).toMatch(/no such file or directory/);
    expect((error2 as any).startIndex).toBe(9);
    expect((error2 as any).endIndex).toBe(28);
    ErrorCollection.clear();
  });

  test('letFile', async () => {
    const text =
      '<let src="assets/peopleList.json" name="people" /><p>hello {{people[0].first_name}}</p>';
    expect(write(await read(text, undefined, undefined, undefined, __filename))).toBe('hello Jeanette');
  });

  test('letContent', async () => {
    const text = '<let>{ "name": "world" }</let><p>hello {{name}}</p>';
    expect(write(await read(text))).toBe('hello world');
  });

  test('letObject', async () => {
    const text = '<let>{ "object": { "complex": true } }</let><p>{{object}}</p>';
    expect(write(await read(text))).toBe('{"complex":true}');
  });
});

describe('expressionEvaluation', () => {
  test('captures expression tokens for meta lang="expr"', () => {
    const text = `<poml>
      <let name="fields" value='["name", "age"]' />
      <meta type="responseSchema" lang="expr">
        z.object({
          name: z.string(),
          age: z.number()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    
    const tokens = file.getExpressionTokens();
    // Should have tokens for: let value attribute and meta expr content
    expect(tokens.length).toBeGreaterThanOrEqual(2);
    
    // Find the let value token
    const letToken = tokens.find(t => t.expression === '["name", "age"]');
    expect(letToken).toBeDefined();
    expect(letToken?.type).toBe('expression');
    
    // Find the meta expr token
    const metaToken = tokens.find(t => t.expression?.includes('z.object'));
    expect(metaToken).toBeDefined();
    expect(metaToken?.type).toBe('expression');
  });

  test('captures evaluation history', () => {
    ErrorCollection.clear();
    const text = '<p for="i in [1,2]">{{i}}</p>';
    const file = new PomlFile(text);
    file.react();
    const tokens = file.getExpressionTokens();
    expect(tokens.length).toBe(2);
    const position = text.indexOf('{{i}}');
    expect(file.getExpressionEvaluations({ start: position, end: position + 4 })).toStrictEqual([1, 2]);
    expect(ErrorCollection.empty()).toBe(true);
  });

  test('tracks meta expr evaluation', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <let name="num" value="42" />
      <meta type="responseSchema" lang="expr">
        z.object({ value: z.number().max(num) })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    
    // Verify the schema was created successfully
    const schema = file.getResponseSchema();
    expect(schema).toBeDefined();
    
    // Verify expression tokens are collected
    const tokens = file.getExpressionTokens();
    const metaToken = tokens.find(t => t.expression?.includes('z.object'));
    expect(metaToken).toBeDefined();
    expect(metaToken?.type).toBe('expression');
    
    // The expression should be the full z.object expression
    expect(metaToken?.expression?.trim()).toContain('z.object');
    expect(metaToken?.expression?.trim()).toContain('z.number()');
    
    ErrorCollection.clear();
  });

  test('tracks each expression separately', () => {
    ErrorCollection.clear();
    const text = '<p>{{1+2}} {{1+2}}</p>';
    const file = new PomlFile(text);
    file.react();
    const tokens = file.getExpressionTokens();
    expect(tokens.length).toBe(2);
    expect(file.getExpressionEvaluations({ start: tokens[0].range.start, end: tokens[0].range.end })).toStrictEqual([3]);
    expect(file.getExpressionEvaluations({ start: tokens[1].range.start, end: tokens[1].range.end })).toStrictEqual([3]);
  });
});

describe('include', () => {
  test('basic include', async () => {
    const text = '<poml><include src="assets/includeChild.poml"/></poml>';
    const result = write(
      await read(text, undefined, { name: 'world' }, undefined, __filename)
    );
    expect(result).toBe('hello world');
  });

  test('include loop', async () => {
    const text = '<poml><include src="assets/includeNumber.poml" for="i in [1,2]"/></poml>';
    const result = write(await read(text, undefined, undefined, undefined, __filename));
    expect(result).toBe('1\n\n2');
  });

  test('include if', async () => {
    const text = '<poml><include src="assets/includeChild.poml" if="false"/></poml>';
    const result = write(
      await read(text, undefined, { name: 'world' }, undefined, __filename)
    );
    expect(result).toStrictEqual([]);
  });

  test('nested include', async () => {
    const text = '<poml><include src="assets/includeNested.poml"/></poml>';
    const result = write(
      await read(text, undefined, { name: 'world' }, undefined, __filename)
    );
    expect(result).toBe('hello world\n\n3\n\n4');
  });
});

describe('testPropsPreprocess', () => {
  test('parameter', async () => {
    const text = '<div class-name="hello">w12345</div>';
    const stylesheet = { '.hello': { SPEAKER: 'ai' } };
    const result = write(await read(text, undefined, undefined, stylesheet), { speaker: true });
    expect(ErrorCollection.empty()).toBe(true);
    expect(result).toStrictEqual([{ speaker: 'ai', content: 'w12345' }]);
  });

  test('chatFalse', async () => {
    const text = '<example chat="0"><input>hello</input><output>world</output></example>';
    const result = write(await read(text), { speaker: true });
    expect(ErrorCollection.empty()).toBe(true);
    expect(result).toStrictEqual([
      {
        speaker: 'human',
        content: '**Input:** hello\n\n**Output:** world'
      }
    ]);
  });
});

describe('lspFeatures', () => {
  test('hover', () => {
    const text = '<p><p>hello</p></p>';
    const poml = new PomlFile(text);
    const hover = poml.getHoverToken(1);
    expect(hover).toStrictEqual({
      type: 'element',
      range: { start: 1, end: 1 },
      element: 'p'
    });
  });

  test('completion', () => {
    const text = '<p\n';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(2);
    expect(completion).toContainEqual({
      type: 'element',
      range: { start: 1, end: 1 },
      element: 'Paragraph'
    });
  });

  test('completionAlias', () => {
    const text = '<poml><di  </poml>';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(9);
    expect(completion).toStrictEqual([
      {
        type: 'element',
        range: { start: 7, end: 8 },
        element: 'div'
      }
    ]);
  });

  test('completionHyphen', () => {
    const text = '<output-fo';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(10);
    expect(completion).toStrictEqual([
      {
        type: 'element',
        range: { start: 1, end: 9 },
        element: 'output-format'
      }
    ]);
  });

  test('completionClose', () => {
    const text = '<paragraph></para';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(text.length);
    expect(completion).toStrictEqual([
      {
        type: 'element',
        range: { start: 13, end: 16 },
        element: 'paragraph'
      }
    ]);
  });

  test('completionCloseWithNonStandard', () => {
    const text = '<random></>';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(text.length - 1);
    expect(completion).toStrictEqual([
      {
        type: 'element',
        range: { start: text.length - 1, end: text.length - 2 },
        element: 'random'
      }
    ]);
  });

  test('completionAttribute', () => {
    const text = '<question sp';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(text.length);
    expect(completion).toStrictEqual([
      {
        type: 'attribute',
        range: { start: 10, end: 11 },
        element: 'Question',
        attribute: 'speaker'
      }
    ]);
  });

  test('completionAttributeWoPrefix', () => {
    const text = '<question ';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(text.length);
    expect(completion.length).toBeGreaterThan(5);
    expect(completion).toContainEqual({
      attribute: 'questionCaption',
      element: 'Question',
      range: { end: 9, start: 9 },
      type: 'attribute'
    });
  });

  test('completionAttributeValue', () => {
    const text = '<question speaker=""';
    const poml = new PomlFile(text);
    const completion = poml.getCompletions(text.length - 1);
    expect(completion).toContainEqual({
      type: 'attributeValue',
      range: { start: 19, end: 18 },
      element: 'Question',
      attribute: 'speaker',
      value: 'human'
    });
  });
});

describe('meta elements', () => {
  test('responseSchema with JSON', () => {
    const text = `<poml>
      <meta type="responseSchema" lang="json">
        {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "age": { "type": "number" }
          },
          "required": ["name"]
        }
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    const schema = file.getResponseSchema();
    expect(schema).toBeDefined();
    expect(schema?.toOpenAPI()).toEqual({
      type: "object",
      properties: {
        name: { type: "string" },
        age: { type: "number" }
      },
      required: ["name"]
    });
  });

  test('responseSchema with Zod', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="responseSchema">
        z.object({
          name: z.string(),
          age: z.number().optional()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(true);
    const schema = file.getResponseSchema();
    expect(schema).toBeDefined();
    const zodSchema = schema?.toZod();
    expect(zodSchema).toBeDefined();
    ErrorCollection.clear();
  });

  test('tool with JSON schema', () => {
    const text = `<poml>
      <meta type="tool" name="getWeather" description="Get weather information">
        {
          "type": "object",
          "properties": {
            "location": { "type": "string" },
            "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
          },
          "required": ["location"]
        }
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    const toolsSchema = file.getToolsSchema();
    expect(toolsSchema).toBeDefined();
    expect(toolsSchema?.size()).toBe(1);
    const tool = toolsSchema?.getTool('getWeather');
    expect(tool).toBeDefined();
    expect(tool?.name).toBe('getWeather');
    expect(tool?.description).toBe('Get weather information');
  });

  test('tool with Zod schema', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="tool" name="calculate" description="Perform calculation">
        z.object({
          operation: z.enum(['add', 'subtract']),
          a: z.number(),
          b: z.number()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(true);
    const toolsSchema = file.getToolsSchema();
    expect(toolsSchema).toBeDefined();
    expect(toolsSchema?.size()).toBe(1);
    const tool = toolsSchema?.getTool('calculate');
    expect(tool).toBeDefined();
    expect(tool?.name).toBe('calculate');
    expect(tool?.description).toBe('Perform calculation');
    ErrorCollection.clear();
  });

  test('multiple responseSchema error', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="responseSchema" lang="json">{"type": "string"}</meta>
      <meta type="responseSchema" lang="json">{"type": "number"}</meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    expect(error.message).toContain('Multiple responseSchema meta elements found');
    ErrorCollection.clear();
  });

  test('tool without name error', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="tool" description="Missing name">
        {"type": "object"}
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    expect(error.message).toContain('name attribute is required for tool meta type');
    ErrorCollection.clear();
  });

  test('runtime meta parameters', () => {
    const text = `<poml>
      <meta type="runtime" temperature="0.7" max_tokens="1000" model="gpt-4">
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    const runtimeParams = file.getRuntimeParameters();
    expect(runtimeParams).toEqual({
      temperature: "0.7",
      max_tokens: "1000",
      model: "gpt-4"
    });
  });

  test('responseSchema with expression evaluation', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <let name="maxAge" value="100" />
      <meta type="responseSchema" lang="json">
        {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "age": { 
              "type": "number",
              "minimum": 0,
              "maximum": {{ maxAge }}
            }
          }
        }
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(true);
    const schema = file.getResponseSchema();
    expect(schema).toBeDefined();
    expect(schema?.toOpenAPI()).toEqual({
      type: "object",
      properties: {
        name: { type: "string" },
        age: { 
          type: "number",
          minimum: 0,
          maximum: 100
        }
      }
    });
    ErrorCollection.clear();
  });

  test('tool with expression evaluation in Zod', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <let name="operations" value='["add", "subtract", "multiply", "divide"]' />
      <meta type="tool" name="calculator" description="Math operations" lang="expr">
        z.object({
          operation: z.enum(operations),
          a: z.number(),
          b: z.number()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(true);
    const toolsSchema = file.getToolsSchema();
    expect(toolsSchema).toBeDefined();
    expect(toolsSchema?.size()).toBe(1);
    const tool = toolsSchema?.getTool('calculator');
    expect(tool).toBeDefined();
    expect(tool?.name).toBe('calculator');
    expect(tool?.description).toBe('Math operations');
    ErrorCollection.clear();
  });

  test('responseSchema Zod with z variable available', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <let name="fields" value='{ "name": "string", "age": "number" }' />
      <meta type="responseSchema" lang="expr">
        z.object({
          name: z.string(),
          age: z.number(),
          timestamp: z.string().datetime()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(true);
    const schema = file.getResponseSchema();
    expect(schema).toBeDefined();
    const zodSchema = schema?.toZod();
    expect(zodSchema).toBeDefined();
    ErrorCollection.clear();
  });

  test('malformed JSON syntax error', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="responseSchema" lang="json">
        {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
          }
        }
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    // JSON parse errors contain specific messages about the syntax error
    expect(error.message).toBeDefined();
    ErrorCollection.clear();
  });

  test('invalid expression evaluation error', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="responseSchema" lang="expr">
        z.object({
          name: z.nonexistent(),
          age: z.number()
        })
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    expect(error.message).toContain('z.nonexistent is not a function');
    ErrorCollection.clear();
  });

  test('invalid OpenAPI schema structure', () => {
    ErrorCollection.clear();
    const text = `<poml>
      <meta type="responseSchema" lang="json">
        "not an object"
      </meta>
    </poml>`;
    const file = new PomlFile(text);
    file.react();
    // Schema.fromOpenAPI should handle this - it might not error but create a schema
    const schema = file.getResponseSchema();
    expect(ErrorCollection.empty()).toBe(false);
    const error = ErrorCollection.first();
    expect(error.message).toContain('Invalid OpenAPI schema');
    expect(schema).toBeUndefined();
    ErrorCollection.clear();
  });
});



================================================
FILE: packages/poml/tests/index.test.tsx
================================================
import * as React from 'react';
import fs from '../util/fs';
import * as path from 'path';

import { beforeAll, afterAll, describe, expect, test, jest } from '@jest/globals';
import { spyOn } from 'jest-mock';

import { read, write, writeWithSourceMap, poml, commandLine } from 'poml';
import { Markup } from 'poml/presentation';
import { ErrorCollection, ReadError, WriteError } from 'poml/base';

// Add a finalizer to allow any lingering async operations (like from pdf-parse) to complete.
afterAll(async () => {
  await new Promise(resolve => setTimeout(resolve, 500));
});

describe('endToEnd', () => {
  test('simple', async () => {
    const text = '<Markup.Paragraph>Hello, world!</Markup.Paragraph>';
    const element = await poml(text);
    expect(element).toBe('Hello, world!');
  });

  test('charLimitEndToEnd', async () => {
    const text = '<p charLimit="4">abcdefg</p>';
    const element = await poml(text);
    expect(element).toBe('abcd (...truncated)');
  });

  test('tokenLimitEndToEnd', async () => {
    const text = '<p tokenLimit="1">hello world</p>';
    const element = await poml(text);
    expect(element).toBe('hello (...truncated)');
  });

  test('customTruncationOptions', async () => {
    const element = await poml(
      <Markup.Paragraph
        charLimit={3}
        writerOptions={{ truncateDirection: 'start', truncateMarker: '[cut]' }}
      >
        abcdef
      </Markup.Paragraph>
    );
    expect(element).toBe('[cut]def');
  });

  test('priorityEndToEnd', async () => {
    const text =
      '<p charLimit="5"><span priority="1">hello</span><span priority="2">world</span></p>';
    const element = await poml(text);
    expect(element).toBe('world');
  });

  test('priorityTokenEndToEnd', async () => {
    const text =
      '<p tokenLimit="1"><span priority="1">hello</span><span priority="2">world</span></p>';
    const element = await poml(text);
    expect(element).toBe('world');
  });

  test('speakerWithStylesheet', async () => {
    const markup = '<p><p className="myClass">hello</p><p className="myClassB">world</p></p>';
    const stylesheet = {
      '.myClass': {
        speaker: 'ai'
      },
      '.myClassB': {
        speaker: 'human'
      }
    };
    const ir = await read(markup, undefined, undefined, stylesheet);
    expect(ir).toBe(
      '<env presentation=\"markup\" markup-lang=\"markdown\" original-start-index=\"0\" original-end-index=\"71\"><p original-start-index=\"0\" original-end-index=\"71\"><p speaker=\"ai\" original-start-index=\"3\" original-end-index=\"34\">hello</p><p speaker=\"human\" original-start-index=\"35\" original-end-index=\"67\">world</p></p></env>'
    );
    const result = write(ir, { speaker: true });
    expect(result).toStrictEqual([
      { speaker: 'ai', content: 'hello' },
      { speaker: 'human', content: 'world' }
    ]);
  });

  test('system', async () => {
    const text = `<poml>
<p speaker="system">Be brief and clear in your responses</p>
<!-- some comment -->
</poml>`;
    const element = write(await read(text), { speaker: true });
    expect(element).toStrictEqual([
      { speaker: 'system', content: 'Be brief and clear in your responses' }
    ]);
  });

  test('empty', async () => {
    const text = '<poml>\n</poml>';
    const element = write(await read(text), { speaker: true });
    expect(element).toStrictEqual([{ speaker: 'human', content: [] }]);
  });
});

describe('diagnosis', () => {
  test('load', async () => {
    const fn = async () => {
      ErrorCollection.clear();
      await read('<p><paragrapy/><paragraph/></p>');
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(ReadError);
    try {
      await fn();
    } catch (e: any) {
      expect(e.message).toBe('Component paragrapy not found. Do you mean: paragraph?');
      expect(e.startIndex).toBe(4);
      expect(e.endIndex).toBe(12);
    }
  });

  test('loadWithContext', async () => {
    const fn = async () => {
      ErrorCollection.clear();
      await read('<p>{{ name }}</p>', undefined, { naming: 'world' });
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(ReadError);
    try {
      await fn();
    } catch (e: any) {
      expect(e.message).toBe('name is not defined');
      expect(e.startIndex).toBe(3);
      expect(e.endIndex).toBe(12);
    }
  });

  test('read', async () => {
    const fn = async () => {
      ErrorCollection.clear();
      await read('<p speaker="joker">hello</p>');
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(ReadError);
    try {
      await fn();
    } catch (e: any) {
      expect(e.message).toBe('"speaker" should be one of human, ai, system, not joker');
      expect(e.startIndex).toBe(0);
      expect(e.endIndex).toBe(27);
    }
  });

  test('write', async () => {
    const original = '<p speaker="human"><obj syntax="json"/></p>';
    const fn = async () => {
      ErrorCollection.clear();
      write(await read(original));
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(WriteError);
    try {
      await fn();
    } catch (e: any) {
      expect(e.message).toMatch(/^No data attribute in obj:/g);
      const ir = e.relatedIr.slice(e.irStartIndex, e.irEndIndex + 1);
      const originalSlice = original.slice(e.startIndex, e.endIndex + 1);
      expect(ir).toMatch(/^<obj serializer="json"/g);
      expect(originalSlice).toBe('<obj syntax="json"/>');
    }
  });

  test('writeWithSourceMap', async () => {
    const original = '<poml><p>hello <b>world</b></p><p speaker="human">how are you?</p></poml>';
    const fn = async () => {
      ErrorCollection.clear();
      const ir = await read(original);
      const segments = writeWithSourceMap(ir, { speaker: true });
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
      return segments;
    };
    const segments = await fn();
    const p1Start = original.indexOf('<p>');
    const p1End = original.indexOf('</p>') + 4 - 1; // +4 for '</p>', -1 for inclusive end
    const bStart = original.indexOf('<b>');
    const bEnd = original.indexOf('</b>') + 4 - 1;
    const p2Start = original.indexOf('<p speaker="human">');
    const p2End = original.lastIndexOf('</p>') + 4 - 1;
    const expects = [
      {
        startIndex: p1Start,
        endIndex: p1End,
        irStartIndex: 170,
        irEndIndex: 293,
        speaker: 'system',
        content: [
          {
            startIndex: p1Start,
            endIndex: p1End,
            irStartIndex: 170,
            irEndIndex: 293,
            content: 'hello '
          },
          {
            startIndex: bStart,
            endIndex: bEnd,
            irStartIndex: 228,
            irEndIndex: 289,
            content: '**world**'
          }
        ]
      },
      {
        startIndex: p2Start,
        endIndex: p2End,
        irStartIndex: 294,
        irEndIndex: 378,
        speaker: 'human',
        content: [
          {
            startIndex: p2Start,
            endIndex: p2End,
            irStartIndex: 294,
            irEndIndex: 378,
            content: 'how are you?'
          }
        ]
      }
    ];
    expect(segments).toStrictEqual(expects);
  });

  test('writeWithSourceMapWithTask', async () => {
    const original = '<poml><p>hello</p><task>123</task></poml>';
    const fn = async () => {
      ErrorCollection.clear();
      const ir = await read(original);
      const segments = writeWithSourceMap(ir, { speaker: true });
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
      return segments;
    };
    const segments = await fn();
    const pStart = original.indexOf('<p>');
    const pEnd = original.indexOf('</p>') + 4 - 1;
    const taskStart = original.indexOf('<task>');
    const taskEnd = original.indexOf('</task>') + 7 - 1;
    const expects = [
      {
        startIndex: pStart,
        endIndex: taskEnd,
        irStartIndex: 170,
        irEndIndex: 431,
        speaker: 'human',
        content: [
          {
            startIndex: pStart,
            endIndex: pEnd,
            irStartIndex: 170,
            irEndIndex: 230,
            content: 'hello'
          },
          {
            startIndex: 0,
            endIndex: original.length - 1,
            irStartIndex: 99,
            irEndIndex: 439,
            content: '\n\n'
          },
          {
            startIndex: taskStart,
            endIndex: taskEnd,
            irStartIndex: 325,
            irEndIndex: 421,
            content: '# Task'
          },
          {
            startIndex: taskStart,
            endIndex: taskEnd,
            irStartIndex: 231,
            irEndIndex: 435,
            content: '\n\n'
          },
          {
            startIndex: taskStart,
            endIndex: taskEnd,
            irStartIndex: 422,
            irEndIndex: 431,
            content: '123'
          }
        ]
      }
    ];
    expect(segments).toStrictEqual(expects);
  });
});

describe('cli', () => {
  beforeAll(() => {
    spyOn(process.stdout, 'write').mockImplementation(() => true);
  });

  test('simple', async () => {
    const text = '<Markup.Paragraph>Hello, world!</Markup.Paragraph>';
    await commandLine({ input: text, speakerMode: false });
    expect(process.stdout.write).toHaveBeenCalledWith('{"messages":"Hello, world!"}');
  });

  test('context', async () => {
    const text = '<Markup.Paragraph>{{name}}</Markup.Paragraph>';
    await commandLine({ input: text, context: ['name=world'], speakerMode: false });
    expect(process.stdout.write).toHaveBeenCalledWith('{"messages":"world"}');
  });

  test('contextSpeaker', async () => {
    const text = '<Markup.Paragraph>{{name}}</Markup.Paragraph>';
    await commandLine({ input: text, context: ['name=world'] });
    expect(process.stdout.write).toHaveBeenCalledWith(
      '{"messages":[{\"speaker\":\"human\",\"content\":\"world\"}]}'
    );
  });

  test('contentWithResponseSchema', async () => {
    const text =
      '<poml>Hello, world!<meta type="responseSchema">z.object({ operation: z.enum(["add", "subtract"]), a: z.number(), b: z.number() })</meta></poml>';
    await commandLine({ input: text, speakerMode: true });
    expect(process.stdout.write).toHaveBeenCalledWith(
      '{"messages":[{"speaker":"human","content":"Hello, world!"}],"responseSchema":{"type":"object","properties":{"operation":{"type":"string","enum":["add","subtract"]},"a":{"type":"number"},"b":{"type":"number"}},"required":["operation","a","b"],"additionalProperties":false}}'
    );
  });
});

interface ExpectMessage {
  speaker: string;
  contents: string[];
}

function stripEndline(str: string): string {
  return str.replace(/\n+$/, '').replace(/^\n+/, '').replace(/\r\n/g, '\n').replace(/\r/g, '');
}

function parseExpects(expectFile: string): ExpectMessage[] {
  const content = fs.readFileSync(expectFile, 'utf-8').replace(/\r\n/g, '\n');

  // Split by speaker headers (===== speaker =====)
  const sections = content.split(/===== (\w+) =====\n\n/);

  const messages: ExpectMessage[] = [];

  // Process sections in pairs (speaker, content)
  for (let i = 1; i < sections.length; i += 2) {
    if (i + 1 < sections.length) {
      const speaker = sections[i];
      const rawContent = stripEndline(sections[i + 1]);

      // Parse content for mixed text and images
      const contents: string[] = [];

      // Find all JSON image objects first
      const imagePattern = /\{"type":"[^"]+","base64":"[^\n"]+?(\n|$)/g;

      // Split content while keeping track of positions
      let lastEnd = 0;
      let match;

      while ((match = imagePattern.exec(rawContent)) !== null) {
        // Add text before this image (if any)
        const textBefore = stripEndline(rawContent.slice(lastEnd, match.index));
        if (textBefore) {
          contents.push(textBefore);
        }

        // Add image (first 50 chars of base64)
        try {
          const imgData = JSON.parse(match[0]);
          const base64Content = imgData.base64 || '';
          const prefix = base64Content.slice(0, 50);
          contents.push(prefix);
        } catch (e) {
          // Fallback: extract base64 with regex
          const base64Match = match[0].match(/"base64":"([^"\.]+)/);
          if (base64Match) {
            const prefix = base64Match[1].slice(0, 50);
            contents.push(prefix);
          }
        }

        lastEnd = match.index + match[0].length;
      }

      // Add any remaining text after the last image
      const remainingText = stripEndline(rawContent.slice(lastEnd));
      if (remainingText) {
        contents.push(remainingText);
      }

      messages.push({ speaker, contents });
    }
  }

  return messages;
}

function diffMessages(expected: ExpectMessage[], actual: any): string {
  if (!Array.isArray(actual)) {
    return `Expected a list of messages, got ${typeof actual}`;
  }
  if (expected.length !== actual.length) {
    return `Expected ${expected.length} messages, got ${actual.length}`;
  }

  for (let i = 0; i < expected.length; i++) {
    const exp = expected[i];
    const act = actual[i];

    if (typeof act !== 'object' || act === null) {
      return `Message ${i} is not an object: ${typeof act}`;
    }
    if (exp.speaker !== act.speaker) {
      return `Message ${i} speaker mismatch: expected '${exp.speaker}', got '${act.speaker}'`;
    }
    if (!('content' in act)) {
      return `Message ${i} missing 'content' key`;
    }
    if (typeof act.content === 'string') {
      if (exp.contents.length !== 1 || exp.contents[0] !== stripEndline(act.content)) {
        return `Message ${i} contents mismatch: expected ${JSON.stringify(exp.contents)}, got ${JSON.stringify(act.content)}`;
      }
      continue;
    }
    if (!Array.isArray(act.content)) {
      return `Message ${i} contents is not an array: ${typeof act.content}`;
    }
    if (exp.contents.length !== act.content.length) {
      return `Message ${i} content length mismatch: expected ${exp.contents.length}, got ${act.content.length}`;
    }
    for (let j = 0; j < exp.contents.length; j++) {
      const expContent = exp.contents[j];
      const actContent = act.content[j];

      if (typeof actContent === 'string' && expContent === stripEndline(actContent)) {
        continue;
      }
      if (typeof actContent === 'object' && actContent !== null) {
        if ('base64' in actContent && actContent.base64.startsWith(expContent)) {
          continue;
        }
      }
      return `Message ${i} content ${j} mismatch: expected '${expContent}', got '${actContent}'`;
    }
  }
  return '';
}

describe('examples correctness', () => {
  beforeAll(() => {
    spyOn(process.stdout, 'write').mockImplementation(() => true);
  });

  // Dynamically generate tests for all .poml files in the examples folder
  const examplesDir = path.resolve(__dirname, '../../../examples');
  const expectsDir = path.join(examplesDir, 'expects');
  const exampleFiles = fs
    .readdirSync(examplesDir)
    .filter(file => file.endsWith('.poml'))
    .sort(); // Sort for consistent test order

  exampleFiles.forEach(fileName => {
    test(`${fileName} produces correct output`, async () => {
      // FIXME: Skip 301_generate_poml on Windows due to CRLF handling issue
      if (process.platform === 'win32' && fileName === '301_generate_poml.poml') {
        console.warn(
          'Skipping 301_generate_poml on Windows due to CRLF handling issue in txt files'
        );
        return;
      }

      const filePath = path.join(examplesDir, fileName);
      const expectFile = path.join(expectsDir, fileName.replace('.poml', '.txt'));

      if (!fs.existsSync(expectFile)) {
        throw new Error(`Expected output file not found: ${expectFile}`);
      }

      // Get actual result
      let actualResult: any;
      const originalWrite = process.stdout.write;
      const outputs: string[] = [];

      process.stdout.write = jest.fn((str: string) => {
        outputs.push(str);
        return true;
      });

      try {
        await commandLine({
          file: filePath,
          speakerMode: true
        });

        const output = outputs.join('');
        actualResult = JSON.parse(output)['messages'];
      } finally {
        process.stdout.write = originalWrite;
      }

      // Parse expected output
      const expectedMessages = parseExpects(expectFile);
      const diff = diffMessages(expectedMessages, actualResult);

      if (diff) {
        throw new Error(`Example ${fileName} failed:\n${diff}`);
      }
    });
  });

  // Fallback test if no example files are found
  if (exampleFiles.length === 0) {
    test('no .poml files found', () => {
      console.warn(`No .poml files found in ${examplesDir}`);
      expect(true).toBe(true); // Always pass this test
    });
  }
});



================================================
FILE: packages/poml/tests/instructions.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test } from '@jest/globals';

import { poml, read, write } from 'poml';
import { Text, List, ListItem } from 'poml/essentials';
import {
  Role,
  Task,
  OutputFormat,
  Hint,
  Example,
  ExampleSet,
  ExampleInput,
  ExampleOutput
} from 'poml/components/instructions';
import { CaptionedParagraph } from 'poml/components';

describe('instructions', () => {
  test('role', async () => {
    const role = <Role>You are a data scientist.</Role>;
    expect(await poml(role)).toBe('# Role\n\nYou are a data scientist.');

    const roleInJson = <Role syntax="json">You are a data scientist.</Role>;
    expect(await poml(roleInJson)).toBe('{\n  "role": "You are a data scientist."\n}');
  });

  test('roleTaskFormat', async () => {
    const roleTaskFormat = (
      <Text syntax="json">
        <Role>You are a data scientist.</Role>
        <Task>Analyze the data.</Task>
        <OutputFormat>JSON</OutputFormat>
      </Text>
    );
    expect(await poml(roleTaskFormat)).toBe(
      '{\n  "role": "You are a data scientist.",\n  "task": "Analyze the data.",\n  "outputFormat": "JSON"\n}'
    );
    const roleTaskFormatMarkdown = (
      <Text syntax="markdown">
        <Role captionStyle="bold">You are a data scientist.</Role>
        <Task captionStyle="plain" captionTextTransform="upper">
          Analyze the data.
        </Task>
        <OutputFormat captionStyle="header" captionEnding="colon">
          JSON
        </OutputFormat>
      </Text>
    );
    expect(await poml(roleTaskFormatMarkdown)).toBe(
      '**Role:** You are a data scientist.\n\nTASK: Analyze the data.\n\n# Output Format:\n\nJSON'
    );
  });

  test('captionColon', async () => {
    const role = <Role captionEnding="colon">You are a data scientist.</Role>;
    expect(await poml(role)).toBe('# Role:\n\nYou are a data scientist.');

    const roleWithNewline = (
      <Role captionEnding="colon-newline" captionStyle="bold">
        You are a data scientist.
      </Role>
    );
    expect(await poml(roleWithNewline)).toBe('**Role:**\nYou are a data scientist.');
  });

  test('task', async () => {
    const task = (
      <Task>
        Planning a schedule for a travel.
        <List>
          <ListItem>Decide on the destination and plan the duration.</ListItem>
          <ListItem>Find useful information about the destination.</ListItem>
          <ListItem>Write down the schedule for each day.</ListItem>
        </List>
      </Task>
    );
    expect(await poml(task)).toBe(
      '# Task\n\nPlanning a schedule for a travel.\n\n- Decide on the destination and plan the duration.\n- Find useful information about the destination.\n- Write down the schedule for each day.'
    );
  });

  test('captioned paragraph', async () => {
    const task = (
      <CaptionedParagraph caption="Task" syntax="yaml">
        <List>
          <ListItem>Decide on the destination and plan the duration.</ListItem>
          <ListItem>Find useful information about the destination.</ListItem>
        </List>
      </CaptionedParagraph>
    );
    expect(await poml(task)).toBe('Task:\n  - Decide on the destination and plan the duration.\n  - Find useful information about the destination.')
  })

  test('hint', async () => {
    const hint = <Hint>Use the following code to analyze the data.</Hint>;
    expect(await poml(hint)).toBe('**Hint:** Use the following code to analyze the data.');
  });

  test('examples', async () => {
    const examples = (
      <ExampleSet introducer="Here are some examples.">
        <Example>
          <ExampleInput captionStyle="bold">What's the capital of France?</ExampleInput>
          <ExampleOutput captionStyle="bold">Paris</ExampleOutput>
        </Example>
        <Example>
          <ExampleInput captionStyle="bold">What's the capital of Germany?</ExampleInput>
          <ExampleOutput captionStyle="bold">Berlin</ExampleOutput>
        </Example>
      </ExampleSet>
    );
    expect(await poml(examples)).toBe(
      "# Examples\n\nHere are some examples.\n\n**Input:** What's the capital of France?\n\n**Output:** Paris\n\n**Input:** What's the capital of Germany?\n\n**Output:** Berlin"
    );
    expect(JSON.parse((await poml(<Text syntax="json">{examples}</Text>)) as string)).toStrictEqual(
      {
        examples: [
          {
            input: "What's the capital of France?",
            output: 'Paris'
          },
          {
            input: "What's the capital of Germany?",
            output: 'Berlin'
          }
        ]
      }
    );

    const ir = await read(examples);
    const out = write(ir, { speaker: true });
    expect(out).toStrictEqual([
      {
        speaker: 'system',
        content: '# Examples\n\nHere are some examples.'
      },
      {
        speaker: 'human',
        content: "**Input:** What's the capital of France?"
      },
      { speaker: 'ai', content: '**Output:** Paris' },
      {
        speaker: 'human',
        content: "**Input:** What's the capital of Germany?"
      },
      { speaker: 'ai', content: '**Output:** Berlin' }
    ]);
  });

  test('examples for loop', async () => {
    const text = `<poml><let name="examples" value='{{[{"input":"What is the capital of France","output":"Paris"},{"input":"What is the capital of Germany","output":"Berlin"}]}}'/>
<examples>
<example for="example in examples" chat="false" caption="Example {{ loop.index+1 }}" captionStyle="header">
<input captionEnding="none">{{ example.input }}</input>
<output captionEnding="newline" captionStyle="plain">{{ example.output }}</output>
</example>
</examples></poml>`;
    const result = await poml(text);
    expect(result).toBe(`# Examples

## Example 1

**Input** What is the capital of France

Output
Paris

## Example 2

**Input** What is the capital of Germany

Output
Berlin`);
  });

  test('examples with intro', async () => {
    const text = `<poml><example captionStyle="plain"><input>abc</input><output>def</output></example></poml>`;
    const ir = await read(text);
    const result = write(ir, { speaker: true });
    expect(result).toStrictEqual([
      { speaker: 'system', content: 'Example:' },
      { speaker: 'human', content: 'abc' },
      { speaker: 'ai', content: 'def' }
    ]);
  })
});



================================================
FILE: packages/poml/tests/meta.test.tsx
================================================
import * as React from 'react';
import { describe, expect, test } from '@jest/globals';
import { poml, read, write } from 'poml';
import { ErrorCollection, ReadError, component, unregisterComponent } from 'poml/base';


describe('meta tag', () => {
  test('version check pass', async () => {
    const result = await poml('<meta minVersion="0.0.1" maxVersion="999.0.0"/><p>hi</p>');
    expect(result).toBe('hi');
  });

  test('version check fail', async () => {
    const fn = async () => {
      ErrorCollection.clear();
      await read('<meta minVersion="9.9.9"/><p>hi</p>');
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(ReadError);
  });

  test('disable component', async () => {
    const fn = async () => {
      ErrorCollection.clear();
      await read('<poml><meta components="-table"/><table records="a,b\n1,2" parser="csv"/></poml>');
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fn).rejects.toThrow(ReadError);
  });

  test('re-enable component', async () => {
    const result = write(
      await read('<poml><meta components="-table"/><meta components="+table"/><table records="a,b\n1,2" parser="csv"/></poml>')
    );
    expect(result).toMatch(/\|/);
  });

  test('disable alias only', async () => {
    const Hello = component('Hello', { aliases: ['hi'] })(() => {
      return <p>hi</p>;
    });
    const fail = async () => {
      ErrorCollection.clear();
      await read('<poml><meta components="-hi"/><hi/></poml>');
      if (!ErrorCollection.empty()) {
        throw ErrorCollection.first();
      }
    };
    await expect(fail).rejects.toThrow(ReadError);

    const ok = await read('<poml><meta components="-hi"/><Hello/></poml>');
    expect(ok).toContain('hi');
    unregisterComponent('Hello');
  });
});



================================================
FILE: packages/poml/tests/presentation.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test } from '@jest/globals';

import { read } from 'poml';
import { Free, Markup, Serialize } from 'poml/presentation';

describe('markup presentation', () => {
  test('env', async () => {
    const env = <Markup.Environment>hahaha</Markup.Environment>;
    expect(await read(env)).toBe('<env presentation="markup" markup-lang="markdown">hahaha</env>');
  });

  test('paragraph', async () => {
    const paragraph = <Markup.Paragraph>hahaha</Markup.Paragraph>;
    expect(await read(paragraph)).toBe(
      '<env presentation="markup" markup-lang="markdown"><p>hahaha</p></env>'
    );
  });

  test('markupLang', async () => {
    const paragraph = <Markup.Paragraph markupLang="html">hahaha</Markup.Paragraph>;
    expect(await read(paragraph)).toBe(
      '<env presentation="markup" markup-lang="html"><p>hahaha</p></env>'
    );
    const nested = (
      <Markup.Paragraph markupLang="html">
        hahaha<Markup.Paragraph markupLang="html">dadada</Markup.Paragraph>
      </Markup.Paragraph>
    );
    expect(await read(nested)).toBe(
      '<env presentation="markup" markup-lang="html"><p>hahaha<p>dadada</p></p></env>'
    );
    const nestedEnv = <Markup.Environment>{nested}</Markup.Environment>;
    expect(await read(nestedEnv)).toBe(
      '<env presentation="markup" markup-lang="markdown"><env presentation="markup" markup-lang="html"><p>hahaha<p>dadada</p></p></env></env>'
    );
  });
});

describe('markdown json hybrid', () => {
  test('env', async () => {
    const env = (
      <Markup.Environment>
        <Serialize.Environment>
          <Serialize.Any name="hello">world</Serialize.Any>
        </Serialize.Environment>
      </Markup.Environment>
    );
    expect(await read(env)).toBe(
      '<env presentation="markup" markup-lang="markdown"><code inline="false" lang="json"><env presentation="serialize" serializer="json"><any name="hello">world</any></env></code></env>'
    );
  });

  test('jsonMarkdown', async () => {
    const env = (
      <Serialize.Environment>
        <Serialize.Any name="hello">
          <Markup.Paragraph>world</Markup.Paragraph>
        </Serialize.Any>
      </Serialize.Environment>
    );
    expect(await read(env)).toBe(
      '<env presentation="serialize" serializer="json"><any name="hello"><env presentation="markup" markup-lang="markdown"><p>world</p></env></any></env>'
    );
  });
});

describe('free', () => {
  test('freeEnv', async () => {
    const env = <Free.Environment>{'hello\nworld'}</Free.Environment>;
    expect(await read(env)).toBe('<env presentation="free" white-space="pre">hello\nworld</env>');
  });

  test('freeText', async () => {
    const text = <Free.Text>{'hello\nworld'}</Free.Text>;
    expect(await read(text)).toBe('<env presentation="free" white-space="pre"><text white-space="pre">hello\nworld</text></env>');
  });
});



================================================
FILE: packages/poml/tests/schema.test.ts
================================================
import { describe, expect, test } from '@jest/globals';
import { z } from 'zod';
import { Schema, ToolsSchema } from '../util/schema';

describe('Schema', () => {
  describe('fromZod', () => {
    test('should create a Schema from a Zod schema', () => {
      const zodSchema = z.object({
        name: z.string(),
        age: z.number()
      });

      const schema = Schema.fromZod(zodSchema);
      expect(schema).toBeDefined();
      expect(schema.toZod()).toBe(zodSchema);
    });
  });

  describe('fromOpenAPI', () => {
    test('should create a Schema from an OpenAPI schema', () => {
      const openApiSchema = {
        type: 'object',
        properties: {
          name: { type: 'string' },
          age: { type: 'number' }
        },
        required: ['name']
      };

      const schema = Schema.fromOpenAPI(openApiSchema);
      expect(schema).toBeDefined();
      expect(schema.toOpenAPI()).toBe(openApiSchema);
    });

    test('should accept valid JSON schema types', () => {
      const stringSchema = { type: 'string' };
      const numberSchema = { type: 'number' };
      const booleanSchema = { type: 'boolean' };
      const arraySchema = { type: 'array', items: { type: 'string' } };
      
      expect(() => Schema.fromOpenAPI(stringSchema)).not.toThrow();
      expect(() => Schema.fromOpenAPI(numberSchema)).not.toThrow();
      expect(() => Schema.fromOpenAPI(booleanSchema)).not.toThrow();
      expect(() => Schema.fromOpenAPI(arraySchema)).not.toThrow();
    });

    test('should handle schemas without type property', () => {
      const schemaWithoutType = {
        properties: {
          name: { type: 'string' }
        }
      };
      
      // This should not throw - JSON Schema allows schemas without explicit type
      expect(() => Schema.fromOpenAPI(schemaWithoutType)).not.toThrow();
    });
  });

  describe('toZod', () => {
    test('should return the original Zod schema when created from Zod', () => {
      const zodSchema = z.object({
        id: z.string(),
        count: z.number()
      });

      const schema = Schema.fromZod(zodSchema);
      expect(schema.toZod()).toBe(zodSchema);
    });

    test('should convert OpenAPI schema to Zod', () => {
      const openApiSchema = {
        type: 'object',
        properties: {
          name: { type: 'string' },
          age: { type: 'number' }
        },
        required: ['name']
      };

      const schema = Schema.fromOpenAPI(openApiSchema);
      // Note: This uses Function constructor which is similar to eval
      const zodSchema = schema.toZod();
      expect(zodSchema).toBeDefined();

      // Test that the converted schema can parse valid data
      const validData = { name: 'John', age: 30 };
      const parsed = zodSchema.parse(validData);
      expect(parsed).toEqual(validData);

      // Test that required fields are enforced
      const invalidData = { age: 25 }; // missing required 'name'
      expect(() => zodSchema.parse(invalidData)).toThrow();
    });

    test('should throw error when no schema is available', () => {
      // This test is not possible with current constructor validation
      // Constructor requires at least one schema to be provided
    });
  });

  describe('toOpenAPI', () => {
    test('should return the original OpenAPI schema when created from OpenAPI', () => {
      const openApiSchema = {
        type: 'object',
        properties: {
          email: { type: 'string', format: 'email' }
        }
      };

      const schema = Schema.fromOpenAPI(openApiSchema);
      expect(schema.toOpenAPI()).toBe(openApiSchema);
    });

    test('should convert Zod schema to OpenAPI format', () => {
      const zodSchema = z.object({
        name: z.string(),
        age: z.number().optional(),
        tags: z.array(z.string())
      });

      const schema = Schema.fromZod(zodSchema);
      const openApiSchema = schema.toOpenAPI();

      expect(openApiSchema).toBeDefined();
      expect(openApiSchema.type).toBe('object');
      expect(openApiSchema.properties).toBeDefined();
      expect(openApiSchema.properties.name).toBeDefined();
      expect(openApiSchema.properties.age).toBeDefined();
      expect(openApiSchema.properties.tags).toBeDefined();
      expect(openApiSchema.properties.tags.type).toBe('array');
    });
  });
});

describe('ToolsSchema', () => {
  let toolsSchema: ToolsSchema;

  beforeEach(() => {
    toolsSchema = new ToolsSchema();
  });

  describe('addZodTool', () => {
    test('should add a tool with Zod schema', () => {
      const zodSchema = z.object({
        sign: z.string().describe('An astrological sign like Taurus or Aquarius')
      });

      toolsSchema.addZodTool(
        'get_horoscope',
        "Get today's horoscope for an astrological sign",
        zodSchema
      );

      expect(toolsSchema.size()).toBe(1);
      const tool = toolsSchema.getTool('get_horoscope');
      expect(tool).toBeDefined();
      expect(tool?.name).toBe('get_horoscope');
      expect(tool?.description).toBe("Get today's horoscope for an astrological sign");
    });

    test('should throw existing tool with same name', () => {
      const zodSchema1 = z.object({ param1: z.string() });
      const zodSchema2 = z.object({ param2: z.number() });

      toolsSchema.addZodTool('my_tool', 'First description', zodSchema1);
      expect(() => toolsSchema.addZodTool('my_tool', 'Second description', zodSchema2)).toThrow(
        'Tool with name "my_tool" already exists'
      );
      expect(toolsSchema.size()).toBe(1);
      const tool = toolsSchema.getTool('my_tool');
      expect(tool?.description).toBe('First description');
    });
  });

  describe('addOpenAPITool', () => {
    test('should add a tool with OpenAPI schema', () => {
      const openApiSchema = {
        type: 'object',
        properties: {
          city: { type: 'string', description: 'The city name' },
          units: { type: 'string', enum: ['celsius', 'fahrenheit'] }
        },
        required: ['city']
      };

      toolsSchema.addOpenAPITool('get_weather', 'Get current weather for a city', openApiSchema);

      expect(toolsSchema.size()).toBe(1);
      const tool = toolsSchema.getTool('get_weather');
      expect(tool).toBeDefined();
      expect(tool?.name).toBe('get_weather');
    });
  });

  describe('toVercel', () => {
    test('should convert tools to Vercel AI SDK format', () => {
      const zodSchema = z.object({
        query: z.string(),
        limit: z.number().optional()
      });

      toolsSchema.addZodTool('search', 'Search for information', zodSchema);

      const vercelTools = toolsSchema.toVercel();

      expect(vercelTools).toBeDefined();
      expect(vercelTools.search).toBeDefined();
      expect(vercelTools.search.description).toBe('Search for information');
      expect(vercelTools.search.parameters).toBeDefined();
    });

    test('should handle multiple tools', () => {
      toolsSchema.addZodTool('tool1', 'Description 1', z.object({ a: z.string() }));
      toolsSchema.addZodTool('tool2', 'Description 2', z.object({ b: z.number() }));

      const vercelTools = toolsSchema.toVercel();

      expect(Object.keys(vercelTools)).toHaveLength(2);
      expect(vercelTools.tool1).toBeDefined();
      expect(vercelTools.tool2).toBeDefined();
    });
  });

  describe('toOpenAI', () => {
    test('should convert tools to OpenAI function calling format', () => {
      const zodSchema = z.object({
        location: z.string(),
        unit: z.enum(['celsius', 'fahrenheit']).optional()
      });

      toolsSchema.addZodTool('get_temperature', 'Get temperature for a location', zodSchema);

      const openAITools = toolsSchema.toOpenAI();

      expect(Array.isArray(openAITools)).toBe(true);
      expect(openAITools).toHaveLength(1);
      expect(openAITools[0].type).toBe('function');
      expect(openAITools[0].name).toBe('get_temperature');
      expect(openAITools[0].description).toBe('Get temperature for a location');
      expect(openAITools[0].parameters).toBeDefined();
      expect(openAITools[0].parameters.type).toBe('object');
      expect(openAITools[0].parameters.properties).toBeDefined();
    });

    test('should handle multiple tools', () => {
      toolsSchema.addZodTool('func1', 'Function 1', z.object({ x: z.string() }));
      toolsSchema.addZodTool('func2', 'Function 2', z.object({ y: z.number() }));

      const openAITools = toolsSchema.toOpenAI();

      expect(openAITools).toHaveLength(2);
      expect(openAITools[0].name).toBe('func1');
      expect(openAITools[1].name).toBe('func2');
    });

    test('should work with OpenAPI schema tools', () => {
      const openApiSchema = {
        type: 'object',
        properties: {
          message: { type: 'string' }
        },
        required: ['message']
      };

      toolsSchema.addOpenAPITool('send_message', 'Send a message', openApiSchema);

      const openAITools = toolsSchema.toOpenAI();

      expect(openAITools).toHaveLength(1);
      expect(openAITools[0].parameters).toEqual(openApiSchema);
    });
  });

  describe('getTool', () => {
    test('should return tool if it exists', () => {
      toolsSchema.addZodTool('my_tool', 'My tool', z.object({ param: z.string() }));

      const tool = toolsSchema.getTool('my_tool');
      expect(tool).toBeDefined();
      expect(tool?.name).toBe('my_tool');
    });

    test('should return undefined if tool does not exist', () => {
      const tool = toolsSchema.getTool('non_existent');
      expect(tool).toBeUndefined();
    });
  });

  describe('removeTool', () => {
    test('should remove existing tool and return true', () => {
      toolsSchema.addZodTool('temp_tool', 'Temporary tool', z.object({ x: z.number() }));
      expect(toolsSchema.size()).toBe(1);

      const removed = toolsSchema.removeTool('temp_tool');

      expect(removed).toBe(true);
      expect(toolsSchema.size()).toBe(0);
      expect(toolsSchema.getTool('temp_tool')).toBeUndefined();
    });

    test('should return false when removing non-existent tool', () => {
      const removed = toolsSchema.removeTool('non_existent');
      expect(removed).toBe(false);
    });
  });

  describe('size', () => {
    test('should return correct number of tools', () => {
      expect(toolsSchema.size()).toBe(0);

      toolsSchema.addZodTool('tool1', 'Tool 1', z.object({ a: z.string() }));
      expect(toolsSchema.size()).toBe(1);

      toolsSchema.addZodTool('tool2', 'Tool 2', z.object({ b: z.number() }));
      expect(toolsSchema.size()).toBe(2);

      toolsSchema.removeTool('tool1');
      expect(toolsSchema.size()).toBe(1);
    });
  });

  describe('clear', () => {
    test('should remove all tools', () => {
      toolsSchema.addZodTool('tool1', 'Tool 1', z.object({ a: z.string() }));
      toolsSchema.addZodTool('tool2', 'Tool 2', z.object({ b: z.number() }));
      toolsSchema.addZodTool('tool3', 'Tool 3', z.object({ c: z.boolean() }));

      expect(toolsSchema.size()).toBe(3);

      toolsSchema.clear();

      expect(toolsSchema.size()).toBe(0);
      expect(toolsSchema.getTool('tool1')).toBeUndefined();
      expect(toolsSchema.getTool('tool2')).toBeUndefined();
      expect(toolsSchema.getTool('tool3')).toBeUndefined();
    });
  });
});



================================================
FILE: packages/poml/tests/table.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test } from '@jest/globals';

import {
  Table,
  Task,
  OutputFormat,
  ExampleSet,
  Example,
  ExampleInput,
  ExampleOutput,
  Question
} from 'poml/components';
import { toRecordColumns } from 'poml/components/table';
import { Markup, Serialize } from 'poml/presentation';
import { Code, Text, Inline } from 'poml/essentials';
import { HtmlWriter, MarkdownWriter } from 'poml/writer';
import { read, write } from 'poml';
import { ErrorCollection } from 'poml/base';
import { readFileSync } from '../util/fs';

describe('other formats', () => {
  test('csv', () => {
    const recordColumns = toRecordColumns({ src: __dirname + '/assets/wikitqSampleData.csv' });
    expect(recordColumns.records.length).toBe(17);
    expect(recordColumns.columns!.length).toBe(6);
  });

  test('excel', () => {
    const recordColumns = toRecordColumns({ src: __dirname + '/assets/wikitqSampleData.xlsx' });
    const reference = toRecordColumns({ src: __dirname + '/assets/wikitqSampleData.csv' });
    expect(recordColumns).toStrictEqual(reference);
  });

  test('parse inline', async () => {
    ErrorCollection.clear();
    const table =
      '<poml><table records="start,end,text\n0,10,how are you\n10,20,today" parser="csv"/></poml>';
    const result = write(await read(table));
    expect(result).toMatch(/\| 20  \| today/g);

    const tableIllegal =
      '<poml><table records="start,end,text\\n0,10,how are you\\n10,20,today" parser="csv"/></poml>';
    const resultIllegal = write(await read(tableIllegal));
    expect(resultIllegal).toMatch(
      /\| start \| end \| text\\n0 \| 10 \| how are you\\n10 \| 20 \| today \|/g
    );
    expect(ErrorCollection.empty());
  });

  test('to csv', async () => {
    const writer = new MarkdownWriter();
    const markdown = writer.write(
      await read(<Table src={__dirname + '/assets/wikitqSampleData.csv'} syntax="csv" />)
    );
    expect(markdown).toMatch(readFileSync(__dirname + '/assets/wikitqSampleData.csv', 'utf-8').replaceAll('\r\n', '\n'));

    const markdownSlim = writer.write(
      await read(
        <Table
          src={__dirname + '/assets/wikitqSampleData.csv'}
          syntax="csv"
          selectedRecords={[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
          maxRecords={5}
          maxColumns={4}
        />
      )
    );
    expect(markdownSlim).toMatch(
      /3,México,\.\.\.,5,23\n\.\.\.,\.\.\.,\.\.\.,\.\.\.,\.\.\.\n9,U.S. Virgin Islands,\.\.\.,3,5/gm
    );
  });

  test('to tsv', async () => {
    const writer = new MarkdownWriter();
    const markdown = writer.write(
      await read(<Table src={__dirname + '/assets/wikitqSampleData.csv'} syntax="tsv" />)
    );
    expect(markdown).toMatch(/14\tDominican Republic\t0\t2\t4\t6/g);

    const markdownWithPeriod = writer.write(
      await read(
        <Table
          src={__dirname + '/assets/wikitqSampleData.csv'}
          syntax="tsv"
          writerOptions={{ csvSeparator: '.', csvHeader: false }}
        />
      )
    );
    expect(markdownWithPeriod).toMatch(/9\."U\.S\. Virgin Islands"\.1\.1\.3\.5/g);
  });

  test('to csv no header', async () => {
    const writer = new MarkdownWriter();
    const ir = await read(
      <Table
        src={__dirname + '/assets/wikitqSampleData.csv'}
        syntax="csv"
        writerOptions={{ csvSeparator: ';', csvHeader: false }}
      />
    );
    const markdown = writer.write(ir);
    expect(markdown).toMatch(/^1;Puerto Rico;17;27;13;57\n2;Bahamas;17;15;19;51/g);
  });

  test('list of lists', async () => {
    const recordColumns = toRecordColumns({
      records: [
        [1, 2, 3],
        [4, 5, 6]
      ]
    });
    expect(recordColumns).toStrictEqual({
      records: [
        { '0': 1, '1': 2, '2': 3 },
        { '0': 4, '1': 5, '2': 6 }
      ],
      columns: [
        { field: '0', header: 'Column 0' },
        { field: '1', header: 'Column 1' },
        { field: '2', header: 'Column 2' }
      ]
    });
  });
});

describe('table', () => {
  const records = [
    { name: 'Frozen yoghurt', calories: 159, fat: 6.0, carbs: 24, protein: 4.0 },
    { name: 'Ice cream sandwich', calories: 237, fat: 9.0, carbs: 37, protein: 4.3 },
    { name: 'Eclair', calories: 262, fat: 16.0, carbs: 24, protein: 6.0 },
    { name: 'Cupcake', calories: 305, fat: 3.7, carbs: 67, protein: 4.3 },
    { name: 'Gingerbread', calories: 356, fat: 16.0, carbs: 49, protein: 3.9 }
  ];
  const columns = [
    { field: 'name', header: 'Dessert (100g serving)' },
    { field: 'calories', header: 'Calories' },
    { field: 'fat', header: 'Fat (g)' },
    { field: 'carbs', header: 'Carbs (g)' },
    { field: 'protein', header: 'Protein (g)' }
  ];

  test('markdown', async () => {
    ErrorCollection.clear();
    const table = (
      <Markup.Environment>
        <Table records={records} columns={columns} />
      </Markup.Environment>
    );
    const rendered = await read(table);
    expect(ErrorCollection.empty()).toBe(true);
    expect(rendered).toMatch(/<table><thead><trow><tcell>.*<tbody><trow><tcell>.*<\/table>/g);
    const writer = new MarkdownWriter();
    const markdown = writer.write(rendered);
    const expectMarkdown =
      `| Dessert (100g serving) | Calories | Fat (g) | Carbs (g) | Protein (g) |
      | ---------------------- | -------- | ------- | --------- | ----------- |
      | Frozen yoghurt         | 159      | 6       | 24        | 4           |
      | Ice cream sandwich     | 237      | 9       | 37        | 4.3         |
      | Eclair                 | 262      | 16      | 24        | 6           |
      | Cupcake                | 305      | 3.7     | 67        | 4.3         |
      | Gingerbread            | 356      | 16      | 49        | 3.9         |`.replace(
        /\n\s*/g,
        '\n'
      );
    expect(markdown).toBe(expectMarkdown);

    const writerCollapse = new MarkdownWriter(undefined, { markdownTableCollapse: true } as any);
    const markdownCollapse = writerCollapse.write(rendered);
    expect(markdownCollapse).toMatch('| Frozen yoghurt | 159 | 6 | 24 | 4 |');
  });

  test('markdown selection', async () => {
    const table = (
      <Markup.Environment>
        <Table
          records={records}
          columns={columns}
          selectedColumns={['name', 'fat', 'carbs']}
          maxColumns={2}
          maxRecords={2}
          selectedRecords="1:4"
        />
      </Markup.Environment>
    );
    const rendered = await read(table);
    const writer = new MarkdownWriter();
    const markdown = writer.write(rendered);
    const expectedMarkdown = `| Dessert (100g serving) | ... | Carbs (g) |
      | ---------------------- | --- | --------- |
      | Ice cream sandwich     | ... | 37        |
      | ...                    | ... | ...       |
      | Cupcake                | ... | 67        |`.replace(/\n\s*/g, '\n');
    expect(markdown).toBe(expectedMarkdown);

    const indexedTable = (
      <Markup.Environment>
        <Table
          records={records}
          columns={columns}
          selectedColumns={['index', 'name']}
          maxColumns={2}
          maxRecords={4}
          selectedRecords="1:"
        />
      </Markup.Environment>
    );
    const indexedRendered = await read(indexedTable);
    const indexedMarkdown = writer.write(indexedRendered);
    const indexedExpected = `| Index | Dessert (100g serving) |
      | ----- | ---------------------- |
      | 1     | Ice cream sandwich     |
      | 2     | Eclair                 |
      | 3     | Cupcake                |`.replace(/\n\s*/g, '\n');
    expect(indexedMarkdown).toMatch(indexedExpected);

    const plusIndexedTable = (
      <Markup.Environment markupLang='csv'>
        <Table
          records={records}
          columns={columns}
          selectedColumns='+index'
        />
      </Markup.Environment>
    );
    const plusIndexedRendered = await read(plusIndexedTable);
    const plusIndexedCsv = writer.write(plusIndexedRendered);
    expect(plusIndexedCsv).toMatch('0,Frozen yoghurt,159,6,24,4\n1,Ice cream sandwich,237,9,37,4.3');
  });

  test('xml', async () => {
    const table = (
      <Serialize.Environment serializer="xml">
        <Table records={records} columns={columns} />
      </Serialize.Environment>
    );
    const rendered = write(await read(table));
    expect(rendered).toMatch('<calories>305</calories>');
  });

  test('html', async () => {
    const table = (
      <Markup.Environment markupLang="html">
        <Table records={records} columns={columns} />
      </Markup.Environment>
    );
    const rendered = await read(table);
    expect(rendered).toMatch(/<env presentation="markup" markup-lang="html"><table><thead><trow>/g);
    const writer = new HtmlWriter();
    const html = writer.write(rendered);
    expect(html).toMatch(/<table>\n  <thead>\n/g);
    expect(html).toMatch(/<th>Dessert/g);
  });

  test('serialize', async () => {
    const table = (
      <Markup.Environment>
        <Table records={records} columns={columns} syntax="json" />
      </Markup.Environment>
    );
    const rendered = await read(table);
    const writer = new MarkdownWriter();
    const markdown = writer.write(rendered);
    expect(markdown).toMatch(/```json\n\{[\s\S]*```/g);
  });

  const complexPrompt = (
    <Text>
      <Task>Here is the table to answer this question.</Task>
      <OutputFormat>
        Please provide your explanation first, then answer the question in a short phrase starting
        by 'Therefore, the answer is:'. If the answer contains multiple items, use three hashtags
        {' ('}
        <Code>###</Code>
        {')'} to separate them.
      </OutputFormat>
      <ExampleSet>
        <Example>
          <ExampleInput>
            <Table columns={columns} records={records} />
            <Question>How many calories are in Yogurt?</Question>
          </ExampleInput>
          <ExampleOutput>
            <Inline>
              The table shows the nutritional information of different desserts. Yogurt contains 159
              calories.
            </Inline>{' '}
            Therefore, the answer is: <Inline>159</Inline>
          </ExampleOutput>
        </Example>
      </ExampleSet>
      <Text className="query" name="query">
        <Table columns={columns} records={records.slice(2)} />
        <Question>How many calories are in Cupcake?</Question>
      </Text>
    </Text>
  );

  test('complex', async () => {
    const ir = await read(complexPrompt);
    const messages = write(ir, { speaker: true });
    expect(messages.length).toBe(4);
    expect(messages[3].content).toBe(
      '| Dessert (100g serving) | Calories | Fat (g) | Carbs (g) | Protein (g) |\n' +
        '| ---------------------- | -------- | ------- | --------- | ----------- |\n' +
        '| Eclair                 | 262      | 16      | 24        | 6           |\n' +
        '| Cupcake                | 305      | 3.7     | 67        | 4.3         |\n' +
        '| Gingerbread            | 356      | 16      | 49        | 3.9         |\n' +
        '\n' +
        '**Question:** How many calories are in Cupcake?\n' +
        '\n' +
        '**Answer:**'
    );
  });

  test('complexInJson', async () => {
    const ir = await read(complexPrompt, undefined, undefined, {
      text: { syntax: 'json' },
      table: { syntax: 'json' },
      qa: { captionStyle: 'bold' }
    });
    const output = JSON.parse(write(ir, { speaker: false }) as string);
    expect(Object.keys(output).length).toBe(4);
    expect(Object.keys(output)).toStrictEqual(['task', 'outputFormat', 'examples', 'query']);
  });

  test('file', async () => {
    const result = write(await read(`<table records="{{[{ name: 'Alice', age: 20 }, { name: 'Bob', age: 30 }]}}" />`));
    expect(result).toMatch(`| name  | age |
      | ----- | --- |
      | Alice | 20  |
      | Bob   | 30  |`.replace(/\n\s*/g, '\n'));
  })
});



================================================
FILE: packages/poml/tests/tokenCounterImage.test.ts
================================================
import { describe, expect, test } from '@jest/globals';
import { estimateImageTokens, VisionModel, DetailLevel } from 'poml/util/tokenCounterImage';

describe('estimateImageTokens', () => {
  const cases: { w: number; h: number; model: VisionModel; detail?: DetailLevel; expected: number }[] = [
    { w: 1024, h: 1024, model: 'gpt-4.1-mini', expected: 1024 },
    { w: 1800, h: 2400, model: 'gpt-4.1-mini', expected: 1452 },
    { w: 1024, h: 1024, model: 'gpt-4o', detail: 'high', expected: 765 },
    { w: 2048, h: 4096, model: 'gpt-4o', detail: 'high', expected: 1105 },
    { w: 4096, h: 8192, model: 'gpt-4o', detail: 'low', expected: 85 },
  ];

  test.each(cases)('tokens for %j', ({ w, h, model, detail, expected }) => {
    const got = estimateImageTokens(w, h, { model, detail });
    expect(got).toBe(expected);
  });
});



================================================
FILE: packages/poml/tests/trace.test.tsx
================================================
import fs from '../util/fs';
import * as os from 'os';
import * as path from 'path';
import { describe, beforeEach, afterEach, test, expect } from '@jest/globals';
import { commandLine, setTrace, clearTrace, parseJsonWithBuffers, dumpTrace, read, write } from 'poml';

function stringifyWithBuffers(obj: any): string {
  return JSON.stringify(obj, (_k, v) => {
    if (Buffer.isBuffer(v)) {
      return { __base64__: v.toString('base64') };
    }
    return v;
  });
}

describe('trace dumps', () => {
  let traceDir: string;
  beforeEach(() => {
    traceDir = fs.mkdtempSync(path.join(os.tmpdir(), 'trace-'));
    setTrace(true, traceDir);
  });
  afterEach(() => {
    clearTrace();
    fs.rmSync(traceDir, { recursive: true, force: true });
  });

  test('unused buffer in context is dumped', async () => {
    const buffer = fs.readFileSync(path.join(__dirname, 'assets', 'tomCat.jpg'));
    dumpTrace('<p></p>', { img: buffer });
    const raw = fs.readFileSync(path.join(traceDir, '0001.context.json'), 'utf8');
    expect(raw).toContain('__base64__');
  });

  test('document result includes base64', async () => {
    const markup = `<Document src="${path.join(__dirname, 'assets', 'sampleWord.docx')}" />`;
    await commandLine({ input: markup, speakerMode: false });
    const result = parseJsonWithBuffers(fs.readFileSync(path.join(traceDir, '0001.result.json'), 'utf8'));
    const images = JSON.stringify(result).includes('base64');
    expect(images).toBe(true);
  });

  test('pretty printed result text is dumped', async () => {
    await commandLine({ input: '<p>Hello</p>', speakerMode: false });
    const text = fs.readFileSync(path.join(traceDir, '0001.result.txt'), 'utf8').trim();
    expect(text).toBe('Hello');
  });

  test('env file records source path and enables include', async () => {
    const origDir = fs.mkdtempSync(path.join(os.tmpdir(), 'orig-'));
    const mainPath = path.join(origDir, 'main.poml');
    fs.copyFileSync(path.join(__dirname, 'assets', 'includeChild.poml'), path.join(origDir, 'includeChild.poml'));
    fs.writeFileSync(mainPath, '<poml><include src="includeChild.poml"/></poml>');

    await commandLine({ file: mainPath, speakerMode: false, context: ['name=world'] });

    const envContent = fs.readFileSync(path.join(traceDir, '0001.main.env'), 'utf8').trim();
    expect(envContent).toBe(`SOURCE_PATH=${mainPath}`);

    const tracedMarkupPath = path.join(traceDir, '0001.main.poml');
    const traced = fs.readFileSync(tracedMarkupPath, 'utf8');
    const rerenderIr = await read(traced, undefined, { name: 'world' }, undefined, tracedMarkupPath);
    const rerender = write(rerenderIr);
    expect(fs.existsSync(path.join(traceDir, '0001.main.source.poml'))).toBe(true);
    expect(rerender).toBe('hello world');

    fs.rmSync(origDir, { recursive: true, force: true });
  });
});



================================================
FILE: packages/poml/tests/util.test.tsx
================================================
import * as React from 'react';
import { describe, expect, test } from '@jest/globals';
import { readFileSync } from '../util/fs';
import { component } from 'poml/base';
import { Writable } from 'stream';
import { parseText, readSource } from 'poml/util';
import { preprocessImage } from 'poml/util/image';
import sharp from 'sharp';
import { renderToPipeableStream, renderToString } from 'react-dom/server';
import { reactRender } from 'poml/util/reactRender';

describe('content', () => {
  test('guess type', () => {
    expect(parseText('<p>hello world</p>')).toBe('<p>hello world</p>');
    expect(parseText('-123')).toBe(-123);
    expect(parseText('0.123')).toBe(0.123);
    expect(parseText('0')).toBe(0);
    expect(parseText('True')).toBe(true);
    expect(parseText('FALSE')).toBe(false);
    expect(parseText('NULL')).toBe(null);
    expect(parseText('undefined')).toBe(undefined);
    expect(parseText('[]')).toStrictEqual([]);
    expect(parseText('[1,2,3]')).toStrictEqual([1, 2, 3]);
    expect(parseText('{}')).toStrictEqual({});
    expect(parseText('')).toBe(null);
    expect(parseText('{"invalid": "json"')).toBe('{"invalid": "json"');
  });

  test('parse text', () => {
    expect(parseText('hello', 'string')).toBe('hello');
    expect(parseText('123', 'float')).toBe(123.0);
    expect(parseText('0.123', 'float')).toBe(0.123);
    expect(parseText('1', 'boolean')).toBe(true);
    expect(parseText('0', 'boolean')).toBe(false);
    expect(parseText('something', 'null')).toBe(null);
    expect(parseText('anything', 'undefined')).toBe(undefined);
    expect(parseText('{"hello":"world"}', 'object')).toStrictEqual({ hello: 'world' });
    expect(parseText('[1,2,3]', 'array')).toStrictEqual([1, 2, 3]);
  });

  test('read file', () => {
    const json = readSource('assets/peopleList.json', __dirname);
    expect(json.length).toBe(4);
    expect(json[0]).toStrictEqual({
      id: 1,
      first_name: 'Jeanette',
      last_name: 'Penddreth',
      email: 'jpenddreth0@census.gov',
      gender: 'Female',
      ip_address: '26.58.193.2'
    });

    const image = readSource('assets/tomCat.jpg', __dirname, 'buffer');
    expect(image.length).toBeGreaterThan(0);
  });
});

describe('preprocessImage', () => {
  const sampleImagePath = __dirname + '/assets/tomCat.jpg';
  const sampleImageBase64 = readFileSync(sampleImagePath).toString('base64');

  test('should process an image from a supported file path', async () => {
    const result = await preprocessImage({ src: sampleImagePath });
    expect(result.base64).toBeTruthy();
    expect(result.mimeType).toBe('image/jpeg');
  });

  test('should process an image from base64 data', async () => {
    const result = await preprocessImage({ base64: sampleImageBase64, type: 'image/png' });
    expect(result.base64).toBeTruthy();
    expect(result.mimeType).toBe('image/png');
    const metadata = await sharp(Buffer.from(result.base64, 'base64')).metadata();
    expect(metadata.format).toBe('png');
  });

  test('should resize the image with the resize parameter', async () => {
    const result = await preprocessImage({ base64: sampleImageBase64, type: 'png', resize: 0.5 });
    expect(result.base64).toBeTruthy();
    expect(result.mimeType).toBe('image/png');
    const oldMetadata = await sharp(sampleImagePath).metadata();
    const newMetadata = await sharp(Buffer.from(result.base64, 'base64')).metadata();
    expect(newMetadata.width).toBeCloseTo(oldMetadata.width! * 0.5);
    expect(newMetadata.height).toBeCloseTo(oldMetadata.height! * 0.5);
  });
});

describe('sse', () => {
  test('should render a component with a promise', async () => {
    const dummyPromise = () => new Promise<string>(resolve => setTimeout(() => resolve('done'), 500));
    const CustomComponent = component('custom')((props: any) => {
      const msg = React.use<string>(dummyPromise());
      return <div>{msg}</div>;
    });
    const result = await reactRender(
      <React.Suspense fallback="loading">
        <CustomComponent />
      </React.Suspense>);
    expect(result).toContain('done');
    const resultShell = await reactRender(
      <React.Suspense fallback="loading">
        <CustomComponent />
      </React.Suspense>, true);
    expect(resultShell).toMatch(/loading|done/);
  });
});



================================================
FILE: packages/poml/tests/writer.test.tsx
================================================
import * as React from 'react';

import { describe, expect, test } from '@jest/globals';
import { MarkdownWriter, JsonWriter, MultiMediaWriter, YamlWriter, XmlWriter } from 'poml/writer';
import * as cheerio from 'cheerio';
import { readFileSync } from '../util/fs';
import { ErrorCollection, richContentFromSourceMap } from 'poml/base';

describe('markdown', () => {
  test('markdownSimple', () => {
    const writer = new MarkdownWriter();
    const testIr = `<p><p>hello <b>world</b><nl count="4"/>hahaha</p><h level="3">heading</h><p>new paragraph <code inline="false"> this code </code></p><code lang="ts">console.log("hello world")</code></p>`;
    const result = writer.write(testIr);
    expect(result).toBe(
      'hello **world**\n\n\n\nhahaha\n\n### heading\n\nnew paragraph \n\n```\n this code \n```\n\n`console.log("hello world")`'
    );
  });

  // test('markdownSpace', () => {
  //   const tests = [
  //     {
  //       ir: '<p>hello <!-- comment --> <b>world</b></p>',
  //       result: 'hello **world**'
  //     },
  //     {
  //       ir: '<p>hello <b>world</b>foo</p>',
  //       result: 'hello **world**foo'
  //     },
  //     {
  //       ir: '<p>hello <nl count="2"/> world</p>',
  //       result: 'hello\n\nworld'
  //     },
  //     {
  //       ir: '<p><p>hello <nl count="1"/></p><p>world</p></p>',
  //       result: 'hello\n\nworld'
  //     },
  //     {
  //       ir: '<p><p>hello</p>  <nl count="3"/>  <!-- --> <p> <!-- --> world</p></p>',
  //       result: 'hello\n\n\nworld'
  //     }
  //   ];

  //   for (const test of tests) {
  //     const writer = new MarkdownWriter();
  //     const result = writer.write(test.ir);
  //     // expect(result).toBe(test.result);
  //     console.log(result);
  //   }
  // })

  test('markdownWithEnv', () => {
    const writer = new MarkdownWriter();
    const testEnv = `<p>hello world<code inline="false"><env presentation="serialize"><any name="hello">world</any></p>`;
    const result = writer.write(testEnv);
    expect(result).toBe('hello world\n\n```\n{\n  "hello": "world"\n}\n```');
  });

  test('markdownSourceMapSimple', () => {
    const writer = new MarkdownWriter();
    const simple = `<p>hello world <b>foo</b></p>`;
    const result = writer.writeWithSourceMap(simple);
    expect(result).toStrictEqual([
      { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: 28, content: 'hello world ' },
      { startIndex: 0, endIndex: 0, irStartIndex: 15, irEndIndex: 24, content: '**foo**' }
    ]);
  });

  test('markdownSourceMapWithSpeaker', () => {
    const writer = new MarkdownWriter();
    const withSpeaker = `<p><p speaker="system">hello world</p><p speaker="human">foo bar</p><p>something</p></p>`;
    const result = writer.writeWithSourceMap(withSpeaker);
    expect(result).toStrictEqual([
      { startIndex: 0, endIndex: 0, irStartIndex: 3, irEndIndex: 37, content: 'hello world' },
      { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: 87, content: '\n\n' },
      { startIndex: 0, endIndex: 0, irStartIndex: 38, irEndIndex: 67, content: 'foo bar' },
      { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: 87, content: '\n\n' },
      { startIndex: 0, endIndex: 0, irStartIndex: 68, irEndIndex: 83, content: 'something' }
    ]);
  });

  test('markdownMessagesSourceMap', () => {
    const writer = new MarkdownWriter();
    const withSpeaker = `<p><p speaker="system">hello world</p><p speaker="human">foo bar</p><p>something</p></p>`;
    const result = writer.writeMessagesWithSourceMap(withSpeaker);
    expect(result).toStrictEqual([
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: 3,
        irEndIndex: 37,
        speaker: 'system',
        content: [
          { startIndex: 0, endIndex: 0, irStartIndex: 3, irEndIndex: 37, content: 'hello world' }
        ]
      },
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: 38,
        irEndIndex: 83,
        speaker: 'human',
        content: [
          { startIndex: 0, endIndex: 0, irStartIndex: 38, irEndIndex: 67, content: 'foo bar' },
          { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: 87, content: '\n\n' },
          { startIndex: 0, endIndex: 0, irStartIndex: 68, irEndIndex: 83, content: 'something' }
        ]
      }
    ]);
  });

  test('emptyMessages', () => {
    // Turn off console.warn in this test case.
    const originalWarn = console.warn;
    try {
      console.warn = (m, ...a) => {
        if (m.includes('output')) {
          return;
        }
        originalWarn(m, ...a);
      };
      const writer = new MarkdownWriter();
      const ir = `<p><p speaker="human"></p><p speaker="ai"></p></p>`;
      const direct = writer.writeMessages(ir);
      const segs = writer.writeMessagesWithSourceMap(ir);
      const reconstructed = segs.map(m => ({
        speaker: m.speaker,
        content: richContentFromSourceMap(m.content)
      }));
      expect(direct).toStrictEqual(reconstructed);
      expect(segs).toStrictEqual([
        { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: 0, speaker: 'human', content: [] }
      ]);
    } finally {
      console.warn = originalWarn; // Restore console.warn
    }
  });

  test('markdownWriteMatchesSegments', () => {
    const writer = new MarkdownWriter();
    const ir = `<p><p speaker="human">hello</p><p>world</p></p>`;
    const direct = writer.write(ir);
    const segs = writer.writeWithSourceMap(ir);
    const reconstructed = richContentFromSourceMap(segs);
    expect(direct).toStrictEqual(reconstructed);
  });

  test('markdownWriteMessagesMatchesSegments', () => {
    const writer = new MarkdownWriter();
    const ir = `<p><p speaker="system">hello</p><p speaker="ai">world</p></p>`;
    const direct = writer.writeMessages(ir);
    const segs = writer.writeMessagesWithSourceMap(ir);
    const reconstructed = segs.map(m => ({
      speaker: m.speaker,
      content: richContentFromSourceMap(m.content)
    }));
    expect(direct).toStrictEqual(reconstructed);
  });

  test('markdownSourceMapMultimedia', () => {
    const writer = new MarkdownWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const ir = `<p>hello<env presentation="multimedia"><img base64="${base64}" alt="img"/></env>world</p>`;
    const segs = writer.writeWithSourceMap(ir);
    const rootEnd = ir.length - 1;
    const imgStart = ir.indexOf('<img');
    const imgEnd = ir.indexOf('/>', imgStart) + 1;
    expect(segs).toStrictEqual([
      { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: rootEnd, content: 'hello' },
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: imgStart,
        irEndIndex: imgEnd,
        content: [{ type: 'image', base64, alt: 'img' }]
      },
      { startIndex: 0, endIndex: 0, irStartIndex: 0, irEndIndex: rootEnd, content: 'world' }
    ]);
  });

  test('markdownMessagesSourceMapMultimedia', () => {
    const writer = new MarkdownWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const ir = `<p><p speaker="human">hello</p><p speaker="ai"><env presentation="multimedia"><img base64="${base64}" alt="img"/></env>world</p></p>`;
    const segs = writer.writeMessagesWithSourceMap(ir);
    const humanStart = ir.indexOf('<p speaker="human"');
    const humanEnd = ir.indexOf('</p>', humanStart) + '</p>'.length - 1;
    const aiStart = ir.indexOf('<p speaker="ai"');
    const aiEnd = ir.indexOf('</p>', aiStart) + '</p>'.length - 1;
    const imgStart = ir.indexOf('<img');
    const imgEnd = ir.indexOf('/>', imgStart) + 1;
    const rootEnd = ir.length - 1;
    expect(segs).toStrictEqual([
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: humanStart,
        irEndIndex: humanEnd,
        speaker: 'human',
        content: [
          {
            startIndex: 0,
            endIndex: 0,
            irStartIndex: humanStart,
            irEndIndex: humanEnd,
            content: 'hello'
          }
        ]
      },
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: aiStart,
        irEndIndex: aiEnd,
        speaker: 'ai',
        content: [
          {
            startIndex: 0,
            endIndex: 0,
            irStartIndex: imgStart,
            irEndIndex: imgEnd,
            content: [{ type: 'image', base64, alt: 'img' }]
          },
          { startIndex: 0, endIndex: 0, irStartIndex: aiStart, irEndIndex: aiEnd, content: 'world' }
        ]
      }
    ]);
  });

  test('markdownMessagesSourceMapImagePosition', () => {
    const writer = new MarkdownWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const ir = `<p><p speaker="human"><env presentation="multimedia"><img base64="${base64}" alt="img1" position="top"/></env>Hello</p><p speaker="ai"><env presentation="multimedia"><img base64="${base64}" alt="img2" position="top"/></env>World</p></p>`;
    const segs = writer.writeMessagesWithSourceMap(ir);
    const humanStart = ir.indexOf('<p speaker="human"');
    const humanEnd = ir.indexOf('</p>', humanStart) + '</p>'.length - 1;
    const aiStart = ir.indexOf('<p speaker="ai"');
    const aiEnd = ir.indexOf('</p>', aiStart) + '</p>'.length - 1;
    const img1Start = ir.indexOf('<img', humanStart);
    const img1End = ir.indexOf('/>', img1Start) + 1;
    const img2Start = ir.indexOf('<img', aiStart);
    const img2End = ir.indexOf('/>', img2Start) + 1;
    expect(segs).toStrictEqual([
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: humanStart,
        irEndIndex: humanEnd,
        speaker: 'human',
        content: [
          {
            startIndex: 0,
            endIndex: 0,
            irStartIndex: img1Start,
            irEndIndex: img1End,
            content: [{ type: 'image', base64, alt: 'img1' }]
          },
          {
            startIndex: 0,
            endIndex: 0,
            irStartIndex: humanStart,
            irEndIndex: humanEnd,
            content: 'Hello'
          }
        ]
      },
      {
        startIndex: 0,
        endIndex: 0,
        irStartIndex: aiStart,
        irEndIndex: aiEnd,
        speaker: 'ai',
        content: [
          {
            startIndex: 0,
            endIndex: 0,
            irStartIndex: img2Start,
            irEndIndex: img2End,
            content: [{ type: 'image', base64, alt: 'img2' }]
          },
          { startIndex: 0, endIndex: 0, irStartIndex: aiStart, irEndIndex: aiEnd, content: 'World' }
        ]
      }
    ]);
  });

  test('markdownCharLimit', () => {
    const writer = new MarkdownWriter();
    const ir = `<p char-limit="5">helloworld</p>`;
    const result = writer.write(ir);
    expect(result).toBe('hello (...truncated)');
  });

  test('freeCharLimit', () => {
    const writer = new MarkdownWriter();
    const ir = `<p><env presentation="free" char-limit="4">abcdefg</env></p>`;
    const result = writer.write(ir);
    expect(result).toBe('abcd (...truncated)');
  });

  test('markdownCharLimitStart', () => {
    const writer = new MarkdownWriter(undefined, { truncateDirection: 'start' } as any);
    const ir = `<p char-limit="5">helloworld</p>`;
    const result = writer.write(ir);
    expect(result).toBe(' (...truncated)world');
  });

  test('markdownCharLimitMiddleCustomMarker', () => {
    const writer = new MarkdownWriter(undefined, { truncateDirection: 'middle', truncateMarker: '[cut]' } as any);
    const ir = `<p char-limit="5">helloworld</p>`;
    const result = writer.write(ir);
    expect(result).toBe('hel[cut]ld');
  });

  test('markdownPriorityProperty', () => {
    const writer: any = new MarkdownWriter();
    const $ = cheerio.load('<p priority="2">abc</p>', { xml: { xmlMode: true, withStartIndices: true, withEndIndices: true } }, false);
    const box = writer.makeBox('abc', 'inline', $('p'));
    expect(box.priority).toBe(2);
  });

  test('markdownPriorityRemoval', () => {
    const writer = new MarkdownWriter();
    const ir = '<p char-limit="5"><span priority="1">hello</span><span priority="2">world</span></p>';
    const result = writer.write(ir);
    expect(result).toBe('world');
  });

  test('markdownPriorityTruncateAfterRemoval', () => {
    const writer = new MarkdownWriter();
    const ir = '<p char-limit="3"><span priority="1">ab</span><span priority="1">cd</span></p>';
    const result = writer.write(ir);
    expect(result).toBe('abc (...truncated)');
  });

  test('markdownTokenLimit', () => {
    const writer = new MarkdownWriter();
    const ir = `<p token-limit="1">hello world</p>`;
    const result = writer.write(ir);
    expect(result).toBe('hello (...truncated)');
  });

  test('freeTokenLimit', () => {
    const writer = new MarkdownWriter();
    const ir = `<p><env presentation="free" token-limit="1">hello world</env></p>`;
    const result = writer.write(ir);
    expect(result).toBe('hello (...truncated)');
  });

  test('markdownPriorityRemovalToken', () => {
    const writer = new MarkdownWriter();
    const ir = '<p token-limit="1"><span priority="1">hello</span><span priority="2">world</span></p>';
    const result = writer.write(ir);
    expect(result).toBe('world');
  });

  test('markdownPriorityTokenTruncateAfterRemoval', () => {
    const writer = new MarkdownWriter();
    const ir = '<p token-limit="1"><span priority="1">hi</span><span priority="1">there</span></p>';
    const result = writer.write(ir);
    expect(result).toBe('h (...truncated)');
  });
});

describe('serialize', () => {
  test('jsonSimple', () => {
    const writer = new JsonWriter();
    const testIr = `<any><any name="hello">world</any><any name="foo"><any type="integer">123</any><any type="boolean">false</any></any></any>`;
    const result = writer.write(testIr);
    expect(result).toBe('{\n  "hello": "world",\n  "foo": [\n    123,\n    false\n  ]\n}');
  });

  test('jsonDataObject', () => {
    const writer = new JsonWriter();
    const testIr = `<obj data="{&quot;hello&quot;:&quot;world&quot;,&quot;foo&quot;:[123,false]}"/>`;
    const result = writer.write(testIr);
    expect(result).toBe('{\n  "hello": "world",\n  "foo": [\n    123,\n    false\n  ]\n}');
  });

  test('yaml', () => {
    const writer = new YamlWriter();
    const testIr = `<any><any name="hello">world</any><any name="foo"><any type="integer">123</any><any type="boolean">false</any></any></any>`;
    const result = writer.write(testIr);
    expect(result).toBe('hello: world\nfoo:\n  - 123\n  - false');
  });

  test('xml', () => {
    const writer = new XmlWriter();
    const testIr = `<any><any name="hello">world</any><any name="foo"><any type="integer">123</any><any type="boolean">false</any></any></any>`;
    const result = writer.write(testIr);
    expect(result).toBe(
      '<hello>world</hello>\n<foo>\n  <item>123</item>\n  <item>false</item>\n</foo>'
    );
  });

  test('xmlNestMultimedia', async () => {
    const writer = new XmlWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const imageIr = `<env presentation="multimedia"><img base64="${base64}" alt="example"/></env>`;
    const testIr = `<env presentation="serialize" serializer="xml"><any>${imageIr}</any></env>`;
    ErrorCollection.clear();
    writer.write(testIr);
    expect(ErrorCollection.first().message).toMatch('Invalid presentation:');
  });
});

describe('free', () => {
  test('freeText', () => {
    const writer = new MarkdownWriter();
    const testIr = `<env presentation="free">hello\nworld</env>`;
    const result = writer.write(testIr);
    expect(result).toBe('hello\nworld');

    const testIr2 = `<env presentation="free">hello\nworld<text>\n\n</text>hahaha</env>`;
    const result2 = writer.write(testIr2);
    expect(result2).toBe('hello\nworld\n\nhahaha');
  });

  test('textWithEnv', () => {
    const writer = new MarkdownWriter();
    const testIr = `<env presentation="free">hello\nworld<env presentation="serialize"><any name="hello">world</any></env></env>`;
    const result = writer.write(testIr);
    expect(result).toBe('hello\nworld{\n  "hello": "world"\n}');
  });
});

describe('multimedia', () => {
  test('image', () => {
    const writer = new MultiMediaWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const testIr = `<env presentation="multimedia"><img base64="${base64}" alt="example"/></env>`;
    ErrorCollection.clear();
    const result = writer.write(testIr);
    expect(ErrorCollection.empty()).toBe(true);
    expect(result).toStrictEqual([{ type: 'image', base64, alt: 'example' }]);
  });

  test('imageInText', () => {
    const writer = new MarkdownWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const ir1 = `<env presentation="markup" markup-lang="markdown">hello\nworld<env presentation="multimedia"><img base64="${base64}" alt="example1"/><img base64="${base64}" alt="example2"/></env></env>`;
    ErrorCollection.clear();
    const result1 = writer.write(ir1);
    expect(ErrorCollection.empty()).toBe(true);
    expect(result1).toStrictEqual([
      'hello\nworld',
      { type: 'image', base64, alt: 'example1' },
      { type: 'image', base64, alt: 'example2' }
    ]);

    const ir2 = `<env presentation="markup" markup-lang="markdown">hello\nworld<env presentation="multimedia"><img base64="${base64}" alt="example1"/></env><p>hahaha</p><env presentation="multimedia"><img base64="${base64}" alt="example2"/></env></env>`;
    const result2 = writer.write(ir2);
    expect(result2).toStrictEqual([
      'hello\nworld',
      { type: 'image', base64, alt: 'example1' },
      'hahaha',
      { type: 'image', base64, alt: 'example2' }
    ]);
  });

  test('imagePosition', () => {
    const writer = new MarkdownWriter();
    const base64 = readFileSync(__dirname + '/assets/tomCat.jpg').toString('base64');
    const ir = `<env presentation="markup" markup-lang="markdown">hello<env presentation="multimedia"><img base64="${base64}" alt="example1" position="top"/></env>world<p>foo<env presentation="multimedia"><img base64="${base64}" alt="example2" position="bottom"/></env></p></env>`;
    ErrorCollection.clear();
    const result = writer.write(ir);
    expect(ErrorCollection.empty()).toBe(true);
    expect(result).toStrictEqual([
      { type: 'image', base64, alt: 'example1' },
      'helloworld\n\nfoo',
      { type: 'image', base64, alt: 'example2' }
    ]);
  });
});



================================================
FILE: packages/poml/tests/assets/galleryTest.json
================================================
{
    "prompt": "How can I improve the performance of this code?\n\nPlease do this quick.",
    "files": [
        "ask.poml"
    ]
}


================================================
FILE: packages/poml/tests/assets/includeChild.poml
================================================
<p>hello {{name}}</p>



================================================
FILE: packages/poml/tests/assets/includeNested.poml
================================================
<include src="includeChild.poml"/>
<include src="includeNumber.poml" for="i in [3,4]"/>



================================================
FILE: packages/poml/tests/assets/includeNumber.poml
================================================
<p>{{i}}</p>



================================================
FILE: packages/poml/tests/assets/peopleList.json
================================================
[
  {
    "id": 1,
    "first_name": "Jeanette",
    "last_name": "Penddreth",
    "email": "jpenddreth0@census.gov",
    "gender": "Female",
    "ip_address": "26.58.193.2"
  },
  {
    "id": 2,
    "first_name": "Giavani",
    "last_name": "Frediani",
    "email": "gfrediani1@senate.gov",
    "gender": "Male",
    "ip_address": "229.179.4.212"
  },
  {
    "id": 3,
    "first_name": "Noell",
    "last_name": "Bea",
    "email": "nbea2@imageshack.us",
    "gender": "Female",
    "ip_address": "180.66.162.255"
  },
  {
    "id": 4,
    "first_name": "Willard",
    "last_name": "Valek",
    "email": "wvalek3@vk.com",
    "gender": "Male",
    "ip_address": "67.76.188.26"
  }
]



================================================
FILE: packages/poml/tests/assets/sampleWebpage.html
================================================
<html>
<!-- Text between angle brackets is an HTML tag and is not displayed.
Most tags, such as the HTML and /HTML tags that surround the contents of
a page, come in pairs; some tags, like HR, for a horizontal rule, stand 
alone. Comments, such as the text you're reading, are not displayed when
the Web page is shown. The information between the HEAD and /HEAD tags is 
not displayed. The information between the BODY and /BODY tags is displayed.-->
<head>
<title>Enter a title, displayed at the top of the window.</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<!-- The information between the BODY and /BODY tags is displayed.-->
<body>
<h1>Enter the main heading, usually the same as the title.</h1>
<p>Be <b>bold</b> in stating your key points. Put them in a list: </p>
<ul>
<li>The first item in your list</li>
<li>The second item; <i>italicize</i> key words</li>
</ul>
<p>Improve your image by including an image. </p>
<p><img src="http://www.mygifs.com/CoverImage.gif" alt="A Great HTML Resource"></p>
<p>Add a link to your favorite <a href="https://www.dummies.com/">Web site</a>.
Break up your page with a horizontal rule or two. </p>
<hr>
<p>Finally, link to <a href="page2.html">another page</a> in your own Web site.</p>
<!-- And add a copyright notice.-->
<p>© Wiley Publishing, 2011</p>
<script type="text/javascript">
  // This is a comment in JavaScript
  alert("Hello, world!");
</script>
</body>
</html>


================================================
FILE: packages/poml/tests/assets/sampleWord.docx
================================================
[Binary file]


================================================
FILE: packages/poml/tests/assets/wikitqSampleData.csv
================================================
Rank,Nation,Gold,Silver,Bronze,Total
1,Puerto Rico,17,27,13,57
2,Bahamas,17,15,19,51
3,México,9,9,5,23
4,Jamaica,8,6,4,18
5,Barbados,7,3,6,16
6,Trinidad and Tobago,7,2,2,11
7,Venezuela,3,3,8,14
8,Colombia,3,1,2,6
9,U.S. Virgin Islands,1,1,3,5
10,Martinique,1,1,0,2
11,Antigua and Barbuda,1,0,1,2
12,Suriname,1,0,0,1
13,Bermuda,0,4,2,6
14,Dominican Republic,0,2,4,6
15,Panamá,0,1,2,3
16,Cayman Islands,0,0,2,2
16,Saint Kitts and Nevis,0,0,2,2


================================================
FILE: packages/poml/tests/assets/wikitqSampleData.xlsx
================================================
[Binary file]


================================================
FILE: packages/poml/tests/assets/directory/.ignoremeplease
================================================
abcde
fhijk


================================================
FILE: packages/poml/tests/assets/directory/anotherdirectory/123.jsx
================================================
function Main() {
    return <div>Hello world</div>;
}



================================================
FILE: packages/poml/tests/assets/directory/anotherdirectory/456.cpp
================================================
#include <iostream>
int main() {
    std::cout << "Hello from anotherdirectory/456.cpp" << std::endl;
    return 0;
}



================================================
FILE: packages/poml/tests/assets/directory/nested1/nested2/nested3/nested5/nestedFile.txt
================================================
hello
world


================================================
FILE: packages/poml/tests/assets/directory/nested1/nested2/nested4/.ignoreplease
================================================
12345
67890



================================================
FILE: packages/poml/util/audio.ts
================================================
import fs from './fs';
import path from 'path';

interface PreprocessAudioArgs {
  src?: string;
  base64?: string;
  type?: string;
}

interface ProcessedAudio {
  base64: string;
  mimeType: string;
}

function readAudio(src?: string, base64?: string): Buffer {
  if (src) {
    return fs.readFileSync(src);
  }
  if (base64) {
    return Buffer.from(base64, 'base64');
  }
  throw new Error('src or base64 is required');
}

function canonicalizeType(type: string | undefined, src?: string): string {
  if (type) {
    return type.startsWith('audio/') ? type : `audio/${type}`;
  }
  if (src) {
    const ext = path.extname(src).toLowerCase();
    switch (ext) {
      case '.mp3': return 'audio/mpeg';
      case '.wav': return 'audio/wav';
      case '.ogg': return 'audio/ogg';
      case '.flac': return 'audio/flac';
      case '.aac': return 'audio/aac';
      default: throw new Error('Cannot determine audio format');
    }
  }
  throw new Error('Cannot determine audio format');
}

export async function preprocessAudio(args: PreprocessAudioArgs): Promise<ProcessedAudio> {
  const { src, base64, type } = args;
  const buffer = readAudio(src, base64);
  const mimeType = canonicalizeType(type, src);
  return {
    base64: buffer.toString('base64'),
    mimeType,
  };
}



================================================
FILE: packages/poml/util/fs.ts
================================================
import * as fs from 'fs';

export const readFileSync = fs.readFileSync;
export const writeFileSync = fs.writeFileSync;
export const existsSync = fs.existsSync;
export const mkdirSync = fs.mkdirSync;
export const openSync = fs.openSync;
export const closeSync = fs.closeSync;
export const writeSync = fs.writeSync;
export const symlinkSync = fs.symlinkSync;

export default fs;



================================================
FILE: packages/poml/util/image.ts
================================================
import sharp from 'sharp';

interface PreprocessImageArgs {
  src?: string;
  base64?: string;
  type?: string;
  maxWidth?: number;
  maxHeight?: number;
  resize?: number;
}

interface ProcessedImage {
  base64: string;
  mimeType: string;
}

function readImage(src?: string, base64?: string) {
  if (src) {
    return sharp(src);
  }
  if (base64) {
    return sharp(Buffer.from(base64, 'base64'));
  }
  throw new Error('src or base64 is required');
}

function resizeImage(image: sharp.Sharp, metadata: sharp.Metadata, maxWidth?: number, maxHeight?: number, resize?: number): sharp.Sharp {
  let width = metadata.width || 1;
  let height = metadata.height || 1;
  const resizes: number[] = [];
  if (resize) {
    resizes.push(resize);
  }
  if (maxWidth) {
    resizes.push(maxWidth / width);
  }
  if (maxHeight) {
    resizes.push(maxHeight / height);
  }
  if (resizes.length === 0) {
    return image;
  }
  const resizeFactor = Math.min(...resizes);
  return image.resize(Math.round(width * resizeFactor), Math.round(height * resizeFactor));
}

function convertType(image: sharp.Sharp, metadata: sharp.Metadata, type?: string): [sharp.Sharp, string] {
  let fileType: string = metadata.format || '';
  if (!fileType) {
    throw new Error('Cannot determine image format');
  }

  if (type) {
    fileType = type.startsWith('image/') ? type.split('/', 2)[1] : type;
    image = image.toFormat(fileType as any);
  }

  return [image, fileType];
}

export async function preprocessImage(args: PreprocessImageArgs): Promise<ProcessedImage> {
  const { src, base64, type, maxWidth, maxHeight, resize } = args;
  let sharpObj = readImage(src, base64);
  const metadata = await sharpObj.metadata();
  const resizedImage = resizeImage(sharpObj, metadata, maxWidth, maxHeight, resize);
  const [converted, fileType] = convertType(resizedImage, metadata, type);

  return {
    base64: await converted.toBuffer().then(buffer => buffer.toString('base64')),
    mimeType: 'image/' + fileType
  }
}

export async function getImageWidthHeight(base64: string): Promise<{ width: number; height: number }> {
  const image = sharp(Buffer.from(base64, 'base64'));
  const metadata = await image.metadata();
  if (!metadata.width || !metadata.height) {
    throw new Error('Cannot determine image dimensions');
  }
  return { width: metadata.width, height: metadata.height };
}



================================================
FILE: packages/poml/util/index.ts
================================================
import { readFileSync } from './fs';
import path from "path";

export const deepMerge = (target: any, source: any): any => {
  // Object can not be array or class instance (like children).
  const isObject = (item: any) => {
    return (
      item !== undefined &&
      item !== null &&
      typeof item === 'object' &&
      !Array.isArray(item) &&
      !('$$typeof' in item) &&
      // https://stackoverflow.com/questions/57227185/how-to-detect-if-a-variable-is-a-pure-javascript-object
      item.constructor === Object
    );
  };

  if (isObject(target) && isObject(source)) {
    target = { ...target }; // Copy target;
    for (const key in source) {
      if (isObject(source[key])) {
        if (!target[key]) {
          Object.assign(target, { [key]: {} });
        }
        if (isObject(target[key])) {
          target[key] = deepMerge(target[key], source[key]);
        } else {
          Object.assign(target, { [key]: source[key] });
        }
      } else {
        Object.assign(target, { [key]: source[key] });
      }
    }
  }

  return target;
};

export type AnyValue = 'string' | 'integer' | 'float' | 'boolean' | 'array' | 'object' | 'buffer' | 'null' | 'undefined';

export const readSource = (source: string, directory?: string | undefined, type?: AnyValue): any => {
  // Read file content and convert to type.
  // Check whether path is absolute or relative.
  source = !path.isAbsolute(source) && directory ? path.join(directory, source) : source;
  if (type === 'buffer') {
    const buffer: Buffer = readFileSync(source);
    return buffer;
  } else {
    const text: string = readFileSync(source, 'utf8');
    return parseText(text, type);
  }
}

export const parseText = (object: string | Buffer, type?: AnyValue): any => {
  if (typeof object === 'string') {
    if (type === 'buffer') {
      return Buffer.from(object);
    } else if (type === 'string') {
      return object;
    } else if (!type) {
      return guessStringType(object)[0];
    } else if (type === 'integer') {
      return parseInt(object);
    } else if (type === 'float') {
      return parseFloat(object);
    } else if (type === 'boolean') {
      if (object.toLowerCase() === 'true' || object === '1') {
        return true;
      } else if (object.toLowerCase() === 'false' || object === '0') {
        return false;
      } else {
        throw new Error('Invalid boolean value: ' + object);
      }
    } else if (type === 'array' || type === 'object') {
      return JSON.parse(object);
    } else if (type === 'null') {
      return null;
    } else if (type === 'undefined') {
      return undefined;
    } else {
      throw new Error('Invalid type: ' + type);
    }
  } else if (Buffer.isBuffer(object)) {
    if (type === 'buffer') {
      return object;
    } else {
      return parseText(object.toString(), type);
    }
  } else {
    throw new Error('Invalid object type (expect buffer or string): ' + typeof object);
  }
}

export const guessStringType = (value: string): [any, AnyValue] => {
  if (value.toLowerCase() === 'null' || value === '') {
    return [null, 'null'];
  } else if (value.toLowerCase() === 'undefined') {
    return [undefined, 'undefined'];
  } else if (value.toLowerCase() === 'true') {
    return [true, 'boolean'];
  } else if (value.toLowerCase() === 'false') {
    return [false, 'boolean'];
  } else if (!isNaN(Number(value))) {
    // https://stackoverflow.com/questions/16775547/javascript-guess-data-type-from-string
    if (parseFloat(value) === parseInt(value)) {
      return [parseInt(value), "integer"];
    } else {
      return [parseFloat(value), "float"];
    }
  } else if (/^\d*(\.|,)\d*$/.test(value) || /^(\d{0,3}(,)?)+\.\d*$/.test(value) || /^(\d{0,3}(\.)?)+,\d*$/.test(value)) {
    return [Number(value), "float"];
  } else {
    try {
      const parsed = JSON.parse(value);
      if (Array.isArray(parsed)) {
        return [parsed, 'array'];
      } else {
        return [parsed, 'object'];
      }
    } catch (e) {
      return [value, 'string'];
    }
  }
}




================================================
FILE: packages/poml/util/pdf.ts
================================================
const log = console.log;
console.log = (m, ...a) =>
  /Cannot polyfill `(DOMMatrix|Path2D)`/.test(m) ? null : log(m, ...a);

// import * as PDFJS from 'pdfjs-dist';
// import PDFJS from 'pdfjs-dist/legacy/build/pdf.js';
import * as PDFJS from 'pdfjs-dist/legacy/build/pdf.js';

let pdfjs = PDFJS;

if (PDFJS.GlobalWorkerOptions === undefined) {
  // in esm
  pdfjs = (PDFJS as any).default;
} else {
  // in commonjs
  pdfjs = PDFJS;
}

pdfjs.GlobalWorkerOptions.workerSrc = 'pdfjs-dist/legacy/build/pdf.worker.js';

console.log = log; // restore original console.log

export async function getNumPages(pdfBuffer: ArrayBuffer | Buffer): Promise<number> {
  const uint8Array = pdfBuffer instanceof ArrayBuffer ? new Uint8Array(pdfBuffer) : new Uint8Array(pdfBuffer);
  const loadingTask = pdfjs.getDocument({ data: uint8Array });
  const pdfDocument = await loadingTask.promise;
  return pdfDocument.numPages;
}

export async function pdfParse(pdfBuffer: ArrayBuffer | Buffer, maxPages?: number): Promise<string> {
  const uint8Array = pdfBuffer instanceof ArrayBuffer ? new Uint8Array(pdfBuffer) : new Uint8Array(pdfBuffer);
  const loadingTask = pdfjs.getDocument({ data: uint8Array });
  const pdfDocument = await loadingTask.promise;

  let fullTexts: string[] = [];

  if (maxPages == undefined) {
    maxPages = pdfDocument.numPages;
  } else {
    maxPages = Math.min(maxPages, pdfDocument.numPages);
  }

  for (let pageNum = 1; pageNum <= maxPages; pageNum++) {
    const page = await pdfDocument.getPage(pageNum);
    const pageText = await extractTextFromPage(page);
    fullTexts.push(pageText);
  }

  return fullTexts.join('\n\n');
}

async function extractTextFromPage(page: PDFJS.PDFPageProxy): Promise<string> {
  const textContent = await page.getTextContent();
  let lastY, text = '';
  for (let item of textContent.items) {
    if (lastY == (item as any).transform[5] || !lastY) {
      text += (item as any).str;
    } else {
      text += '\n' + (item as any).str;
    }
    lastY = (item as any).transform[5];
  }
  return text;
}



================================================
FILE: packages/poml/util/reactRender.ts
================================================
import { renderToPipeableStream } from 'react-dom/server';

import { Writable } from 'stream';

const pipeableStreamToString = async (
  stream: (destination: NodeJS.WritableStream) => NodeJS.WritableStream
) => {
  return new Promise<string>((resolve, reject) => {
    const chunks: Buffer[] = [];
    const writable = new Writable({
      write(chunk, encoding, callback) {
        chunks.push(chunk);
        callback();
      },
      final(callback) {
        resolve(Buffer.concat(chunks).toString());
        callback();
      },
      destroy(err, callback) {
        reject(err);
        callback(err);
      }
    });
    stream(writable);
  });
};

export const reactRender = (element: React.ReactElement, shellOnly?: boolean) => {
  const promise = new Promise<string>((resolve, reject) => {
    const { pipe } = renderToPipeableStream(element, {
      onAllReady: () => {
        if (!shellOnly) {
          resolve(pipeableStreamToString(pipe));
        }
      },
      onError: (error, errorInfo) => {
        console.error(errorInfo);
        reject(error);
      },
      onShellError: error => {
        reject(error);
      },
      onShellReady: () => {
        if (shellOnly) {
          resolve(pipeableStreamToString(pipe));
        }
      }
    });
  });
  return promise;
};



================================================
FILE: packages/poml/util/schema.ts
================================================
import { z } from 'zod';
import { jsonSchemaToZod } from 'json-schema-to-zod';

/**
 * A unified schema representation that can work with both Zod and OpenAPI schemas.
 * Provides conversion methods between different schema formats.
 */
export class Schema {

  private constructor(
    private zodSchema?: z.ZodTypeAny,
    private openApiSchema?: any
  ) {
    if (!zodSchema && !openApiSchema) {
      throw new Error("At least one schema must be provided");
    }
    this.zodSchema = zodSchema;
    this.openApiSchema = openApiSchema;
  }

  /**
   * Creates a Schema instance from an OpenAPI schema object.
   * @param openApiSchema The OpenAPI schema object
   * @returns A new Schema instance
   */
  public static fromOpenAPI(openApiSchema: any): Schema {
    const schema = new Schema(undefined, openApiSchema);
    // TODO: openapi schema full validation should be added here
    if (typeof openApiSchema !== 'object' || openApiSchema === null) {
      throw new Error("Invalid OpenAPI schema provided");
    }
    return schema;
  }

  /**
   * Creates a Schema instance from a Zod schema.
   * @param zodSchema The Zod schema
   * @returns A new Schema instance
   */
  public static fromZod(zodSchema: z.ZodTypeAny): Schema {
    return new Schema(zodSchema);
  }

  /**
   * Converts the schema to a Zod schema.
   * @returns The Zod schema representation
   * @throws Error if no schema is available
   */
  public toZod(): z.ZodTypeAny {
    if (this.zodSchema) {
      return this.zodSchema;
    } else if (this.openApiSchema) {
      // It's not safe and even prohibited to use eval in browser environments.
      // We need to make z available in the eval context
      const zodSchemaString = jsonSchemaToZod(this.openApiSchema);
      // Create a function that has z in scope and evaluate the schema string
      const evalWithZ = new Function('z', `return ${zodSchemaString}`);
      return evalWithZ(z) as z.ZodTypeAny;
    } else {
      throw new Error("No Zod schema available");
    }
  }

  /**
   * Converts the schema to an OpenAPI/JSON schema format.
   * @returns The OpenAPI schema representation
   * @throws Error if no schema is available
   */
  public toOpenAPI(): any {
    if (this.openApiSchema) {
      return this.openApiSchema;
    } else if (this.zodSchema) {
      const schema = z.toJSONSchema(this.zodSchema);
      // pop the $schema property if it exists
      if (schema.$schema) {
        delete schema.$schema;
      }
      return schema;
    } else {
      throw new Error("No schema available");
    }
  }
}

/**
 * Represents a tool schema with name, description, and input parameters.
 */
interface ToolSchema {
  name: string;
  description: string | undefined;
  inputSchema: Schema;
}

/**
 * Manages a collection of tool schemas and provides conversion methods
 * for different AI provider formats (OpenAI, Vercel, etc.).
 */
export class ToolsSchema {
  private tools: Map<string, ToolSchema>;

  public constructor() {
    this.tools = new Map<string, ToolSchema>();
  }

  /**
   * Adds a tool with a Zod schema to the collection.
   * @param name The name of the tool
   * @param description A description of what the tool does
   * @param zodSchema The Zod schema for the tool's input parameters
   */
  public addZodTool(name: string, description: string | undefined, zodSchema: z.ZodTypeAny): void {
    const schema = Schema.fromZod(zodSchema);
    if (this.tools.has(name)) {
      throw new Error(`Tool with name "${name}" already exists`);
    }
    this.tools.set(name, {
      name,
      description,
      inputSchema: schema
    });
  }

  /**
   * Adds a tool with an OpenAPI schema to the collection.
   * @param name The name of the tool
   * @param description A description of what the tool does
   * @param openApiSchema The OpenAPI schema for the tool's input parameters
   */
  public addOpenAPITool(name: string, description: string | undefined, openApiSchema: any): void {
    const schema = Schema.fromOpenAPI(openApiSchema);
    if (this.tools.has(name)) {
      throw new Error(`Tool with name "${name}" already exists`);
    }
    this.tools.set(name, {
      name,
      description,
      inputSchema: schema
    });
  }

  /**
   * Add a tool with pre-parsed schema.
   * @param name The name of the tool
   * @param description A description of what the tool does
   * @param schema The pre-parsed schema for the tool's input parameters
   */
  public addTool(name: string, description: string | undefined, schema: Schema): void {
    if (this.tools.has(name)) {
      throw new Error(`Tool with name "${name}" already exists`);
    }
    this.tools.set(name, {
      name,
      description,
      inputSchema: schema
    });
  }

  /**
   * Converts the tools collection to Vercel AI SDK format.
   * @returns An object mapping tool names to their Vercel AI SDK representations
   */
  public toVercel(): any {
    const vercelTools: Record<string, any> = {};
    
    for (const [name, tool] of this.tools) {
      vercelTools[name] = {
        description: tool.description,
        parameters: tool.inputSchema.toZod()
      };
    }
    
    return vercelTools;
  }

  /**
   * Converts the tools collection to OpenAI function calling format.
   * @returns An array of OpenAI function definitions
   * @example
   * [
   *   {
   *     "type": "function",
   *     "name": "get_horoscope",
   *     "description": "Get today's horoscope for an astrological sign.",
   *     "parameters": {
   *       "type": "object",
   *       "properties": {
   *         "sign": {
   *           "type": "string",
   *           "description": "An astrological sign like Taurus or Aquarius"
   *         }
   *       },
   *       "required": ["sign"]
   *     }
   *   }
   * ]
   */
  public toOpenAI(): any {
    const openAITools: any[] = [];
    
    for (const [_, tool] of this.tools) {
      openAITools.push({
        type: 'function',
        name: tool.name,
        description: tool.description,
        parameters: tool.inputSchema.toOpenAPI()
      });
    }
    
    return openAITools;
  }

  /**
   * Gets a tool by name.
   * @param name The name of the tool to retrieve
   * @returns The tool schema if found, undefined otherwise
   */
  public getTool(name: string): ToolSchema | undefined {
    return this.tools.get(name);
  }

  /**
   * Removes a tool from the collection.
   * @param name The name of the tool to remove
   * @returns true if the tool was removed, false if it didn't exist
   */
  public removeTool(name: string): boolean {
    return this.tools.delete(name);
  }

  /**
   * Gets the number of tools in the collection.
   * @returns The number of tools
   */
  public size(): number {
    return this.tools.size;
  }

  /**
   * Clears all tools from the collection.
   */
  public clear(): void {
    this.tools.clear();
  }

}


================================================
FILE: packages/poml/util/tokenCounterImage.ts
================================================
/**
 * Image-token estimator covering OpenAI’s three vision price rules
 * (docs dated 2025-07-01).
 */

export type VisionModel =
  | 'gpt-4.1-mini' | 'gpt-4.1-nano' | 'o4-mini'
  | 'gpt-4o' | 'gpt-4.1' | 'gpt-4.5' | '4o-mini'
  | 'o1' | 'o1-pro' | 'o3' | 'computer-use-preview'
  | 'gpt-image-1';

export type DetailLevel = 'low' | 'high' | 'auto';

const PATCH_MODELS: Record<VisionModel, { factor: number }> = {
  'gpt-4.1-mini':        { factor: 1.62 },
  'gpt-4.1-nano':        { factor: 2.46 },
  'o4-mini':             { factor: 1.72 },
  // non-patch models:
  'gpt-4o':              { factor: 0 },
  'gpt-4.1':             { factor: 0 },
  'gpt-4.5':             { factor: 0 },
  '4o-mini':             { factor: 0 },
  'o1':                  { factor: 0 },
  'o1-pro':              { factor: 0 },
  'o3':                  { factor: 0 },
  'computer-use-preview':{ factor: 0 },
  'gpt-image-1':         { factor: 0 },
};

const DETAIL_MODEL_TABLE: Record<VisionModel,
  { base: number; tile: number; shortest: number }> = {
  // detail-based families
  'gpt-4o':  { base: 85,   tile: 170,  shortest: 768 },
  'gpt-4.1': { base: 85,   tile: 170,  shortest: 768 },
  'gpt-4.5': { base: 85,   tile: 170,  shortest: 768 },

  '4o-mini': { base: 2_833, tile: 5_667, shortest: 768 },

  'o1':      { base: 75,   tile: 150,  shortest: 768 },
  'o1-pro':  { base: 75,   tile: 150,  shortest: 768 },
  'o3':      { base: 75,   tile: 150,  shortest: 768 },

  'computer-use-preview': { base: 65, tile: 129, shortest: 768 },

  // GPT-Image-1 (same algo, but 512-px shortest side)
  'gpt-image-1': { base: 65, tile: 129, shortest: 512 },

  // dummy rows for patch models (never consulted)
  'gpt-4.1-mini': { base: 0, tile: 0, shortest: 0 },
  'gpt-4.1-nano': { base: 0, tile: 0, shortest: 0 },
  'o4-mini':      { base: 0, tile: 0, shortest: 0 },
};

interface Options {
  model: VisionModel;
  /** Ignored for patch models; required for detail models except GPT-Image-1. */
  detail?: DetailLevel;
  /** Return *billable* tokens instead of raw image tokens for patch models. */
  billable?: boolean;
}

/* --- PUBLIC API --- */
export function estimateImageTokens(
  width: number,
  height: number,
  { model, detail = 'high', billable = false }: Options,
): number {
  if (width <= 0 || height <= 0) {
    throw new Error('width/height must be > 0');
  }

  if (!PATCH_MODELS[model] && !DETAIL_MODEL_TABLE[model]) {
    console.warn(`Unknown model "${model}"; using gpt-4o as default.`);
    // If the model is unknown, default to gpt-4o
    // This is a fallback; ideally, the caller should ensure a valid model.
    model = 'gpt-4o';
  }

  /* Patch-grid models (32 px, cap = 1 536) */
  if (PATCH_MODELS[model]?.factor) {
    const raw = patchModelTokens(width, height);
    return billable ? Math.ceil(raw * PATCH_MODELS[model].factor) : raw;
  }

  /* Detail-based models */
  return detailModelTokens(width, height, model, detail);
}

/* --- Patch-grid helper --- */
const PATCH_SIZE = 32;
const PATCH_CAP  = 1_536;

/**
 * Implements the two-step doc algorithm:
 *   1. Isotropic shrink so area ≤ cap patches
 *   2. Reduce width patches to an integer that still covers the image but
 *      produces ≤ cap total tokens, keeping aspect ratio.
 */
function patchModelTokens(w: number, h: number): number {
  // quick path
  let pw = Math.ceil(w / PATCH_SIZE);
  let ph = Math.ceil(h / PATCH_SIZE);
  if (pw * ph <= PATCH_CAP) {
    return pw * ph;
  }

  /* Step-1: first isotropic shrink */
  const shrink = Math.sqrt(
    (PATCH_CAP * PATCH_SIZE * PATCH_SIZE) / (w * h)
  );
  const sw = w * shrink;
  const sh = h * shrink;

  /* Step-2: choose the largest integer patch-width that fits cap */
  const pwFloat = sw / PATCH_SIZE;                 // e.g. 33.94
  for (let pwInt = Math.floor(pwFloat); pwInt >= 1; pwInt--) {
    const scale2 = pwInt / pwFloat;                // second isotropic scale
    const newH   = sh * scale2;
    const phInt  = Math.ceil(newH / PATCH_SIZE);
    const tokens = pwInt * phInt;
    if (tokens <= PATCH_CAP) {
      return tokens;        // first one ≤ cap wins
    }
  }
  return PATCH_CAP;                                // fallback – should never hit
}

/* --- Detail-based helper --- */
const MAX_DIM = 2_048;
const TILE    = 512;

function detailModelTokens(
  w: number,
  h: number,
  model: VisionModel,
  detail: DetailLevel,
): number {
  const { base, tile, shortest } = DETAIL_MODEL_TABLE[model];

  // GPT-Image-1 ignores detail flag; others honour 'low'
  if (model !== 'gpt-image-1' && detail === 'low') {
    return base;
  }

  // (1) Fit inside 2048^2 square
  if (w > MAX_DIM || h > MAX_DIM) {
    const scale = Math.min(MAX_DIM / w, MAX_DIM / h);
    w *= scale; h *= scale;
  }

  // (2) Ensure shortest side == 768 (or 512)
  const scale = shortest / Math.min(w, h);
  w *= scale; h *= scale;

  // (3) Count 512-px tiles
  const tiles = Math.ceil(w / TILE) * Math.ceil(h / TILE);
  return base + tile * tiles;
}



================================================
FILE: packages/poml/util/trace.ts
================================================
import { mkdirSync, writeFileSync, openSync, closeSync, writeSync, symlinkSync } from './fs';
import path from 'path';

interface Base64Wrapper { __base64__: string }

function replaceBuffers(value: any): any {
  if (Buffer.isBuffer(value)) {
    const wrapper: Base64Wrapper = { __base64__: value.toString('base64') };
    return wrapper;
  } else if (Array.isArray(value)) {
    return value.map(replaceBuffers);
  } else if (value && typeof value === 'object') {
    const result: any = {};
    for (const k of Object.keys(value)) {
      result[k] = replaceBuffers(value[k]);
    }
    return result;
  }
  return value;
}

export function parseJsonWithBuffers(text: string): any {
  return JSON.parse(text, (_key, value) => {
    if (value && typeof value === 'object' && value.__base64__) {
      return Buffer.from(value.__base64__, 'base64');
    }
    return value;
  });
}

let traceEnabled = false;
let traceDir: string | undefined;

export function setTrace(enabled = true, dir?: string): string | undefined {
  traceEnabled = enabled;
  if (!enabled) {
    traceDir = undefined;
    return undefined;
  }
  const envDir = process.env.POML_TRACE;
  if (dir) {
    const base = path.resolve(dir);
    mkdirSync(base, { recursive: true });
    traceDir = base;
  } else if (envDir) {
    mkdirSync(envDir, { recursive: true });
    traceDir = envDir;
  } else {
    traceDir = undefined;
  }
  return traceDir;
}

export function clearTrace() {
  traceEnabled = false;
  traceDir = undefined;
}

export function isTracing(): boolean {
  return traceEnabled && !!traceDir;
}

function nextIndex(sourcePath?: string): [number, string, number] {
  if (!traceDir) {
    return [0, '', -1];
  }
  const fileName = sourcePath ? path.basename(sourcePath, '.poml') : '';
  for (let i = 1; ; i++) {
    const idxStr = i.toString().padStart(4, '0');
    const prefix = path.join(traceDir, idxStr) + (fileName ? `.${fileName}` : '');
    const filePath = `${prefix}.poml`;
    try {
      const fd = openSync(filePath, 'wx');
      return [i, prefix, fd];
    } catch (err: any) {
      if (err.code === 'EEXIST') {
        continue;
      }
      throw err;
    }
  }
}

export function dumpTrace(markup: string, context?: any, stylesheet?: any, result?: any, sourcePath?: string, prettyResult?: string) {
  if (!isTracing()) {
    return;
  }
  const [_idx, prefix, fd] = nextIndex(sourcePath);
  try {
    writeSync(fd, markup);
  } finally {
    closeSync(fd);
  }
  if (sourcePath) {
    const envFile = `${prefix}.env`;
    writeFileSync(envFile, `SOURCE_PATH=${sourcePath}\n`);
    const linkPath = `${prefix}.source.poml`;
    try {
      symlinkSync(sourcePath, linkPath);
    } catch {
      console.warn(`Failed to create symlink for source path: ${sourcePath}`);
    }
  }
  if (context && Object.keys(context).length > 0) {
    writeFileSync(`${prefix}.context.json`, JSON.stringify(replaceBuffers(context), null, 2));
  }
  if (stylesheet && Object.keys(stylesheet).length > 0) {
    writeFileSync(`${prefix}.stylesheet.json`, JSON.stringify(replaceBuffers(stylesheet), null, 2));
  }
  if (result !== undefined) {
    writeFileSync(`${prefix}.result.json`, JSON.stringify(replaceBuffers(result), null, 2));
    if (prettyResult !== undefined) {
      writeFileSync(`${prefix}.result.txt`, prettyResult);
    }
  }
}

if (process.env.POML_TRACE) {
  setTrace(true, process.env.POML_TRACE);
}



================================================
FILE: packages/poml/util/xmlContentAssist.d.ts
================================================
// Adapted from https://github.com/SAP/xml-tools/blob/master/packages/content-assist/api.d.ts

import { IToken } from "chevrotain";
import { DocumentCstNode } from "@xml-tools/parser";
import {
  XMLElement,
  XMLDocument,
} from "@xml-tools/ast";

import { SuggestionProviders, ProviderOptions, SuggestionProvider } from "@xml-tools/content-assist";

declare function getSuggestions<OUT>(options: {
  cst: DocumentCstNode;
  ast: XMLDocument;
  offset: number;
  tokenVector: IToken[];
  providers: SuggestionProvidersWithClose<OUT>;
}): OUT[];

declare function getSuggestions<OUT, CONTEXT>(options: {
  cst: DocumentCstNode;
  ast: XMLDocument;
  offset: number;
  tokenVector: IToken[];
  providers: SuggestionProvidersWithClose<OUT, CONTEXT>;
  context: CONTEXT;
}): OUT[];

declare type SuggestionProvidersWithClose<OUT, CONTEXT = undefined> = SuggestionProviders<OUT, CONTEXT> & {
  elementNameClose?: ElementNameCloseCompletion<OUT, CONTEXT>[];
};

declare type ProviderOptionsWithClose<CONTEXT = undefined> = ProviderOptions<CONTEXT> | ElementNameCloseCompletion<CONTEXT>;

declare type ElementNameCloseCompletionOptions<CONTEXT = undefined> = {
  element: XMLElement;
  prefix: string | undefined;

  context: CONTEXT;
};

declare type ElementNameCloseCompletion<
  OUT,
  CONTEXT = undefined
> = SuggestionProvider<ElementNameCloseCompletionOptions<CONTEXT>, OUT, CONTEXT>;



================================================
FILE: packages/poml/util/xmlContentAssist.js
================================================
// Adapted from https://github.com/SAP/xml-tools/blob/master/packages/content-assist/lib/content-assist.js

const {
  defaultsDeep,
  forEach,
  isArray,
  find,
  findIndex,
  flatMap,
  identity,
  last,
  isEmpty
} = require('lodash');  // eslint-disable-line
const { BaseXmlCstVisitor } = require('@xml-tools/parser');  // eslint-disable-line
const { findNextTextualToken } = require('@xml-tools/common');  // eslint-disable-line

function getSuggestions(options) {
  const actualOptions = defaultsDeep(options, {
    providers: {
      elementContent: [],
      elementName: [],
      elementCloseName: [],
      attributeName: [],
      attributeValue: [],
    },
    context: undefined
  });

  let { providerType, providerArgs } = computeCompletionSyntacticContext({
    cst: actualOptions.cst,
    tokenVector: actualOptions.tokenVector,
    ast: actualOptions.ast,
    offset: actualOptions.offset
  });

  // Inject Additional semantic context for the content assist providers.
  providerArgs.context = actualOptions.context;

  if (providerType === null) {
    return [];
  } else {
    const selectedProviders = actualOptions.providers[providerType];

    const suggestions = flatMap(selectedProviders, suggestionProvider =>
      suggestionProvider(providerArgs)
    );
    return suggestions;
  }
}

function computeCompletionSyntacticContext({ cst, ast: docAst, offset, tokenVector }) {
  const contextVisitor = new SuggestionContextVisitorWithClose(docAst, offset, tokenVector);
  contextVisitor.visit(cst);
  return contextVisitor.result;
}

/* eslint-disable no-unused-vars -- consistent signatures in visitor methods even if they are empty placeholders */
class SuggestionContextVisitorWithClose extends BaseXmlCstVisitor {
  constructor(docAst, offset, tokenVector) {
    super();
    this.docAst = docAst;
    this.targetOffset = offset;
    this.tokenVector = tokenVector;
    this.result = { providerType: null, providerArgs: {} };
    this.found = false;
  }

  /**
   * @param {DocumentCtx} ctx
   */
  document(ctx) {
    this.visit(ctx.element, this.docAst.rootElement);
  }

  /**
   * @param {PrologCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  prolog(ctx, astNode) {}

  /**
   * @param {docTypeDeclCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  docTypeDecl(ctx, astNode) {}

  /**
   * @param {ExternalIDCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  externalID(ctx, astNode) {}

  /**
   * @param {ContentCtx} ctx
   * @param {XMLElement} astNode
   *
   */
  content(ctx, astNode) {
    forEach(ctx.element, (elem, idx) => {
      this.visit(elem, astNode.subElements[idx]);
    });
  }

  /**
   * @param {ElementCtx} ctx
   * @param {XMLElement} astNode
   */
  element(ctx, astNode) {
    // Order of handlers can affect the result!
    // They are ordered by priority, the more specific handlers are listed first.
    handleElementNameWithoutPrefixScenario(ctx, astNode, this);

    if (this.found === false) {
      handleElementNameWithPrefixScenario(ctx, astNode, this);
    }

    // Traverse Deeper
    if (this.found === false) {
      forEach(ctx.attribute, (attrib, idx) => this.visit(attrib, astNode.attributes[idx]));
      this.visit(ctx.content, astNode);
    }

    if (this.found === false) {
      handleNewAttributeKeyScenario(ctx, astNode, this.tokenVector, this);
    }

    if (this.found === false) {
      handleElementContentScenario(ctx, astNode, this);
    }

    if (this.found === false) {
      handleElementNameCloseWithoutPrefixScenario(ctx, astNode, this);
    }

    if (this.found === false) {
      handleElementNameCloseWithPrefixScenario(ctx, astNode, this);
    }
  }

  /**
   * @param {ReferenceCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  reference(ctx, astNode) {}

  /**
   * @param {AttributeCtx} ctx
   * @param {XMLAttribute} astNode
   */
  attribute(ctx, astNode) {
    // potential Attribute Value scenarios
    /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
    if (exists(ctx.STRING)) {
      const valueTok = ctx.STRING[0];
      if (
        // The content assist point must be inside the string quotes
        valueTok.startOffset < this.targetOffset &&
        valueTok.endOffset >= this.targetOffset
      ) {
        const prefixEnd = this.targetOffset - valueTok.startOffset;
        const prefix = valueTok.image.substring(1, prefixEnd);
        this.result.providerType = 'attributeValue';
        this.result.providerArgs = {
          element: astNode.parent,
          attribute: astNode,
          prefix: prefix !== '' ? prefix : undefined
        };
        this.found = true;
      }
    }

    /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
    if (exists(ctx.Name)) {
      const keyTok = ctx.Name[0];

      if (keyTok.startOffset <= this.targetOffset && keyTok.endOffset + 1 >= this.targetOffset) {
        const prefixEnd = this.targetOffset - keyTok.startOffset;
        const prefix = keyTok.image.substring(0, prefixEnd);
        this.result.providerType = 'attributeName';
        this.result.providerArgs = {
          element: astNode.parent,
          attribute: astNode,
          prefix: prefix !== '' ? prefix : undefined
        };
        this.found = true;
      }
    }
  }

  /**
   * @param {ChardataCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  chardata(ctx, astNode) {}

  /**
   * @param {MiscCtx} ctx
   */
  /* istanbul ignore next - place holder*/
  misc(ctx, astNode) {}
}
/* eslint-enable no-unused-vars -- see matching pair above */

function handleElementNameWithoutPrefixScenario(ctx, astNode, visitor) {
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.OPEN)) {
    const openTok = ctx.OPEN[0];
    if (openTok.endOffset + 1 === visitor.targetOffset) {
      visitor.result.providerType = 'elementName';
      visitor.result.providerArgs = { element: astNode, prefix: undefined };
      visitor.found = true;
    }
  }
}

function handleElementNameWithPrefixScenario(ctx, astNode, visitor) {
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.Name)) {
    const nameTok = ctx.Name[0];
    if (
      nameTok.startOffset < visitor.targetOffset &&
      nameTok.endOffset + 1 >= visitor.targetOffset
    ) {
      visitor.result.providerType = 'elementName';
      const prefixLength = visitor.targetOffset - nameTok.startOffset;
      const prefix = nameTok.image.substring(0, prefixLength);
      visitor.result.providerArgs = { element: astNode, prefix: prefix };
      visitor.found = true;
    }
  }
}

function handleElementNameCloseWithoutPrefixScenario(ctx, astNode, visitor) {
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.SLASH_OPEN)) {
    const openTok = ctx.SLASH_OPEN[0];
    if (openTok.endOffset + 1 === visitor.targetOffset) {
      visitor.result.providerType = 'elementNameClose';
      visitor.result.providerArgs = { element: astNode, prefix: undefined };
      visitor.found = true;
    }
  }
}

function handleElementNameCloseWithPrefixScenario(ctx, astNode, visitor) {
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.END_NAME)) {
    const nameTok = ctx.END_NAME[0];
    if (
      nameTok.startOffset < visitor.targetOffset &&
      nameTok.endOffset + 1 >= visitor.targetOffset
    ) {
      visitor.result.providerType = 'elementNameClose';
      const prefixLength = visitor.targetOffset - nameTok.startOffset;
      const prefix = nameTok.image.substring(0, prefixLength);
      visitor.result.providerArgs = { element: astNode, prefix: prefix };
      visitor.found = true;
    }
  }
}

function handleNewAttributeKeyScenario(ctx, astNode, tokenVector, visitor) {
  // Potential AttributeKey scenario in a completely new attribute
  // Note the guard condition (in caller) to avoid this branch if one of the attributes scenarios was already detected.
  // This means the order of checking the scenarios is meaningful!
  // Example of the problem:
  // -  `<person gen⇶>` should be matched as attributeName **with prefix** (In attribute handler code)
  // -  `<person gen="Y"⇶>` should be matched as a **new** attributeName **without prefix** (in the code below).
  // But the logic below cannot distinguish these, so it must only be executed if the attribute handler failed.
  const attributesRange = { from: undefined, to: undefined };
  let hasTerminatedAttribRange = false;
  let hasAttributeCloseToken = false;
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.Name)) {
    attributesRange.from = ctx.Name[0].endOffset + 1;
    // Figure where does the attributes area end
    if (exists(ctx.START_CLOSE)) {
      attributesRange.to = ctx.START_CLOSE[0].startOffset;
      hasTerminatedAttribRange = true;
      hasAttributeCloseToken = true;
    } else if (exists(ctx.SLASH_CLOSE)) {
      attributesRange.to = ctx.SLASH_CLOSE[0].startOffset;
      hasTerminatedAttribRange = true;
      hasAttributeCloseToken = true;
      // If we do not have a proper Attribute Section closing mark we use the last attribute instead
    } else if (isEmpty(ctx.attribute) === false) {
      attributesRange.to = last(ctx.attribute).location.endOffset;
      hasTerminatedAttribRange = true;
    }
  }

  if (
    hasTerminatedAttribRange &&
    visitor.targetOffset <= attributesRange.to &&
    attributesRange.from <= visitor.targetOffset
  ) {
    const isNotInExistingAttribute =
      find(ctx.attribute, attribCst => {
        const attribLoc = attribCst.location;
        return (
          visitor.targetOffset >= attribLoc.startOffset &&
          visitor.targetOffset <= attribLoc.endOffset
        );
      }) === undefined;

    // inside attribute area but not contained in any existing attribute
    /* istanbul ignore else - else branch is handled inside the attributes themselves and can never occur here */
    if (isNotInExistingAttribute) {
      visitor.result.providerType = 'attributeName';
      visitor.result.providerArgs = {
        element: astNode,
        attribute: undefined,
        prefix: undefined
      };
      visitor.found = true;
    }
  } else if (
    /**
     * Heuristic when we some attributes but no proper attribute Range
     * and we request the assist after the last attribute.
     * <people>
     *     <person age="66" ⇶
     * </people>
     */
    hasTerminatedAttribRange &&
    visitor.targetOffset > attributesRange.to &&
    hasAttributeCloseToken === false
  ) {
    handleNewAttributeKeyForPartialElement(
      // dummy pesudo token a we are searching the following token using the endOffset
      { endOffset: attributesRange.to },
      tokenVector,
      visitor,
      astNode
    );
    /**
     * Heuristic when we have no attribute range, e.g:
     * <people>
     *     <person ⇶
     * </people>
     */
  } else if (hasTerminatedAttribRange === false) {
    handleNewAttributeKeyForPartialElement(
      ctx.Name ? ctx.Name[0] : ctx.OPEN[0],
      tokenVector,
      visitor,
      astNode
    );
  }
}

function handleNewAttributeKeyForPartialElement(
  possibleAttribKeyRangeStartTok,
  tokenVector,
  visitor,
  astNode
) {
  const nextAfterElemNameTok = findNextTextualToken(
    tokenVector,
    possibleAttribKeyRangeStartTok.endOffset
  );
  if (
    visitor.targetOffset > possibleAttribKeyRangeStartTok.endOffset &&
    (nextAfterElemNameTok === null || // `null`` means there are no more textual tokens in the input
      visitor.targetOffset <= nextAfterElemNameTok.startOffset)
  ) {
    visitor.result.providerType = 'attributeName';
    visitor.result.providerArgs = {
      element: astNode,
      attribute: undefined,
      prefix: undefined
    };
    visitor.found = true;
  }
}

function handleElementContentScenario(ctx, astNode, visitor) {
  const contentRange = { from: undefined, to: undefined };
  let hasContentRange = false;
  /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
  if (exists(ctx.START_CLOSE)) {
    contentRange.from = ctx.START_CLOSE[0].endOffset + 1;
    // visitor logic only works when the attribute section is properly terminated
    /* istanbul ignore else - Very difficult to reproduce specific partial CSTs */
    if (exists(ctx.SLASH_OPEN)) {
      contentRange.to = ctx.SLASH_OPEN[0].startOffset;
      hasContentRange = true;
    } else if (exists(ctx.SLASH_CLOSE)) {
      contentRange.to = ctx.SLASH_CLOSE[0].startOffset;
      hasContentRange = true;
    }
  }

  if (
    hasContentRange &&
    visitor.targetOffset <= contentRange.to &&
    contentRange.from <= visitor.targetOffset
  ) {
    const allContentChildren = flatMap(ctx.content[0].children, identity);
    const innerContentPart = find(allContentChildren, subContent => {
      // Handling either CSTNodes or Tokens
      const subContentLoc = subContent.location ? subContent.location : subContent;

      // Our offset ranges are Inclusive to Exclusive
      // <person>abc⇶</person> --> Not inside the CharData Location, but uses `abc` as prefix
      // <person>⇶abc</person> --> Inside the CharData Location, but does not have any prefix
      const targetOffsetForPrefix = visitor.targetOffset - 1;

      return (
        targetOffsetForPrefix >= subContentLoc.startOffset &&
        targetOffsetForPrefix <= subContentLoc.endOffset
      );
    });

    // ElementContent without prefix
    if (innerContentPart === undefined) {
      visitor.result.providerType = 'elementContent';
      visitor.result.providerArgs = {
        element: astNode,
        textContent: undefined,
        prefix: undefined
      };
      visitor.found = true;
    } else if (innerContentPart.name === 'chardata') {
      const textNodeIdx = findIndex(ctx.content[0].children.chardata, innerContentPart);
      const textContentsAstNode = astNode.textContents[textNodeIdx];
      const prefixEnd = visitor.targetOffset - textContentsAstNode.position.startOffset;
      visitor.result.providerType = 'elementContent';
      visitor.result.providerArgs = {
        element: astNode,
        textContent: textContentsAstNode,
        prefix: textContentsAstNode.text.substring(0, prefixEnd)
      };
      visitor.found = true;
    }
  }
}

function exists(tokArr) {
  return isArray(tokArr) && tokArr.length === 1 && tokArr[0].isInsertedInRecovery !== true;
}

module.exports = {
  computeCompletionSyntacticContext: computeCompletionSyntacticContext,
  getSuggestions: getSuggestions
};



================================================
FILE: packages/poml-build/package.json
================================================
{
  "name": "pomljs",
  "version": "0.0.8",
  "description": "Prompt Orchestration Markup Language",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs",
      "types": "./dist/index.d.ts"
    },
    "./package.json": "./package.json"
  },
  "files": [
    "dist"
  ],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/microsoft/poml"
  },
  "homepage": "https://github.com/microsoft/poml",
  "keywords": [
    "poml",
    "prompt",
    "markup",
    "language",
    "ai",
    "llm"
  ],
  "engines": {
    "node": ">=18"
  },
  "sideEffects": false,
  "scripts": {
    "clean": "rm -rf dist .build README.md LICENSE poml-*.tgz",
    "prebuild": "npm run clean",
    "build": "tspc -p tsconfig.json && rollup -c rollup.config.js",
    "prepack": "cp ../../README.md . && cp ../../LICENSE . && npm run build",
    "postpack": "rm -rf README.md LICENSE"
  },
  "dependencies": {
    "@xml-tools/ast": "^5.0.5",
    "@xml-tools/content-assist": "^3.1.11",
    "@xml-tools/parser": "^1.0.11",
    "cheerio": "^1.0.0",
    "closest-match": "^1.3.3",
    "d3-dsv": "~2.0.0",
    "js-yaml": "^4.1.0",
    "json-schema-to-zod": "^2.6.1",
    "lodash.throttle": "^4.1.1",
    "mammoth": "^1.9.0",
    "pdf-parse": "^1.1.1",
    "pdfjs-dist": "~3.11.174",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-is": "^19.0.0",
    "react-keyed-flatten-children": "^5.0.0",
    "sharp": "^0.33.5",
    "showdown": "^2.1.0",
    "xlsx": "^0.18.5",
    "xmlbuilder2": "^3.1.1",
    "yargs": "^17.7.2",
    "zod": "^4.0.17"
  },
  "bin": {
    "poml": "./dist/cli.cjs"
  }
}



================================================
FILE: packages/poml-build/rollup.config.js
================================================
import commonjs from '@rollup/plugin-commonjs';
import json from '@rollup/plugin-json';
import pkg from './package.json' with { type: 'json' };

const peerDependencies = Object.keys(pkg.peerDependencies || {});
const external = [...Object.keys(pkg.dependencies || {}), ...peerDependencies];

export default {
  // The entry point of your library
  input: [
    '.build/index.js',
    '.build/cli.js',
  ],
  output: [
    {
      dir: 'dist',
      format: 'esm',
      preserveModules: true, // Keep file structure
      preserveModulesRoot: '.build',
      sourcemap: true, // Turn off source maps for production
      entryFileNames: '[name].js', // Ensure output files have .js extension
    },
    // 2. CommonJS output
    {
      dir: 'dist',
      format: 'cjs',
      preserveModules: true,
      preserveModulesRoot: '.build',
      sourcemap: true,
      entryFileNames: '[name].cjs', // Ensure output files have .cjs extension
    },
  ],
  plugins: [
    json(),
    commonjs(),
  ],
  external: external,
};


================================================
FILE: packages/poml-build/tsconfig.json
================================================
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "outDir": ".build",
    "rootDir": "../poml",
    "declaration": true,
    "composite": false,
    "module": "ESNext",
    "moduleResolution": "bundler"
  },
  "include": ["../poml/**/*"],
  "exclude": ["tests/**/*", "node_modules", "dist", ".build"]
}



================================================
FILE: packages/poml-vscode/extension.ts
================================================
import * as path from 'path';
import * as os from 'os';
import * as vscode from 'vscode';

import { CommandManager } from './util/commandManager';
import * as command from './command';
import { Logger } from './util/logger';
import { POMLWebviewPanelManager } from './panel/manager';
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  TransportKind
} from 'vscode-languageclient/node';
import { initializeReporter, getTelemetryReporter, TelemetryClient } from './util/telemetryClient';
import { TelemetryEvent } from './util/telemetryServer';
import { registerPomlChatParticipant } from './chat/participant';
import { registerPromptGallery, PromptGalleryProvider } from './chat/gallery';

let extensionPath = "";

export function getExtensionPath(): string {
  return extensionPath;
}

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
  extensionPath = context.extensionPath;

  const logger = new Logger();

  const webviewManager = new POMLWebviewPanelManager(context, logger);
  const galleryProvider = registerPromptGallery(context);

  const commandManager = new CommandManager();
  context.subscriptions.push(commandManager);
  commandManager.register(new command.TestCommand(webviewManager));
  commandManager.register(new command.TestNonChatCommand(webviewManager));
  commandManager.register(new command.TestRerunCommand(webviewManager));
  commandManager.register(new command.TestAbortCommand(webviewManager));
  commandManager.register(new command.ShowPreviewCommand(webviewManager));
  commandManager.register(new command.ShowPreviewToSideCommand(webviewManager));
  commandManager.register(new command.ShowLockedPreviewToSideCommand(webviewManager));
  commandManager.register(new command.ShowSourceCommand(webviewManager));
  commandManager.register(new command.AddContextFileCommand(webviewManager));
  commandManager.register(new command.AddStylesheetFileCommand(webviewManager));
  commandManager.register(new command.RemoveContextFileCommand(webviewManager));
  commandManager.register(new command.RemoveStylesheetFileCommand(webviewManager));
  commandManager.register(new command.AddPromptCommand(galleryProvider));
  commandManager.register(new command.DeletePromptCommand(galleryProvider));
  commandManager.register(new command.EditPromptCommand(galleryProvider));

  registerPomlChatParticipant(context, galleryProvider);

  const connectionString = getConnectionString();
  if (connectionString) {
    const reporter = initializeReporter(connectionString);
    reporter.reportTelemetry(TelemetryEvent.Activate, environmentData());
  }

  // This must be after telemetry is initialized
  commandManager.register(new command.TelemetryCompletionAcceptanceCommand(webviewManager));

  activateClient(context, getTelemetryReporter());
  return { getClient };
}

// This method is called when your extension is deactivated
export function deactivate() {
  deactivateClient();
}

let client: LanguageClient;

export function activateClient(context: vscode.ExtensionContext, reporter?: TelemetryClient) {
  // The server is implemented in node
  const serverModule = context.asAbsolutePath(
    path.join('dist', 'server.js')
  );

  // If the extension is launched in debug mode then the debug server options are used
  // Otherwise the run options are used
  const serverOptions: ServerOptions = {
    run: { module: serverModule, transport: TransportKind.ipc },
    debug: {
      module: serverModule,
      transport: TransportKind.ipc,
    }
  };

  // Options to control the language client
  const clientOptions: LanguageClientOptions = {
    // Register the server for plain text documents
    documentSelector: [{ scheme: 'file', language: 'poml' }]
  };

  // Create the language client and start the client.
  client = new LanguageClient(
    'poml-vscode',
    'POML Language Server',
    serverOptions,
    clientOptions
  );

  if (reporter) {
    client.onTelemetry(reporter.handleDataFromServer, reporter);
  }

  // Start the client. This will also launch the server
  client.start();
}

export function getClient(): LanguageClient {
  return client;
}

export function deactivateClient(): Thenable<void> | undefined {
  if (!client) {
    return undefined;
  }
  return client.stop();
}

function environmentData(): { [key: string]: string | undefined } {
  return {
    version: vscode.extensions.getExtension('poml-team.poml')?.packageJSON.version,
    os: os.platform(),
    osRelease: os.release(),
    architecture: os.arch(),
    vscodeVersion: vscode.version
  };
}

function getConnectionString(): string | undefined {
  return vscode.workspace
    .getConfiguration('poml')
    .get<string>('telemetry.connection');
}


================================================
FILE: packages/poml-vscode/settings.ts
================================================
import * as vscode from 'vscode';
import * as fs from 'fs';

export type LanguageModelProvider = 'openai' | 'microsoft' | 'anthropic' | 'google';

export interface LanguageModelSetting {
  provider: LanguageModelProvider;
  model: string;
  temperature?: number;
  apiKey?: string;
  apiUrl?: string;
  apiVersion?: string;
  maxTokens?: number;
}

export interface ResourceOptions {
  contexts: string[];
  stylesheets: string[];
}

/**
 * Settings for the extension.
 */
export class Settings {
  public static getForResource(resource: vscode.Uri) {
    return new Settings(resource);
  }

  public readonly scrollBeyondLastLine: boolean;
  public readonly wordWrap: boolean;
  public readonly previewFrontMatter: string;
  public readonly lineBreaks: boolean;
  public readonly doubleClickToSwitchToEditor: boolean;
  public readonly scrollEditorWithPreview: boolean;
  public readonly scrollPreviewWithEditor: boolean;
  public readonly markEditorSelection: boolean;
  public readonly languageModel: LanguageModelSetting;

  public readonly styles: string[];

  private constructor(resource: vscode.Uri) {
    const editorSettings = vscode.workspace.getConfiguration('editor', resource);
    const pomlSettings = vscode.workspace.getConfiguration('poml', resource);
    const pomlEditorSettings = vscode.workspace.getConfiguration('[poml]', resource);

    this.scrollBeyondLastLine = editorSettings.get<boolean>('scrollBeyondLastLine', false);

    this.wordWrap = editorSettings.get<string>('wordWrap', 'off') !== 'off';
    if (pomlEditorSettings && pomlEditorSettings['editor.wordWrap']) {
      this.wordWrap = pomlEditorSettings['editor.wordWrap'] !== 'off';
    }

    this.previewFrontMatter = pomlSettings.get<string>('previewFrontMatter', 'hide');
    this.scrollPreviewWithEditor = !!pomlSettings.get<boolean>('preview.scrollPreviewWithEditor', true);
    this.scrollEditorWithPreview = !!pomlSettings.get<boolean>('preview.scrollEditorWithPreview', true);
    this.lineBreaks = !!pomlSettings.get<boolean>('preview.breaks', false);
    this.doubleClickToSwitchToEditor = !!pomlSettings.get<boolean>('preview.doubleClickToSwitchToEditor', true);
    this.markEditorSelection = !!pomlSettings.get<boolean>('preview.markEditorSelection', true);

    this.languageModel = {
      provider: pomlSettings.get<LanguageModelProvider>('languageModel.provider', 'openai'),
      model: pomlSettings.get<string>('languageModel.model', ''),
      temperature: pomlSettings.get<number>('languageModel.temperature', 0.5),
      apiKey: pomlSettings.get<string>('languageModel.apiKey', '') || undefined,
      apiUrl: pomlSettings.get<string>('languageModel.apiUrl', '') || undefined,
      apiVersion: pomlSettings.get<string>('languageModel.apiVersion', '') || undefined,
      maxTokens: pomlSettings.get<number>('languageModel.maxTokens', 0) || undefined,
    }

    this.styles = pomlSettings.get<string[]>('styles', []);
  }

  public isEqualTo(otherSettings: Settings) {
    for (let key in this) {
      if (this.hasOwnProperty(key) && key !== 'styles' && key !== 'languageModel') {
        if (this[key] !== otherSettings[key]) {
          return false;
        }
      }
    }

    // Check styles
    if (this.styles.length !== otherSettings.styles.length) {
      return false;
    }
    for (let i = 0; i < this.styles.length; ++i) {
      if (this.styles[i] !== otherSettings.styles[i]) {
        return false;
      }
    }

    // Check language model properties
    if (!otherSettings.languageModel) {
      return false;
    }
    for (const prop in this.languageModel) {
      if ((this.languageModel as any)[prop] !== (otherSettings.languageModel as any)[prop]) {
        return false;
      }
    }

    return true;
  }

  [key: string]: any;
}

export class SettingsManager {
  private readonly previewSettingsForWorkspaces = new Map<string, Settings>();
  private readonly resourceOptions = new Map<string, ResourceOptions>();

  public loadAndCacheSettings(
    resource: vscode.Uri
  ): Settings {
    const config = Settings.getForResource(resource);
    this.previewSettingsForWorkspaces.set(this.getKey(resource), config);
    return config;
  }

  public hasSettingsChanged(
    resource: vscode.Uri
  ): boolean {
    const key = this.getKey(resource);
    const currentSettings = this.previewSettingsForWorkspaces.get(key);
    const newSettings = Settings.getForResource(resource);
    return (!currentSettings || !currentSettings.isEqualTo(newSettings));
  }

  public getResourceOptions(resource: vscode.Uri): ResourceOptions {
    let saved = this.resourceOptions.get(resource.fsPath);
    if (!saved) {
      saved = this.tryLoadAssociatedFiles(resource);
    }
    if (saved) {
      return { contexts: [...saved.contexts], stylesheets: [...saved.stylesheets] };
    }
    return { contexts: [], stylesheets: [] };
  }

  public setResourceOptions(resource: vscode.Uri, options: ResourceOptions) {
    this.resourceOptions.set(resource.fsPath, { contexts: [...options.contexts], stylesheets: [...options.stylesheets] });
  }

  public hasResourceOptions(resource: vscode.Uri): boolean {
    return this.resourceOptions.has(resource.fsPath);
  }

  private tryLoadAssociatedFiles(resource: vscode.Uri): ResourceOptions | undefined {
    const resourcePath = resource.fsPath;
    if (!resourcePath.endsWith('.poml')) {
      return undefined;
    }

    const base = resourcePath.replace(/(\.source)?\.poml$/i, '');
    const contexts: string[] = [];
    const stylesheets: string[] = [];
    const addIfExists = (arr: string[], file: string) => {
      if (fs.existsSync(file)) {
        arr.push(file);
        return true;
      }
      return false;
    };

    let changed = false;
    changed = addIfExists(contexts, `${base}.context.json`) || changed;
    changed = addIfExists(stylesheets, `${base}.stylesheet.json`) || changed;

    if (changed) {
      const opts = { contexts, stylesheets };
      this.resourceOptions.set(resource.fsPath, opts);
      return opts;
    }
    return undefined;
  }

  private getKey(
    resource: vscode.Uri
  ): string {
    const folder = vscode.workspace.getWorkspaceFolder(resource);
    return folder ? folder.uri.toString() : '';
  }
}



================================================
FILE: packages/poml-vscode/chat/gallery.ts
================================================
import * as vscode from 'vscode';

export interface PromptEntry {
  category: 'default' | 'user';
  name: string;
  file: string;
}

interface PromptCategory {
  type: 'category';
  label: string;
}

type TreeNode = PromptEntry | PromptCategory;

function isCategory(node: TreeNode): node is PromptCategory {
  return node && (node as PromptCategory).type === 'category';
}

const STORAGE_KEY = 'poml.promptGallery';

const DEFAULT_PROMPTS_LABEL = 'Default Prompts';
const MY_PROMPTS_LABEL = 'My Prompts';

export class PromptGalleryProvider implements vscode.TreeDataProvider<TreeNode> {
  private _onDidChangeTreeData = new vscode.EventEmitter<void>();
  readonly onDidChangeTreeData = this._onDidChangeTreeData.event;

  constructor(private context: vscode.ExtensionContext, private defaultEntries: PromptEntry[]) { }

  private get userEntries(): PromptEntry[] {
    return this.context.globalState.get<PromptEntry[]>(STORAGE_KEY, []);
  }

  private update(entries: PromptEntry[]) {
    void this.context.globalState.update(STORAGE_KEY, entries);
    this._onDidChangeTreeData.fire();
  }

  getChildren(element?: TreeNode): TreeNode[] {
    if (!element) {
      return [
        { type: 'category', label: DEFAULT_PROMPTS_LABEL },
        { type: 'category', label: MY_PROMPTS_LABEL },
      ];
    }
    if (isCategory(element)) {
      return element.label === DEFAULT_PROMPTS_LABEL
        ? this.defaultEntries
        : this.userEntries;
    }
    return [];
  }

  getTreeItem(element: TreeNode): vscode.TreeItem {
    if (isCategory(element)) {
      const item = new vscode.TreeItem(element.label, vscode.TreeItemCollapsibleState.Expanded);
      item.contextValue = 'pomlPrompt.category';
      return item;
    } else {
      const item = new vscode.TreeItem(element.name, vscode.TreeItemCollapsibleState.None);
      item.resourceUri = vscode.Uri.file(element.file);
      item.command = {
        command: 'vscode.open',
        title: 'Open Prompt',
        arguments: [vscode.Uri.file(element.file)],
      };
      item.contextValue = element.category === 'default' ? 'pomlPrompt.default' : 'pomlPrompt.user';
      return item;
    }
  }

  addPrompt(entry: PromptEntry) {
    const list = [...this.userEntries, entry];
    this.update(list);
  }

  removePrompt(entry: PromptEntry) {
    this.update(this.userEntries.filter(e => e !== entry));
  }

  updatePrompt(entry: PromptEntry, newEntry: PromptEntry) {
    const list = this.userEntries.map(e => (e === entry ? newEntry : e));
    this.update(list);
  }

  hasPrompt(name: string): boolean {
    return this.userEntries.some(e => e.name === name) || this.defaultEntries.some(e => e.name === name);
  }

  get prompts(): PromptEntry[] {
    return [...this.defaultEntries, ...this.userEntries];
  }
}

export function registerPromptGallery(context: vscode.ExtensionContext): PromptGalleryProvider {
  const galleryDir = vscode.Uri.joinPath(context.extensionUri, 'gallery');
  const defaultEntries: PromptEntry[] = [
    { name: 'ask', file: vscode.Uri.joinPath(galleryDir, 'ask.poml').fsPath, category: 'default' },
    { name: 'edit', file: vscode.Uri.joinPath(galleryDir, 'edit.poml').fsPath, category: 'default' },
    { name: 'latex-edit', file: vscode.Uri.joinPath(galleryDir, 'latex_edit.poml').fsPath, category: 'default' },
    { name: 'latex-write', file: vscode.Uri.joinPath(galleryDir, 'latex_write.poml').fsPath, category: 'default' },
    { name: 'pdf-understanding', file: vscode.Uri.joinPath(galleryDir, 'pdf_understanding.poml').fsPath, category: 'default' },
    { name: 'word-understanding', file: vscode.Uri.joinPath(galleryDir, 'word_understanding.poml').fsPath, category: 'default' },
    { name: 'table-understanding', file: vscode.Uri.joinPath(galleryDir, 'table_understanding.poml').fsPath, category: 'default' },
  ];
  const provider = new PromptGalleryProvider(context, defaultEntries);
  const view = vscode.window.createTreeView('pomlPromptGallery', { treeDataProvider: provider });
  context.subscriptions.push(view);
  return provider;
}



================================================
FILE: packages/poml-vscode/chat/participant.ts
================================================
import * as vscode from 'vscode';
import { getClient } from 'poml-vscode/extension';
import { PreviewMethodName, PreviewParams, PreviewResponse } from 'poml-vscode/panel/types';
import { Message } from 'poml';
import { PromptGalleryProvider } from '../chat/gallery';

export function registerPomlChatParticipant(context: vscode.ExtensionContext, gallery: PromptGalleryProvider) {
  const handler: vscode.ChatRequestHandler = async (
    request: vscode.ChatRequest,
    _chatContext: vscode.ChatContext,
    stream: vscode.ChatResponseStream,
    token: vscode.CancellationToken
  ): Promise<vscode.ChatResult | void> => {
    const files = request.references
      .map(ref => ref.value)
      .map(v => (v instanceof vscode.Location ? v.uri : v))
      .filter((v): v is vscode.Uri => v instanceof vscode.Uri);

    // Default to the gallery chat prompt file if no specific file is provided
    let filePath = vscode.Uri.joinPath(context.extensionUri, 'gallery', 'chat.poml');

    let promptText = request.prompt.trimStart();
    // if prompt starts with /<file> then use that file as the prompt
    const matchedPrompt = gallery.prompts.find(p => promptText.match(new RegExp(`^/${p.name}\\b`)));
    if (matchedPrompt) {
      promptText = promptText.replace(new RegExp(`^/${matchedPrompt.name}\\b`), '').trimStart();
      filePath = vscode.Uri.file(matchedPrompt.file);
    } else {
      // do not trim start then.
      promptText = request.prompt;
    }

    const pomlContext = {
      prompt: promptText,
      files: files.map(f => f.fsPath),
    };

    const params: PreviewParams = {
      uri: filePath.toString(),
      speakerMode: true,
      displayFormat: 'rendered',
      inlineContext: pomlContext,
      contexts: [], 
      stylesheets: [],
    };
    const response: PreviewResponse = await getClient().sendRequest(PreviewMethodName, params);
    if (response.error) {
      const errorMessage = Array.isArray(response.error) 
        ? response.error.map(err => typeof err === 'object' ? JSON.stringify(err) : String(err)).join(', ')
        : String(response.error);
      throw new Error(`Error rendering POML: ${errorMessage}`);
    } else {
      console.log('Rendered POML:', response.content);
      // stream.button('View Rendered Prompt', )
    }
    const messages = response.content as Message[];
    const chatMessages = messages.map(m => {
      const text = typeof m.content === 'string' ? m.content : JSON.stringify(m.content);
      return m.speaker === 'human'
        ? vscode.LanguageModelChatMessage.User(text)
        : vscode.LanguageModelChatMessage.Assistant(text);
    });

    const [model] = await vscode.lm.selectChatModels();
    if (!model) {
      throw new Error('No chat model available.');
    }
    const chatResponse = await model.sendRequest(chatMessages, {}, token);
    for await (const part of chatResponse.text) {
      stream.markdown(part);
    }
    return {};
  };

  const participant = vscode.chat.createChatParticipant('poml.runner', handler);
  participant.iconPath = vscode.Uri.joinPath(context.extensionUri, 'media/icon/poml-icon-16.svg');
  context.subscriptions.push(participant);
}



================================================
FILE: packages/poml-vscode/command/addResources.ts
================================================
import * as vscode from 'vscode';
import { Command } from '../util/commandManager';
import { POMLWebviewPanelManager } from '../panel/manager';

export class AddContextFileCommand implements Command {
  public readonly id = 'poml.addContextFile';
  public constructor(private readonly manager: POMLWebviewPanelManager) {}

  public async execute() {
    const panel = this.manager.activePreview;
    if (!panel) {
      return;
    }
    const uris = await vscode.window.showOpenDialog({
      canSelectMany: true,
      openLabel: 'Add Context',
      title: 'Select Context JSON Files to Associate with POML',
      filters: { 'JSON Files': ['json'], 'All Files': ['*'] }
    });
    if (!uris) {
      return;
    }
    for (const uri of uris) {
      panel.addContext(uri.fsPath);
    }
  }
}

export class AddStylesheetFileCommand implements Command {
  public readonly id = 'poml.addStylesheetFile';
  public constructor(private readonly manager: POMLWebviewPanelManager) {}

  public async execute() {
    const panel = this.manager.activePreview;
    if (!panel) {
      return;
    }
    const uris = await vscode.window.showOpenDialog({
      canSelectMany: true,
      openLabel: 'Add Stylesheet',
      title: 'Select Stylesheet JSON Files to Associate with POML',
      filters: { 'JSON Files': ['json'], 'All Files': ['*'] }
    });
    if (!uris) {
      return;
    }
    for (const uri of uris) {
      panel.addStylesheet(uri.fsPath);
    }
  }
}

export class RemoveContextFileCommand implements Command {
  public readonly id = 'poml.removeContextFile';
  public constructor(private readonly manager: POMLWebviewPanelManager) {}

  public execute(file: string) {
    const panel = this.manager.activePreview;
    panel?.removeContext(file);
  }
}

export class RemoveStylesheetFileCommand implements Command {
  public readonly id = 'poml.removeStylesheetFile';
  public constructor(private readonly manager: POMLWebviewPanelManager) {}

  public execute(file: string) {
    const panel = this.manager.activePreview;
    panel?.removeStylesheet(file);
  }
}



================================================
FILE: packages/poml-vscode/command/index.ts
================================================
export {
  ShowPreviewCommand,
  ShowPreviewToSideCommand,
  ShowLockedPreviewToSideCommand
} from './showPreview';
export { ShowSourceCommand } from './showSource';
export { TestCommand, TestNonChatCommand, TestRerunCommand, TestAbortCommand } from './testCommand';
export { TelemetryCompletionAcceptanceCommand } from './telemetry';
export {
  AddContextFileCommand,
  AddStylesheetFileCommand,
  RemoveContextFileCommand,
  RemoveStylesheetFileCommand,
} from './addResources';
export {
  AddPromptCommand,
  DeletePromptCommand,
  EditPromptCommand,
} from './promptGallery';



================================================
FILE: packages/poml-vscode/command/promptGallery.ts
================================================
import * as vscode from 'vscode';
import { Command } from '../util/commandManager';
import { PromptGalleryProvider, PromptEntry } from '../chat/gallery';
import * as path from 'path';

function isValidPromptName(name: string): boolean {
  // Check if the name contains only alphanumeric characters, underscores, and hyphens
  const regex = /^[a-zA-Z0-9_-]+$/;
  return regex.test(name);
}

export class AddPromptCommand implements Command {
  public readonly id = 'poml.gallery.addPrompt';
  public constructor(private readonly provider: PromptGalleryProvider) {}

  public async execute() {
    const uri = await vscode.window.showOpenDialog({
      openLabel: 'Select POML',
      filters: { POML: ['poml'], 'All Files': ['*'] }
    });
    if (!uri || !uri[0]) {
      return;
    }
    while (true) {
      const name = await vscode.window.showInputBox({
        prompt: 'Name for the prompt (use /<name> in chat panel)',
        value: path.basename(uri[0].fsPath, '.poml')
      });
      if (!name) {
        break;
      }
      if (!isValidPromptName(name)) {
        vscode.window.showErrorMessage('Invalid prompt name. Only alphanumeric characters, underscores, and hyphens are allowed.');
        continue;
      }
      if (this.provider.hasPrompt(name)) {
        vscode.window.showErrorMessage(
          `A prompt with the name "${name}" already exists.`
        );
        continue;
      }
      this.provider.addPrompt({ name, file: uri[0].fsPath, category: 'user' });
      break;
    }
  }
}

export class DeletePromptCommand implements Command {
  public readonly id = 'poml.gallery.deletePrompt';
  public constructor(private readonly provider: PromptGalleryProvider) {}

  public execute(item: PromptEntry) {
    if (item) {
      this.provider.removePrompt(item);
    }
  }
}

export class EditPromptCommand implements Command {
  public readonly id = 'poml.gallery.editPrompt';
  public constructor(private readonly provider: PromptGalleryProvider) {}

  public async execute(item: PromptEntry) {
    if (!item) {
      return;
    }
    let name: string | undefined;
    while (true) {
      name = await vscode.window.showInputBox({
        prompt: 'Name for the prompt (use /<name> in chat panel)',
        value: item.name
      });
      if (!name) {
        return;
      }
      if (!isValidPromptName(name)) {
        vscode.window.showErrorMessage('Invalid prompt name. Only alphanumeric characters, underscores, and hyphens are allowed.');
        continue;
      }
      if (name !== item.name && this.provider.hasPrompt(name)) {
        vscode.window.showErrorMessage(
          `A prompt with the name "${name}" already exists.`
        );
        continue;
      }
      break;
    }
    const uri = await vscode.window.showOpenDialog({
      openLabel: 'Select POML',
      defaultUri: vscode.Uri.file(item.file),
      filters: { POML: ['poml'], 'All Files': ['*'] }
    });
    if (!uri || !uri[0]) {
      return;
    }
    this.provider.updatePrompt(item, { name, file: uri[0].fsPath, category: 'user' });
  }
}



================================================
FILE: packages/poml-vscode/command/showPreview.ts
================================================
import * as vscode from 'vscode';

import { Command } from '../util/commandManager';
import { POMLWebviewPanelManager } from '../panel/manager';
import { PanelSettings } from '../panel/types';
import { getClient } from 'poml-vscode/extension';
import { getTelemetryReporter } from 'poml-vscode/util/telemetryClient';
import { TelemetryEvent } from 'poml-vscode/util/telemetryServer';

interface ShowPreviewSettings {
  readonly sideBySide?: boolean;
  readonly locked?: boolean;
}

async function showPreview(
  webviewManager: POMLWebviewPanelManager,
  uri: vscode.Uri | undefined,
  previewSettings: ShowPreviewSettings,
): Promise<any> {

  let resource = uri;
  if (!(resource instanceof vscode.Uri)) {
    if (vscode.window.activeTextEditor) {
      // we are relaxed and don't check for poml files
      resource = vscode.window.activeTextEditor.document.uri;
    }
  }

  if (!(resource instanceof vscode.Uri)) {
    if (!vscode.window.activeTextEditor) {
      // this is most likely toggling the preview
      return vscode.commands.executeCommand('poml.showSource');
    }
    // nothing found that could be shown or toggled
    return;
  }

  const resourceColumn = (vscode.window.activeTextEditor && vscode.window.activeTextEditor.viewColumn) || vscode.ViewColumn.One;
  webviewManager.preview(resource, {
    resourceColumn: resourceColumn,
    previewColumn: previewSettings.sideBySide ? resourceColumn + 1 : resourceColumn,
    locked: !!previewSettings.locked
  });

}

export class ShowPreviewCommand implements Command {
  public readonly id = 'poml.showPreview';

  public constructor(
    private readonly webviewManager: POMLWebviewPanelManager,
  ) { }

  public execute(mainUri?: vscode.Uri, allUris?: vscode.Uri[], panelSettings?: PanelSettings) {
    for (const uri of Array.isArray(allUris) ? allUris : [mainUri]) {
      showPreview(this.webviewManager, uri, {
        sideBySide: false,
        locked: panelSettings && panelSettings.locked
      });
    }
  }
}

export class ShowPreviewToSideCommand implements Command {
  public readonly id = 'poml.showPreviewToSide';

  public constructor(
    private readonly webviewManager: POMLWebviewPanelManager,
  ) { }

  public execute(uri?: vscode.Uri, panelSettings?: PanelSettings) {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.CommandInvoked, {
      command: this.id
    });
    showPreview(this.webviewManager, uri, {
      sideBySide: true,
      locked: panelSettings && panelSettings.locked
    });
  }
}


export class ShowLockedPreviewToSideCommand implements Command {
  public readonly id = 'poml.showLockedPreviewToSide';

  public constructor(
    private readonly webviewManager: POMLWebviewPanelManager
  ) { }

  public execute(uri?: vscode.Uri) {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.CommandInvoked, {
      command: this.id
    });
    showPreview(this.webviewManager, uri, {
      sideBySide: true,
      locked: true
    });
  }
}



================================================
FILE: packages/poml-vscode/command/showSource.ts
================================================
import * as vscode from 'vscode';
import { Command } from '../util/commandManager';
import { POMLWebviewPanelManager } from '../panel/manager';
import { getTelemetryReporter } from 'poml-vscode/util/telemetryClient';
import { TelemetryEvent } from 'poml-vscode/util/telemetryServer';

export class ShowSourceCommand implements Command {
  public readonly id = 'poml.showSource';

  public constructor(
    private readonly previewManager: POMLWebviewPanelManager
  ) { }

  public execute() {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.CommandInvoked, {
      command: this.id
    });
    if (this.previewManager.activePreviewResource) {
      return vscode.workspace.openTextDocument(this.previewManager.activePreviewResource)
        .then(document => vscode.window.showTextDocument(document));
    }
    return undefined;
  }
}



================================================
FILE: packages/poml-vscode/command/telemetry.ts
================================================
import { Command } from '../util/commandManager';
import { POMLWebviewPanelManager } from '../panel/manager';
import { getTelemetryReporter } from 'poml-vscode/util/telemetryClient';
import { DelayedTelemetryReporter, TelemetryEvent } from 'poml-vscode/util/telemetryServer';

export class TelemetryCompletionAcceptanceCommand implements Command {
  public readonly id = 'poml.telemetry.completion';
  private acceptCount: number = 0;
  private reporter: DelayedTelemetryReporter | undefined;

  public constructor(
    private readonly previewManager: POMLWebviewPanelManager
  ) {
    const reporter = getTelemetryReporter();
    this.reporter = reporter ? new DelayedTelemetryReporter(reporter) : undefined;
  }

  public execute() {
    if (this.reporter) {
      this.acceptCount++;
      this.reporter.reportTelemetry(
        TelemetryEvent.CompletionAcceptanceStatistics,
        {
          acceptCount: this.acceptCount
        }
      ).then((reported) => {
        if (reported) {
          this.acceptCount = 0;
        }
      });
    }
  }
}



================================================
FILE: packages/poml-vscode/command/testCommand.ts
================================================
import * as vscode from 'vscode';
import { Command } from '../util/commandManager';
import { POMLWebviewPanelManager } from '../panel/manager';
import { PanelSettings } from 'poml-vscode/panel/types';
import { PreviewMethodName, PreviewParams, PreviewResponse } from '../panel/types';
import { getClient } from '../extension';
import { Message } from 'poml';

import { createOpenAI } from '@ai-sdk/openai';
import { createAnthropic } from '@ai-sdk/anthropic';
import { createGoogleGenerativeAI } from '@ai-sdk/google';
import { createAzure } from '@ai-sdk/azure';
import { ModelMessage, streamText, tool, jsonSchema, Tool, streamObject, TextStreamPart } from 'ai';

import ModelClient from '@azure-rest/ai-inference';
import { AzureKeyCredential } from '@azure/core-auth';
import { createSseStream } from '@azure/core-sse';
import { fileURLToPath } from 'url';
import { LanguageModelSetting } from 'poml-vscode/settings';
import { IncomingMessage } from 'node:http';
import { getTelemetryReporter } from 'poml-vscode/util/telemetryClient';
import { TelemetryEvent } from 'poml-vscode/util/telemetryServer';

let _globalGenerationController: GenerationController | undefined = undefined;

class GenerationController {
  private readonly abortControllers: AbortController[];

  private constructor() {
    this.abortControllers = [];
  }

  public static getNewAbortController() {
    if (!_globalGenerationController) {
      _globalGenerationController = new GenerationController();
    }
    const controller = new AbortController();
    _globalGenerationController.abortControllers.push(controller);
    return controller;
  }

  public static abortAll() {
    if (_globalGenerationController) {
      for (const controller of _globalGenerationController.abortControllers) {
        controller.abort();
      }
      _globalGenerationController.abortControllers.length = 0;
    }
  }
}

let outputChannel: vscode.OutputChannel | undefined = undefined;
let lastCommand: string | undefined = undefined;

function getOutputChannel() {
  if (!outputChannel) {
    outputChannel = vscode.window.createOutputChannel('POML', 'log');
  }
  return outputChannel;
}

export class TestCommand implements Command {
  public id = 'poml.test';
  private readonly outputChannel: vscode.OutputChannel;

  public constructor(private readonly previewManager: POMLWebviewPanelManager) {
    this.outputChannel = getOutputChannel();
  }

  public execute(uri?: vscode.Uri, panelSettings?: PanelSettings) {
    lastCommand = this.id;
    if (!(uri instanceof vscode.Uri)) {
      if (vscode.window.activeTextEditor) {
        // we are relaxed and don't check for poml files
        uri = vscode.window.activeTextEditor.document.uri;
      }
    }

    if (uri) {
      this.testPrompt(uri);
    }
  }

  public async testPrompt(uri: vscode.Uri) {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.CommandInvoked, {
      command: this.id
    });
    const fileUrl = fileURLToPath(uri.toString());
    this.outputChannel.show(true);
    const reporter = getTelemetryReporter();
    const reportParams: { [key: string]: string } = {};
    if (reporter) {
      const document = await vscode.workspace.openTextDocument(uri);
      reportParams.uri = uri.toString();
      reportParams.rawText = document.getText();
    }

    // Check if language model settings are configured
    const setting = this.getLanguageModelSettings(uri);
    if (!setting) {
      vscode.window.showErrorMessage('Language model settings are not configured. Please configure your language model settings first.');
      this.log('error', 'Prompt test aborted: Language model settings not found.');
      return;
    }
    
    if (!setting.provider) {
      vscode.window.showErrorMessage('Language model provider is not configured. Please set your provider in the extension settings.');
      this.log('error', 'Prompt test aborted: setting.provider is not configured.');
      return;
    }
    
    if (!setting.model) {
      vscode.window.showErrorMessage('Language model is not configured. Please set your model in the extension settings.');
      this.log('error', 'Prompt test aborted: setting.model is not configured.');
      return;
    }
    
    if (!setting.apiKey) {
      vscode.window.showErrorMessage('API key is not configured. Please set your API key in the extension settings.');
      this.log('error', 'Prompt test aborted: setting.apiKey not configured.');
      return;
    }

    if (!setting.apiUrl) {
      this.log('info', 'No API URL configured, using default for the provider.');
    }

    this.log(
      'info',
      `Testing prompt with ${this.isChatting ? 'chat model' : 'text completion model'}: ${fileUrl}`
    );
    const startTime = Date.now();
    let nextInterval: number = 1;
    const showProgress = () => {
      const timeElapsed = (Date.now() - startTime) / 1000;
      this.log('info', `Test in progress. ${Math.round(timeElapsed)} seconds elapsed.`);
      nextInterval *= 2;
      timer = setTimeout(showProgress, nextInterval * 1000);
    };

    let timer = setTimeout(showProgress, nextInterval * 1000);
    let result: string[] = [];
    try {
      const prompt = await this.renderPrompt(uri);
      const setting = this.getLanguageModelSettings(uri);
      reporter?.reportTelemetry(TelemetryEvent.PromptTestingStart, {
        ...reportParams,
        languageModel: JSON.stringify(setting),
        rendered: JSON.stringify(prompt)
      });

      const stream = this.routeStream(prompt, setting);
      let hasChunk = false;
      for await (const chunk of stream) {
        clearTimeout(timer);
        hasChunk = true;
        result.push(chunk);
        this.outputChannel.append(chunk);
      }
      if (!hasChunk) {
        this.log('error', 'No response received from the language model.');
      } else {
        this.outputChannel.appendLine('');
      }
      const timeElapsed = Date.now() - startTime;
      this.log('info', `Test completed in ${Math.round(timeElapsed / 1000)} seconds. Language models can make mistakes. Check important info.`);

      if (reporter) {
        reporter.reportTelemetry(TelemetryEvent.PromptTestingEnd, {
          ...reportParams,
          result: result.join(''),
          timeElapsed: timeElapsed
        });
      }
    } catch (e) {
      clearTimeout(timer);
      vscode.window.showErrorMessage(String(e));
      if (reporter) {
        reporter.reportTelemetry(TelemetryEvent.PromptTestingError, {
          ...reportParams,
          error: e ? e.toString() : '',
          partialResult: result.join('')
        });
      }

      if (e && (e as any).stack) {
        this.log('error', (e as any).stack);
      } else {
        this.log('error', String(e));
      }
    }
  }

  protected get isChatting() {
    return true;
  }

  private async renderPrompt(uri: vscode.Uri) {
    const options = this.previewManager.previewConfigurations.getResourceOptions(uri);
    const requestParams: PreviewParams = {
      uri: uri.toString(),
      speakerMode: this.isChatting,
      displayFormat: 'rendered',
      contexts: options.contexts,
      stylesheets: options.stylesheets,
    };

    const response: PreviewResponse = await getClient().sendRequest<PreviewResponse>(
      PreviewMethodName,
      requestParams
    );
    if (response.error) {
      throw new Error(`Error rendering prompt: ${uri}\n${response.error}`);
    }
    return response;
  }

  private async *routeStream(
    prompt: PreviewResponse,
    settings: LanguageModelSetting,
  ): AsyncGenerator<string> {
    if (settings.provider === 'microsoft' && settings.apiUrl?.includes('.models.ai.azure.com')) {
      yield* this.azureAiStream(prompt.content as Message[], settings);
    } else if (prompt.responseSchema) {
      yield* this.handleResponseSchemaStream(prompt, settings);
    } else {
      yield* this.handleRegularTextStream(prompt, settings);
    }
  }

  private async *handleResponseSchemaStream(
    prompt: PreviewResponse,
    settings: LanguageModelSetting,
  ): AsyncGenerator<string> {
    const model = this.getActiveVercelModel(settings);
    const vercelPrompt = this.isChatting ? this.pomlMessagesToVercelMessage(prompt.content as Message[])
      : prompt.content as string;
    
    if (prompt.tools) {
      throw new Error('Tools are not supported when response schema is provided.');
    }

    if (!prompt.responseSchema) {
      throw new Error('Response schema is required but not provided.');
    }

    const stream = streamObject({
      model: model,
      prompt: vercelPrompt,
      onError: ({ error }) => {
        // Immediately throw the error
        throw error;
      },
      schema: this.toVercelResponseSchema(prompt.responseSchema),
      maxRetries: 0,
      temperature: settings.temperature,
      maxOutputTokens: settings.maxTokens,
      ...prompt.runtime,
    });

    for await (const text of stream.textStream) {
      yield text;
    }
  }

  private async *handleRegularTextStream(
    prompt: PreviewResponse,
    settings: LanguageModelSetting,
  ): AsyncGenerator<string> {
    const model = this.getActiveVercelModel(settings);
    const vercelPrompt = this.isChatting ? this.pomlMessagesToVercelMessage(prompt.content as Message[])
      : prompt.content as string;

    const stream = streamText({
      model: model,
      prompt: vercelPrompt,
      onError: ({ error }) => {
        // Immediately throw the error
        throw error;
      },
      tools: prompt.tools ? this.toVercelTools(prompt.tools) : undefined,
      maxRetries: 0,
      temperature: settings.temperature,
      maxOutputTokens: settings.maxTokens,
      ...prompt.runtime,
    });

    let lastChunkEndline: boolean = false;
    for await (const chunk of stream.fullStream) {
      const result = this.processStreamChunk(chunk, lastChunkEndline);
      if (result !== null) {
        yield result;
        lastChunkEndline = result.endsWith('\n');
      }
    }
  }

  private processStreamChunk(chunk: TextStreamPart<any>, lastChunkEndline: boolean): string | null {
    const newline = lastChunkEndline ? '' : '\n';
    if (chunk.type === 'text-delta' || chunk.type === 'reasoning-delta') {
      return chunk.text;
    } else if (chunk.type === 'finish') {
      return this.formatUsageInfo(chunk, lastChunkEndline);
    } else if (chunk.type === 'tool-call') {
      return `${newline}Tool call (${chunk.toolCallId}) ${chunk.toolName}  Input: ${JSON.stringify(chunk.input)}`;
    } else if (chunk.type.startsWith('tool-input')) {
      return null;
    } else if (chunk.type === 'reasoning-start') {
      return `${newline}[Reasoning]`;
    } else if (chunk.type === 'reasoning-end') {
      return '\n[/Reasoning]';
    } else if (['start', 'finish', 'start-step', 'finish-step', 'message-metadata'].includes(chunk.type)) {
      return null;
    } else if (chunk.type === 'abort') {
      return `${newline}[Aborted]`;
    } else if (chunk.type === 'error') {
      // errors will be thrown, so we don't need to handle them here
      return null;
    } else {
      return `${newline}[${chunk.type} chunk: ${JSON.stringify(chunk)}]`;
    }
  }

  private formatUsageInfo(chunk: any, lastChunkEndline: boolean): string {
    const newline = lastChunkEndline ? '' : '\n';
    let usageInfo = `${newline}[Usage: input=${chunk.totalUsage.inputTokens}, output=${chunk.totalUsage.outputTokens}, ` +
      `total=${chunk.totalUsage.totalTokens}`;
    
    if (chunk.totalUsage.cachedInputTokens) {
      usageInfo += `, cached=${chunk.totalUsage.cachedInputTokens}`;
    }
    if (chunk.totalUsage.reasoningTokens) {
      usageInfo += `, reasoning=${chunk.totalUsage.reasoningTokens}`;
    }
    usageInfo += ']';
    
    return usageInfo;
  }

  private async *azureAiStream(
    prompt: Message[],
    settings: LanguageModelSetting
  ): AsyncGenerator<string> {
    if (!settings.apiUrl || !settings.apiKey) {
      throw new Error('Azure AI API URL or API key is not configured.');
    }
    if (!this.isChatting) {
      throw new Error('Azure AI is only supported for chat models.');
    }
    const client = ModelClient(settings.apiUrl, new AzureKeyCredential(settings.apiKey));

    const args: any = {};
    if (settings.maxTokens) {
      args.max_tokens = settings.maxTokens;
    }
    if (settings.temperature) {
      args.temperature = settings.temperature;
    }
    if (settings.model) {
      args.model = settings.model;
    }

    const response = await client
      .path('/chat/completions')
      .post({
        body: {
          messages: this.toMessageObjects(prompt, 'openai'),
          stream: true,
          ...args
        }
      })
      .asNodeStream();

    const stream = response.body;
    if (!stream) {
      throw new Error('The response stream is undefined');
    }

    if (response.status !== '200') {
      throw new Error(
        `Failed to get chat completions (status code ${response.status}): ${await streamToString(stream)}`
      );
    }

    const sses = createSseStream(stream as IncomingMessage);

    for await (const event of sses) {
      if (event.data === '[DONE]') {
        return;
      }
      for (const choice of JSON.parse(event.data).choices) {
        yield choice.delta?.content ?? '';
      }
    }

    async function streamToString(stream: NodeJS.ReadableStream): Promise<string> {
      const chunks: Buffer[] = [];
      for await (const chunk of stream) {
        chunks.push(Buffer.from(chunk));
      }
      return Buffer.concat(chunks).toString('utf-8');
    }
  }

  private getActiveVercelModelProvider(settings: LanguageModelSetting) {
    switch (settings.provider) {
      case 'anthropic':
        return createAnthropic({
          baseURL: settings.apiUrl,
          apiKey: settings.apiKey,
        });
      case 'microsoft':
        return createAzure({
          baseURL: settings.apiUrl,
          apiKey: settings.apiKey
        });
      case 'openai':
        return createOpenAI({
          baseURL: settings.apiUrl,
          apiKey: settings.apiKey
        });
      case 'google':
        return createGoogleGenerativeAI({
          baseURL: settings.apiUrl,
          apiKey: settings.apiKey
        });
    }
  }

  private getActiveVercelModel(settings: LanguageModelSetting) {
    const provider = this.getActiveVercelModelProvider(settings);
    return provider(settings.model);
  }

  private pomlMessagesToVercelMessage(messages: Message[]): ModelMessage[] {
    const speakerToRole = {
      ai: 'assistant',
      human: 'user',
      system: 'system'
    }
    const result: ModelMessage[] = [];
    for (const msg of messages) {
      if (!msg.speaker) {
        throw new Error(`Message must have a speaker, found: ${JSON.stringify(msg)}`);
      }
      const role = speakerToRole[msg.speaker];
      const contents = typeof msg.content === 'string' ? msg.content : msg.content.map(part => {
        if (typeof part === 'string') {
          return { type: 'text', text: part };
        } else if (part.type.startsWith('image/')) {
          if (!part.base64) {
            throw new Error(`Image content must have base64 data, found: ${JSON.stringify(part)}`);
          }
          return { type: 'image', image: part.base64 };
        } else {
          throw new Error(`Unsupported content type: ${part.type}`);
        }
      });
      result.push({
        role: role as any,
        content: contents as any
      });
    }
    return result;
  }

  private toVercelTools(tools: { [key: string]: any }[]) {
    const result: { [key: string]: Tool } = {};
    for (const t of tools) {
      if (!t.name || !t.description || !t.parameters) {
        throw new Error(`Tool must have name, description, and parameters: ${JSON.stringify(t)}`);
      }
      if (t.type !== 'function') {
        throw new Error(`Unsupported tool type: ${t.type}. Only 'function' type is supported.`);
      }
      const schema = jsonSchema(t.parameters);
      result[t.name] = tool({
        description: t.description,
        inputSchema: schema
      });
    };
    this.log('info', 'Registered tools: ' + Object.keys(result).join(', '));
    return result;
  }

  private toVercelResponseSchema(responseSchema: { [key: string]: any }) {
    return jsonSchema(responseSchema);
  }

  private toMessageObjects(messages: Message[], style: 'openai' | 'google') {
    const speakerMapping = {
      ai: 'assistant',
      human: 'user',
      system: 'system'
    };
    return messages.map(msg => {
      return {
        role: speakerMapping[msg.speaker] ?? msg.speaker,
        content: msg.content
      };
    });
  }

  private getLanguageModelSettings(uri: vscode.Uri) {
    const settings = this.previewManager.previewConfigurations;
    return settings.loadAndCacheSettings(uri).languageModel;
  }

  private log(level: 'error' | 'info', message: string) {
    const tzOffset = new Date().getTimezoneOffset() * 60000;
    const time = new Date(Date.now() - tzOffset).toISOString().replace('T', ' ').replace('Z', '');
    this.outputChannel.appendLine(`${time} [${level}] ${message}`);
  }
}

export class TestNonChatCommand extends TestCommand {
  public id = 'poml.testNonChat';

  protected get isChatting() {
    return false;
  }
}

export class TestRerunCommand implements Command {
  public id = 'poml.testRerun';
  private readonly outputChannel: vscode.OutputChannel;

  constructor(previewManager: POMLWebviewPanelManager) {
    this.outputChannel = getOutputChannel();
  }

  public execute(...args: any[]): void {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.CommandInvoked, {
      command: this.id
    });
    if (lastCommand) {
      this.outputChannel.clear();
      vscode.commands.executeCommand(lastCommand, ...args);
    } else {
      vscode.window.showErrorMessage('No test command to rerun');
    }
  }
}

export class TestAbortCommand implements Command {
  public readonly id = 'poml.testAbort';

  public constructor(private readonly previewManager: POMLWebviewPanelManager) { }

  public execute() {
    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.PromptTestingAbort, {});
    GenerationController.abortAll();
  }
}



================================================
FILE: packages/poml-vscode/lsp/documentFormatter.ts
================================================
import { ComponentSpec, Parameter, PomlComponent } from 'poml/base';

export function formatComponentDocumentation(
  componentSpec: ComponentSpec,
  baseLevel?: number
): string {
  baseLevel = baseLevel || 2;
  const docParts: string[] = [];
  docParts.push(componentSpec.description);
  if (componentSpec.example) {
    docParts.push('#'.repeat(baseLevel) + ' Usages', componentSpec.example);
  }
  const component = PomlComponent.fromSpec(componentSpec);
  const params = component.parameters();
  if (params.length > 0) {
    docParts.push(
      '#'.repeat(baseLevel) + ' Parameters',
      params
        .map(param => {
          return '- ' + formatParameterDocumentation(param);
        })
        .join('\n')
    );
  }
  return docParts.join('\n\n');
}

export function formatParameterDocumentation(param: Parameter): string {
  let desc: string = '';
  if (param.type !== 'string' && param.type.length >= 1) {
    desc += param.type.charAt(0).toUpperCase() + param.type.slice(1) + '. ';
  }
  if (param.choices.length > 0) {
    desc += 'Can be one of: ' + param.choices.join(', ') + '. ';
  }
  desc += param.description;
  return `**${param.name}**: ${desc.replaceAll('\n', '\n  ')}`;
}



================================================
FILE: packages/poml-vscode/lsp/parseComments.ts
================================================
import 'poml';
import { ComponentSpec, Parameter } from 'poml/base';

import { readFileSync, readdirSync, writeFile, writeFileSync } from 'fs';
import { join } from 'path';
import { formatComponentDocumentation } from './documentFormatter';

const basicComponents: string[] = [];
const intentions: string[] = [];
const dataDisplays: string[] = [];
const utilities: string[] = [];

function tsCommentToMarkdown(comment: string): ComponentSpec {
  // The comment is a multi-line comment starting with `/**` and ending with `*/`.
  // We first strip the leading `/**` and trailing `*/` and the leading `*` from each line.
  // Then we split the comment into lines.
  const strippedComment = comment
    .replace(/^\/\*\*?/, '')
    .replace(/\*\/$/, '')
    .split('\n')
    .map(line => line.replace(/^\s*\*( )?/, ''))
    .map(line => line.replace(/\s+$/, ''))
    .join('\n');

  // Recognize description, @param and @example in the comment.
  const descriptionRegex = /([\s\S]*?)(?=@param|@example|@see|$)/;
  const paramRegex =
    /@param\s+(\{([\S'"\|]+?)\}\s+)?(\w+)\s+-\s+([\s\S]*?)(?=@param|@example|@see|$)/g;
  const exampleRegex = /@example\s+([\s\S]*?)(?=@param|@example|@see|$)/;
  const seeRegex = /@see\s+([\s\S]*?)(?=@param|@example|@see|$)/g;

  const descriptionMatch = strippedComment.match(descriptionRegex);
  const description = descriptionMatch ? descriptionMatch[1].trim() : '';
  const params: Parameter[] = [];
  let paramMatch;
  while ((paramMatch = paramRegex.exec(strippedComment)) !== null) {
    let choices: string[] = [];
    let type: string = 'string';
    let fallbackType: string | undefined = undefined;
    if (paramMatch[2] === 'object|string') {
      type = 'object';
      fallbackType = 'string';
    } else if (paramMatch[2] === 'Buffer|string') {
      type = 'Buffer';
      fallbackType = 'string';
    } else if (paramMatch[2] === 'RegExp|string') {
      type = 'RegExp';
      fallbackType = 'string';
    } else if (paramMatch[2] === 'string|Buffer') {
      type = 'Buffer';
      fallbackType = 'string';
    } else if (paramMatch[2] && paramMatch[2].includes('|')) {
      type = 'string';
      choices = paramMatch[2].split('|').map(choice => choice.replace(/['"\s]/g, '').trim());
    } else if (paramMatch[2]) {
      type = paramMatch[2];
    }
    const defaultMatch = paramMatch[4].match(/Default is `([\w\d]+?)`./);
    params.push({
      name: paramMatch[3],
      type,
      fallbackType,
      choices,
      description: paramMatch[4].trim(),
      defaultValue: defaultMatch ? defaultMatch[1] : undefined,
      required: false
    });
  }
  const exampleMatch = strippedComment.match(exampleRegex);
  const example = exampleMatch ? exampleMatch[1].trim() : '';
  const baseComponents: string[] = [];
  let seeMatch;
  while ((seeMatch = seeRegex.exec(strippedComment)) !== null) {
    const baseComponentsMatch = /\{@link (\w+)\} for other props available/.exec(seeMatch[1]);
    if (baseComponentsMatch) {
      baseComponents.push(baseComponentsMatch[1]);
    }
  }
  return {
    description,
    params,
    example,
    baseComponents
  };
}

function extractTsComments(text: string) {
  const comments: ComponentSpec[] = [];
  const commentRegex = /\/\*\*([\s\S]*?)\*\//g;
  let match;
  while ((match = commentRegex.exec(text)) !== null) {
    comments.push(tsCommentToMarkdown(match[1]));
  }
  return comments;
}

function extractComponentComments(text: string) {
  const comments: ComponentSpec[] = [];
  const commentRegex =
    /(\/\*\*([\s\S]*?)\*\/)\nexport const [\w]+ = component\(['"](\w+)['"](,[\S\s]*?)?\)/g;
  let match;
  while ((match = commentRegex.exec(text)) !== null) {
    const doc = { name: match[3], ...tsCommentToMarkdown(match[2]) };
    comments.push(doc);
  }
  return comments;
}

function* walk(folderPath: string): IterableIterator<string> {
  for (const entry of readdirSync(folderPath, { withFileTypes: true })) {
    if (entry.isFile() && (entry.name.endsWith('.tsx') || entry.name.endsWith('.ts'))) {
      yield join(folderPath, entry.name);
    }

    if (entry.isDirectory()) {
      yield* walk(join(folderPath, entry.name));
    }
  }
}

function scanComponentDocs(folderPath: string) {
  // Walk through the folder and extract comments from all files.
  const allComments: ComponentSpec[] = [];
  for (const filePath of walk(folderPath)) {
    const tsCode = readFileSync(filePath, { encoding: 'utf-8' });
    const components = extractComponentComments(tsCode);
    const names = components.map(c => c.name!);
    allComments.push(...components);
    if (filePath.endsWith('essentials.tsx') || filePath.endsWith('utils.tsx')) {
      basicComponents.push(...names.filter(name => name !== 'Image' && name !== 'Object'));
      dataDisplays.push(...names.filter(name => name === 'Image' || name === 'Object'));
    } else if (filePath.endsWith('instructions.tsx')) {
      intentions.push(...names);
    } else if (filePath.endsWith('document.tsx') || filePath.endsWith('table.tsx')) {
      dataDisplays.push(...names);
    } else {
      utilities.push(...names);
    }
  }
  return allComments;
}

function docsToMarkdown(docs: ComponentSpec[]) {
  const parts: string[] = [];
  parts.push('# Components');
  const categories = [
    { title: 'Basic Components', names: basicComponents },
    { title: 'Intentions', names: intentions },
    { title: 'Data Displays', names: dataDisplays },
    { title: 'Utilities', names: utilities }
  ];
  for (const { title, names } of categories) {
    parts.push(`## ${title}`);
    for (const name of names.sort()) {
      const doc = docs.find(d => d.name === name)!;
      parts.push(`### ${name}`);
      parts.push(formatComponentDocumentation(doc, 4));
    }
  }
  return parts.join('\n\n');
}

function camelToSnake(str: string): string {
  return str
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1_$2') // Handles cases like "XMLFile" -> "XML_File"
    .replace(/([a-z\d])([A-Z])/g, '$1_$2') // Handles "camelCase" -> "camel_Case"
    .toLowerCase(); // Converts to lowercase: "XML_File" -> "xml_file"
}

function getPythonType(jsonType: string, paramName: string): string {
  const lcJsonType = jsonType.toLowerCase();
  switch (lcJsonType) {
    case 'string':
      return 'str';
    case 'boolean':
      return 'bool';
    case 'buffer':
      return 'bytes';
    case 'number':
      // Heuristic for int vs float based on common parameter names
      if (
        paramName.includes('max') ||
        paramName.includes('count') ||
        paramName.includes('depth') ||
        paramName.endsWith('Index')
      ) {
        return 'int';
      }
      return 'float';
    case 'object':
      return 'Any'; // Could be Dict[str, Any]
    case 'regexp':
      return 'str'; // Python uses strings for regex patterns
    default:
      if (jsonType.endsWith('[]')) {
        // Handles array types like TreeItemData[]
        return 'List[Any]'; // Generic list type
      }
      // For unknown or complex non-array types (e.g., a specific object schema name)
      return 'Any';
  }
}

function generatePythonMethod(tag: ComponentSpec): string {
  const methodName = camelToSnake(tag.name!);
  let paramsSignatureList: string[] = ['        self'];
  let argsDocstring = '';
  const callArgsList: string[] = [`tag_name="${tag.name}"`];

  tag.params.forEach(param => {
    const paramName = param.name; // Use original JSON name for Python parameter
    const pythonType = getPythonType(param.type, paramName);
    const typeHint = `Optional[${pythonType}]`;

    paramsSignatureList.push(`        ${paramName}: ${typeHint} = None`);
    callArgsList.push(`${paramName}=${paramName}`);

    let paramDesc = param.description.replace(/\n/g, '\n            ');
    if (param.defaultValue !== undefined) {
      const defValStr =
        typeof param.defaultValue === 'string' ? `"${param.defaultValue}"` : param.defaultValue;
      paramDesc += ` Default is \`${defValStr}\`.`;
    }
    if (param.choices && param.choices.length > 0) {
      paramDesc += ` Choices: ${param.choices.map(c => `\`${JSON.stringify(c)}\``).join(', ')}.`;
    }
    argsDocstring += `            ${paramName} (${typeHint}): ${paramDesc}\n`;
  });

  paramsSignatureList.push('        **kwargs: Any');

  const paramsString = paramsSignatureList.join(',\n');

  let docstring = `"""${tag.description.replace(/\n/g, '\n        ')}\n\n`;
  if (argsDocstring) {
    docstring += `        Args:\n${argsDocstring}`;
  }
  if (tag.example) {
    const exampleIndented = tag.example
      .replace(/\\/g, '\\\\') // Escape backslashes for string literal
      .replace(/"""/g, '\\"\\"\\"') // Escape triple quotes if any in example
      .replace(/\n/g, '\n            ');
    docstring += `\n        Example:\n            ${exampleIndented}\n`;
  }
  docstring += `        """`;

  const methodBody = `return self.tag(
            ${callArgsList.join(',\n            ')},
            **kwargs,
        )`;

  return `
    def ${methodName}(
${paramsString},
    ):
        ${docstring}
        ${methodBody}
    `;
}

function generatePythonFile(jsonData: ComponentSpec[]): string {
  let pythonCode = `# This file is auto-generated from component documentation.
# Do not edit manually. Run \`npm run build-comment\` to regenerate.

from typing import Optional, Any, Union, List, Dict
# from numbers import Number # For more specific number types if needed

class _TagLib:

    def tag(self, tag_name: str, **kwargs: Any) -> Any:
        """Helper method to create a tag with the given name and attributes.
        Implemented by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
`;

  jsonData.forEach(tag => {
    if (!tag.name) {
      console.warn('Skipping tag with no name:', tag);
      return;
    }
    pythonCode += generatePythonMethod(tag);
  });

  return pythonCode;
}

const allDocs = scanComponentDocs('packages/poml');
const pythonCode = generatePythonFile(allDocs);
writeFileSync('packages/poml/assets/componentDocs.json', JSON.stringify(allDocs, null, 2));
writeFileSync('docs/language/components.md', docsToMarkdown(allDocs));
writeFileSync('python/poml/_tags.py', pythonCode);
console.log('Component documentation generated successfully!');



================================================
FILE: packages/poml-vscode/lsp/server.ts
================================================
import {
  createConnection,
  TextDocuments,
  Diagnostic,
  DiagnosticSeverity,
  ProposedFeatures,
  InitializeParams,
  DidChangeConfigurationNotification,
  CompletionItem,
  CompletionItemKind,
  TextDocumentPositionParams,
  TextDocumentSyncKind,
  InitializeResult,
  DocumentDiagnosticReportKind,
  type DocumentDiagnosticReport,
  DocumentDiagnosticParams,
  HoverParams,
  MarkupKind,
  RelatedFullDocumentDiagnosticReport,
  TelemetryEventNotification,
  FullDocumentDiagnosticReport,
  UnchangedDocumentDiagnosticReport,
  CodeLens,
  CodeLensParams,
  Command,
  ExecuteCommandParams,
  Range
} from 'vscode-languageserver/node';

import { TextDocument } from 'vscode-languageserver-textdocument';
import * as crypto from 'crypto';
import { Message, _readWithFile, writeWithSourceMap, SourceMapMessage, SourceMapRichContent, richContentFromSourceMap } from 'poml';
import {
  ErrorCollection,
  BufferCollection,
  findComponentByAlias,
  listComponents,
  Parameter,
  ReadError,
  RichContent,
  SystemError,
  WriteError
} from 'poml/base';
import { PomlFile, PomlToken } from 'poml/file';
import { encodingForModel, Tiktoken } from 'js-tiktoken';
import { readFile } from 'fs/promises';
import * as fs from 'fs';
import { fileURLToPath, pathToFileURL } from 'url';
import { PreviewParams, PreviewMethodName, PreviewResponse, WebviewUserOptions } from '../panel/types';
import { formatComponentDocumentation, formatParameterDocumentation } from './documentFormatter';
import {
  DelayedTelemetryReporter,
  TelemetryEvent,
  TelemetryServer
} from 'poml-vscode/util/telemetryServer';
import { parseJsonWithBuffers } from 'poml/util/trace';
import { getImageWidthHeight } from 'poml/util/image';
import { estimateImageTokens } from 'poml/util/tokenCounterImage';

interface ComputationCache {
  key: string; // Can be file uri, file content, ...
  latestComputedTime: number;
  latestResult: PreviewResponse;
}

interface DiagnosticCache {
  key: string;
  fileContent: string;
  diagnostics: Diagnostic[];
}

class PomlLspServer {
  // Create a connection for the server, using Node's IPC as a transport.
  // Also include all preview / proposed LSP features.
  private readonly connection;
  private readonly documents;
  private throttleTime: number;
  private cache: Map<string, ComputationCache>;
  private diagnosticCache: Map<string, DiagnosticCache>;
  private encodingCache: Map<string, Tiktoken>;
  private associatedOptions: Map<string, WebviewUserOptions>;
  private telemetryReporter: TelemetryServer;
  private statisticsReporter: DelayedTelemetryReporter;
  private edittingReporter: DelayedTelemetryReporter;
  private diagnosticsReporter: DelayedTelemetryReporter;
  private statistics: { [key: string]: number };

  private hasDiagnosticRelatedInformationCapability: boolean;

  constructor() {
    this.connection = createConnection(ProposedFeatures.all);

    // Create a simple text document manager.
    this.documents = new TextDocuments(TextDocument);

    this.hasDiagnosticRelatedInformationCapability = false;

    this.throttleTime = 10; // 10 ms
    this.cache = new Map();
    this.diagnosticCache = new Map();
    // this is a hack to store the options in the preview into the server.
    this.associatedOptions = new Map();

    this.encodingCache = new Map();

    this.statistics = {};

    this.telemetryReporter = new TelemetryServer(this.sendTelemetry.bind(this));
    this.statisticsReporter = new DelayedTelemetryReporter(this.telemetryReporter);
    this.edittingReporter = new DelayedTelemetryReporter(this.telemetryReporter);
    this.diagnosticsReporter = new DelayedTelemetryReporter(this.telemetryReporter);
  }

  private getAssociatedOptions(uri: string): WebviewUserOptions {
    let options = this.associatedOptions.get(uri);
    if (!options) {
      const filePath = fileURLToPath(uri);
      const base = filePath.replace(/(\.source)?\.poml$/i, '');
      const contexts: string[] = [];
      const stylesheets: string[] = [];
      if (fs.existsSync(`${base}.context.json`)) {
        contexts.push(`${base}.context.json`);
      }
      if (fs.existsSync(`${base}.stylesheet.json`)) {
        stylesheets.push(`${base}.stylesheet.json`);
      }
      options = {
        speakerMode: true,
        displayFormat: 'plain',
        contexts,
        stylesheets,
      };
      if (contexts.length > 0 || stylesheets.length > 0) {
        this.associatedOptions.set(uri, options);
      }
    }
    return options;
  }

  public listen() {
    this.connection.onInitialize((params: InitializeParams): InitializeResult => {
      const capabilities = params.capabilities;

      // We only need the related info capability currently
      this.hasDiagnosticRelatedInformationCapability = !!(
        capabilities.textDocument &&
        capabilities.textDocument.publishDiagnostics &&
        capabilities.textDocument.publishDiagnostics.relatedInformation
      );

      return {
        capabilities: {
          textDocumentSync: TextDocumentSyncKind.Incremental,
          completionProvider: {
            resolveProvider: true
          },
          diagnosticProvider: {
            interFileDependencies: false,
            workspaceDiagnostics: false
          },
          hoverProvider: true,
          codeLensProvider: { resolveProvider: false },
          executeCommandProvider: { commands: ['poml.evaluateExpression'] }
        }
      };
    });

    this.connection.onHover(this.onHover.bind(this));
    this.connection.onCompletion(this.onCompletion.bind(this));
    this.connection.onCompletionResolve(this.onCompletionResolve.bind(this));
    this.connection.languages.diagnostics.on(this.onDiagnostic.bind(this));

    this.connection.onRequest(PreviewMethodName, this.onPreview.bind(this));
    this.connection.onCodeLens(this.onCodeLens.bind(this));
    this.connection.onExecuteCommand(this.onExecuteCommand.bind(this));

    // Provide a way to force the diagnostics to be reset.
    this.documents.onDidSave(change => {
      // Invalidate the diagnostic cache
      const uri = change.document.uri.toString();
      this.diagnosticCache.delete(uri);
      BufferCollection.clear();
      // Ask the client to pull fresh diagnostics
      this.connection.languages.diagnostics.refresh();
    });

    // Make the text document manager listen on the connection
    // for open, change and close text document events
    this.documents.listen(this.connection);

    // Listen on the connection
    return this.connection.listen();
  }

  private async sendTelemetry(data: any) {
    return await this.connection.sendNotification(TelemetryEventNotification.method, data);
  }

  private async incrementStatistics(key: string, n?: number) {
    // Do not await this.
    this.statistics[key] = (this.statistics[key] ?? 0) + (n ?? 1);
    const reported = await this.statisticsReporter.reportTelemetry(
      TelemetryEvent.LanguageServerStatistics,
      this.statistics
    );
    if (reported) {
      this.statistics = {};
    }
  }

  private onCodeLens(params: CodeLensParams): CodeLens[] {
    const document = this.documents.get(params.textDocument.uri);
    if (!document) {
      return [];
    }
    const text = document.getText();
    const pomlFile = new PomlFile(text);
    const tokens = pomlFile.getExpressionTokens();
    const lenses: CodeLens[] = [];
    for (let i = 0; i < tokens.length; i++) {
      const token = tokens[i];
      if (token.expression === undefined) {
        continue;
      }
      const expr = token.expression;
      let titleExpr = expr;
      if (titleExpr.length > 20) {
        titleExpr = `${titleExpr.slice(0, 10)}...${titleExpr.slice(-10)}`;
      }
      const command: Command = {
        title: `▶️ Evaluate ${titleExpr}`,
        command: 'poml.evaluateExpression',
        arguments: [params.textDocument.uri, text, token.range.start, token.range.end]
      };
      const vscodeRange: Range = {
        start: document.positionAt(token.range.start),
        end: document.positionAt(token.range.end + 1)
      }
      lenses.push({ range: vscodeRange, command });
    }
    return lenses;
  }

  private async onExecuteCommand(params: ExecuteCommandParams): Promise<any> {
    if (params.command !== 'poml.evaluateExpression') {
      return;
    }
    const uri = params.arguments?.[0] as string | undefined;
    const text = params.arguments?.[1] as string | undefined;
    const rangeStart = params.arguments?.[2] as number | undefined;
    const rangeEnd = params.arguments?.[3] as number | undefined;
    if (!uri || !text || rangeStart === undefined || rangeEnd === undefined) {
      this.connection.console.error(`${new Date().toLocaleString()} Invalid arguments for poml.evaluateExpression command`);
      return;
    }
    const expression = text.slice(rangeStart, rangeEnd + 1);
    ErrorCollection.clear();
    const file = new PomlFile(text, undefined, fileURLToPath(uri));

    const options = this.getAssociatedOptions(uri);
    let context: any = {};
    if (options) {
      for (const c of options.contexts ?? []) {
        try {
          context = { ...context, ...parseJsonWithBuffers(await readFile(c, 'utf-8')) };
        } catch (e) {
          console.error(`Failed to parse context file ${c}: ${e}`);
        }
      }
    }

    file.react(context);

    if (!ErrorCollection.empty()) {
      const err = ErrorCollection.first()?.toString() ?? 'Unknown error';
      this.connection.console.error(`${new Date().toLocaleString()} Error during evaluation: ${expression} => ${err}`);
    }

    const evaluations = file.getExpressionEvaluations({ start: rangeStart, end: rangeEnd });
    if (evaluations.length === 0) {
      this.connection.console.warn(`${new Date().toLocaleString()} No evaluations found for expression: ${expression} (${rangeStart}-${rangeEnd})`);
      return;
    }
    for (let i = 0; i < evaluations.length; i++) {
      let result = evaluations[i];
      if (typeof result === 'object') {
        result = JSON.stringify(result, null, 2);
      }
      if (result.length > 1024) {
        result = `${result.slice(0, 1024)} ...[truncated]`;
      }
      this.connection.console.log(`${new Date().toLocaleString()} [Eval ${i + 1}] ${expression} => ${result}`);
    }
  }

  private getModelEncoding(model: string): Tiktoken {
    if (this.encodingCache.has(model)) {
      return this.encodingCache.get(model)!;
    }
    try {
      const enc = encodingForModel(model as any);
      this.encodingCache.set(model, enc);
      return enc;
    } catch (e) {
      console.warn(`Unknown model "${model}"; using gpt-4o as default: ${e}`);
      const enc = encodingForModel('gpt-4o');
      this.encodingCache.set(model, enc);
      return enc;
    }
  }

  private async computeTokens(content: RichContent, model: string): Promise<number> {
    const enc = this.getModelEncoding(model);
    if (typeof content === 'string') {
      return enc.encode(content).length;
    } else {
      let total = 0;
      for (const part of content) {
        if (typeof part === 'string') {
          total += enc.encode(part).length;
        } else {
          const { width, height } = await getImageWidthHeight(part.base64);
          // For images, we can use a heuristic based on width and height
          total += estimateImageTokens(width, height, { model: model as any });
        }
      }
      return total;
    }
  }

  private async computePreviewResponse(params: PreviewParams): Promise<PreviewResponse> {
    const { speakerMode, uri } = params;

    const filePath = fileURLToPath(uri);
    let documentContent: string = '';
    if (params.text !== undefined) {
      documentContent = params.text;
    } else {
      const textDocument = this.documents.get(uri);

      if (textDocument) {
        documentContent = textDocument.getText();
      } else {
        // Sometimes the request happens before the document is opened
        // so we need to read the file from disk
        try {
          documentContent = await readFile(filePath, 'utf-8');
        } catch (e) {
          // Unable to read the file
          return {
            rawText: '',
            ir: '',
            content: [],
            error: `Unable to read file: ${e}`
          };
        }
      }
    }

    ErrorCollection.clear();
    let ir: string;
    let pomlFile: PomlFile | undefined;
    try {
      let context: { [key: string]: any } = params.inlineContext ?? {};
      for (const c of params.contexts ?? []) {
        try {
          context = { ...context, ...parseJsonWithBuffers(await readFile(c, 'utf-8')) };
        } catch (e) {
          console.error(`Failed to parse context file ${c}: ${e}`);
        }
      }
      let stylesheet: { [key: string]: any } = {};
      for (const s of params.stylesheets ?? []) {
        try {
          stylesheet = { ...stylesheet, ...parseJsonWithBuffers(await readFile(s, 'utf-8')) };
        } catch (e) {
          console.error(`Failed to parse stylesheet file ${s}: ${e}`);
        }
      }

      [ir, pomlFile] = await _readWithFile(documentContent, undefined, context, stylesheet, filePath);
    } catch (e) {
      this.telemetryReporter.reportTelemetryError(TelemetryEvent.ReadUncaughtException, e);
      console.error(e);
      return {
        rawText: documentContent,
        ir: '',
        content: [],
        error: `Unable to perform "read" step when rendering file: ${e}`
      };
    }
    let result: Message[] | RichContent;
    let sourceMap: SourceMapMessage[] | SourceMapRichContent[] | undefined;
    let tokens: { perMessage?: number[]; total: number } | undefined = undefined;
    try {
      if (speakerMode) {
        const map = writeWithSourceMap(ir, { speaker: true }) as SourceMapMessage[];
        sourceMap = map;
        result = map.map(m => ({
          speaker: m.speaker,
          content: richContentFromSourceMap(m.content)
        }));
        if (params.returnTokenCounts) {
          const model = params.returnTokenCounts.model;
          const perMessageTokens = await Promise.all(
            result.map(async m => await this.computeTokens(m.content, model))
          );
          tokens = {
            perMessage: perMessageTokens,
            total: perMessageTokens.reduce((a, b) => a + b, 0)
          };
        }
      } else {
        const map = writeWithSourceMap(ir) as SourceMapRichContent[];
        sourceMap = map;
        result = richContentFromSourceMap(map);
        if (params.returnTokenCounts) {
          const model = params.returnTokenCounts.model;
          tokens = {
            total: await this.computeTokens(result, model)
          };
        }
      }
    } catch (e) {
      this.telemetryReporter.reportTelemetryError(TelemetryEvent.WriteUncaughtException, e);
      console.error(e);
      return {
        rawText: documentContent,
        ir,
        content: [],
        error: `Unable to perform "write" step when rendering file: ${e}`
      };
    }

    return {
      rawText: documentContent,
      ir,
      content: result,
      tokens,
      sourceMap,
      responseSchema: pomlFile?.getResponseSchema()?.toOpenAPI(),
      tools: pomlFile?.getToolsSchema()?.toOpenAI(),
      runtime: pomlFile?.getRuntimeParameters(),
      error: params.returnAllErrors
        ? ErrorCollection.list()
        : ErrorCollection.empty()
          ? undefined
          : ErrorCollection.first().toString()
    };
  }

  private async onPreview(params: PreviewParams): Promise<PreviewResponse> {
    const key = JSON.stringify(params);
    const requestedTime = Date.now();
    await new Promise(resolve => setTimeout(resolve, this.throttleTime));

    // After waiting for, e.g., 10ms, there is a result computed later than the request time.
    if (requestedTime < (this.cache.get(key)?.latestComputedTime ?? 0)) {
      return this.cache.get(key)!.latestResult;
    }

    // Otherwise compute a new one.
    const computedTime = Date.now();
    // FIXME: this is not locked. potentially race
    const response = await this.computePreviewResponse(params);
    const completeTime = Date.now();
    const elapsed = completeTime - computedTime;
    const allocatedTime = elapsed * 2; // Double the time for the next request

    // NOTE: The lsp server uses the configuration from preview as the associated options.
    // This is a hack to set the options in the server.
    this.associatedOptions.set(params.uri.toString(), {
      speakerMode: params.speakerMode,
      displayFormat: params.displayFormat,
      contexts: [...params.contexts],
      stylesheets: [...params.stylesheets]
    });

    // Send telemetry
    this.incrementStatistics('preview');
    this.edittingReporter.reportTelemetry(TelemetryEvent.EdittingCurrently, {
      rawText: response.rawText,
      uri: params.uri,
      request: JSON.stringify(params),
      compileTime: elapsed,
      throttleTime: this.throttleTime
    });

    // Dynamically adjust the throttle time
    const throttleTime = this.throttleTime * 0.9 + allocatedTime * 0.1;
    this.throttleTime = Math.min(Math.max(throttleTime, 10), 1000);

    this.cache.set(key, {
      key,
      latestComputedTime: computedTime, // Use the computed time as the time when source is retrieved
      latestResult: response
    });

    return response;
  }

  private async onDiagnostic(
    params: DocumentDiagnosticParams
  ): Promise<UnchangedDocumentDiagnosticReport | FullDocumentDiagnosticReport> {
    const key = params.textDocument.uri.toString();
    const document = this.documents.get(params.textDocument.uri);
    const cache = this.diagnosticCache.get(key) ?? { key, fileContent: undefined, diagnostics: [] };
    if (cache.fileContent === document?.getText()) {
      // Compute hash of the file content
      const hash = crypto.createHash('sha256').update(cache.fileContent ?? '').digest('hex');
      return {
        kind: DocumentDiagnosticReportKind.Unchanged,
        resultId: hash
      };
    } else {
      const result = document !== undefined ? await this.validateTextDocument(document) : [];
      this.incrementStatistics('diagnostic');
      if (result.length > 0) {
        this.diagnosticsReporter.reportTelemetry(TelemetryEvent.Diagnostics, {
          rawText: document?.getText(),
          uri: params.textDocument.uri.toString(),
          diagnostics: JSON.stringify(result)
        });
      }
      this.diagnosticCache.set(key, { key, fileContent: document!.getText(), diagnostics: result });
      const hash = crypto.createHash('sha256').update(document!.getText()).digest('hex');
      return {
        kind: DocumentDiagnosticReportKind.Full,
        items: result,
        resultId: hash
      };
    }
  }

  private async validateTextDocument(textDocument: TextDocument): Promise<Diagnostic[]> {
    const text = textDocument.getText();
    const diagnostics: Diagnostic[] = [];
    const otherDiagnostics: Record<string, { text: string; diags: Diagnostic[] }> = {};

    const options = this.getAssociatedOptions(textDocument.uri.toString());

    const response = await this.onPreview({
      uri: textDocument.uri,
      text: text,
      speakerMode: options.speakerMode,
      displayFormat: options.displayFormat,
      returnAllErrors: true,
      contexts: options.contexts,
      stylesheets: options.stylesheets,
      returnTokenCounts: undefined
    });
    const errors = Array.isArray(response.error) ? response.error : response.error ? [response.error] : [];

    const normalizeStartEnd = (
      start: number | undefined,
      end: number | undefined,
      length: number
    ): [number, number] => {
      start = start ?? 0;
      if (isNaN(start)) {
        start = 0;
      }
      end = Math.max(start + 1, end !== undefined ? end + 1 : length);
      if (isNaN(end)) {
        end = length;
      }
      return [start, end];
    };

    for (const e of errors) {
      const src = (e as any).sourcePath
        ? pathToFileURL((e as any).sourcePath).toString()
        : textDocument.uri.toString();
      let targetText = text;
      let doc = textDocument;
      if (src !== textDocument.uri.toString()) {
        const cached = this.documents.get(src as any);
        if (cached) {
          targetText = cached.getText();
          doc = cached;
        } else {
          try {
            targetText = await readFile((e as any).sourcePath, 'utf-8');
          } catch {
            targetText = '';
          }
          // FIXME: I don't think we should create a new TextDocument here.
          // Confirm this setting.
          doc = TextDocument.create(src, 'poml', 0, targetText);
        }
      }
      if (typeof e === 'string') {
        const diag = {
          severity: DiagnosticSeverity.Error,
          range: {
            start: doc.positionAt(0),
            end: doc.positionAt(targetText.length)
          },
          message: e,
          source: 'POML Unknown Error (please report)'
        } as Diagnostic;
        if (src === textDocument.uri.toString()) {
          diagnostics.push(diag);
        } else {
          (otherDiagnostics[src] ??= { text: targetText, diags: [] }).diags.push(diag);
        }
      } else if (e instanceof ReadError) {
        const [start, end] = normalizeStartEnd(e.startIndex, e.endIndex, targetText.length);
        const diag: Diagnostic = {
          severity: DiagnosticSeverity.Warning,
          range: {
            start: doc.positionAt(start),
            end: doc.positionAt(end)
          },
          message: e.message,
          source: 'POML Reader'
        };
        if (src === textDocument.uri.toString()) {
          diagnostics.push(diag);
        } else {
          (otherDiagnostics[src] ??= { text: targetText, diags: [] }).diags.push(diag);
        }
      } else if (e instanceof WriteError) {
        const [start, end] = normalizeStartEnd(e.startIndex, e.endIndex, targetText.length);
        const diagnostic: Diagnostic = {
          severity: DiagnosticSeverity.Warning,
          range: {
            start: doc.positionAt(start),
            end: doc.positionAt(end)
          },
          message: e.message,
          source: 'POML Writer'
        };
        if (this.hasDiagnosticRelatedInformationCapability) {
          diagnostic.relatedInformation = [
            {
              location: {
                uri: textDocument.uri,
                range: diagnostic.range
              },
              message:
                e.relatedIr?.slice(
                  e.startIndex ?? 0,
                  e.endIndex !== undefined ? e.endIndex + 1 : text.length
                ) ?? ''
            }
          ];
        }
        if (src === textDocument.uri.toString()) {
          diagnostics.push(diagnostic);
        } else {
          (otherDiagnostics[src] ??= { text: targetText, diags: [] }).diags.push(diagnostic);
        }
      } else if (e instanceof SystemError) {
        const diag = {
          severity: DiagnosticSeverity.Error,
          range: {
            start: doc.positionAt(0),
            end: doc.positionAt(targetText.length)
          },
          message: e.message,
          source: 'POML System (please report)'
        } as Diagnostic;
        if (src === textDocument.uri.toString()) {
          diagnostics.push(diag);
        } else {
          (otherDiagnostics[src] ??= { text: targetText, diags: [] }).diags.push(diag);
        }
      } else {
        const diag = {
          severity: DiagnosticSeverity.Error,
          range: {
            start: doc.positionAt(0),
            end: doc.positionAt(targetText.length)
          },
          message: e.message,
          source: 'POML Unknown Error (please report)'
        } as Diagnostic;
        if (src === textDocument.uri.toString()) {
          diagnostics.push(diag);
        } else {
          (otherDiagnostics[src] ??= { text: targetText, diags: [] }).diags.push(diag);
        }
      }
    }

    for (const [uri, { text: targetText, diags }] of Object.entries(otherDiagnostics)) {
      this.diagnosticCache.set(uri, { key: uri, fileContent: targetText, diagnostics: diags });
      this.connection.sendDiagnostics({ uri, diagnostics: diags });
    }

    return diagnostics;
  }

  private async onHover(params: HoverParams) {
    const textDocument = this.documents.get(params.textDocument.uri);
    if (textDocument === undefined) {
      return;
    }

    const offset = textDocument.offsetAt(params.position);
    const pomlFile = new PomlFile(textDocument.getText());
    const token = pomlFile.getHoverToken(offset);
    if (token) {
      this.telemetryReporter.reportTelemetry(TelemetryEvent.Hover, {
        rawText: textDocument.getText(),
        uri: textDocument.uri.toString(),
        token: JSON.stringify(token)
      });
      this.incrementStatistics('hover');
      const markdown = {
        kind: MarkupKind.Markdown,
        value:
          token.type !== 'element' && token.attribute
            ? this.queryDocumentationForParameter(token.element!, token.attribute)
            : this.queryDocumentationForComponent(token.element!)
      };
      return {
        contents: markdown,
        range: {
          start: textDocument.positionAt(token.range.start),
          end: textDocument.positionAt(token.range.end + 1)
        }
      };
    }
  }

  private queryDocumentationForComponent(componentName: string): string {
    const component = findComponentByAlias(componentName);
    if (typeof component === 'string') {
      return component;
    }
    const doc = component.spec();
    if (doc === undefined) {
      return `Documentation unavailable for ${component.name}.`;
    } else {
      return formatComponentDocumentation(doc);
    }
  }

  private queryDocumentationForParameter(componentName: string, parameter: string): string {
    const component = findComponentByAlias(componentName);
    if (typeof component === 'string') {
      return component;
    }
    const doc = component.spec();
    if (doc === undefined) {
      return `Documentation unavailable for ${component.name}.`;
    } else {
      const param = doc.params.find(param => param.name === parameter);
      if (param === undefined) {
        return `Documentation unavailable for ${parameter} in component ${component.name}.`;
      } else {
        return formatParameterDocumentation(param);
      }
    }
  }

  private onCompletion(textDocumentPosition: TextDocumentPositionParams): CompletionItem[] {
    const textDocument = this.documents.get(textDocumentPosition.textDocument.uri);
    if (textDocument === undefined) {
      return [];
    }
    const offset = textDocument.offsetAt(textDocumentPosition.position);
    const pomlFile = new PomlFile(textDocument.getText());
    const suggestions = pomlFile.getCompletions(offset);

    const toTextEdit = (suggestion: PomlToken, content: string) => {
      return {
        range: {
          start: textDocument.positionAt(suggestion.range.start),
          end: textDocument.positionAt(suggestion.range.end + 1)
        },
        newText: content
      };
    };

    const command = { command: 'poml.telemetry.completion', title: '' };

    const vscodeSuggestions = suggestions.map((suggestion): CompletionItem | undefined => {
      if (suggestion.type === 'element') {
        return {
          label: suggestion.element!,
          kind: CompletionItemKind.Class,
          textEdit: toTextEdit(suggestion, suggestion.element!),
          data: suggestion,
          command
        };
      } else if (suggestion.type === 'attribute' && suggestion.attribute !== undefined) {
        return {
          label: suggestion.attribute,
          kind: CompletionItemKind.Property,
          textEdit: toTextEdit(suggestion, suggestion.attribute),
          data: suggestion,
          command
        };
      } else if (suggestion.type === 'attributeValue' && suggestion.value !== undefined) {
        return {
          label: suggestion.value,
          kind: CompletionItemKind.Value,
          textEdit: toTextEdit(suggestion, suggestion.value),
          data: suggestion,
          command
        };
      } else {
        return undefined;
      }
    });
    const result = vscodeSuggestions.filter(suggestion => suggestion !== undefined);
    this.incrementStatistics('completion');
    this.incrementStatistics('completionItems', result.length);
    return result;
  }

  private onCompletionResolve(item: CompletionItem): CompletionItem {
    if (item.data === undefined) {
      return item;
    }
    const suggestion = item.data as PomlToken;
    if (suggestion.type === 'element') {
      item.detail = suggestion.element! + ' (Component)';
      item.documentation = {
        kind: MarkupKind.Markdown,
        value: this.queryDocumentationForComponent(suggestion.element!)
      };
    } else if (
      (suggestion.type === 'attribute' || suggestion.type === 'attributeValue') &&
      suggestion.attribute !== undefined
    ) {
      item.detail = suggestion.attribute + ' (Parameter of ' + suggestion.element! + ')';
      item.documentation = {
        kind: MarkupKind.Markdown,
        value: this.queryDocumentationForParameter(suggestion.element!, suggestion.attribute)
      };
    }
    this.incrementStatistics('completionResolve');
    return item;
  }
}

const lspServer = new PomlLspServer();
lspServer.listen();



================================================
FILE: packages/poml-vscode/panel/content.tsx
================================================
import * as React from 'react';
import { renderToString } from 'react-dom/server';
import { PreviewResponse, WebviewState, WebviewUserOptions } from './types';
import { Message, RichContent, SourceMapMessage, SourceMapRichContent } from 'poml';
import { Converter as MarkdownConverter } from 'showdown';

type HeadlessPomlVscodePanelContentProps = WebviewUserOptions & PreviewResponse;

interface PomlVscodePanelContentProps extends WebviewState, HeadlessPomlVscodePanelContentProps {
  extensionResourcePath: (mediaFile: string) => string;
  localResourcePath: (resourceFile: string) => string;
}

function lineFromIndex(text: string, index: number): number {
  return text.slice(0, index).split(/\r?\n/g).length - 1;
}

function ButtonContent(props: { icon: string; content: string }) {
  const { icon, content } = props;
  return (
    <>
      <div className="avatar">
        <i className={`codicon codicon-${icon}`}></i>
      </div>
      <div className="content">{content}</div>
    </>
  );
}

function ToolBar(props: WebviewUserOptions) {
  const { speakerMode, displayFormat } = props;

  const applicableDisplayFormats = [
    { value: 'rendered', content: 'Rendered' },
    { value: 'plain', content: 'Plain Text' },
    { value: 'ir', content: 'IR (debug mode)' }
  ];

  return (
    <div className="toolbar">
      <div className="toolbar-buttons">
        <div className="button oneclick" id="copy" role="button" tabIndex={0} aria-label="Copy content">
          <ButtonContent icon="copy" content="Copy" />
        </div>

        <div
          className={`button onoff ${props.contexts.length + props.stylesheets.length ? 'active' : ''}`}
          id="context-stylesheet"
          role="button"
          tabIndex={0}
          aria-label="Toggle context and stylesheet view"
        >
          <ButtonContent icon="references" content="Context & Stylesheet" />
          {props.contexts.length + props.stylesheets.length > 0 && (
            <div className="badge">
              {props.contexts.length + props.stylesheets.length}
            </div>
          )}
        </div>

        <div
          className={`button onoff ${speakerMode ? 'active' : ''}`}
          id="speaker-mode"
          data-value={speakerMode}
          role="button"
          tabIndex={0}
          aria-label="Toggle speaker mode"
        >
          <ButtonContent icon="comment-discussion" content="Speaker Mode" />
        </div>
        <div className="button menu-selection" id="display-format" data-value={displayFormat} role="button" tabIndex={0} aria-label="Select display format">
          <ButtonContent
            icon="code-oss"
            content={`Display: ${applicableDisplayFormats.find(val => val.value === displayFormat)?.content}`}
          />
          <div className="expand">
            <i className="codicon codicon-triangle-down"></i>
          </div>
          <div className="menu">
            {applicableDisplayFormats.map(item => (
              <div
                className={`item ${displayFormat === item.value ? 'selected' : ''}`}
                data-value={item.value}
                key={item.value}
                role="menuitem"
                tabIndex={0}
                aria-label={`Display format: ${item.content}`}
              >
                <ButtonContent icon="check" content={item.content} />
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className={`toolbar-files chips ${props.contexts.length + props.stylesheets.length ? '' : 'hidden'}`} id="context-stylesheet-files">
        {/* This is set on the client side. */}
      </div>
    </div>
  );
}

function CodeBlock(props: { className?: string; content: RichContent; mappings?: SourceMapRichContent[]; rawText?: string }) {
  const { content, className, mappings, rawText } = props;
  if (mappings && rawText) {
    const spans = mappings.map((m, i) => {
      const text = typeof m.content === 'string' ? m.content : JSON.stringify(m.content, null, 2);
      const line = lineFromIndex(rawText, m.startIndex);
      return (
        <span key={i} data-line={line} className="code-span">{text}</span>
      );
    });
    return (
      <pre className={className}>
        <code>{spans}</code>
      </pre>
    );
  }
  if (typeof content === 'string') {
    return (
      <pre className={className}>
        <code>{content}</code>
      </pre>
    );
  } else {
    return (
      <pre className={className}>
        <code>{JSON.stringify(content, null, 2)}</code>
      </pre>
    );
  }
}

function Markdown(props: { content: RichContent }) {
  const converter = new MarkdownConverter({
    headerLevelStart: 2,
    strikethrough: true,
    tables: true,
    underline: true
  });

  const concatenatedMarkdown =
    typeof props.content === 'string'
      ? props.content
      : props.content
        .map(part => {
          if (typeof part === 'string') {
            return part;
          } else {
            const { type, base64, alt } = part;
            return `![${alt ?? ''}](data:${type};base64,${base64})`;
          }
        })
        .join('\n\n');

  return <div dangerouslySetInnerHTML={{ __html: converter.makeHtml(concatenatedMarkdown) }} />;
}

function ChatMessages(props: {
  messages: Message[];
  toRender: boolean;
  tokens?: number[];
  mappings?: SourceMapMessage[];
  rawText?: string;
  responseSchema?: { [key: string]: any };
  tools?: { [key: string]: any }[];
  runtime?: { [key: string]: any };
}) {
  const { messages, toRender, tokens, mappings, rawText, responseSchema, tools, runtime } = props;
  const chatMessages = messages.map((message, idx) => {
    const map = mappings ? mappings[idx] : undefined;
    const line = map && rawText !== undefined ? lineFromIndex(rawText, map.startIndex) : undefined;
    let role: string = message.speaker;
    let icon = 'feedback';
    if (role === 'system') {
      role = 'System';
      icon = 'lightbulb';
    } else if (role === 'human') {
      role = 'Human';
      icon = 'account';
    } else if (role === 'ai') {
      role = 'AI';
      icon = 'robot';
    }
    return (
      <div className={`chat-message chat-message-${message.speaker}`} key={`message-${idx}`} data-line={line}>
        <div className="chat-message-header">
          <div className="content">
            <div className="avatar">
              <div className={`codicon codicon-${icon}`}></div>
            </div>
            <h3 className="name">
              {role}
              {tokens && tokens[idx] !== undefined && (
                <span className="token-count">{tokens[idx]} tokens</span>
              )}
            </h3>
          </div>
          <div className="chat-message-toolbar">
            <div className="toolbar-item tooltip-anchor">
              <a
                className="codicon codicon-code"
                role="button"
                aria-label="Jump to Source Code"
                data-line={line}
              ></a>
              <span className="tooltip">Source Code</span>
            </div>
            <div className="toolbar-item tooltip-anchor">
              <a
                className="codicon codicon-copy"
                role="button"
                aria-label="Copy"
                data-value={
                  typeof message.content === 'string'
                    ? message.content
                    : JSON.stringify(message.content, null, 2)
                }
              ></a>
              <span className="tooltip">Copy</span>
            </div>
          </div>
        </div>
        <div className="chat-message-content">
          {toRender ? (
            <Markdown content={message.content} />
          ) : (
            <CodeBlock content={message.content} mappings={map?.content} rawText={rawText} />
          )}
        </div>
      </div>
    );
  });
  return <div className="chat-messages">
    {chatMessages}
    {(responseSchema || tools || runtime) && (
      <div className="chat-message">
        <div className="chat-message-header">
          <div className="content">
            <div className="avatar">
              <div className="codicon codicon-symbol-keyword"></div>
            </div>
            <h3 className="name">
              Meta information
            </h3>
          </div>
        </div>
        <div className="chat-message-content">
          {responseSchema && (
            <>
              <h4>Response Schema</h4>
              <CodeBlock content={JSON.stringify(responseSchema, null, 2)} />
            </>
          )}
          {tools && (
            <>
              <h4>Tool Definitions</h4>
              <CodeBlock content={JSON.stringify(tools, null, 2)} />
            </>
          )}
          {runtime && (
            <>
              <h4>Runtime Parameters</h4>
              <CodeBlock content={JSON.stringify(runtime, null, 2)} />
            </>
          )}
        </div>
      </div>)}
  </div>;
}

function Content(props: WebviewUserOptions & PreviewResponse) {
  let { displayFormat, ir, content, sourceMap, rawText, tokens, responseSchema, tools, runtime } = props;

  let toCopy: string =
    typeof content === 'string'
      ? content
      : JSON.stringify(content, null, 2);
  let result: React.ReactElement;
  if (content.length > 0 && content[0].hasOwnProperty('speaker')) {
    content = content as Message[];
    if (displayFormat === 'ir') {
      result = <CodeBlock content={ir} />;
    } else if (displayFormat === 'plain') {
      result = (
        <ChatMessages
          messages={content}
          toRender={false}
          tokens={tokens?.perMessage}
          mappings={sourceMap as SourceMapMessage[]}
          rawText={rawText}
          responseSchema={responseSchema}
          tools={tools}
          runtime={runtime}
        />
      );
    } else if (displayFormat === 'rendered') {
      result = <ChatMessages messages={content} toRender={true} tokens={tokens?.perMessage} responseSchema={responseSchema} tools={tools} runtime={runtime} />;
    } else {
      result = <div>Invalid display format</div>;
    }
  } else {
    content = content as RichContent;
    if (displayFormat === 'ir') {
      result = <div className="main-container"><CodeBlock content={ir} /></div>;
    } else if (displayFormat === 'plain') {
      result = <div className="main-container"><CodeBlock content={content} mappings={sourceMap as SourceMapRichContent[]} rawText={rawText} /></div>;
    } else if (displayFormat === 'rendered') {
      result = <div className="main-container"><Markdown content={content} /></div>;
    } else {
      result = <div>Invalid display format</div>;
    }
  }

  return (
    <div className="main" id="content">
      <div className="hidden" id="copy-content" data-value={toCopy} />
      {result}
      {tokens && (
        <div className="token-total">Total tokens: {tokens.total}</div>
      )}
    </div>
  );
}

function Root(props: PomlVscodePanelContentProps) {
  const { extensionResourcePath, localResourcePath, ...state } = props;
  const nonce = new Date().getTime() + '' + new Date().getMilliseconds();

  return (
    <html lang="en">
      <head>
        <meta httpEquiv="Content-type" content="text/html;charset=UTF-8" />
        <meta id="webview-state" data-state={JSON.stringify(props)} />
        <script src={extensionResourcePath('index.js')} nonce={nonce}></script>
        <link href={extensionResourcePath('style.css')} rel="stylesheet" nonce={nonce} />
        <link href={extensionResourcePath('codicons/codicon.css')} rel="stylesheet" nonce={nonce} />
        <base href={localResourcePath(state.source)} />
      </head>
      <body className="vscode-body">
        <ToolBar {...state} />
        <Content {...state} />
      </body>
    </html>
  );
}

export function pomlVscodePanelContent(config: PomlVscodePanelContentProps) {
  return renderToString(<Root {...config} />);
}

export function headlessPomlVscodePanelContent(config: HeadlessPomlVscodePanelContentProps) {
  return renderToString(<Content {...config} />);
}



================================================
FILE: packages/poml-vscode/panel/manager.ts
================================================
import * as vscode from 'vscode';
import { Logger } from '../util/logger';
import { disposeAll } from '../util/dispose';
import { HTMLFileTopmostLineMonitor } from '../util/topmostLineMonitor';
import { PanelSettings } from './types';
import { POMLWebviewPanel } from './panel';
import { SettingsManager } from '../settings';

export class POMLWebviewPanelManager implements vscode.WebviewPanelSerializer {
  private static readonly pomlPreviewActiveContextKey = 'pomlPreviewFocus';

  private readonly _topmostLineMonitor = new HTMLFileTopmostLineMonitor();
  private readonly _previewConfigurations = new SettingsManager();
  private readonly _previews: POMLWebviewPanel[] = [];
  private _activePreview: POMLWebviewPanel | undefined = undefined;
  private readonly _disposables: vscode.Disposable[] = [];

  public constructor(
    private readonly _extensionContext: vscode.ExtensionContext,
    private readonly _logger: Logger,
  ) {
    this._disposables.push(vscode.window.registerWebviewPanelSerializer(POMLWebviewPanel.viewType, this));
  }

  public dispose(): void {
    disposeAll(this._disposables);
    disposeAll(this._previews);
  }

  public refresh() {
    for (const preview of this._previews) {
      preview.refresh();
    }
  }

  public updateConfiguration() {
    for (const preview of this._previews) {
      preview.updateConfiguration();
    }
  }

  public preview(
    resource: vscode.Uri,
    previewSettings: PanelSettings
  ): void {
    let preview = this.getExistingPreview(resource, previewSettings);
    if (preview) {
      preview.reveal(previewSettings.previewColumn);
    } else {
      preview = this.createNewPreview(resource, previewSettings);
    }

    preview.update(resource);
  }

  public get previewConfigurations() {
    return this._previewConfigurations;
  }

  public get activePreviewResource() {
    return this._activePreview && this._activePreview.pomlUri;
  }

  public get activePreview() {
    return this._activePreview;
  }

  public toggleLock() {
    const preview = this._activePreview;
    if (preview) {
      preview.toggleLock();

      // Close any previews that are now redundant, such as having two dynamic previews in the same editor group
      for (const otherPreview of this._previews) {
        if (otherPreview !== preview && preview.matches(otherPreview)) {
          otherPreview.dispose();
        }
      }
    }
  }

  public async deserializeWebviewPanel(
    webview: vscode.WebviewPanel,
    state: any
  ): Promise<void> {
    const preview = await POMLWebviewPanel.revive(
      webview,
      state,
      this._extensionContext,
      this._previewConfigurations,
      this._logger,
      this._topmostLineMonitor
    );

    this.registerPreview(preview);
  }

  private getExistingPreview(
    resource: vscode.Uri,
    previewSettings: PanelSettings
  ): POMLWebviewPanel | undefined {
    return this._previews.find(preview =>
      preview.matchesResource(resource, previewSettings.previewColumn, previewSettings.locked));
  }

  private createNewPreview(
    resource: vscode.Uri,
    previewSettings: PanelSettings
  ): POMLWebviewPanel {
    const preview = POMLWebviewPanel.create(
      resource,
      previewSettings.previewColumn,
      previewSettings.locked,
      this._extensionContext,
      this._previewConfigurations,
      this._logger,
      this._topmostLineMonitor);

    this.setPreviewActiveContext(true);
    this._activePreview = preview;
    return this.registerPreview(preview);
  }

  private registerPreview(
    preview: POMLWebviewPanel
  ): POMLWebviewPanel {
    this._previews.push(preview);

    preview.onDispose(() => {
      const existing = this._previews.indexOf(preview);
      if (existing === -1) {
        return;
      }

      this._previews.splice(existing, 1);
      if (this._activePreview === preview) {
        this.setPreviewActiveContext(false);
        this._activePreview = undefined;
      }
    });

    preview.onDidChangeViewState(({ webviewPanel }) => {
      disposeAll(this._previews.filter(otherPreview => preview !== otherPreview && preview!.matches(otherPreview)));
      this.setPreviewActiveContext(webviewPanel.active);
      this._activePreview = webviewPanel.active ? preview : undefined;
    });

    return preview;
  }

  private setPreviewActiveContext(value: boolean) {
    vscode.commands.executeCommand('setContext', POMLWebviewPanelManager.pomlPreviewActiveContextKey, value);
  }
}




================================================
FILE: packages/poml-vscode/panel/panel.ts
================================================
import * as vscode from 'vscode';
import * as path from 'path';

import { WebviewConfig, WebviewState, WebviewUserOptions, WebviewMessage, PreviewMethodName, PreviewParams, PreviewResponse } from './types';
import { headlessPomlVscodePanelContent, pomlVscodePanelContent } from './content';
import { SettingsManager } from '../settings';
import { isPomlFile } from '../util/file';
import { getVisibleLine, HTMLFileTopmostLineMonitor } from '../util/topmostLineMonitor';
import { Logger } from '../util/logger';
import { disposeAll } from '../util/dispose';
import { getClient } from 'poml-vscode/extension';
import { getTelemetryReporter } from 'poml-vscode/util/telemetryClient';
import { TelemetryEvent } from 'poml-vscode/util/telemetryServer';

/**
 * A wrapper for a webview panel, exposing "preview"-specific functionalities.
 * It's responsible for creating, reviving the panel and handling editor events.
 * One instance is responsible for one single preview panel.
 * The wrapper can be created by either a revive method or a create method.
 */
export class POMLWebviewPanel {
  public static viewType = 'poml.preview';

  private _pomlUri: vscode.Uri;
  private _locked: boolean;

  private readonly editor: vscode.WebviewPanel;
  private throttleTimer: any;
  private line: number | undefined = undefined;
  private readonly disposables: vscode.Disposable[] = [];
  private firstUpdate = true;
  private currentVersion?: { resource: vscode.Uri; version: number };
  private forceUpdate = false;
  private isScrolling = false;
  private _disposed: boolean = false;
  private _userOptions: WebviewUserOptions;

  public static async revive(
    webview: vscode.WebviewPanel,
    state: WebviewState,
    context: vscode.ExtensionContext,
    previewConfigurations: SettingsManager,
    logger: Logger,
    topmostLineMonitor: HTMLFileTopmostLineMonitor
  ): Promise<POMLWebviewPanel> {
    // Unpack the state.
    const config = state;
    const resource = vscode.Uri.parse(config.source);
    const locked = config.locked;
    const line = config.line;

    const preview = new POMLWebviewPanel(
      webview,
      resource,
      locked,
      {
        speakerMode: state.speakerMode,
        displayFormat: state.displayFormat,
        contexts: state.contexts ?? [],
        stylesheets: state.stylesheets ?? []
      },
      context,
      previewConfigurations,
      logger,
      topmostLineMonitor
    );

    preview.editor.webview.options = POMLWebviewPanel.getWebviewOptions(resource, context);

    if (line !== undefined && !isNaN(line)) {
      preview.line = line;
    }
    await preview.doUpdate();
    return preview;
  }

  public static create(
    resource: vscode.Uri,
    previewColumn: vscode.ViewColumn,
    locked: boolean,
    context: vscode.ExtensionContext,
    previewConfigurations: SettingsManager,
    logger: Logger,
    topmostLineMonitor: HTMLFileTopmostLineMonitor
  ): POMLWebviewPanel {
    const webview = vscode.window.createWebviewPanel(
      POMLWebviewPanel.viewType,
      POMLWebviewPanel.getPreviewTitle(resource, locked),
      previewColumn,
      {
        enableFindWidget: true,
        ...POMLWebviewPanel.getWebviewOptions(resource, context)
      }
    );

    const userOptions: WebviewUserOptions = {
      speakerMode: true,
      displayFormat: 'plain',
      contexts: [],
      stylesheets: []
    };

    return new POMLWebviewPanel(
      webview,
      resource,
      locked,
      userOptions,
      context,
      previewConfigurations,
      logger,
      topmostLineMonitor
    );
  }

  private constructor(
    webview: vscode.WebviewPanel,
    resource: vscode.Uri,
    locked: boolean,
    userOptions: WebviewUserOptions,
    private readonly _context: vscode.ExtensionContext,
    private readonly _previewConfigurations: SettingsManager,
    private readonly _logger: Logger,
    topmostLineMonitor: HTMLFileTopmostLineMonitor
  ) {
    this._pomlUri = resource;
    this._locked = locked;
    this._userOptions = userOptions;
    this.editor = webview;

    this.editor.onDidDispose(
      () => {
        this.dispose();
      },
      null,
      this.disposables
    );

    this.editor.onDidChangeViewState(
      e => {
        this._onDidChangeViewStateEmitter.fire(e);
      },
      null,
      this.disposables
    );

    this.editor.webview.onDidReceiveMessage(
      e => {
        if (e.source !== this._pomlUri.toString()) {
          return;
        }

        switch (e.type) {
          case WebviewMessage.Command:
            vscode.commands.executeCommand(e.body.command, ...e.body.args);
            break;

          case WebviewMessage.RevealLine:
            this.onDidScrollPreview(e.body.line);
            break;

          case WebviewMessage.DidClick:
            this.onDidClickPreview(e.body.line);
            break;

          case WebviewMessage.Form:
            this._userOptions = { ...this._userOptions, ...e.body };
            this.onDidUserOptionsChange();
            break;
        }
      },
      null,
      this.disposables
    );

    vscode.workspace.onDidChangeTextDocument(
      event => {
        if (this.isPreviewOf(event.document.uri)) {
          this.refresh();
        }
      },
      null,
      this.disposables
    );

    topmostLineMonitor.onDidChangeTopmostLine(
      event => {
        if (this.isPreviewOf(event.resource)) {
          this.updateForView(event.resource, event.line);
        }
      },
      null,
      this.disposables
    );

    vscode.window.onDidChangeTextEditorSelection(
      event => {
        if (this.isPreviewOf(event.textEditor.document.uri)) {
          this.postMessage({
            type: 'onDidChangeTextEditorSelection',
            line: event.selections[0].active.line,
            source: this._pomlUri.toString()
          });
        }
      },
      null,
      this.disposables
    );

    vscode.window.onDidChangeActiveTextEditor(
      editor => {
        if (editor && isPomlFile(editor.document) && !this._locked) {
          this.update(editor.document.uri);
        }
      },
      null,
      this.disposables
    );
  }

  private readonly _onDisposeEmitter = new vscode.EventEmitter<void>();
  public readonly onDispose = this._onDisposeEmitter.event;

  private readonly _onDidChangeViewStateEmitter =
    new vscode.EventEmitter<vscode.WebviewPanelOnDidChangeViewStateEvent>();
  public readonly onDidChangeViewState = this._onDidChangeViewStateEmitter.event;

  public get pomlUri(): vscode.Uri {
    return this._pomlUri;
  }

  public dispose() {
    if (this._disposed) {
      return;
    }

    this._disposed = true;
    this._onDisposeEmitter.fire();

    this._onDisposeEmitter.dispose();
    this._onDidChangeViewStateEmitter.dispose();
    this.editor.dispose();

    disposeAll(this.disposables);
  }

  public update(resource: vscode.Uri) {
    const editor = vscode.window.activeTextEditor;
    if (editor && editor.document.uri.fsPath === resource.fsPath) {
      this.line = getVisibleLine(editor);
    }

    // If we have changed resources, cancel any pending updates
    const isResourceChange = resource.fsPath !== this._pomlUri.fsPath;
    if (isResourceChange) {
      clearTimeout(this.throttleTimer);
      this.throttleTimer = undefined;
    }

    if (isResourceChange || this.firstUpdate) {
      const saved = this._previewConfigurations.getResourceOptions(resource);
      this._userOptions.contexts = [...saved.contexts];
      this._userOptions.stylesheets = [...saved.stylesheets];
    }

    this._pomlUri = resource;

    // Schedule update if none is pending
    if (!this.throttleTimer) {
      if (isResourceChange || this.firstUpdate) {
        this.doUpdate();
      } else {
        this.throttleTimer = setTimeout(() => this.doUpdate(), 300);
      }
    }

    this.firstUpdate = false;
  }

  public refresh() {
    this.forceUpdate = true;
    this.update(this._pomlUri);
  }

  public updateConfiguration() {
    if (this._previewConfigurations.hasSettingsChanged(this._pomlUri)) {
      this.refresh();
    }
  }

  public get position(): vscode.ViewColumn | undefined {
    return this.editor.viewColumn;
  }

  public matchesResource(
    otherResource: vscode.Uri,
    otherPosition: vscode.ViewColumn | undefined,
    otherLocked: boolean
  ): boolean {
    if (this.position !== otherPosition) {
      return false;
    }

    if (this._locked) {
      return otherLocked && this.isPreviewOf(otherResource);
    } else {
      return !otherLocked;
    }
  }

  public matches(otherPreview: POMLWebviewPanel): boolean {
    return this.matchesResource(otherPreview._pomlUri, otherPreview.position, otherPreview._locked);
  }

  public reveal(viewColumn: vscode.ViewColumn) {
    this.editor.reveal(viewColumn);
  }

  public toggleLock() {
    this._locked = !this._locked;
    this.editor.title = POMLWebviewPanel.getPreviewTitle(this._pomlUri, this._locked);
  }

  public addContext(file: string) {
    if (!this._userOptions.contexts) {
      this._userOptions.contexts = [];
    }
    if (!this._userOptions.contexts.includes(file)) {
      this._userOptions.contexts.push(file);
      this._previewConfigurations.setResourceOptions(this._pomlUri, {
        contexts: [...this._userOptions.contexts],
        stylesheets: [...(this._userOptions.stylesheets ?? [])],
      });
      this.onDidUserOptionsChange();
    }
  }

  public addStylesheet(file: string) {
    if (!this._userOptions.stylesheets) {
      this._userOptions.stylesheets = [];
    }
    if (!this._userOptions.stylesheets.includes(file)) {
      this._userOptions.stylesheets.push(file);
      this._previewConfigurations.setResourceOptions(this._pomlUri, {
        contexts: [...(this._userOptions.contexts ?? [])],
        stylesheets: [...this._userOptions.stylesheets],
      });
      this.onDidUserOptionsChange();
    }
  }

  public removeContext(file: string) {
    if (this._userOptions.contexts) {
      this._userOptions.contexts = this._userOptions.contexts.filter(f => f !== file);
      this._previewConfigurations.setResourceOptions(this._pomlUri, {
        contexts: [...this._userOptions.contexts],
        stylesheets: [...(this._userOptions.stylesheets ?? [])],
      });
      this.onDidUserOptionsChange();
    }
  }

  public removeStylesheet(file: string) {
    if (this._userOptions.stylesheets) {
      this._userOptions.stylesheets = this._userOptions.stylesheets.filter(f => f !== file);
      this._previewConfigurations.setResourceOptions(this._pomlUri, {
        contexts: [...(this._userOptions.contexts ?? [])],
        stylesheets: [...this._userOptions.stylesheets],
      });
      this.onDidUserOptionsChange();
    }
  }

  private get iconPath() {
    const root = path.join(this._context.extensionPath, 'media');
    return {
      light: vscode.Uri.file(path.join(root, 'icon', 'preview.svg')),
      dark: vscode.Uri.file(path.join(root, 'icon', 'preview-inverse.svg'))
    };
  }

  private isPreviewOf(resource: vscode.Uri): boolean {
    return this._pomlUri.fsPath === resource.fsPath;
  }

  private static getPreviewTitle(resource: vscode.Uri, locked: boolean): string {
    return locked
      ? `[Preview] ${path.basename(resource.fsPath)}`
      : `Preview ${path.basename(resource.fsPath)}`;
  }

  private updateForView(resource: vscode.Uri, topLine: number | undefined) {
    if (!this.isPreviewOf(resource)) {
      return;
    }

    if (this.isScrolling) {
      this.isScrolling = false;
      return;
    }

    if (typeof topLine === 'number') {
      this._logger.log('updateForView', { htmlFile: resource });
      this.line = topLine;
      this.postMessage({
        type: 'updateView',
        line: topLine,
        source: resource.toString()
      });
    }
  }

  private postMessage(msg: any) {
    if (!this._disposed) {
      this.editor.webview.postMessage(msg);
    }
  }

  private getWebviewConfig(document: vscode.TextDocument): WebviewConfig {
    const settings = this._previewConfigurations.loadAndCacheSettings(this._pomlUri);
    return {
      source: this._pomlUri.toString(),
      line: this.line,
      lineCount: document.lineCount,
      locked: this._locked,
      scrollPreviewWithEditor: settings.scrollPreviewWithEditor,
      scrollEditorWithPreview: settings.scrollEditorWithPreview,
      doubleClickToSwitchToEditor: settings.doubleClickToSwitchToEditor
    };
  }

  private getLanguageModelSettings(uri: vscode.Uri) {
    const settings = this._previewConfigurations.loadAndCacheSettings(uri);
    return settings.languageModel;
  }

  private extensionResourcePath(mediaFile: string): string {
    return this.editor.webview
      .asWebviewUri(vscode.Uri.joinPath(this._context.extensionUri, 'media', mediaFile))
      .toString();
  }

  private localResourcePath(resourceFile: string): string {
    return this.editor.webview.asWebviewUri(vscode.Uri.parse(resourceFile)).toString();
  }

  private async doUpdate(): Promise<void> {
    const resource = this._pomlUri;

    clearTimeout(this.throttleTimer);
    this.throttleTimer = undefined;

    const document = await vscode.workspace.openTextDocument(resource);
    if (
      !this.forceUpdate &&
      this.currentVersion &&
      this.currentVersion.resource.fsPath === resource.fsPath &&
      this.currentVersion.version === document.version
    ) {
      if (this.line) {
        this.updateForView(resource, this.line);
      }
      return;
    }
    this.forceUpdate = false;

    this.currentVersion = { resource, version: document.version };
    const webviewConfig = this.getWebviewConfig(document);

    const languageModelSettings = this.getLanguageModelSettings(resource);
    const requestParams: PreviewParams = {
      uri: resource.toString(),
      returnTokenCounts: { model: languageModelSettings.model },
      ...this._userOptions
    };

    const response = await getClient().sendRequest<PreviewResponse>(PreviewMethodName, requestParams);

    const content = pomlVscodePanelContent({
      ...webviewConfig,
      ...this._userOptions,
      ...response,
      extensionResourcePath: this.extensionResourcePath.bind(this),
      localResourcePath: this.localResourcePath.bind(this)
    });

    if (this._pomlUri === resource) {
      this.editor.title = POMLWebviewPanel.getPreviewTitle(this._pomlUri, this._locked);
      this.editor.iconPath = this.iconPath;
      this.editor.webview.options = POMLWebviewPanel.getWebviewOptions(resource, this._context);
      this.editor.webview.html = content;
    }
  }

  private static getWebviewOptions(
    resource: vscode.Uri,
    context: vscode.ExtensionContext
  ): vscode.WebviewOptions {
    return {
      enableScripts: true,
      enableCommandUris: true,
      localResourceRoots: POMLWebviewPanel.getLocalResourceRoots(resource, context)
    };
  }

  private static getLocalResourceRoots(
    resource: vscode.Uri,
    context: vscode.ExtensionContext
  ): vscode.Uri[] {
    const baseRoots: vscode.Uri[] = [vscode.Uri.joinPath(context.extensionUri, 'media')];

    const folder = vscode.workspace.getWorkspaceFolder(resource);
    if (folder) {
      return baseRoots.concat(folder.uri);
    }

    if (!resource.scheme || resource.scheme === 'file') {
      return baseRoots.concat(vscode.Uri.file(path.dirname(resource.fsPath)));
    }

    return baseRoots;
  }

  private onDidScrollPreview(line: number) {
    this.line = line;
    for (const editor of vscode.window.visibleTextEditors) {
      if (!this.isPreviewOf(editor.document.uri)) {
        continue;
      }

      this.isScrolling = true;
      const sourceLine = Math.floor(line);
      const fraction = line - sourceLine;
      const text = editor.document.lineAt(sourceLine).text;
      const start = Math.floor(fraction * text.length);
      editor.revealRange(
        new vscode.Range(sourceLine, start, sourceLine + 1, 0),
        vscode.TextEditorRevealType.AtTop
      );
    }
  }

  private async onDidClickPreview(line: number): Promise<void> {
    for (const visibleEditor of vscode.window.visibleTextEditors) {
      if (this.isPreviewOf(visibleEditor.document.uri)) {
        const editor = await vscode.window.showTextDocument(
          visibleEditor.document,
          visibleEditor.viewColumn
        );
        const position = new vscode.Position(line, 0);
        editor.selection = new vscode.Selection(position, position);
        return;
      }
    }

    vscode.workspace.openTextDocument(this._pomlUri).then(vscode.window.showTextDocument);
  }

  private async onDidUserOptionsChange(): Promise<void> {
    const resource = this._pomlUri;
    const languageModelSettings = this.getLanguageModelSettings(resource);
    const requestParams: PreviewParams = {
      uri: resource.toString(),
      returnTokenCounts: { model: languageModelSettings.model },
      ...this._userOptions
    };

    getTelemetryReporter()?.reportTelemetry(TelemetryEvent.PreviewUserOptionsChange, this._userOptions);

    const response = await getClient().sendRequest<PreviewResponse>(PreviewMethodName, requestParams);

    const content = headlessPomlVscodePanelContent({
      ...this._userOptions,
      ...response,
    });
    this.editor.webview.postMessage({ type: WebviewMessage.UpdateContent, content: content, source: resource.toString() });
    this.editor.webview.postMessage({ type: WebviewMessage.UpdateUserOptions, options: this._userOptions, source: resource.toString() });
  }

}



================================================
FILE: packages/poml-vscode/panel/types.ts
================================================
import { Message, RichContent, SourceMapMessage, SourceMapRichContent } from 'poml';
import * as vscode from 'vscode';

/**
 * Messages sent from the webview to the extension.
 */
export enum WebviewMessage {
  Command = 'command',
  RevealLine = 'revealLine',
  DidClick = 'didClick',
  Form = 'form',
  UpdateContent = 'updateContent',
  UpdateUserOptions = 'updateUserOptions',
}

/**
 * The general settings for a panel, set from the outside when creating it.
 * This is only visible to preview manager.
 */
export interface PanelSettings {
  readonly resourceColumn: vscode.ViewColumn;
  readonly previewColumn: vscode.ViewColumn;
  readonly locked: boolean;
}

/**
 * Config for one webview panel.
 * Data will be sent to the HTML.
 * Synced with webview/config.ts
 */
export interface WebviewConfig {
  source: string;
  line: number | undefined;
  lineCount: number;
  locked: boolean;
  scrollPreviewWithEditor?: boolean;
  scrollEditorWithPreview: boolean;
  doubleClickToSwitchToEditor: boolean;
}

/**
 * The inputs from webview panel.
 */
export interface WebviewUserOptions {
  speakerMode: boolean;
  displayFormat: 'rendered' | 'plain' | 'ir';
  contexts: string[];
  stylesheets: string[];
}

export const PreviewMethodName = 'poml/preview';

export interface PreviewParams extends WebviewUserOptions {
  uri: string;
  text?: string;
  inlineContext?: { [key: string]: any };
  returnAllErrors?: boolean;
  returnTokenCounts?: { model: string };
}

export interface PreviewResponse {
  rawText: string;
  ir: string;
  content: RichContent | Message[];
  error?: string | any[];
  sourceMap?: SourceMapRichContent[] | SourceMapMessage[];
  tokens?: {
    perMessage?: number[];
    total: number;
  };
  responseSchema?: { [key: string]: any };
  tools?: { [key: string]: any }[];
  runtime?: { [key: string]: any };
}

/**
 * The state that is used for serialization.
 * Useful when reviving a webview panel.
 * Synced with webview/state.ts
 */
export type WebviewState = WebviewConfig & WebviewUserOptions;



================================================
FILE: packages/poml-vscode/test-fixtures/badInclude.poml
================================================
<p>hello



================================================
FILE: packages/poml-vscode/test-fixtures/badSyntax.poml
================================================
<poml



================================================
FILE: packages/poml-vscode/test-fixtures/badSyntaxLsp.poml
================================================
<poml



================================================
FILE: packages/poml-vscode/test-fixtures/includeMain.poml
================================================
<poml><include src="badInclude.poml"/></poml>



================================================
FILE: packages/poml-vscode/test-fixtures/test.poml
================================================
<p speaker="ai">hello</p>



================================================
FILE: packages/poml-vscode/tests/commands.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';

suite('Commands', () => {
  test('expected commands are registered', async () => {
    const ext = vscode.extensions.getExtension('poml-team.poml');
    await ext?.activate();
    const cmds = await vscode.commands.getCommands(true);
    const expected = [
      'poml.test',
      'poml.testNonChat',
      'poml.testRerun',
      'poml.testAbort',
      'poml.showPreview',
      'poml.showPreviewToSide',
      'poml.showLockedPreviewToSide',
      'poml.showSource',
      'poml.telemetry.completion',
    ];
    for (const id of expected) {
      assert.ok(cmds.includes(id), `Missing command ${id}`);
    }
  });
});



================================================
FILE: packages/poml-vscode/tests/diagnosticsDuplicate.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';

suite('Diagnostics duplicates', () => {
  test('diagnostics are not duplicated on save', async function() {
    this.timeout(20000);
    const bad = path.resolve(__dirname, '../../../packages/poml-vscode/test-fixtures/badSyntax.poml');
    const uri = vscode.Uri.file(bad);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);

    await new Promise(resolve => setTimeout(resolve, 1500));

    let diags = vscode.languages.getDiagnostics(uri);
    assert.strictEqual(diags.length, 1, 'Expected one diagnostic before save');

    await doc.save();
    await new Promise(resolve => setTimeout(resolve, 1500));

    diags = vscode.languages.getDiagnostics(uri);
    assert.strictEqual(diags.length, 1, 'Expected diagnostics not to duplicate after save');
  });
});



================================================
FILE: packages/poml-vscode/tests/extension.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';

suite('Extension Activation', () => {
  test('extension activates', async () => {
    const ext = vscode.extensions.getExtension('poml-team.poml');
    assert.ok(ext, 'Extension not found');
    await ext?.activate();
    assert.ok(ext?.isActive, 'Extension did not activate');
  });
});



================================================
FILE: packages/poml-vscode/tests/includeDiagnostics.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';

suite('Include diagnostics', () => {
  test('errors in included files are reported', async function() {
    this.timeout(20000);
    const main = path.resolve(__dirname, '../../../packages/poml-vscode/test-fixtures/includeMain.poml');
    const bad = path.resolve(__dirname, '../../../packages/poml-vscode/test-fixtures/badInclude.poml');

    const mainUri = vscode.Uri.file(main);
    const doc = await vscode.workspace.openTextDocument(mainUri);
    await vscode.window.showTextDocument(doc);

    // wait for diagnostics to be processed
    await new Promise(resolve => setTimeout(resolve, 1500));

    const badUri = vscode.Uri.file(bad);
    const diags = vscode.languages.getDiagnostics(badUri);
    assert.strictEqual(diags.length, 1, 'Expected one diagnostic for included file');
    assert.ok(/Expecting token/.test(diags[0].message), 'Unexpected diagnostic message');
  });
});



================================================
FILE: packages/poml-vscode/tests/lsp.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';
import {
  PreviewMethodName,
  PreviewParams,
  PreviewResponse
} from '../panel/types';
import { LanguageClient, State } from 'vscode-languageclient/node';

suite('LSP Server', () => {
  let client: LanguageClient;

  suiteSetup(async function() {
    this.timeout(20000);
    const ext = vscode.extensions.getExtension('poml-team.poml');
    await ext?.activate();
    const extensionApi = ext?.exports as { getClient: () => LanguageClient } | undefined;
    assert.ok(extensionApi, 'Extension API not available');
    client = extensionApi.getClient();
    await new Promise<void>(resolve => {
      if (client.state === State.Running) {
        resolve();
      } else {
        const disposable = client.onDidChangeState(e => {
          if (e.newState === State.Running) {
            disposable.dispose();
            resolve();
          }
        });
      }
    });
  });

  teardown(async () => {
    await vscode.commands.executeCommand('workbench.action.closeAllEditors');
    // give LSP server time to clear diagnostics
    await new Promise(resolve => setTimeout(resolve, 500));
  });

  test('diagnostics are produced for bad files', async function() {
    this.timeout(20000);
    const bad = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/badSyntaxLsp.poml'
    );
    const uri = vscode.Uri.file(bad);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await new Promise(resolve => setTimeout(resolve, 1500));
    const diags = vscode.languages.getDiagnostics(uri);
    assert.ok(diags.length > 0, 'Expected diagnostics for bad file');
  });

  test('no diagnostics for valid files', async function() {
    this.timeout(20000);
    const good = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/test.poml'
    );
    const uri = vscode.Uri.file(good);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await new Promise(resolve => setTimeout(resolve, 1500));
    const diags = vscode.languages.getDiagnostics(uri);
    assert.strictEqual(diags.length, 0, 'Expected no diagnostics for clean file');
  });

  test('hover provides documentation', async function() {
    this.timeout(20000);
    const sample = path.resolve(__dirname, '../../../packages/poml-vscode/test-fixtures/test.poml');
    const uri = vscode.Uri.file(sample);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await new Promise(resolve => setTimeout(resolve, 1500));
    const pos = new vscode.Position(0, 1); // inside <p>
    const hovers = (await vscode.commands.executeCommand('vscode.executeHoverProvider', uri, pos)) as vscode.Hover[];
    assert.ok(hovers && hovers.length > 0, 'No hover result');
    const text = (hovers[0].contents[0] as any).value ?? '';
    assert.ok(/Paragraph/.test(text), 'Hover text does not mention Paragraph');
  });

  test('completion suggests attributes', async function() {
    this.timeout(20000);
    const doc = await vscode.workspace.openTextDocument({ language: 'poml', content: '<question sp' });
    await vscode.window.showTextDocument(doc);
    await new Promise(resolve => setTimeout(resolve, 1500));
    const pos = new vscode.Position(0, doc.getText().length);
    const list = (await vscode.commands.executeCommand('vscode.executeCompletionItemProvider', doc.uri, pos)) as vscode.CompletionList;
    const labels = list.items.map(item => (typeof item.label === 'string' ? item.label : item.label.label));
    assert.ok(labels.includes('speaker'), 'Expected "speaker" completion');
  });

  test('server preview request returns content', async function() {
    this.timeout(20000);
    const sample = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/test.poml'
    );
    const uri = vscode.Uri.file(sample);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await new Promise(resolve => setTimeout(resolve, 1500));

    const params: PreviewParams = {
      uri: uri.toString(),
      speakerMode: true,
      displayFormat: 'rendered',
      contexts: [],
      stylesheets: [],
    };
    assert.ok(client, 'Language client not available');
    const response: PreviewResponse = await client.sendRequest(PreviewMethodName, params);
    assert.strictEqual(response.error, undefined, 'Preview response contains error');
    assert.ok(response.content, 'Expected preview content');
  });

  test('evaluate expression returns result', async function() {
    this.timeout(20000);
    const docPath = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/test.poml'
    );
    const result = await client.sendRequest('workspace/executeCommand', {
      command: 'poml.evaluateExpression',
      arguments: [vscode.Uri.file(docPath).toString(), '<p>{{1+2}}</p>', 4, 10]
    });
    assert.strictEqual(result, null, 'Evaluation result mismatch');
  });
});




================================================
FILE: packages/poml-vscode/tests/panelAutoAdd.test.ts
================================================
import * as assert from 'assert';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import * as vscode from 'vscode';

import { POMLWebviewPanel } from '../panel/panel';
import { SettingsManager } from '../settings';
import { Logger } from '../util/logger';

class DummyTopmostLineMonitor {
  public readonly onDidChangeTopmostLine = (_: any) => {};
  dispose() {}
}

function canonical(p: string): string {
  return vscode.Uri.file(p).fsPath;
}

function createPanel(uri: vscode.Uri, context: vscode.ExtensionContext): POMLWebviewPanel {
  const webviewPanel = {
    viewColumn: vscode.ViewColumn.One,
    title: '',
    iconPath: undefined,
    webview: {
      html: '',
      options: {},
      postMessage: (_msg: any) => {},
      onDidReceiveMessage: () => new vscode.Disposable(() => {}),
      asWebviewUri: (u: vscode.Uri) => u,
    },
    onDidDispose: () => new vscode.Disposable(() => {}),
    onDidChangeViewState: () => new vscode.Disposable(() => {}),
    reveal: () => {},
    dispose: () => {},
  } as unknown as vscode.WebviewPanel;

  const PanelClass: any = POMLWebviewPanel;
  const panel = new PanelClass(
    webviewPanel,
    uri,
    false,
    { speakerMode: true, displayFormat: 'plain', contexts: [], stylesheets: [] },
    context,
    new SettingsManager(),
    new Logger(),
    new DummyTopmostLineMonitor() as any
  );
  (panel as any).doUpdate = async () => {};
  (panel as any).onDidUserOptionsChange = async () => {};
  return panel;
}

suite('autoAddAssociatedFiles', () => {
  test('associated files are auto added', () => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'poml-'));
    const pomlPath = path.join(dir, 'sample.poml');
    const ctxPath = canonical(path.join(dir, 'sample.context.json'));
    const stylePath = canonical(path.join(dir, 'sample.stylesheet.json'));
    fs.writeFileSync(pomlPath, '<poml></poml>');
    fs.writeFileSync(ctxPath, '{}');
    fs.writeFileSync(stylePath, '{}');

    const ext = vscode.extensions.getExtension('poml-team.poml')!;
    const context = { extensionUri: ext.extensionUri, extensionPath: ext.extensionPath, subscriptions: [] } as unknown as vscode.ExtensionContext;

    const panel = createPanel(vscode.Uri.file(pomlPath), context);
    panel.update(vscode.Uri.file(pomlPath));

    const options = (panel as any)._userOptions;
    assert.ok(options.contexts.includes(ctxPath), 'context auto add');
    assert.ok(options.stylesheets.includes(stylePath), 'stylesheet auto add');

    fs.rmSync(dir, { recursive: true, force: true });
  });

  test('manual changes prevent re-adding associated files', () => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'poml-'));
    const pomlPath = path.join(dir, 'sample.poml');
    const ctxPath = canonical(path.join(dir, 'sample.context.json'));
    const stylePath = canonical(path.join(dir, 'sample.stylesheet.json'));
    const customCtx = canonical(path.join(dir, 'custom.context.json'));
    fs.writeFileSync(pomlPath, '<poml></poml>');
    fs.writeFileSync(ctxPath, '{}');
    fs.writeFileSync(stylePath, '{}');
    fs.writeFileSync(customCtx, '{}');

    const ext = vscode.extensions.getExtension('poml-team.poml')!;
    const context = { extensionUri: ext.extensionUri, extensionPath: ext.extensionPath, subscriptions: [] } as unknown as vscode.ExtensionContext;

    const panel = createPanel(vscode.Uri.file(pomlPath), context);
    panel.update(vscode.Uri.file(pomlPath));

    panel.addContext(customCtx);
    panel.removeContext(ctxPath);
    panel.removeStylesheet(stylePath);
    panel.update(vscode.Uri.file(pomlPath));

    const options = (panel as any)._userOptions;
    assert.deepStrictEqual(options.contexts, [customCtx], 'contexts should match manual changes');
    assert.deepStrictEqual(options.stylesheets, [], 'stylesheets should match manual changes');

    fs.rmSync(dir, { recursive: true, force: true });
  });
});




================================================
FILE: packages/poml-vscode/tests/panelContent.test.ts
================================================
import * as assert from 'assert';
import { pomlVscodePanelContent } from '../panel/content';

suite('Panel content helper', () => {
  test('basic rendering works', () => {
    const html = pomlVscodePanelContent({
      source: 'source',
      line: 0,
      lineCount: 1,
      locked: false,
      scrollPreviewWithEditor: false,
      scrollEditorWithPreview: false,
      doubleClickToSwitchToEditor: false,
      speakerMode: true,
      displayFormat: 'rendered',
      contexts: [],
      stylesheets: [],
      rawText: '<p>test</p>',
      ir: '',
      content: [],
      extensionResourcePath: (p: string) => p,
      localResourcePath: (p: string) => p,
    });
    assert.ok(html.includes('test'));
  });
});



================================================
FILE: packages/poml-vscode/tests/panelContentMapping.test.ts
================================================
import * as assert from 'assert';
import { pomlVscodePanelContent } from '../panel/content';
import { Message } from 'poml';

test('panel embeds line numbers', () => {
  const msg: Message = { speaker: 'ai', content: 'hello' };
  const html = pomlVscodePanelContent({
    source: 'source',
    line: 0,
    lineCount: 1,
    locked: false,
    scrollPreviewWithEditor: false,
    scrollEditorWithPreview: false,
    doubleClickToSwitchToEditor: false,
    speakerMode: true,
    displayFormat: 'plain',
    contexts: [],
    stylesheets: [],
    rawText: '<p speaker="ai">hello</p>',
    ir: '',
    content: [msg],
    sourceMap: [{
      startIndex: 0, endIndex: 20, irStartIndex: 0, irEndIndex: 0, speaker: 'ai',
      content: [{ startIndex: 0, endIndex: 20, irStartIndex: 0, irEndIndex: 0, content: 'hello' }]
    }],
    extensionResourcePath: p => p,
    localResourcePath: p => p,
  });
  assert.ok(html.includes('data-line="0"'));
});



================================================
FILE: packages/poml-vscode/tests/preview.test.ts
================================================
import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';

suite('Preview Feature', () => {
  teardown(async () => {
    await vscode.commands.executeCommand('workbench.action.closeAllEditors');
    await new Promise(resolve => setTimeout(resolve, 500));
  });

  test('showPreview executes without error', async function() {
    this.timeout(10000);
    const sample = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/test.poml'
    );
    const uri = vscode.Uri.file(sample);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await vscode.commands.executeCommand('poml.showPreview', uri);
    // give VS Code some time to process
    await new Promise(resolve => setTimeout(resolve, 1000));
    assert.ok(true);
  });

  test('showPreviewToSide executes without error', async function() {
    this.timeout(10000);
    const sample = path.resolve(
      __dirname,
      '../../../packages/poml-vscode/test-fixtures/test.poml'
    );
    const uri = vscode.Uri.file(sample);
    const doc = await vscode.workspace.openTextDocument(uri);
    await vscode.window.showTextDocument(doc);
    await vscode.commands.executeCommand('poml.showPreviewToSide', uri);
    await new Promise(resolve => setTimeout(resolve, 1000));
    assert.ok(true);
  });
});



================================================
FILE: packages/poml-vscode/util/commandManager.ts
================================================
import * as vscode from 'vscode';

export interface Command {
  readonly id: string;

  execute(...args: any[]): void;
}

export class CommandManager {
  private readonly commands = new Map<string, vscode.Disposable>();

  public dispose() {
    for (const registration of this.commands.values()) {
      registration.dispose();
    }
    this.commands.clear();
  }

  public register<T extends Command>(command: T): T {
    this.registerCommand(command.id, command.execute, command);
    return command;
  }

  private registerCommand(id: string, impl: (...args: any[]) => void, thisArg?: any) {
    if (this.commands.has(id)) {
      return;
    }

    this.commands.set(id, vscode.commands.registerCommand(id, impl, thisArg));
  }
}



================================================
FILE: packages/poml-vscode/util/dispose.ts
================================================
import * as vscode from 'vscode';

export function disposeAll(disposables: vscode.Disposable[]) {
  while (disposables.length) {
    const item = disposables.pop();
    if (item) {
      item.dispose();
    }
  }
}



================================================
FILE: packages/poml-vscode/util/file.ts
================================================
import * as vscode from 'vscode';

export function isPomlFile(document: vscode.TextDocument) {
  return document.languageId === 'spml';
}



================================================
FILE: packages/poml-vscode/util/logger.ts
================================================
import * as vscode from 'vscode';

enum Trace {
  Off,
  Verbose
}

namespace Trace {
  export function fromString(value: string): Trace {
    value = value.toLowerCase();
    switch (value) {
      case 'off':
        return Trace.Off;
      case 'verbose':
        return Trace.Verbose;
      default:
        return Trace.Off;
    }
  }
}

export interface Lazy<T> {
  readonly value: T;
  readonly hasValue: boolean;
  map<R>(f: (x: T) => R): Lazy<R>;
}

class LazyValue<T> implements Lazy<T> {
  private _hasValue: boolean = false;
  private _value?: T;

  constructor(
    private readonly _getValue: () => T
  ) { }

  get value(): T {
    if (!this._hasValue) {
      this._hasValue = true;
      this._value = this._getValue();
    }
    return this._value!;
  }

  get hasValue(): boolean {
    return this._hasValue;
  }

  public map<R>(f: (x: T) => R): Lazy<R> {
    return new LazyValue(() => f(this.value));
  }
}

export function lazy<T>(getValue: () => T): Lazy<T> {
  return new LazyValue<T>(getValue);
}

function isString(value: any): value is string {
  return Object.prototype.toString.call(value) === '[object String]';
}

export class Logger {
  private trace?: Trace;

  private readonly outputChannel = lazy(() => vscode.window.createOutputChannel('HTML'));

  constructor() {
    this.updateConfiguration();
  }

  public log(message: string, data?: any): void {
    if (this.trace === Trace.Verbose) {
      this.appendLine(`[Log - ${(new Date().toLocaleTimeString())}] ${message}`);
      if (data) {
        this.appendLine(Logger.data2String(data));
      }
    }
  }

  public updateConfiguration() {
    this.trace = Trace.fromString('off');
  }

  private appendLine(value: string) {
    return this.outputChannel.value.appendLine(value);
  }

  private readTrace(): Trace {
    return Trace.fromString(vscode.workspace.getConfiguration().get<string>('html.trace', 'off'));
  }

  private static data2String(data: any): string {
    if (data instanceof Error) {
      if (isString(data.stack)) {
        return data.stack;
      }
      return (data as Error).message;
    }
    if (isString(data)) {
      return data;
    }
    return JSON.stringify(data, undefined, 2);
  }
}



================================================
FILE: packages/poml-vscode/util/telemetryClient.ts
================================================
// This is put into a separate file because it contains imports from vscode.
import TelemetryReporter from '@vscode/extension-telemetry';
import { TelemetryBase, TelemetryServerMessage } from './telemetryServer';

let telemetryClient: TelemetryClient | undefined = undefined;

export class TelemetryClient extends TelemetryBase {
  private reporter: TelemetryReporter;

  constructor(connectionString: string) {
    super();
    this.reporter = new TelemetryReporter(connectionString);
  }

  public reportTelemetry(event: string, properties: { [key: string]: any }): Promise<void> {
    this.reporter.sendDangerousTelemetryEvent(event, {
      ...this.formatProperties(properties)
    });
    return Promise.resolve();
  }

  public reportTelemetryError(event: string, error: any): Promise<void> {
    this.reporter.sendDangerousTelemetryErrorEvent(event, {
      ...this.formatError(error)
    });
    return Promise.resolve();
  }

  public handleDataFromServer(data: TelemetryServerMessage) {
    if (data.type === 'telemetry') {
      this.reportTelemetry(data.event, data.properties);
    } else if (data.type === 'error') {
      this.reportTelemetryError(data.event, data.properties);
    } else {
      throw new Error(`Unknown telemetry message type: ${data.type}`);
    }
  }
}

export function initializeReporter(connectionString: string) {
  telemetryClient = new TelemetryClient(connectionString);
  return telemetryClient;
}

export function getTelemetryReporter(): TelemetryClient | undefined {
  return telemetryClient;
}



================================================
FILE: packages/poml-vscode/util/telemetryServer.ts
================================================
export interface TelemetryServerMessage {
  type: 'telemetry' | 'error';
  event: string;
  properties: { [key: string]: string | undefined };
}

export enum TelemetryEvent {
  ReadUncaughtException = 'ReadUncaughtException',
  WriteUncaughtException = 'WriteUncaughtException',
  Activate = 'Activate',
  LanguageServerStatistics = 'LanguageServerStatistics',
  CompletionAcceptanceStatistics = 'CompletionAcceptanceStatistics',
  Diagnostics = 'Diagnostics',
  Hover = 'Hover',
  EdittingCurrently = 'EdittingCurrently',
  CommandInvoked = 'CommandInvoked',
  PromptTestingStart = 'PromptTestingStart',
  PromptTestingEnd = 'PromptTestingEnd',
  PromptTestingAbort = 'PromptTestingAbort',
  PromptTestingError = 'PromptTestingError',
  PreviewUserOptionsChange = 'PreviewUserOptionsChange',
}

export class TelemetryBase {
  protected formatProperties(properties: { [key: string]: any }) {
    const normalizedProperties: { [key: string]: string | undefined } = Object.entries(
      properties
    ).reduce(
      (acc: { [key: string]: string | undefined }, [key, value]) => {
        if (typeof value === 'object') {
          value = JSON.stringify(value);
        } else if (typeof value !== 'string') {
          value = value?.toString();
        }
        acc[key] = value;
        return acc;
      },
      {} as { [key: string]: string | undefined }
    );
    return normalizedProperties;
  }

  protected formatError(error: any): { [key: string]: string | undefined } {
    let errorInfo: { [key: string]: string | undefined } = {
      message: error ? error.toString() : 'unknown'
    };
    try {
      errorInfo = {
        name: error.name,
        message: error.message,
        stack: error.stack,
        cause: error.cause ? error.cause.toString() : undefined
      };
    } catch (e) {}
    return errorInfo;
  }

  public reportTelemetry(event: string, properties: { [key: string]: any }): Promise<void> {
    throw new Error('reportTelemetry not implemented');
  }

  public reportTelemetryError(event: string, error: any): Promise<void> {
    throw new Error('reportTelemetryError not implemented');
  }
}

export class TelemetryServer extends TelemetryBase {
  private sender: (msg: TelemetryServerMessage) => Promise<void>;

  constructor(sender: (msg: TelemetryServerMessage) => Promise<void>) {
    super();
    this.sender = sender;
  }

  public async reportTelemetry(event: string, properties: { [key: string]: any }) {
    return await this.sender({
      type: 'telemetry',
      event,
      properties: this.formatProperties(properties)
    });
  }

  public async reportTelemetryError(event: string, error: any) {
    return await this.sender({
      type: 'error',
      event,
      properties: this.formatError(error)
    });
  }
}

export class DelayedTelemetryReporter {
  private reporter: TelemetryBase;
  private delayMilliseconds: number;
  private counter: number = 0;
  private lastReportedTime = 0;

  constructor(reporter: TelemetryBase, delayMilliseconds?: number) {
    this.reporter = reporter;
    this.delayMilliseconds = delayMilliseconds ?? 10000;
    this.counter = 0;
  }

  /** Do not wait for this. It can take quite long. */
  public async reportTelemetry(
    event: string,
    properties: { [key: string]: any }
  ): Promise<boolean> {
    // It waits for the specified delay before sending the telemetry event.
    // If another event is sent during this delay, the previous report is canceled.
    ++this.counter;
    const currentCounter = this.counter;
    if (Date.now() - this.lastReportedTime < this.delayMilliseconds) {
      await new Promise(resolve => setTimeout(resolve, this.delayMilliseconds));
    }
    if (currentCounter === this.counter) {
      await this.reporter.reportTelemetry(event, properties);
      return true;
    }
    return false;
  }
}



================================================
FILE: packages/poml-vscode/util/topmostLineMonitor.ts
================================================
import * as vscode from 'vscode';
import { disposeAll } from './dispose';
import { isPomlFile } from '../../poml-vscode/util/file';

export class HTMLFileTopmostLineMonitor {
  private readonly disposables: vscode.Disposable[] = [];

  private readonly pendingUpdates = new Map<string, number>();

  private readonly throttle = 50;

  constructor() {
    vscode.window.onDidChangeTextEditorVisibleRanges(event => {
      if (isPomlFile(event.textEditor.document)) {
        const line = getVisibleLine(event.textEditor);
        if (typeof line === 'number') {
          this.updateLine(event.textEditor.document.uri, line);
        }
      }
    }, null, this.disposables);
  }

  dispose() {
    disposeAll(this.disposables);
  }

  private readonly _onDidChangeTopmostLineEmitter = new vscode.EventEmitter<{ resource: vscode.Uri, line: number }>();
  public readonly onDidChangeTopmostLine = this._onDidChangeTopmostLineEmitter.event;

  private updateLine(
    resource: vscode.Uri,
    line: number
  ) {
    const key = resource.toString();
    if (!this.pendingUpdates.has(key)) {
      // schedule update
      setTimeout(() => {
        if (this.pendingUpdates.has(key)) {
          this._onDidChangeTopmostLineEmitter.fire({
            resource,
            line: this.pendingUpdates.get(key) as number
          });
          this.pendingUpdates.delete(key);
        }
      }, this.throttle);
    }

    this.pendingUpdates.set(key, line);
  }
}

/**
 * Get the top-most visible range of `editor`.
 *
 * Returns a fractional line number based the visible character within the line.
 * Floor to get real line number
 */
export function getVisibleLine(
  editor: vscode.TextEditor
): number | undefined {
  if (!editor.visibleRanges.length) {
    return undefined;
  }

  const firstVisiblePosition = editor.visibleRanges[0].start;
  const lineNumber = firstVisiblePosition.line;
  const line = editor.document.lineAt(lineNumber);
  const progress = firstVisiblePosition.character / (line.text.length + 2);
  return lineNumber + progress;
}



================================================
FILE: packages/poml-vscode-webview/index.ts
================================================
import $ from 'jquery';
import { createPosterForVsCode } from './util';
import { getState } from './state';
import { setupToolbar } from './toolbar';

import throttle from 'lodash.throttle';

declare let acquireVsCodeApi: any;

// var scrollDisabled = true;
// const marker = new ActiveLineMarker();
const state = getState();
const vscode = acquireVsCodeApi();
vscode.setState(state);

const messaging = createPosterForVsCode(vscode);

$(() => {
  setupToolbar(vscode, messaging);
  // if (state.scrollPreviewWithEditor) {
  //     setTimeout(() => {
  //         const initialLine = +state.line;
  //         if (!isNaN(initialLine)) {
  //             scrollDisabled = true;
  //         }
  //     }, 0);
  // }
});

const onUpdateView = (() => {
  const doScroll = throttle((line: number) => {
    // scrollDisabled = true;
  }, 50);

  return (line: number, state: any) => {
    if (!isNaN(line)) {
      state.line = line;
      doScroll(line);
    }
  };
})();

window.addEventListener('resize', () => {
  // scrollDisabled = true;
}, true);

window.addEventListener('message', event => {
  if (event.data.source !== state.source) {
    return;
  }

  switch (event.data.type) {
    case 'onDidChangeTextEditorSelection':
      // FIXME
      // marker.onDidChangeTextEditorSelection(event.data.line);
      break;

    case 'updateView':
      onUpdateView(event.data.line, state);
      break;
  }
}, false);

document.addEventListener('click', event => {
  if (!event) {
    return;
  }

  // FIXME: click links for opening documents in editor
  // let node: any = event.target;
  // while (node) {
  //     if (node.tagName && node.tagName === 'A' && node.href) {
  //         if (node.getAttribute('href').startsWith('#')) {
  //             break;
  //         }
  //         if (node.href.startsWith('file://') || node.href.startsWith('vscode-resource:')) {
  //             const [path, fragment] = node.href.replace(/^(file:\/\/|vscode-resource:)/i, '').split('#');
  //             messaging.postCommand('_html.openDocumentLink', [{ path, fragment }]);
  //             event.preventDefault();
  //             event.stopPropagation();
  //             break;
  //         }
  //         break;
  //     }
  //     node = node.parentNode;
  // }
}, true);

// FIXME: scroll sync
// if (state.scrollEditorWithPreview) {
//     window.addEventListener('scroll', throttle(() => {
//         if (scrollDisabled) {
//             scrollDisabled = false;
//         } else {
//             const line = getEditorLineNumberForPageOffset(window.scrollY);
//             if (typeof line === 'number' && !isNaN(line)) {
//                 messaging.postMessage('revealLine', { line });
//             }
//         }
//     }, 50));
// }


================================================
FILE: packages/poml-vscode-webview/scrollSync.ts
================================================
// This is currently unused as the scroll-sync feature is not implemented yet.

import { getState } from './state';


function clamp(min: number, max: number, value: number) {
  return Math.min(max, Math.max(min, value));
}

function clampLine(line: number) {
  return clamp(0, getState().lineCount - 1, line);
}


export interface CodeLineElement {
  element: HTMLElement;
  line: number;
}

const getCodeLineElements = (() => {
  let elements: CodeLineElement[];
  return () => {
    if (!elements) {
      elements = Array.prototype.map.call(
        document.getElementsByClassName('code-line'),
        (element: any) => {
          const line = +element.getAttribute('data-line');
          return { element, line };
        })
        .filter((x: any) => !isNaN(x.line)) as any;
    }
    return elements;
  };
})();

/**
 * Find the html elements that map to a specific target line in the editor.
 *
 * If an exact match, returns a single element. If the line is between elements,
 * returns the element prior to and the element after the given line.
 */
export function getElementsForSourceLine(targetLine: number): { previous: CodeLineElement; next?: CodeLineElement; } {
  const lineNumber = Math.floor(targetLine);
  const lines = getCodeLineElements();
  let previous = lines[0] || null;
  for (const entry of lines) {
    if (entry.line === lineNumber) {
      return { previous: entry, next: undefined };
    }
    else if (entry.line > lineNumber) {
      return { previous, next: entry };
    }
    previous = entry;
  }
  return { previous };
}

/**
 * Find the html elements that are at a specific pixel offset on the page.
 */
export function getLineElementsAtPageOffset(offset: number): { previous: CodeLineElement; next?: CodeLineElement; } {
  const lines = getCodeLineElements();
  const position = offset - window.scrollY;
  let lo = -1;
  let hi = lines.length - 1;
  while (lo + 1 < hi) {
    const mid = Math.floor((lo + hi) / 2);
    const bounds = lines[mid].element.getBoundingClientRect();
    if (bounds.top + bounds.height >= position) {
      hi = mid;
    }
    else {
      lo = mid;
    }
  }
  const hiElement = lines[hi];
  const hiBounds = hiElement.element.getBoundingClientRect();
  if (hi >= 1 && hiBounds.top > position) {
    const loElement = lines[lo];
    return { previous: loElement, next: hiElement };
  }
  return { previous: hiElement };
}

/**
 * Attempt to reveal the element for a source line in the editor.
 */
export function scrollToRevealSourceLine(line: number) {
  const { previous, next } = getElementsForSourceLine(line);
  if (previous && getState().scrollPreviewWithEditor) {
    let scrollTo = 0;
    const rect = previous.element.getBoundingClientRect();
    const previousTop = rect.top;
    if (next && next.line !== previous.line) {
      // Between two elements. Go to percentage offset between them.
      const betweenProgress = (line - previous.line) / (next.line - previous.line);
      const elementOffset = next.element.getBoundingClientRect().top - previousTop;
      scrollTo = previousTop + betweenProgress * elementOffset;
    }
    else {
      scrollTo = previousTop;
    }
    window.scroll(0, Math.max(1, window.scrollY + scrollTo));
  }
}

export function getEditorLineNumberForPageOffset(offset: number) {
  const { previous, next } = getLineElementsAtPageOffset(offset);
  if (previous) {
    const previousBounds = previous.element.getBoundingClientRect();
    const offsetFromPrevious = (offset - window.scrollY - previousBounds.top);
    if (next) {
      const progressBetweenElements = offsetFromPrevious / (next.element.getBoundingClientRect().top - previousBounds.top);
      const line = previous.line + progressBetweenElements * (next.line - previous.line);
      return clampLine(line);
    }
    else {
      const progressWithinElement = offsetFromPrevious / (previousBounds.height);
      const line = previous.line + progressWithinElement;
      return clampLine(line);
    }
  }
  return null;
}

/**
 * Useful for activating the selected elements.
 * Currently unused.
 */
export class ActiveLineMarker {
  private _current: any;

  onDidChangeTextEditorSelection(line: number) {
    const { previous } = getElementsForSourceLine(line);
    this._update(previous && previous.element);
  }

  _update(before: HTMLElement | undefined) {
    this._unmarkActiveElement(this._current);
    this._markActiveElement(before);
    this._current = before;
  }

  _unmarkActiveElement(element: HTMLElement | undefined) {
    if (!element) {
      return;
    }
    element.className = element.className.replace(/\bcode-active-line\b/g, '');
  }

  _markActiveElement(element: HTMLElement | undefined) {
    if (!element) {
      return;
    }
    element.className += ' code-active-line';
  }
}


================================================
FILE: packages/poml-vscode-webview/state.ts
================================================
import $ from "jquery";
import { MessagePoster } from "./util";
import { WebviewState, WebviewMessage, WebviewUserOptions } from "../poml-vscode/panel/types";

export function getData(key: string): any {
  // Preview data must be stored in the DOM (webview-state) by the extension side.
  const element = getElementOrThrowException('webview-state');
  if (element) {
    const data = element.getAttribute(key);
    if (data) {
      return JSON.parse(data);
    }
  }

  throw new Error(`Could not load data for ${key}`);
}

let cachedState: WebviewState | undefined = undefined;

export function getState(): WebviewState {
  if (cachedState) {
    return cachedState;
  }

  cachedState = getData('data-state');
  if (cachedState) {
    return cachedState;
  }

  throw new Error('Could not load state');
}

export function setCachedState(state: WebviewState): void {
  cachedState = state;
}

function getElementOrThrowException(id: string): HTMLElement {
  const element = document.getElementById(id);
  if (!element) {
    throw new Error(`Could not find element with id ${id}`);
  }
  return element;
}



================================================
FILE: packages/poml-vscode-webview/toolbar.ts
================================================
import $ from 'jquery';
import { MessagePoster } from './util';
import { WebviewState, WebviewMessage, WebviewUserOptions } from '../poml-vscode/panel/types';
import { getState, setCachedState } from './state';

/* The function to submit a toolbar configuration update. */
let toolbarUpdate: (() => void) | undefined = undefined;

/* Rerender chips when the user adds/removes context or stylesheet files.
   This is called when the backend sends an update to the webview to update the chip contents. */
let chipUpdate: (() => void) | undefined = undefined;

let vscodeApi: any = undefined;

function basename(p: string): string {
  const parts = p.split(/[/\\]/);
  return parts[parts.length - 1];
}

function rerenderChips(options: WebviewUserOptions) {
  const contexts = options.contexts ?? [];
  const stylesheets = options.stylesheets ?? [];

  // Remove existing chips.
  $('#context-stylesheet-files .chip').remove();

  // Add the chips onto #context-stylesheet-files before the add buttons
  for (const file of contexts) {
    const chip = $('<span class="context chip chip-context tooltip-anchor"/>').attr('data-file', file);
    $('<span class="codicon codicon-file-symlink-file" />').appendTo(chip);
    $('<span class="content"></span>').text(basename(file)).appendTo(chip);
    $('<span class="remove codicon codicon-close"/>').appendTo(chip);
    $('<span class="tooltip tooltip-long"></span>').text('Context: ' + file).appendTo(chip);
    chip.appendTo($('#context-stylesheet-files'));
  }

  for (const file of stylesheets) {
    const chip = $('<span class="stylesheet chip chip-stylesheet tooltip-anchor"/>').attr('data-file', file);
    $('<span class="codicon codicon-symbol-color" />').appendTo(chip);
    $('<span class="content"></span>').text(basename(file)).appendTo(chip);
    $('<span class="remove codicon codicon-close"/>').appendTo(chip);
    $('<span class="tooltip tooltip-long"></span>').text('Stylesheet: ' + file).appendTo(chip);
    chip.appendTo($('#context-stylesheet-files'));
  }

  $('<span class="chip add" id="add-context"/>')
    .append('<span class="codicon codicon-plus"></span>')
    .append('<span class="content">Add Context...</span>')
    .appendTo($('#context-stylesheet-files'));

  $('<span class="chip add" id="add-stylesheet"/>')
    .append('<span class="codicon codicon-plus"></span>')
    .append('<span class="content">Add Stylesheet...</span>')
    .appendTo($('#context-stylesheet-files'));

  $('#context-stylesheet .badge').text(
    contexts.length + stylesheets.length
  ).toggleClass('hidden', contexts.length + stylesheets.length === 0);
}

/* This function is called once to set up the toolbar and its event handlers. */
export const setupToolbar = (vscode: any, messaging: MessagePoster) => {
  vscodeApi = vscode;
  toolbarUpdate = function () {
    const form: any = {
      speakerMode: $('#speaker-mode').data('value') === true,
      displayFormat: $('#display-format').data('value'),
    };
    const newState: WebviewState = { ...getState(), ...form };
    vscode.setState(newState);
    setCachedState(newState);
    messaging.postMessage(WebviewMessage.Form, form);
  };

  chipUpdate = function () {
    rerenderChips(getState());
  };

  /* ------------------------------------------------------------------ */
  /* Delegated click-handlers (registered ONCE)                         */
  /* ------------------------------------------------------------------ */

  $(document)
    // Add context / stylesheet
    .off('click', '#add-context')
    .on('click', '#add-context', () => messaging.postCommand('poml.addContextFile', []))
    .off('click', '#add-stylesheet')
    .on('click', '#add-stylesheet', () => messaging.postCommand('poml.addStylesheetFile', []))
    // Remove context / stylesheet
    .off('click', '.context .remove')
    .on('click', '.context .remove', function () {
      const file = $(this).parent().data('file');
      messaging.postCommand('poml.removeContextFile', [file]);
    })
    .off('click', '.stylesheet .remove')
    .on('click', '.stylesheet .remove', function () {
      const file = $(this).parent().data('file');
      messaging.postCommand('poml.removeStylesheetFile', [file]);
    });

  /* ------------------------------------------------------------------ */
  /* One-time toolbar button handlers                                   */
  /* ------------------------------------------------------------------ */

  $('#copy').on('click', function () {
    const copyText = $('#copy-content').attr('data-value') ?? '';
    navigator.clipboard.writeText(copyText);
  });

  $('#context-stylesheet').on('click', function () {
    $("#context-stylesheet-files").toggleClass('hidden');
  });

  $(document).on('click', '.chat-message-toolbar .codicon-copy', function () {
    const copyText = $(this).attr('data-value') ?? '';
    navigator.clipboard.writeText(copyText);
  });

  $(document).on('click', '.chat-message-toolbar .codicon-code', function () {
    const line = parseInt($(this).data('line'));
    if (!isNaN(line)) {
      messaging.postMessage(WebviewMessage.DidClick, { line });
    }
  });

  $(document).on('dblclick', '[data-line]', function (e) {
    // Stop the event from bubbling up to parent elements that also match '[data-line]'.
    // This ensures the code inside only runs ONCE for the innermost element clicked.
    e.stopPropagation();

    if (!getState().doubleClickToSwitchToEditor) {
      return;
    }

    const line = $(this).attr('data-line');
    if (line) {
      const num = parseInt(line, 10);
      if (!isNaN(num)) {
        messaging.postMessage(WebviewMessage.DidClick, { line: num });

        // Prevent the browser's default double-click action (e.g., selecting text).
        e.preventDefault();
      }
    }
  });

  $('.toolbar .button.onoff').on('click', function () {
    $(this).toggleClass('active');
    $(this).data('value', $(this).hasClass('active'));
    toolbarUpdate?.();
  });

  $('.toolbar .button.menu-selection').on('click', function (e) {
    e.stopPropagation();
    $(this).toggleClass('active');
  });
  $('.button.menu-selection .menu .item').on('click', function (e) {
    const button = $(this).closest('.button.menu-selection');
    button.data('value', $(this).data('value')).attr('data-value', $(this).data('value'));
    button.find('> .content').text('Display: ' + $(this).find('.content').text());
    button.find('.menu .item').removeClass('selected');
    $(this).addClass('selected');
    button.removeClass('active');
    e.stopPropagation();
    toolbarUpdate?.();
  });
  $(document).on('click', function () {
    $('.toolbar .button.menu-selection').removeClass('active');
  });

  chipUpdate?.(); // initial render
};

/* -------------------------------------------------------------------- */
/* Handle messages from the extension                                   */
/* -------------------------------------------------------------------- */
window.addEventListener('message', e => {
  const message = e.data as any;
  if (message === undefined) {
    return;
  }
  if (message.type === WebviewMessage.UpdateContent) {
    $('#content').replaceWith(message.content);
  }
  if (message.type === WebviewMessage.UpdateUserOptions) {
    // The contexts and stylesheets are updated from the server side,
    // though the update is initially initiated by the client side.
    const newState: WebviewState = { ...getState(), ...message.options };
    vscodeApi?.setState(newState);
    setCachedState(newState);
    chipUpdate?.();
  }
});



================================================
FILE: packages/poml-vscode-webview/util.ts
================================================
import { getState } from './state';

export interface MessagePoster {
  /**
   * Post a message to the poml extension
   */
  postMessage(type: string, body: object): void;

  /**
   * Post a command to be executed to the poml extension
   */
  postCommand(command: string, args: any[]): void;
}

/**
 * Poster is a class that allows sending messages to the extension
 * @param vscode Provided by the vscode API.
 * @returns The message poster class.
 */
export const createPosterForVsCode = (vscode: any) => {
  return new class implements MessagePoster {
    postMessage(type: string, body: object): void {
      vscode.postMessage({
        type,
        source: getState().source,
        body
      });
    }
    postCommand(command: string, args: any[]) {
      this.postMessage('command', { command, args });
    }
  };
};



================================================
FILE: packages/poml-vscode-webview/tests/jumpToSource.test.ts
================================================
/** @jest-environment jsdom */

import $ from 'jquery';
import { describe, test, expect, jest } from '@jest/globals';
import { setupToolbar } from '../toolbar';

jest.mock('../state', () => ({
  getState: () => ({ doubleClickToSwitchToEditor: true })
}));

describe('jump to source', () => {
  test('button click posts message', () => {
    document.body.innerHTML = `
      <div class="chat-message">
        <div class="chat-message-toolbar">
          <div class="toolbar-item">
            <a class="codicon codicon-code" role="button" data-line="3"></a>
          </div>
        </div>
      </div>`;
    const vscode = { setState: jest.fn() } as any;
    const messaging = { postMessage: jest.fn() } as any;
    setupToolbar(vscode, messaging);
    $('.codicon-code').trigger('click');
    expect(messaging.postMessage).toHaveBeenCalledWith('didClick', { line: 3 });
  });

  test('double click posts message', () => {
    document.body.innerHTML = `<div data-line="2">text</div>`;
    const vscode = { setState: jest.fn() } as any;
    const messaging = { postMessage: jest.fn() } as any;
    setupToolbar(vscode, messaging);
    $('[data-line="2"]').trigger('dblclick');
    expect(messaging.postMessage).toHaveBeenCalledWith('didClick', { line: 2 });
  });
});



================================================
FILE: packages/poml-vscode-webview/tests/messageCopy.test.ts
================================================
/** @jest-environment jsdom */

import $ from 'jquery';
import { describe, test, expect, jest } from '@jest/globals';
import { setupToolbar } from '../toolbar';

jest.mock('../state', () => ({
  getState: () => ({})
}));

describe('message copy button', () => {
  test('click copies message text', () => {
    document.body.innerHTML = `
      <div class="chat-message">
        <div class="chat-message-toolbar">
          <div class="toolbar-item">
            <a class="codicon codicon-copy" role="button" data-value="msg"></a>
          </div>
        </div>
      </div>
    `;

    (navigator as any).clipboard = { writeText: jest.fn() };

    const vscode = { setState: jest.fn() } as any;
    const messaging = { postMessage: jest.fn() } as any;

    setupToolbar(vscode, messaging);
    $('.codicon-copy').trigger('click');

    expect((navigator as any).clipboard.writeText).toHaveBeenCalledWith('msg');
  });
});



================================================
FILE: packages/poml-vscode-webview/tests/toolbar.test.ts
================================================
/** @jest-environment jsdom */

import $ from 'jquery';
import { describe, test, expect, jest } from '@jest/globals';
import { setupToolbar } from '../toolbar';

jest.mock('../state', () => ({
  getState: () => ({})
}));

describe('toolbar copy button', () => {
  test('click copies content to clipboard', () => {
    document.body.innerHTML = `
      <div class="toolbar">
        <div class="button oneclick" id="copy"></div>
      </div>
      <div id="copy-content" data-value="hello"></div>
    `;

    (navigator as any).clipboard = { writeText: jest.fn() };

    const vscode = { setState: jest.fn() } as any;
    const messaging = { postMessage: jest.fn() } as any;

    setupToolbar(vscode, messaging);
    $('#copy').trigger('click');

    expect((navigator as any).clipboard.writeText).toHaveBeenCalledWith('hello');
  });
});



================================================
FILE: packages/poml-vscode-webview/tests/util.test.ts
================================================
import { describe, test, expect, jest } from '@jest/globals';
import { createPosterForVsCode } from '../util';

jest.mock('../state', () => ({
  getState: () => ({ source: 'test-source' })
}));

describe('createPosterForVsCode', () => {
  test('postMessage sends payload to vscode', () => {
    const vscode = { postMessage: jest.fn() };
    const poster = createPosterForVsCode(vscode);
    poster.postMessage('type', { foo: 'bar' });
    expect(vscode.postMessage).toHaveBeenCalledWith({
      type: 'type',
      source: 'test-source',
      body: { foo: 'bar' }
    });
  });

  test('postCommand wraps command type', () => {
    const vscode = { postMessage: jest.fn() };
    const poster = createPosterForVsCode(vscode);
    poster.postCommand('cmd', [1, 2]);
    expect(vscode.postMessage).toHaveBeenCalledWith({
      type: 'command',
      source: 'test-source',
      body: { command: 'cmd', args: [1, 2] }
    });
  });
});



================================================
FILE: python/poml/__init__.py
================================================
from ._version import __version__

from .api import *
from .cli import entrypoint, run
from .prompt import Prompt



================================================
FILE: python/poml/__main__.py
================================================
from .cli import entrypoint

if __name__ == '__main__':
    entrypoint()



================================================
FILE: python/poml/_version.py
================================================
__version__ = '0.0.8'



================================================
FILE: python/poml/api.py
================================================
from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Literal, Union
from pydantic import BaseModel
import warnings
from .cli import run

__all__ = [
    "set_trace",
    "clear_trace",
    "get_trace",
    "trace_artifact",
    "poml",
    "Backend",
    "OutputFormat",
]

_trace_enabled: bool = False
_weave_enabled: bool = False
_agentops_enabled: bool = False
_mlflow_enabled: bool = False
_trace_log: List[Dict[str, Any]] = []
_trace_dir: Optional[Path] = None

Backend = Literal["local", "weave", "agentops", "mlflow"]
OutputFormat = Literal["raw", "dict", "openai_chat", "langchain", "pydantic"]


def set_trace(
    enabled: bool | List[Backend] | Backend = True, /, *, trace_dir: Optional[str | Path] = None
) -> Optional[Path]:
    """Enable or disable tracing of ``poml`` calls with optional backend integrations.

    Args:
        enabled: Controls which tracing backends to enable. Can be:
            - True: Enable local tracing only (equivalent to ["local"])
            - False: Disable all tracing (equivalent to [])
            - str: Enable a single backend ("local", "weave", "agentops", "mlflow")
            - List[str]: Enable multiple backends. "local" is auto-enabled if any backends are specified.
        trace_dir: Optional directory for local trace files. If provided when local
            tracing is enabled, a subdirectory named by the current timestamp
            (YYYYMMDDHHMMSSffffff) is created inside trace_dir.

    Returns:
        Path to the trace directory if local tracing is enabled, None otherwise.
        The directory may be shared with POML Node.js by setting the
        POML_TRACE environment variable in the invoking script.

    Available backends:
        - "local": Save trace files to disk
        - "weave": Log to Weights & Biases Weave (requires local tracing)
        - "agentops": Log to AgentOps (requires local tracing)
        - "mlflow": Log to MLflow (requires local tracing)
    """

    if enabled is True:
        enabled = ["local"]
    elif enabled is False:
        enabled = []

    if isinstance(enabled, str):
        enabled = [enabled]

    global _trace_enabled, _trace_dir, _weave_enabled, _agentops_enabled, _mlflow_enabled
    if enabled or "local" in enabled:
        # When enabled is non-empty, we always enable local tracing.
        _trace_enabled = True
        env_dir = os.environ.get("POML_TRACE")
        if trace_dir is not None:
            base = Path(trace_dir)
            base.mkdir(parents=True, exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d%H%M%S%f")
            run_dir = base / ts
            run_dir.mkdir(parents=True, exist_ok=True)
            _trace_dir = run_dir
        elif env_dir:
            run_dir = Path(env_dir)
            run_dir.mkdir(parents=True, exist_ok=True)
            _trace_dir = run_dir
        else:
            _trace_dir = None
    else:
        _trace_enabled = False
        _trace_dir = None

    if "weave" in enabled:
        _weave_enabled = True
    else:
        _weave_enabled = False

    if "agentops" in enabled:
        _agentops_enabled = True
    else:
        _agentops_enabled = False

    if "mlflow" in enabled:
        _mlflow_enabled = True
    else:
        _mlflow_enabled = False

    return _trace_dir


def clear_trace() -> None:
    """Clear the collected trace log."""
    _trace_log.clear()


def get_trace() -> List[Dict[str, Any]]:
    """Return a copy of the trace log."""
    return list(_trace_log)


def _current_trace_version() -> Optional[str]:
    """Return the current trace version."""
    if not (_trace_enabled and _trace_dir):
        return None
    else:
        return _trace_dir.name


def _latest_trace_prefix() -> Optional[Path]:
    if not (_trace_enabled and _trace_dir):
        return None

    pattern = re.compile(r"^(\d{4}.*?)(?:\.source)?\.poml$")
    latest_idx = -1
    latest_prefix: Optional[Path] = None

    for f in _trace_dir.iterdir():
        match = pattern.match(f.name)
        if not match:
            continue
        prefix_part = match.group(1)
        # skip any source link files
        if prefix_part.endswith(".source"):
            continue
        try:
            idx = int(prefix_part.split(".")[0])
        except ValueError:
            continue
        if idx > latest_idx:
            latest_idx = idx
            latest_prefix = _trace_dir / prefix_part

    return latest_prefix


def _read_latest_traced_file(file_suffix: str) -> Optional[str]:
    """Read the most recent traced file with the given suffix."""
    prefix = _latest_trace_prefix()
    if prefix is None:
        return None
    path = Path(str(prefix) + file_suffix)
    if not path.exists():
        return None
    with open(path, "r") as f:
        return f.read()


def trace_artifact(file_suffix: str, contents: str | bytes) -> Optional[Path]:
    """Write an additional artifact file for the most recent ``poml`` call."""
    prefix = _latest_trace_prefix()
    if prefix is None:
        return None
    suffix = file_suffix if file_suffix.startswith(".") else f".{file_suffix}"
    path = Path(str(prefix) + suffix)
    mode = "wb" if isinstance(contents, (bytes, bytearray)) else "w"
    with open(path, mode) as f:
        f.write(contents)
    return path


def write_file(content: str):
    temp_file = tempfile.NamedTemporaryFile("w")
    temp_file.write(content)
    temp_file.flush()
    return temp_file


class ContentMultiMedia(BaseModel):
    type: str  # image/png, image/jpeg, ...
    base64: str
    alt: Optional[str] = None


RichContent = Union[str, List[Union[str, ContentMultiMedia]]]

Speaker = Literal["human", "ai", "system"]


class PomlMessage(BaseModel):
    speaker: Speaker
    content: RichContent


def _poml_response_to_openai_chat(messages: List[PomlMessage]) -> List[Dict[str, Any]]:
    """Convert PomlMessage objects to OpenAI chat format."""
    openai_messages = []
    speaker_to_role = {
        "human": "user",
        "ai": "assistant",
        "system": "system",
    }

    for msg in messages:
        if msg.speaker not in speaker_to_role:
            raise ValueError(f"Unknown speaker: {msg.speaker}")
        role = speaker_to_role[msg.speaker]

        if isinstance(msg.content, str):
            openai_messages.append({"role": role, "content": msg.content})
        elif isinstance(msg.content, list):
            contents = []
            for content_part in msg.content:
                if isinstance(content_part, str):
                    contents.append({"type": "text", "text": content_part})
                elif isinstance(content_part, ContentMultiMedia):
                    contents.append(
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{content_part.type};base64,{content_part.base64}"},
                        }
                    )
                else:
                    raise ValueError(f"Unexpected content part: {content_part}")
            openai_messages.append({"role": role, "content": contents})
        else:
            raise ValueError(f"Unexpected content type: {type(msg.content)}")

    return openai_messages


def _poml_response_to_langchain(messages: List[PomlMessage]) -> List[Dict[str, Any]]:
    """Convert PomlMessage objects to Langchain format."""
    langchain_messages = []
    for msg in messages:
        if isinstance(msg.content, str):
            langchain_messages.append({"type": msg.speaker, "data": {"content": msg.content}})
        elif isinstance(msg.content, list):
            content_parts = []
            for content_part in msg.content:
                if isinstance(content_part, str):
                    content_parts.append({"type": "text", "text": content_part})
                elif isinstance(content_part, ContentMultiMedia):
                    content_parts.append(
                        {
                            "type": "image",
                            "source_type": "base64",
                            "data": content_part.base64,
                            "mime_type": content_part.type,
                        }
                    )
                else:
                    raise ValueError(f"Unexpected content part: {content_part}")
            langchain_messages.append({"type": msg.speaker, "data": {"content": content_parts}})
        else:
            raise ValueError(f"Unexpected content type: {type(msg.content)}")
    return langchain_messages


def poml(
    markup: str | Path,
    context: dict | str | Path | None = None,
    stylesheet: dict | str | Path | None = None,
    chat: bool = True,
    output_file: str | Path | None = None,
    format: OutputFormat = "dict",
    extra_args: Optional[List[str]] = None,
) -> list | dict | str:
    """Process POML markup and return the result in the specified format.

    POML (Prompt Orchestration Markup Language) is a markup language for creating
    structured prompts and conversations. This function processes POML markup
    with optional context and styling, returning the result in various formats.

    Args:
        markup: POML markup content as a string, or path to a POML file.
            If a string that looks like a file path but doesn't exist,
            a warning is issued and it's treated as markup content.
        context: Optional context data to inject into the POML template.
            Can be a dictionary, JSON string, or path to a JSON file.
        stylesheet: Optional stylesheet for customizing POML rendering.
            Can be a dictionary, JSON string, or path to a JSON file.
        chat: If True, process as a chat conversation (default).
            If False, process as a single prompt.
        output_file: Optional path to save the output. If not provided,
            output is returned directly without saving to disk.
        format: Output format for the result:
            - "raw": Return raw string output from POML processor
            - "dict": Return the core LLM prompt as a dict or list
            - "openai_chat": Return OpenAI chat completion format
            - "langchain": Return LangChain message format
            - "pydantic": Return list of PomlMessage objects
        extra_args: Additional command-line arguments to pass to the POML processor.

    Returns:
        The processed result in the specified format:
        - str: When format="raw"
        - dict/list: When format="dict"
        - List[Dict[str, Any]]: When format="openai_chat" or "langchain"
        - List[PomlMessage]: When format="pydantic"

    Raises:
        FileNotFoundError: When a specified file path doesn't exist.
        RuntimeError: When the POML processor fails or backend tracing requirements aren't met.
        ValueError: When an invalid output format is specified.

    Examples:
        Basic usage with markup string:
        >>> result = poml("<p>Hello {{name}}!</p>", context={"name": "World"})

        Load from file with context:
        >>> result = poml("template.poml", context="context.json")

        Get OpenAI chat format:
        >>> messages = poml("chat.poml", format="openai_chat")

        Use with custom stylesheet:
        >>> result = poml(
        ...     markup="template.poml",
        ...     context={"user": "Alice"},
        ...     stylesheet={"role": {"captionStyle": "bold"}},
        ...     format="pydantic"
        ... )

        Save output to file:
        >>> poml("template.poml", output_file="output.json", format="raw")

    Note:
        - When tracing is enabled via set_trace(), call details are automatically logged
        - The function supports various backend integrations (Weave, AgentOps, MLflow)
        - Multi-modal content (images, etc.) is supported in chat format
    """
    temp_input_file = temp_context_file = temp_stylesheet_file = None
    trace_record: Dict[str, Any] | None = None
    try:
        if _trace_enabled:
            trace_record = {}
            if isinstance(markup, Path) or os.path.exists(str(markup)):
                path = Path(markup)
                trace_record["markup_path"] = str(path)
                if path.exists():
                    trace_record["markup"] = path.read_text()
            else:
                trace_record["markup"] = str(markup)

            if isinstance(context, dict):
                trace_record["context"] = json.dumps(context)
            elif context:
                if os.path.exists(str(context)):
                    cpath = Path(context)
                    trace_record["context_path"] = str(cpath)
                    trace_record["context"] = cpath.read_text()
            if isinstance(stylesheet, dict):
                trace_record["stylesheet"] = json.dumps(stylesheet)
            elif stylesheet:
                if os.path.exists(str(stylesheet)):
                    spath = Path(stylesheet)
                    trace_record["stylesheet_path"] = str(spath)
                    trace_record["stylesheet"] = spath.read_text()

        if isinstance(markup, Path):
            if not markup.exists():
                raise FileNotFoundError(f"File not found: {markup}")
        else:
            if os.path.exists(markup):
                markup = Path(markup)
            else:
                # Test if the markup looks like a path.
                if re.match(r"^[\w\-./]+$", markup):
                    warnings.warn(
                        f"The markup '{markup}' looks like a file path, but it does not exist. Assuming it is a POML string."
                    )

                temp_input_file = write_file(markup)
                markup = Path(temp_input_file.name)
        with tempfile.NamedTemporaryFile("r") as temp_output_file:
            if output_file is None:
                output_file = temp_output_file.name
                output_file_specified = False
            else:
                output_file_specified = True
                if isinstance(output_file, Path):
                    output_file = str(output_file)
            args = ["-f", str(markup), "-o", output_file]
            if isinstance(context, dict):
                temp_context_file = write_file(json.dumps(context))
                args.extend(["--context-file", temp_context_file.name])
            elif context:
                if os.path.exists(context):
                    args.extend(["--context-file", str(context)])
                else:
                    raise FileNotFoundError(f"File not found: {context}")

            if isinstance(stylesheet, dict):
                temp_stylesheet_file = write_file(json.dumps(stylesheet))
                args.extend(["--stylesheet-file", temp_stylesheet_file.name])
            elif stylesheet:
                if os.path.exists(stylesheet):
                    args.extend(["--stylesheet-file", str(stylesheet)])
                else:
                    raise FileNotFoundError(f"File not found: {stylesheet}")

            if chat:
                args.extend(["--chat", "true"])
            else:
                args.extend(["--chat", "false"])

            if _trace_enabled and _trace_dir is not None:
                args.extend(["--traceDir", str(_trace_dir)])

            if extra_args:
                args.extend(extra_args)
            process = run(*args)
            if process.returncode != 0:
                raise RuntimeError(
                    f"POML command failed with return code {process.returncode}. See the log for details."
                )

            if output_file_specified:
                with open(output_file, "r") as output_file_handle:
                    result = output_file_handle.read()
            else:
                result = temp_output_file.read()

            if format == "raw":
                # Do nothing
                pass
            else:
                result = json.loads(result)
                if isinstance(result, dict) and "messages" in result:
                    # The new versions will always return a dict with "messages" key.
                    result = result["messages"]
                if format != "dict":
                    # Continue to validate the format.
                    if chat:
                        pydantic_result = [PomlMessage(**item) for item in result]
                    else:
                        # TODO: Make it a RichContent object
                        pydantic_result = [PomlMessage(speaker="human", content=result)]

                    if format == "pydantic":
                        return pydantic_result
                    elif format == "openai_chat":
                        return _poml_response_to_openai_chat(pydantic_result)
                    elif format == "langchain":
                        return _poml_response_to_langchain(pydantic_result)
                    else:
                        raise ValueError(f"Unknown output format: {format}")

            if _weave_enabled:
                from .integration import weave

                trace_prefix = _latest_trace_prefix()
                current_version = _current_trace_version()
                if trace_prefix is None or current_version is None:
                    raise RuntimeError("Weave tracing requires local tracing to be enabled.")
                poml_content = _read_latest_traced_file(".poml")
                context_content = _read_latest_traced_file(".context.json")
                stylesheet_content = _read_latest_traced_file(".stylesheet.json")

                weave.log_poml_call(
                    trace_prefix.name,
                    poml_content or str(markup),
                    json.loads(context_content) if context_content else None,
                    json.loads(stylesheet_content) if stylesheet_content else None,
                    result,
                )

            if _agentops_enabled:
                from .integration import agentops

                trace_prefix = _latest_trace_prefix()
                current_version = _current_trace_version()
                if trace_prefix is None or current_version is None:
                    raise RuntimeError("AgentOps tracing requires local tracing to be enabled.")
                poml_content = _read_latest_traced_file(".poml")
                context_content = _read_latest_traced_file(".context.json")
                stylesheet_content = _read_latest_traced_file(".stylesheet.json")
                agentops.log_poml_call(
                    trace_prefix.name,
                    str(markup),
                    json.loads(context_content) if context_content else None,
                    json.loads(stylesheet_content) if stylesheet_content else None,
                    result,
                )

            if _mlflow_enabled:
                from .integration import mlflow

                trace_prefix = _latest_trace_prefix()
                current_version = _current_trace_version()
                if trace_prefix is None or current_version is None:
                    raise RuntimeError("MLflow tracing requires local tracing to be enabled.")
                poml_content = _read_latest_traced_file(".poml")
                context_content = _read_latest_traced_file(".context.json")
                stylesheet_content = _read_latest_traced_file(".stylesheet.json")
                mlflow.log_poml_call(
                    trace_prefix.name,
                    poml_content or str(markup),
                    json.loads(context_content) if context_content else None,
                    json.loads(stylesheet_content) if stylesheet_content else None,
                    result,
                )

            if trace_record is not None:
                trace_record["result"] = result
            return result
    finally:
        if temp_input_file:
            temp_input_file.close()
        if temp_context_file:
            temp_context_file.close()
        if temp_stylesheet_file:
            temp_stylesheet_file.close()
        if trace_record is not None:
            _trace_log.append(trace_record)


if os.getenv("POML_TRACE") and not _trace_enabled:
    set_trace(True)



================================================
FILE: python/poml/cli.py
================================================
from __future__ import annotations

import os
import sys
import subprocess
import nodejs_wheel
from typing import Any, NoReturn


def node(*args: str, **kwargs: Any) -> subprocess.CompletedProcess[bytes | str]:
    return nodejs_wheel.node(args, return_completed_process=True, **kwargs)


def run(*args: str, **kwargs: Any) -> subprocess.CompletedProcess[bytes | str]:
    script = os.path.join(os.path.dirname(__file__), 'js', 'cli.js')
    if not os.path.exists(script):
        raise RuntimeError(f'Expected CLI entrypoint: {script} to exist')

    return node(script, *args, **kwargs)


def entrypoint() -> NoReturn:
    sys.exit(run(*sys.argv[1:]).returncode)



================================================
FILE: python/poml/prompt.py
================================================
import xml.etree.ElementTree as ET
import base64
import json
import tempfile
import warnings

from .api import poml
from ._tags import _TagLib


def _write_file_for_poml(content: str):
    """Writes content to a named temporary file that is not deleted on close."""
    # The caller is responsible for managing the lifecycle of this file, including deletion.
    temp_file = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False)
    temp_file.write(content)
    temp_file.flush()  # Ensure content is written to disk
    # temp_file.close() # Consider if the file should be closed here or by the caller.
    return temp_file


class _ImplicitDualTagHandler:
    """
    Handles XML tags that can be self-closing or act as context managers for nested content.
    It creates an ET.Element on initialization and adds it to the current parent.
    If used with 'with', it pushes the element onto the Prompt's parent stack.
    """

    def __init__(self, prompt_instance: "Prompt", tag_name: str, attrs: dict):
        self.prompt = prompt_instance
        self.tag_name = tag_name

        prepared_attrs = self.prompt._prepare_attrs(**attrs)
        self.element = ET.Element(tag_name, prepared_attrs)

        if self.prompt.current_parent_stack:
            # Append as child to the currently open element
            self.prompt.current_parent_stack[-1].append(self.element)
        else:
            # No parent on stack, so this is a root-level element
            self.prompt.root_elements.append(self.element)

        self._is_context_managed = False  # True if __enter__ completes successfully

    def __enter__(self):
        # This element now becomes the current parent for any nested tags or text.
        self.prompt.current_parent_stack.append(self.element)
        self._is_context_managed = True
        return self.prompt  # Return Prompt instance for chained calls like p.text()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._is_context_managed:
            # This means __enter__ did not complete successfully, or the handler
            # was instantiated but not used correctly in a 'with' statement.
            raise SystemError(
                f"Exiting tag handler for '{self.element.tag}' that was not properly context-managed. "
                "Ensure it's used in a 'with' statement and __enter__ completed."
            )

        # If __enter__ completed, self.element was pushed onto the stack.
        if not self.prompt.current_parent_stack:
            # This indicates a critical internal logic error.
            raise SystemError(
                f"Internal error: Tag stack empty while exiting context for '{self.element.tag}'. "
                "_is_context_managed was True, implying a tag should be on stack."
            )

        popped_element = self.prompt.current_parent_stack.pop()
        if popped_element is not self.element:
            # This is a critical internal error, indicating mismatched tags or stack corruption.
            self.prompt.current_parent_stack.append(popped_element)  # Restore the stack to its previous state
            raise SystemError(
                f"XML structure error: Mismatched tag on context exit. Expected to pop '{self.element.tag}', "
                f"but found '{popped_element.tag}'. This suggests an issue with nested contexts."
            )


class Prompt(_TagLib):
    """
    Builds an XML structure using ElementTree, supporting context-managed tags.
    """

    def __init__(self):
        self.root_elements: list[ET.Element] = []
        self.current_parent_stack: list[ET.Element] = []  # Stack of current ET.Element parents

    def _prepare_attrs(self, **attrs) -> dict[str, str]:
        """Converts attribute values to strings suitable for ElementTree."""
        prepared = {}
        for k, v in attrs.items():
            if v is None:  # Skip None attributes
                continue
            key_str = str(k)  # Keys are typically strings
            if isinstance(v, bool):
                val_str = str(v).lower()  # XML often uses "true"/"false"
            elif isinstance(v, bytes):
                b64 = base64.b64encode(v).decode()
                if key_str == "buffer":
                    prepared["base64"] = b64
                    continue
                else:
                    val_str = base64.b64encode(v).decode("ascii")
            elif isinstance(v, (int, float, str)):
                val_str = str(v)
            else:
                val_str = json.dumps(v)  # Fallback for complex types, convert to JSON string
            prepared[key_str] = val_str
        return prepared

    def text(self, content: str):
        """Adds text content to the currently open XML element."""
        if not self.current_parent_stack:
            raise ValueError("Cannot add text: No tag is currently open. Use a 'with' block for a tag.")

        current_el = self.current_parent_stack[-1]
        # ElementTree handles XML escaping for text content automatically
        content_str = str(content)

        # Append text correctly for mixed content (text between child elements)
        if len(current_el) > 0:  # If current element has children
            last_child = current_el[-1]
            if last_child.tail is None:
                last_child.tail = content_str
            else:
                last_child.tail += content_str
        else:  # No children yet in the current element, add to its primary text
            if current_el.text is None:
                current_el.text = content_str
            else:
                current_el.text += content_str

    def _generate_xml_string(self, pretty: bool) -> str:
        """
        Serializes the built XML structure to a string.
        Can optionally pretty-print the output.
        """
        if self.current_parent_stack:
            # This warning is for cases where rendering/dumping happens with unclosed tags.
            print(
                f"Warning: Generating XML with open tags: {[el.tag for el in self.current_parent_stack]}. "
                "Ensure all 'with' blocks for tags are properly exited before finalizing XML."
            )

        xml_strings = []
        for root_el in self.root_elements:
            if pretty:
                # ET.indent modifies the element in-place (Python 3.9+)
                ET.indent(root_el, space="  ", level=0)
                xml_strings.append(ET.tostring(root_el, encoding="unicode", method="xml"))
            else:
                # Serialize compactly without extra whitespace
                xml_strings.append(ET.tostring(root_el, encoding="unicode", method="xml"))

        # Join the string representations of each root-level element.
        # If pretty printing and multiple roots, join with newlines for readability.
        # Otherwise, join directly to form a contiguous XML stream.
        joiner = "\n" if pretty and len(xml_strings) > 0 else ""  # Add newline between pretty roots
        return joiner.join(xml_strings)

    def render(self, chat: bool = True, context=None, stylesheet=None) -> list | dict | str:
        """
        Renders the final XML. Raises error if tags are still open.
        """
        if self.current_parent_stack:
            raise ValueError(
                f"Cannot render: Open tags remaining: {[el.tag for el in self.current_parent_stack]}. "
                "Ensure all 'with' blocks for tags are properly exited."
            )
        # poml likely expects a compact, single XML string.
        final_xml = self._generate_xml_string(pretty=False)
        return poml(final_xml, context=context, stylesheet=stylesheet, chat=chat)

    def dump_xml(self) -> str:
        """
        Dumps the generated XML string, pretty-printed by default (useful for debugging).
        """
        return self._generate_xml_string(pretty=True)

    def __enter__(self):
        """Enter a context for building a prompt.

        The Prompt instance can be reused across multiple ``with`` blocks. On
        each entry we simply reset the stack of currently open elements while
        preserving any previously created root elements so that additional tags
        can be appended in subsequent sessions.
        """

        # Reset the stack of open elements for this new session but leave any
        # existing root elements intact so the prompt can be extended across
        # multiple ``with`` blocks.
        self.current_parent_stack = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cleans up Prompt state upon exiting a 'with' block."""
        if self.current_parent_stack and exc_type is None:
            # This means the Prompt context itself exited while some _ImplicitDualTagHandler
            # contexts (tags) were still notionally open.
            warnings.warn(
                f"Warning: Prompt context exited with open tags: {[el.tag for el in self.current_parent_stack]}. "
                "This may indicate nested tag context managers were not properly closed before the Prompt context ended."
            )

        # Clear any open elements from the stack.  Previously the entire state
        # was discarded on exit which meant ``dump_xml`` and ``render`` could
        # only be called while inside the ``with`` block.  By keeping the root
        # elements around we allow callers to finalize or extend the prompt
        # after the block has exited.
        self.current_parent_stack.clear()

    def tag(self, tag_name: str, **attrs) -> _ImplicitDualTagHandler:
        return _ImplicitDualTagHandler(self, tag_name, attrs)


if __name__ == '__main__':
    # Example usage of the Prompt class
    with Prompt() as p:
        with p.paragraph():
            with p.task(id="task1", status="open"):
                p.text("This is a task description.")
            with p.paragraph():
                p.text("This is a paragraph in the document.")

        xml_output = p.dump_xml()  # Get pretty-printed XML for debugging
        print(xml_output)
        prompt_output = p.render()
        print(prompt_output)

        # <p>
        #   <Task id="task1" status="open">This is a task description.</Task>
        #   <p>This is a paragraph in the document.</p>
        # </p>
        # [{'speaker': 'human', 'content': '# Task\n\nThis is a task description.\n\nThis is a paragraph in the document.'}]



================================================
FILE: python/poml/integration/__init__.py
================================================
[Empty file]


================================================
FILE: python/poml/integration/agentops.py
================================================
from __future__ import annotations

from typing import Any
import agentops


def log_poml_call(name: str, prompt: str, context: dict | None, stylesheet: dict | None, result: Any) -> Any:
    """Log the entire poml call to agentops."""

    @agentops.operation(name="poml")
    def poml(prompt, context, stylesheet):
        return result

    poml(prompt, context, stylesheet)



================================================
FILE: python/poml/integration/langchain.py
================================================
from pathlib import Path
from typing import Union, Any
from typing_extensions import override
from poml.api import poml
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import messages_from_dict
from langchain_core.prompt_values import ChatPromptValue, StringPromptValue


def poml_formatter(markup: Union[str, Path], speaker_mode: bool, context: dict | None = None):
    messages = poml(markup, chat=speaker_mode, context=context, format="langchain")
    return messages_from_dict(messages)


class LangchainPomlTemplate(PromptTemplate):
    """A LangChain-compatible prompt template that uses POML (Prompt Markup Language) for formatting.

    This class extends LangChain's PromptTemplate to support POML markup, enabling rich prompt
    formatting with speaker modes and structured content. It can load templates from files or
    strings and format them into either ChatPromptValue or StringPromptValue objects.

    Attributes:
        template_file (Union[str, Path, None]): Path to the POML template file, if loaded from file.
        speaker_mode (bool): Whether to format output as chat messages (True) or plain text (False).
            Defaults to True.

    Examples:
        Create from a template string:
        >>> template = LangchainPomlTemplate.from_template(
        ...     "Hello {{name}}!", speaker_mode=True
        ... )
        >>> result = template.format(name="Alice")

        Load from a POML file:
        >>> template = LangchainPomlTemplate.from_file(
        ...     "path/to/template.poml", speaker_mode=False
        ... )
        >>> result = template.format(user_input="What is AI?")

    Note:
        - In speaker_mode=True, returns ChatPromptValue with structured messages
        - In speaker_mode=False, returns StringPromptValue with plain text
        - The from_examples() method is not supported and will raise NotImplementedError
    """

    template_file: Union[str, Path, None] = None
    speaker_mode: bool = True

    @property
    @override
    def lc_attributes(self) -> dict[str, Any]:
        return {
            "template_file": self.template_file,
            "speaker_mode": self.speaker_mode,
            # Template format is not used
            # "template_format": self.template_format,
        }

    @classmethod
    @override
    def get_lc_namespace(cls) -> list[str]:
        return ["poml", "integration", "langchain"]

    @classmethod
    def from_examples(cls, *args, **kwargs):
        raise NotImplementedError(
            "LangchainPomlTemplate does not support from_examples. Use from_template or from_file instead."
        )

    @classmethod
    def from_file(
        cls, template_file: Union[str, Path], *args, speaker_mode: bool = True, **kwargs
    ) -> "LangchainPomlTemplate":
        instance: LangchainPomlTemplate = super().from_file(template_file, **kwargs)  # type: ignore
        instance.template_file = template_file
        instance.speaker_mode = speaker_mode
        return instance

    @classmethod
    def from_template(cls, *args, speaker_mode: bool = True, **kwargs) -> "LangchainPomlTemplate":
        instance: LangchainPomlTemplate = super().from_template(*args, **kwargs)  # type: ignore
        instance.speaker_mode = speaker_mode
        return instance

    def format(self, **kwargs) -> Union[ChatPromptValue, StringPromptValue]:  # type: ignore
        kwargs = self._merge_partial_and_user_variables(**kwargs)
        if self.template_file:
            formatted_messages = poml_formatter(self.template_file, self.speaker_mode, kwargs)
        else:
            formatted_messages = poml_formatter(self.template, self.speaker_mode, kwargs)
        if self.speaker_mode:
            return ChatPromptValue(messages=formatted_messages)
        else:
            if len(formatted_messages) == 1:
                if isinstance(formatted_messages[0].content, str):
                    return StringPromptValue(text=formatted_messages[0].content)
                elif isinstance(formatted_messages[0].content, list):
                    # If the content is a list, we assume it's a single message with multiple parts.
                    if len(formatted_messages[0].content) == 1:
                        # If there's only one part, return it as a StringPromptValue
                        if isinstance(formatted_messages[0].content[0], str):
                            return StringPromptValue(text=formatted_messages[0].content[0])
                        else:
                            raise ValueError(
                                f"Unsupported content type for non-speaker mode: {formatted_messages[0].content[0]}"
                            )
                    else:
                        raise ValueError(
                            f"Multi-part contents is not supported for non-speaker mode: {formatted_messages[0].content}"
                        )
                else:
                    raise ValueError(f"Unsupported content type for non-speaker mode: {formatted_messages[0].content}")
            else:
                raise ValueError(
                    f"Multiple messages returned, but non-speaker mode requires a single message: {formatted_messages}"
                )

    def format_prompt(self, **kwargs):
        return self.format(**kwargs)



================================================
FILE: python/poml/integration/mlflow.py
================================================
from __future__ import annotations

from typing import Any
import mlflow
import mlflow.genai


def log_poml_call(name: str, prompt: str, context: dict | None, stylesheet: dict | None, result: Any) -> Any:
    """Log the entire poml call to mlflow."""

    @mlflow.trace
    def poml(prompt, context, stylesheet):
        return result

    prompt_registered = mlflow.genai.register_prompt(
        name=name,
        template=prompt,
        tags={
            "format": "poml",
            "source": "auto"
        },
    )

    poml(prompt, context, stylesheet)



================================================
FILE: python/poml/integration/weave.py
================================================
from __future__ import annotations

from typing import Any
import weave


def log_poml_call(name: str, prompt: str, context: dict | None, stylesheet: dict | None, result: Any) -> Any:
    """Log the entire poml call to weave."""

    @weave.op
    def poml(prompt, context, stylesheet):
        return result

    prompt_ref = weave.publish(prompt, name=name)
    if context is not None:
        context_ref = weave.publish(context, name=name + ".context")
    else:
        context_ref = context
    if stylesheet is not None and stylesheet != "{}":
        stylesheet_ref = weave.publish(stylesheet, name=name + ".stylesheet")
    else:
        stylesheet_ref = stylesheet

    poml(prompt_ref, context_ref, stylesheet_ref)



================================================
FILE: python/tests/test_basic.py
================================================
import os
import subprocess
import sys
import re
from pathlib import Path
import multiprocessing

from poml import poml, Prompt, set_trace, clear_trace, get_trace, trace_artifact


def test_basic():
    assert poml("<p>Hello, World!</p>") == [{"speaker": "human", "content": "Hello, World!"}]


def test_prompt():
    with Prompt() as p:
        with p.task(caption="My Task"):
            p.text("This is a task description.")
            with p.paragraph():
                with p.header():
                    p.text("Subheading")
                p.text("This is a paragraph in the document.")

        xml_output = p.dump_xml()
        assert xml_output == (
            """<Task caption="My Task">This is a task description.<Paragraph>
    <Header>Subheading</Header>This is a paragraph in the document.</Paragraph>
</Task>"""
        )
        prompt_output = p.render()
        assert prompt_output == [
            {
                "speaker": "human",
                "content": "# My Task\n\nThis is a task description.\n\n## Subheading\n\nThis is a paragraph in the document.",
            }
        ]


def test_document():
    with open(Path(__file__).parent / "assets" / "pdf_latex_image.pdf", "rb") as f:
        pdf_contents = f.read()
    with Prompt() as p:
        with p.document(buffer=pdf_contents, parser="pdf"):
            p.text("This is a PDF document.")
        xml_output = p.dump_xml()
        assert "<Document" in xml_output
        assert "base64=" in xml_output

        result = p.render()
        assert isinstance(result, list)
        assert "Lorem ipsum" in result[0]["content"]


def test_prompt_reuse_appendable():
    """Ensure a Prompt instance can be reused across multiple context blocks."""

    prompt = Prompt()

    with prompt:
        with prompt.role():
            prompt.text("You are helpful.")
        with prompt.task(caption="First"):
            prompt.text("Describe A.")

    # Results should be available outside the context
    first_xml = prompt.dump_xml()
    assert first_xml.count("<Task") == 1
    first_render = prompt.render()
    assert "Describe A." in first_render[0]["content"]

    # Re-enter the context and append more content
    with prompt:
        with prompt.task(caption="Second"):
            prompt.text("Describe B.")

    second_xml = prompt.dump_xml()
    # Both tasks should be present
    assert second_xml.count("<Task") == 2
    second_render = prompt.render()
    assert "Describe A." in second_render[0]["content"]
    assert "Describe B." in second_render[0]["content"]


def test_trace():
    clear_trace()
    set_trace(True)
    result = poml("<p>Trace Me</p>")
    traces = get_trace()
    set_trace(False)
    assert result == [{"speaker": "human", "content": "Trace Me"}]
    assert len(traces) == 1
    assert "Trace Me" in traces[0]["markup"]


def test_trace_directory(tmp_path: Path):
    clear_trace()
    run_dir = set_trace(True, trace_dir=tmp_path)
    assert run_dir is not None
    result = poml("<p>Dir</p>")
    set_trace(False)
    assert result == [{"speaker": "human", "content": "Dir"}]
    files = list(run_dir.glob("*.poml"))
    assert len(files) == 2


def test_trace_artifact(tmp_path: Path):
    clear_trace()
    run_dir = set_trace(trace_dir=tmp_path)
    poml("<p>A</p>")
    trace_artifact("reply.txt", "hello")
    set_trace(False)
    artifacts = list(run_dir.glob("*.reply.txt"))
    assert len(artifacts) == 1
    assert artifacts[0].read_text().strip() == "hello"


def test_trace_prefix_regex(tmp_path: Path):
    clear_trace()
    run_dir = set_trace(True, trace_dir=tmp_path)
    src = tmp_path / "my.file.poml"
    src.write_text("<p>B</p>")
    poml(src)
    trace_artifact("custom.txt", "bye")
    set_trace(False)
    artifact = run_dir / "0001.my.file.custom.txt"
    assert artifact.exists()


def test_trace_directory_name_format(tmp_path: Path):
    clear_trace()
    run_dir = set_trace(trace_dir=tmp_path)
    assert run_dir is not None
    assert re.fullmatch(r"\d{20}", run_dir.name)
    set_trace(False)


def _mp_worker():
    poml("<p>MP</p>")


def test_multiprocessing_trace(tmp_path: Path):
    clear_trace()
    run_dir = set_trace(True, trace_dir=tmp_path)
    os.environ["POML_TRACE"] = str(run_dir)
    procs = [multiprocessing.Process(target=_mp_worker) for _ in range(3)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    set_trace(False)
    os.environ.pop("POML_TRACE", None)
    assert len(list(run_dir.glob("*.poml"))) == 6


def test_envvar_autotrace(tmp_path: Path):
    env = os.environ.copy()
    trace_dir = tmp_path / "run"
    env["POML_TRACE"] = str(trace_dir)
    script = "from poml import poml; poml('<p>E</p>')"
    subprocess.check_call([sys.executable, "-c", script], env=env)
    assert any(f.name.endswith(".poml") for f in trace_dir.iterdir())



================================================
FILE: python/tests/test_examples.py
================================================
import re
import poml
import json
import pytest
import sys
from pathlib import Path
from typing import Any, TypedDict

example_directory = Path(__file__).parent.parent.parent / "examples"


class Message(TypedDict):
    speaker: str
    contents: list[str]


def parse_expects(expect_file: Path) -> list[Message]:
    content = expect_file.read_text().replace("\r\n", "\n")

    # Split by speaker headers (===== speaker =====)
    sections = re.split(r"===== (\w+) =====\n\n", content)

    messages = []

    # Process sections in pairs (speaker, content)
    for i in range(1, len(sections), 2):
        if i + 1 < len(sections):
            speaker = sections[i]
            raw_content = sections[i + 1].replace("\r\n", "\n").strip("\n")

            # Parse content for mixed text and images
            contents = []

            # Find all JSON image objects first
            image_pattern = r'\{"type":"[^"]+","base64":"[^\n"]+?(\n|$)'

            # Split content while keeping track of positions
            last_end = 0
            for match in re.finditer(image_pattern, raw_content):
                # Add text before this image (if any)
                text_before = raw_content[last_end : match.start()].replace("\r\n", "\n").strip("\n")
                if text_before:
                    contents.append(text_before)

                # Add image (first 50 chars of base64)
                try:
                    img_data = json.loads(match.group())
                    base64_content = img_data.get("base64", "")
                    prefix = base64_content[:50]
                    contents.append(prefix)
                except json.JSONDecodeError:
                    # Fallback: extract base64 with regex
                    base64_match = re.search(r'"base64":"([^"\.]+)', match.group())
                    if base64_match:
                        prefix = base64_match.group(1)[:50]
                        contents.append(prefix)

                last_end = match.end()

            # Add any remaining text after the last image
            remaining_text = raw_content[last_end:].replace("\r\n", "\n").strip("\n")
            if remaining_text:
                contents.append(remaining_text)

            messages.append({"speaker": speaker, "contents": contents})

    return messages


def _diff(expected: list[Message], actual: Any) -> str:
    if not isinstance(actual, list):
        return f"Expected a list of messages, got {type(actual).__name__}"
    if len(expected) != len(actual):
        return f"Expected {len(expected)} messages, got {len(actual)}"

    for i, (exp, act) in enumerate(zip(expected, actual)):
        if not isinstance(act, dict):
            return f"Message {i} is not a dict: {type(act).__name__}"
        if exp["speaker"] != act.get("speaker"):
            return f"Message {i} speaker mismatch: expected '{exp['speaker']}', got '{act.get('speaker')}'"
        if "content" not in act:
            return f"Message {i} missing 'content' key"
        if isinstance(act["content"], str):
            if len(exp["contents"]) != 1 or exp["contents"][0] != act["content"].replace("\r\n", "\n").strip("\n"):
                return f"Message {i} contents mismatch: expected {exp['contents']}, got {repr(act['content'])}"
            continue
        if not isinstance(act["content"], list):
            return f"Message {i} contents is not a list: {type(act['content']).__name__}"
        if len(exp["contents"]) != len(act.get("content", [])):
            return f"Message {i} content length mismatch: expected {len(exp['contents'])}, got {len(act.get('content', []))}"
        for j, (exp_content, act_content) in enumerate(zip(exp["contents"], act.get("content", []))):
            if isinstance(act_content, str) and exp_content == act_content.replace("\r\n", "\n").strip("\n"):
                continue
            if isinstance(act_content, dict):
                if "base64" in act_content and act_content["base64"].startswith(exp_content):
                    continue
            return f"Message {i} content {j} mismatch: expected '{exp_content}', got '{act_content}'"
    return ""


def list_example_files():
    """
    Test that all example files can be processed without errors.
    """
    return list(sorted(example_directory.glob("*.poml")))


@pytest.mark.parametrize("example_file", list_example_files())
def test_example_file(example_file):
    """
    Test that a specific example file can be processed without errors.
    """
    # FIXME: Skip 301_generate_poml on Windows due to CRLF handling issue
    if sys.platform.startswith("win") and example_file.name == "301_generate_poml.poml":
        pytest.skip("Skip 301_generate_poml on Windows due to CRLF handling issue in txt files")

    result = poml.poml(example_file)
    expect_file = example_directory / "expects" / (example_file.stem + ".txt")
    if not expect_file.exists():
        raise FileNotFoundError(f"Expected output file not found: {expect_file}")

    # Parse the expected output
    expected_messages = parse_expects(expect_file)
    diff = _diff(expected_messages, result)
    if diff:
        raise AssertionError(f"Example {example_file.name} failed:\n{diff}")



================================================
FILE: python/tests/test_poml_formats.py
================================================
import base64
from pathlib import Path

import poml
from poml.api import PomlMessage, ContentMultiMedia


PNG_DATA = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
)
BASE64_PREFIX = PNG_DATA[:28]


def _create_image(tmp_path: Path) -> Path:
    img_path = tmp_path / "tiny.png"
    img_path.write_bytes(base64.b64decode(PNG_DATA))
    return img_path


def test_poml_format_dict(tmp_path: Path):
    img_path = _create_image(tmp_path)
    markup = f'<p>Image <img src="{img_path}" alt="tiny" syntax="multimedia"/></p>'
    result = poml.poml(markup, format="dict")
    assert result[0]["speaker"] == "human"
    assert result[0]["content"][0] == "Image "
    img = result[0]["content"][1]
    assert img["type"] == "image/png"
    assert img["alt"] == "tiny"
    assert img["base64"].startswith(BASE64_PREFIX)


def test_poml_format_pydantic(tmp_path: Path):
    img_path = _create_image(tmp_path)
    markup = f'<p>Image <img src="{img_path}" alt="tiny" syntax="multimedia"/></p>'
    result = poml.poml(markup, format="pydantic")
    msg = result[0]
    assert isinstance(msg, PomlMessage)
    assert msg.speaker == "human"
    assert msg.content[0] == "Image "
    image = msg.content[1]
    assert isinstance(image, ContentMultiMedia)
    assert image.type == "image/png"
    assert image.alt == "tiny"
    assert image.base64.startswith(BASE64_PREFIX)


def test_poml_format_openai_chat(tmp_path: Path):
    img_path = _create_image(tmp_path)
    markup = f'<p>Image <img src="{img_path}" alt="tiny" syntax="multimedia"/></p>'
    result = poml.poml(markup, format="openai_chat")
    msg = result[0]
    assert msg["role"] == "user"
    assert msg["content"][0] == {"type": "text", "text": "Image "}
    image = msg["content"][1]
    assert image["type"] == "image_url"
    url = image["image_url"]["url"]
    assert url.startswith("data:image/png;base64," + BASE64_PREFIX)


def test_poml_format_langchain(tmp_path: Path):
    img_path = _create_image(tmp_path)
    markup = f'<p>Image <img src="{img_path}" alt="tiny" syntax="multimedia"/></p>'
    result = poml.poml(markup, format="langchain")
    msg = result[0]
    assert msg["type"] == "human"
    first = msg["data"]["content"][0]
    assert first == {"type": "text", "text": "Image "}
    image = msg["data"]["content"][1]
    assert image["type"] == "image"
    assert image["source_type"] == "base64"
    assert image["mime_type"] == "image/png"
    assert image["data"].startswith(BASE64_PREFIX)



================================================
FILE: python/tests/manual/example_agentops_original.py
================================================
import os
from openai import OpenAI
import agentops

agentops.init()
client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": "Write a haiku about AI and humans working together"
    }]
)

print(response.choices[0].message.content)
agentops.end_session('Success')



================================================
FILE: python/tests/manual/example_agentops_poml.py
================================================
import os
from openai import OpenAI
import agentops
import poml

agentops.init()
client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

poml.set_trace("agentops", trace_dir="logs")
messages = poml.poml("example_poml.poml", context={"code_path": "example_agentops_original.py"}, format="openai_chat")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)

print(response.choices[0].message.content)
agentops.end_session('Success')



================================================
FILE: python/tests/manual/example_mlflow_langchain_poml.py
================================================
import mlflow
import os

import poml
from poml.integration.langchain import LangchainPomlTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

poml.set_trace("mlflow", trace_dir="logs")

# Enabling autolog for LangChain will enable trace logging.
mlflow.langchain.autolog()

# Optional: Set a tracking URI and an experiment
mlflow.set_experiment("LangChain")
mlflow.set_tracking_uri("http://localhost:5000")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"]
)

prompt_template = LangchainPomlTemplate.from_file("example_poml.poml")

chain = prompt_template | llm | StrOutputParser()

result = chain.invoke(
    {"code_path": "example_agentops_original.py"}
)
print(result)



================================================
FILE: python/tests/manual/example_mlflow_original.py
================================================
import mlflow
import os

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


# Enabling autolog for LangChain will enable trace logging.
mlflow.langchain.autolog()

# Optional: Set a tracking URI and an experiment
mlflow.set_experiment("LangChain")
mlflow.set_tracking_uri("http://localhost:5000")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"]
)

prompt_template = PromptTemplate.from_template(
    "Answer the question as if you are {person}, fully embodying their style, wit, personality, and habits of speech. "
    "Emulate their quirks and mannerisms to the best of your ability, embracing their traits—even if they aren't entirely "
    "constructive or inoffensive. The question is: {question}"
)

chain = prompt_template | llm | StrOutputParser()

# Let's test another call
chain.invoke(
    {
        "person": "Linus Torvalds",
        "question": "Can I just set everyone's access to sudo to make things easier?",
    }
)



================================================
FILE: python/tests/manual/example_mlflow_poml.py
================================================
import mlflow
import mlflow.openai
import openai
from openai import OpenAI
import os
import poml

# Set up MLflow experiment
mlflow.set_experiment("openai-tracing-quickstart")

# Enable automatic tracing for all OpenAI API calls
mlflow.openai.autolog()

poml.set_trace("mlflow", trace_dir="logs")

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

messages = poml.poml("example_poml.poml", context={"code_path": "example_agentops_original.py"}, format="openai_chat")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.7,
)
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    temperature=0.7,
)
print(response)



================================================
FILE: python/tests/manual/example_poml.poml
================================================
<poml>
  <task>You are a senior Python developer. Please explain the code.</task>
  <code inline="false">
  <document src="{{ code_path }}" parser="txt" />
  </code>
</poml>


================================================
FILE: python/tests/manual/example_weave_original.py
================================================
import weave
import os
from openai import OpenAI

weave.init("intro-example")

prompt = weave.MessagesPrompt(
    [
        {
            "role": "system",
            "content": "You will be provided with a description of a scene and your task is to provide a single word that best describes an associated emotion.",
        },
        {"role": "user", "content": "{scene}"},
    ]
)
weave.publish(prompt, name="emotion_prompt")

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=prompt.format(scene="A dog is lying on a dock next to a fisherman."),
)



================================================
FILE: python/tests/manual/example_weave_poml.py
================================================
import os
import poml
import weave
from openai import OpenAI

weave.init("intro-example")
poml.set_trace("weave", trace_dir="logs")
messages = poml.poml("example_poml.poml", context={"code_path": "example_weave_original.py"}, format="openai_chat")

client = OpenAI(
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)



================================================
FILE: .github/workflows/check-version.yml
================================================
name: Check Version

on:
  workflow_call:
    outputs:
      version:
        description: "The version from the project files"
        value: ${{ jobs.check-version.outputs.version }}
      tag_version:
        description: "The version from the git tag"
        value: ${{ jobs.check-version.outputs.tag_version }}
      npm_version:
        description: "The version from package.json"
        value: ${{ jobs.check-version.outputs.npm_version }}
      pypi_version:
        description: "The version from pyproject.toml"
        value: ${{ jobs.check-version.outputs.pypi_version }}

jobs:
  check-version:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      version: ${{ steps.get_version.outputs.version }}
      tag_version: ${{ steps.get_tag.outputs.tag_version }}
      npm_version: ${{ steps.get_npm_version.outputs.npm_version }}
      pypi_version: ${{ steps.get_pypi_version.outputs.pypi_version }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Get version from pyproject.toml
        id: get_pypi_version
        run: |
          PYPI_VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
          echo "pypi_version=$PYPI_VERSION" >> $GITHUB_OUTPUT
          echo "PyPI version: $PYPI_VERSION"

      - name: Get version from package.json
        id: get_npm_version
        run: |
          NPM_VERSION=$(node -p "require('./packages/poml-build/package.json').version")
          echo "npm_version=$NPM_VERSION" >> $GITHUB_OUTPUT
          echo "NPM version: $NPM_VERSION"

      - name: Set primary version
        id: get_version
        run: |
          # Use pyproject.toml version as the primary version
          VERSION=${{ steps.get_pypi_version.outputs.pypi_version }}
          echo "version=$VERSION" >> $GITHUB_OUTPUT
          echo "Primary version: $VERSION"

      - name: Get tag version
        id: get_tag
        run: |
          if [[ "${{ github.ref }}" == refs/tags/* ]]; then
            TAG_VERSION=${GITHUB_REF#refs/tags/v}
          else
            # For workflow_dispatch, use the primary version
            TAG_VERSION=${{ steps.get_version.outputs.version }}
            echo "Warning: Not triggered by tag, using project version for testing"
          fi
          echo "tag_version=$TAG_VERSION" >> $GITHUB_OUTPUT
          echo "Tag version: $TAG_VERSION"

      - name: Verify versions are in sync
        run: |
          NPM_VERSION=${{ steps.get_npm_version.outputs.npm_version }}
          PYPI_VERSION=${{ steps.get_pypi_version.outputs.pypi_version }}
          
          echo "Comparing versions:"
          echo "  NPM (package.json): $NPM_VERSION"
          echo "  PyPI (pyproject.toml): $PYPI_VERSION"
          
          if [ "$NPM_VERSION" != "$PYPI_VERSION" ]; then
            echo "Error: Version mismatch between package.json ($NPM_VERSION) and pyproject.toml ($PYPI_VERSION)"
            exit 1
          fi
          
          echo "✅ All project versions are synchronized"

      - name: Verify version matches tag
        run: |
          if [[ "${{ github.ref }}" == refs/tags/* ]]; then
            PRIMARY_VERSION=${{ steps.get_version.outputs.version }}
            TAG_VERSION=${{ steps.get_tag.outputs.tag_version }}
            
            if [ "$PRIMARY_VERSION" != "$TAG_VERSION" ]; then
              echo "Error: Primary version ($PRIMARY_VERSION) does not match tag ($TAG_VERSION)"
              exit 1
            fi
            echo "✅ Version check passed!"
          else
            echo "Skipping version check for workflow_dispatch"
          fi



================================================
FILE: .github/workflows/docs.yml
================================================
name: Deploy Documentation

on:
  push:
    branches:
      - main
    tags:
      - 'v*'
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

concurrency:
  group: 'pages'
  cancel-in-progress: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for versioning

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Node dependencies
        run: npm ci

      - name: Build cli
        run: npm run build-cli

      - name: Install Python dependencies
        run: |
          pip install -e ".[dev]"  # Install poml with dev dependencies

      - name: Generate component documentation
        run: npm run generate-component-spec

      - name: Generate TypeScript API documentation
        run: npm run typedoc

      - name: Configure Git for Mike
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"

      - name: Get version from package.json
        id: version
        run: |
          VERSION=$(node -p "require('./package.json').version")
          echo "VERSION=$VERSION" >> $GITHUB_OUTPUT
          echo "Documentation version: $VERSION"

      - name: Deploy documentation with Mike
        run: |
          if [[ "${{ github.ref }}" == refs/tags/v* ]]; then
            # Tagged release - deploy as versioned docs
            VERSION="${{ steps.version.outputs.VERSION }}"
            mike deploy --push --update-aliases $VERSION stable
          elif [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            # Main branch - deploy as latest docs
            mike deploy --push latest
            mike set-default --push latest
          fi



================================================
FILE: .github/workflows/models.yml
================================================
name: Use GitHub Models
on:
  workflow_dispatch:

permissions:
  models: read  # allow calling the Models inference API

jobs:
  call-llm:
    runs-on: ubuntu-latest
    steps:
      - name: Ask a model
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          curl -sS https://models.github.ai/inference/chat/completions \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $GITHUB_TOKEN" \
            -d '{
              "model": "openai/gpt-5",
              "messages": [
                {"role": "system", "content": "You are a concise assistant."},
                {"role": "user", "content": "Explain recursion in 2 sentences."}
              ],
              "max_tokens": 300
            }'


================================================
FILE: .github/workflows/publish-npm.yml
================================================
name: NPM Release

on:
  push:
    tags:
      - 'v*'  # Trigger on version tags like v1.0.0, v1.2.3, etc.
  schedule:
    # Run daily at 10:00 PM UTC for nightly builds
    - cron: '0 22 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  check-version:
    if: startsWith(github.ref, 'refs/tags/')
    uses: ./.github/workflows/check-version.yml

  publish-npm:
    needs: [check-version]
    if: always() && (needs.check-version.result == 'success' || needs.check-version.result == 'skipped')
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write

    steps:
      - uses: actions/checkout@v4

      - name: Determine build type
        id: build_type
        shell: bash
        run: |
          set -ex
          if [[ "${{ github.event_name }}" == "schedule" ]] || ([[ "${{ github.event_name }}" == "workflow_dispatch" ]] && [[ ! "${{ github.ref }}" =~ ^refs/tags/ ]]); then
            echo "type=nightly" >> $GITHUB_OUTPUT
            echo "Build type: nightly"
          else
            echo "type=production" >> $GITHUB_OUTPUT
            echo "Build type: production"
          fi

      - name: Use Node.js 22.x
        uses: actions/setup-node@v4
        with:
          node-version: 22.x
          registry-url: 'https://registry.npmjs.org'
          cache: 'npm'
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

      - name: Get current version
        id: get_version
        shell: bash
        run: |
          VERSION=$(node -p "require('./packages/poml-build/package.json').version")
          echo "version=$VERSION" >> $GITHUB_OUTPUT
          echo "Current version: $VERSION"

      - name: Create nightly version
        if: steps.build_type.outputs.type == 'nightly'
        id: create_nightly
        shell: bash
        run: |
          # Create a nightly version with timestamp
          TIMESTAMP=$(date +%Y%m%d%H%M)
          node bump-version.js ${{ steps.get_version.outputs.version }} "$TIMESTAMP"

          NIGHTLY_VERSION=$(node -p "require('./packages/poml-build/package.json').version")
          echo "Nightly version: $NIGHTLY_VERSION"
          echo "nightly_version=$NIGHTLY_VERSION" >> $GITHUB_OUTPUT

      - name: Install dependencies
        run: npm ci

      - name: Build webview and CLI
        run: |
          npm run build-webview
          npm run build-cli

      - name: Build NPM package
        run: |
          cd packages/poml-build
          npm pack
          ls -la *.tgz

      - name: Upload package artifact
        uses: actions/upload-artifact@v4
        with:
          name: npm-package-${{ github.event_name }}
          path: packages/poml-build/*.tgz
          compression-level: 0

      - name: Publish to npm (nightly)
        if: steps.build_type.outputs.type == 'nightly'
        run: |
          cd packages/poml-build
          npm publish --provenance --access public --tag nightly

      - name: Publish to npm (production)
        if: steps.build_type.outputs.type == 'production'
        run: |
          cd packages/poml-build
          npm publish --provenance --access public

      - name: Verify nightly publication
        if: steps.build_type.outputs.type == 'nightly'
        run: |
          # Wait a bit for the package to be available
          sleep 30
          npm view pomljs@${{ steps.create_nightly.outputs.nightly_version }}
          echo "✅ Nightly package successfully published to npm registry!"

      - name: Verify production publication
        if: steps.build_type.outputs.type == 'production'
        run: |
          # Wait a bit for the package to be available
          sleep 30
          npm view pomljs@${{ needs.check-version.outputs.npm_version }}
          echo "✅ Package successfully published to npm!"



================================================
FILE: .github/workflows/publish-pypi.yml
================================================
name: PyPI Release

on:
  push:
    tags:
      - 'v*'  # Trigger on version tags like v1.0.0, v1.2.3, etc.
  schedule:
    # Run daily at 10:00 PM UTC for nightly builds
    - cron: '0 22 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  check-version:
    if: startsWith(github.ref, 'refs/tags/')
    uses: ./.github/workflows/check-version.yml

  generate-timestamp:
    runs-on: ubuntu-latest
    outputs:
      timestamp: ${{ steps.timestamp.outputs.value }}
      build_type: ${{ steps.build_type.outputs.type }}
    steps:
      - name: Determine build type
        id: build_type
        shell: bash
        run: |
          if [[ "${{ github.event_name }}" == "schedule" ]] || ([[ "${{ github.event_name }}" == "workflow_dispatch" ]] && [[ ! "${{ github.ref }}" =~ ^refs/tags/ ]]); then
            echo "type=nightly" >> $GITHUB_OUTPUT
            echo "Build type: nightly"
          else
            echo "type=production" >> $GITHUB_OUTPUT
            echo "Build type: production"
          fi
      
      - name: Generate timestamp
        id: timestamp
        shell: bash
        run: |
          TIMESTAMP=$(date +%Y%m%d%H%M)
          echo "value=$TIMESTAMP" >> $GITHUB_OUTPUT
          echo "Generated timestamp: $TIMESTAMP"

  publish-to-pypi:
    needs: [check-version, generate-timestamp]
    if: always() && (needs.check-version.result == 'success' || needs.check-version.result == 'skipped')
    strategy:
      matrix:
        include:
          - os: ubuntu-latest
            wheel_platform: manylinux_2_17_x86_64
          - os: ubuntu-24.04-arm
            wheel_platform: manylinux_2_17_aarch64
          - os: windows-latest
            wheel_platform: win_amd64
          - os: macos-13
            wheel_platform: macosx_10_9_x86_64
          - os: macos-latest
            wheel_platform: macosx_11_0_arm64
      fail-fast: false

    runs-on: ${{ matrix.os }}
    permissions:
      id-token: write  # IMPORTANT: this permission is mandatory for trusted publishing
      contents: read

    steps:
      - uses: actions/checkout@v4
      
      - name: Use Node.js 22.x
        uses: actions/setup-node@v4
        with:
          node-version: 22.x
          cache: 'npm'
      - name: Use Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: npm ci
      - run: npm run build-webview
      - run: npm run build-cli
      - run: python -m pip install -e .[dev]

      - name: Get current version
        id: get_version
        shell: bash
        run: |
          VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
          echo "version=$VERSION" >> $GITHUB_OUTPUT
          echo "Current version: $VERSION"

      - name: Create development version
        if: needs.generate-timestamp.outputs.build_type == 'nightly'
        id: create_nightly
        shell: bash
        run: |
          # Create a dev version with shared timestamp
          TIMESTAMP=${{ needs.generate-timestamp.outputs.timestamp }}
          echo "Using shared timestamp: $TIMESTAMP"
          node bump-version.js ${{ steps.get_version.outputs.version }} "$TIMESTAMP"
          NIGHTLY_VERSION=$(python -c "import poml; print(poml.__version__)")
          echo "Nightly version: $NIGHTLY_VERSION"
          echo "nightly_version=$NIGHTLY_VERSION" >> $GITHUB_OUTPUT

      - name: Build package
        run: hatch build -t wheel

      - name: Verify package contents
        shell: bash
        run: |
          python -m zipfile -l dist/*.whl

      - name: Rename wheel for platform
        id: rename-wheel
        shell: bash
        run: |
          WHEEL_FILE=$(find dist -name "*.whl" -type f | head -1)
          if [ -z "$WHEEL_FILE" ]; then
            echo "No wheel file found!"
            exit 1
          fi
          echo "Original wheel: $WHEEL_FILE"
          
          # Parse the original wheel filename to extract components
          WHEEL_NAME=$(basename "$WHEEL_FILE" .whl)
          
          # Split wheel name into components: name-version-python_tag-abi_tag-platform_tag
          IFS='-' read -ra PARTS <<< "$WHEEL_NAME"
          
          if [ ${#PARTS[@]} -ge 5 ]; then
            DIST_NAME="${PARTS[0]}"
            VERSION="${PARTS[1]}"
            PYTHON_TAG="${PARTS[2]}"
            ABI_TAG="${PARTS[3]}"
            # Join remaining parts as platform tag
            PLATFORM_TAG=$(IFS='-'; echo "${PARTS[*]:4}")
          else
            echo "Warning: Unexpected wheel filename format: $WHEEL_NAME"
            exit 1
          fi
          
          # Create platform-specific wheel name
          PLATFORM_WHEEL="${DIST_NAME}-${VERSION}-${PYTHON_TAG}-${ABI_TAG}-${{ matrix.wheel_platform }}.whl"
          echo "Platform-specific wheel: $PLATFORM_WHEEL"
          
          # Rename the wheel file
          mv "$WHEEL_FILE" "dist/$PLATFORM_WHEEL"
          echo "wheel-file=dist/$PLATFORM_WHEEL" >> $GITHUB_OUTPUT

      - name: Upload wheel artifact
        uses: actions/upload-artifact@v4
        with:
          name: wheel-${{ matrix.wheel_platform }}-${{ github.event_name }}
          path: ${{ steps.rename-wheel.outputs.wheel-file }}
          compression-level: 0

      - name: Publish to Test PyPI (nightly)
        if: needs.generate-timestamp.outputs.build_type == 'nightly'
        run: |
          twine upload --non-interactive --repository testpypi dist/*.whl

      - name: Publish to PyPI (production)
        if: needs.generate-timestamp.outputs.build_type == 'production'
        run: |
          twine upload --non-interactive dist/*.whl

      - name: Test installation from Test PyPI (nightly)
        if: needs.generate-timestamp.outputs.build_type == 'nightly'
        shell: bash
        run: |
          pip uninstall -y poml
          # Retry installation up to 5 times with 60-second delays
          for i in {1..5}; do
            echo "Attempt $i/5: Waiting 60 seconds for package to be available..."
            sleep 60
            if pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ poml==${{ steps.create_nightly.outputs.nightly_version }}; then
              python -c "import poml; print('Nightly package installed successfully from Test PyPI')"
              exit 0
            else
              echo "Installation attempt $i failed"
              if [ $i -eq 5 ]; then
                echo "All 5 installation attempts failed"
                exit 1
              fi
            fi
          done

      - name: Test installation from PyPI (production)
        if: needs.generate-timestamp.outputs.build_type == 'production'
        shell: bash
        run: |
          pip uninstall -y poml
          # Retry installation up to 5 times with 60-second delays
          for i in {1..5}; do
            echo "Attempt $i/5: Waiting 60 seconds for package to be available..."
            sleep 60
            if pip install poml==${{ needs.check-version.outputs.pypi_version }}; then
              python -c "import poml; print('Package installed successfully from PyPI')"
              exit 0
            else
              echo "Installation attempt $i failed"
              if [ $i -eq 5 ]; then
                echo "All 5 installation attempts failed"
                exit 1
              fi
            fi
          done



================================================
FILE: .github/workflows/publish-vscode.yml
================================================
name: VSCode Extension Release

on:
  push:
    tags:
      - 'v*'  # Trigger on version tags like v1.0.0, v1.2.3, etc.
  schedule:
    # Run daily at 10:00 PM UTC for nightly builds
    - cron: '0 22 * * *'
  workflow_dispatch:  # Allow manual trigger

jobs:
  check-version:
    if: startsWith(github.ref, 'refs/tags/')
    uses: ./.github/workflows/check-version.yml

  generate-timestamp:
    runs-on: ubuntu-latest
    outputs:
      timestamp: ${{ steps.timestamp.outputs.value }}
      build_type: ${{ steps.build_type.outputs.type }}
    steps:
      - name: Determine build type
        id: build_type
        shell: bash
        run: |
          if [[ "${{ github.event_name }}" == "schedule" ]] || ([[ "${{ github.event_name }}" == "workflow_dispatch" ]] && [[ ! "${{ github.ref }}" =~ ^refs/tags/ ]]); then
            echo "type=nightly" >> $GITHUB_OUTPUT
            echo "Build type: nightly"
          else
            echo "type=production" >> $GITHUB_OUTPUT
            echo "Build type: production"
          fi
      
      - name: Generate timestamp
        id: timestamp
        shell: bash
        run: |
          TIMESTAMP=$(date +%Y%m%d%H%M)
          echo "value=$TIMESTAMP" >> $GITHUB_OUTPUT
          echo "Generated timestamp: $TIMESTAMP"

  build:
    needs: [check-version, generate-timestamp]
    if: always() && (needs.check-version.result == 'success' || needs.check-version.result == 'skipped')
    strategy:
      matrix:
        include:
          - os: ubuntu-latest
            platform: linux-x64
          - os: ubuntu-24.04-arm
            platform: linux-arm64
          - os: windows-latest
            platform: win32-x64
          - os: macos-13
            platform: darwin-x64
          - os: macos-latest
            platform: darwin-arm64
      fail-fast: false

    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v4
    
    - name: Use Node.js 22.x
      uses: actions/setup-node@v4
      with:
        node-version: 22.x
        cache: 'npm'
    - name: Use Python 3.12
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"
    - run: npm ci
    - run: npm run build-webview
    - run: npm run build-cli

    - name: Get current version
      id: get_version
      shell: bash
      run: |
        VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
        echo "version=$VERSION" >> $GITHUB_OUTPUT
        echo "Current version: $VERSION"

    - name: Create development version
      if: needs.generate-timestamp.outputs.build_type == 'nightly'
      shell: bash
      run: |
        # Create a dev version with shared timestamp
        TIMESTAMP=${{ needs.generate-timestamp.outputs.timestamp }}
        echo "Using shared timestamp: $TIMESTAMP"
        node bump-version.js ${{ steps.get_version.outputs.version }} "$TIMESTAMP"
    
    - name: Package VSCode Extension for Windows
      if: matrix.platform == 'win32-x64'
      run: npm run package:win
    - name: Package VSCode Extension for ${{ matrix.platform }}
      if: matrix.platform != 'win32-x64'
      run: npm run package -- --target ${{ matrix.platform }}
    
    # Find and prepare VSIX file
    - name: Find VSIX file
      id: find-vsix
      shell: bash
      run: |
        VSIX_FILE=$(find . -name "*.vsix" -type f | head -1)
        if [ -z "$VSIX_FILE" ]; then
          echo "No VSIX file found!"
          exit 1
        fi
        echo "vsix-file=$VSIX_FILE" >> $GITHUB_OUTPUT
        # Extract base name and create platform-specific name
        BASE_NAME=$(basename "$VSIX_FILE" .vsix)
        PLATFORM_VSIX="${BASE_NAME}.vsix"
        echo "platform-vsix-name=$PLATFORM_VSIX" >> $GITHUB_OUTPUT
        # Copy to platform-specific name (commented out because they are the same)
        # cp "$VSIX_FILE" "$PLATFORM_VSIX"
        echo "platform-vsix-file=$PLATFORM_VSIX" >> $GITHUB_OUTPUT
        
        # For nightly builds, also create latest versioned file
        if [[ "${{ needs.generate-timestamp.outputs.build_type }}" == "nightly" ]]; then
          PLATFORM_LATEST_VSIX="poml-${{ matrix.platform }}-latest.vsix"
          echo "platform-latest-vsix-name=$PLATFORM_LATEST_VSIX" >> $GITHUB_OUTPUT
          cp "$VSIX_FILE" "$PLATFORM_LATEST_VSIX"
          echo "platform-latest-vsix-file=$PLATFORM_LATEST_VSIX" >> $GITHUB_OUTPUT
        fi
    
    # Upload VSIX files as artifacts
    - name: Upload VSIX for ${{ matrix.platform }}
      uses: actions/upload-artifact@v4
      with:
        name: ${{ steps.find-vsix.outputs.platform-vsix-name }}
        path: ${{ steps.find-vsix.outputs.platform-vsix-file }}
        compression-level: 0
    
    # Upload nightly builds to Cloudflare R2
    - name: Upload VSIX to Cloudflare R2 (nightly)
      if: needs.generate-timestamp.outputs.build_type == 'nightly'
      shell: bash
      run: |
        set -ex
        aws s3 cp "${{ steps.find-vsix.outputs.platform-vsix-file }}" \
          s3://poml/vscode/${{ steps.find-vsix.outputs.platform-vsix-name }} \
          --endpoint-url ${{ secrets.CLOUDFLARE_R2_ENDPOINT }}
        aws s3 cp "${{ steps.find-vsix.outputs.platform-latest-vsix-file }}" \
          s3://poml/vscode/${{ steps.find-vsix.outputs.platform-latest-vsix-name }} \
          --endpoint-url ${{ secrets.CLOUDFLARE_R2_ENDPOINT }}
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.CLOUDFLARE_R2_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.CLOUDFLARE_R2_SECRET_ACCESS_KEY }}
        AWS_DEFAULT_REGION: auto


================================================
FILE: .github/workflows/publish.yml
================================================
name: VSCode Extension Package

on:
  workflow_dispatch:

jobs:
  build:
    strategy:
      matrix:
        include:
          - os: ubuntu-latest
            platform: linux-x64
            wheel_platform: manylinux_2_17_x86_64
          - os: ubuntu-24.04-arm
            platform: linux-arm64
            wheel_platform: manylinux_2_17_aarch64
          - os: windows-latest
            platform: win32-x64
            wheel_platform: win_amd64
          - os: macos-13
            platform: darwin-x64
            wheel_platform: macosx_10_9_x86_64
          - os: macos-latest
            platform: darwin-arm64
            wheel_platform: macosx_11_0_arm64

    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v4
    - name: Use Node.js 22.x
      uses: actions/setup-node@v4
      with:
        node-version: 22.x
        cache: 'npm'
    - name: Use Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"
    - run: npm ci
    - run: npm run build-webview
    - run: npm run build-cli
    - name: Package VSCode Extension for Windows
      if: matrix.platform == 'win32-x64'
      run: npm run package:win
    - name: Package VSCode Extension for ${{ matrix.platform }}
      if: matrix.platform != 'win32-x64'
      run: npm run package -- --target ${{ matrix.platform }}
    - run: python -m pip install -e .[dev]
    - run: hatch build -t wheel
    
    # Upload VSIX files individually (not as zip)
    - name: Find VSIX file
      id: find-vsix
      shell: bash
      run: |
        VSIX_FILE=$(find . -name "*.vsix" -type f | head -1)
        if [ -z "$VSIX_FILE" ]; then
          echo "No VSIX file found!"
          exit 1
        fi
        echo "vsix-file=$VSIX_FILE" >> $GITHUB_OUTPUT
        # Extract base name and create platform-specific name
        BASE_NAME=$(basename "$VSIX_FILE" .vsix)
        PLATFORM_VSIX="${BASE_NAME}.vsix"
        echo "platform-vsix-name=$PLATFORM_VSIX" >> $GITHUB_OUTPUT
    
    - name: Upload VSIX for ${{ matrix.platform }}
      uses: actions/upload-artifact@v4
      with:
        name: ${{ steps.find-vsix.outputs.platform-vsix-name }}
        path: ${{ steps.find-vsix.outputs.vsix-file }}
        compression-level: 0
    
    # Upload Python wheel files individually
    - name: Find and upload Python wheel
      shell: bash
      run: |
        WHEEL_FILE=$(find dist -name "*.whl" -type f | head -1)
        if [ -z "$WHEEL_FILE" ]; then
          echo "No wheel file found!"
          exit 1
        fi
        echo "wheel-file=$WHEEL_FILE" >> $GITHUB_OUTPUT
        
        # Parse the original wheel filename to extract components
        WHEEL_NAME=$(basename "$WHEEL_FILE" .whl)
        
        # Split wheel name into components: name-version-python_tag-abi_tag-platform_tag
        # Example: poml-999.0-py3-none-any -> poml, 999.0, py3, none, any
        IFS='-' read -ra PARTS <<< "$WHEEL_NAME"
        
        if [ ${#PARTS[@]} -ge 5 ]; then
          # Standard format: name-version-python_tag-abi_tag-platform_tag
          DIST_NAME="${PARTS[0]}"
          VERSION="${PARTS[1]}"
          PYTHON_TAG="${PARTS[2]}"
          ABI_TAG="${PARTS[3]}"
          # Join remaining parts as platform tag (in case there are extra hyphens)
          PLATFORM_TAG=$(IFS='-'; echo "${PARTS[*]:4}")
        else
          echo "Warning: Unexpected wheel filename format: $WHEEL_NAME"
          # Fallback to original naming
          echo "platform-wheel-name=$WHEEL_NAME-${{ matrix.platform }}.whl" >> $GITHUB_OUTPUT
          exit 0
        fi
        
        # Create platform-specific wheel name with proper platform tag
        PLATFORM_WHEEL="${DIST_NAME}-${VERSION}-${PYTHON_TAG}-${ABI_TAG}-${{ matrix.wheel_platform }}.whl"
        echo "platform-wheel-name=$PLATFORM_WHEEL" >> $GITHUB_OUTPUT
        
        # Rename the wheel file to platform-specific name
        cp "$WHEEL_FILE" "dist/$PLATFORM_WHEEL"
        echo "renamed-wheel-file=dist/$PLATFORM_WHEEL" >> $GITHUB_OUTPUT
      id: find-wheel
    
    - name: Upload Python wheel for ${{ matrix.platform }}
      uses: actions/upload-artifact@v4
      with:
        name: ${{ steps.find-wheel.outputs.platform-wheel-name }}
        path: ${{ steps.find-wheel.outputs.renamed-wheel-file }}
        compression-level: 0

    # Build and pack npm library only once
    - name: Pack NPM package
      if: matrix.os == 'ubuntu-latest'
      run: |
        cd packages/poml-build
        npm pack

    - name: Upload NPM package
      if: matrix.os == 'ubuntu-latest'
      uses: actions/upload-artifact@v4
      with:
        name: poml-npm-universal.tgz
        path: packages/poml-build/pomljs-*.tgz
        compression-level: 0



================================================
FILE: .github/workflows/test.yml
================================================
name: Full Test

on:
  schedule:
    - cron: '0 0 * * *'
  push:
    branches:
      - main
      - master
  pull_request:

  workflow_dispatch:

jobs:
  build:
    strategy:
      matrix:
        include:
          - os: ubuntu-latest
            platform: linux-x64
          - os: ubuntu-24.04-arm
            platform: linux-arm64
          - os: windows-latest
            platform: win32-x64
          - os: macos-13
            platform: darwin-x64
          - os: macos-latest
            platform: darwin-arm64
      fail-fast: false

    runs-on: ${{ matrix.os }}

    steps:
      - uses: actions/checkout@v4
      - name: Use Node.js 22.x
        uses: actions/setup-node@v4
        with:
          node-version: 22.x
          cache: 'npm'
      - name: Use Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: npm ci
      - run: npm run build-webview
      - run: npm run build-cli
      - run: npm run lint
      - run: npm run package:win
        if: matrix.platform == 'win32-x64'
      - run: npm run package -- --target ${{ matrix.platform }}
        if: matrix.platform != 'win32-x64'
      - run: python -m pip install -e .[dev]
      - run: xvfb-run -a npm test
        if: runner.os == 'Linux'
      - run: npm test
        if: runner.os != 'Linux'
      - run: python -m pytest -v python/tests
      - run: xvfb-run -a npm run compile && xvfb-run -a npm run test-vscode
        if: runner.os == 'Linux'
      - uses: nick-invision/retry@v3
        if: matrix.os == 'macos-13'
        with:
          max_attempts: 3
          timeout_minutes: 10
          command: npm run compile && npm run test-vscode
      - run: npm run compile && npm run test-vscode
        if: runner.os != 'Linux' && matrix.os != 'macos-13'

  docs:
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request' || (github.event_name == 'push' && github.ref == 'refs/heads/main')

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for versioning

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Node dependencies
        run: npm ci

      - name: Build cli
        run: npm run build-cli

      - name: Install Python dependencies
        run: pip install -e ".[dev]"

      - name: Generate component documentation
        run: npm run generate-component-spec

      - name: Generate TypeScript API documentation
        run: npm run typedoc

      - name: Build documentation
        run: mkdocs build

      - name: Upload documentation artifact
        uses: actions/upload-artifact@v4
        with:
          name: documentation-site
          path: site/


