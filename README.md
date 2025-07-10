# moje-codex-testy

This repository contains a minimal example for calling the OpenAI API with a simple tool. The `simple_llm_tool.py` script demonstrates how to register a function with the API and send its result back to the model. It targets the OpenAI Python client library version 1.0 and newer.

## Requirements
- Python 3.8+
- The `openai` Python package **version 1.0 or newer** (`pip install --upgrade openai`)
- An OpenAI API key exported as `OPENAI_API_KEY`

## Running the example
1. Install dependencies:
   ```bash
   pip install --upgrade openai
   ```
2. Export your API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```
3. Run the script:
   ```bash
   python simple_llm_tool.py
   ```

The script sends a question to GPT-3.5-turbo asking it to compute `2 + 3`. The model uses the provided `add_numbers` tool to perform the calculation and returns the final answer.
