# AgenticAI

A lightweight Python framework for building intelligent agents powered by LLMs (Large Language Models) using LangChain and Ollama.

## Features

- **Agent Framework**: Create intelligent agents with custom tools and capabilities
- **LangChain Integration**: Leverage the power of LangChain for agent creation and management
- **Ollama Support**: Run local LLMs using Ollama (e.g., `gpt-oss:120b-cloud`)
- **Custom Tools**: Easily extend agents with custom tools (built-in weather tool example)
- **Simple API**: Clean and intuitive interface for agent development

## Prerequisites

- **Python**: 3.13 or higher
- **Ollama**: Installed and running on your system (for LLM models)
  - Download: https://ollama.ai

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd agenticai
```

### 2. Install Dependencies

Using uv (fast and reliable):

```bash
uv pip install -r requirements.txt
```

### 3. Configure Ollama

Ensure Ollama is running on your system:

```bash
ollama run gpt-oss:120b-cloud
```

Or pull your preferred model:

```bash
ollama pull <model-name>
```

## Quick Start

### Running the Sample Agent

The project includes a sample agent that demonstrates weather querying:

```bash
python main.py
```

Or run the sample agent directly:

```bash
python src/agents/sample.py
```

### Example Output

```
Hello from agenticai!
```

## Project Structure

```
agenticai/
├── main.py                          # Entry point
├── pyproject.toml                   # Project configuration
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
└── src/
    ├── 01_class.py                  # Core classes and utilities
    ├── agents/
    │   ├── __init__.py
    │   ├── sample.py                # Sample agent implementation
    │   └── tools/
    │       ├── __init__.py
    │       └── weather.py           # Weather tool example
    │
    └── model/
        ├── __init__.py
        └── llm.py                   # LLM configuration (Ollama)
```

## Usage Guide

### Creating Your First Agent

1. **Define a Tool**

Create a new file in `src/agents/tools/`:

```python
def my_custom_tool(input: str) -> str:
    """Your custom tool implementation"""
    return f"Processing: {input}"
```

2. **Create an Agent**

```python
from langchain.agents import create_agent
from model.llm import llm
from agents.tools.your_tool import my_custom_tool

agent = create_agent(
    model=llm,
    tools=[my_custom_tool],
    system_prompt="You are a helpful assistant."
)

inputs = {"messages": [{"role": "user", "content": "Your question here"}]}
result = agent.invoke(inputs)
print(result)
```

3. **Run Your Agent**

```bash
python src/agents/your_agent.py
```

### Configuring the LLM

Edit `src/model/llm.py` to change the model or configuration:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="your-model-name",
    temperature=0.7,
    base_url="http://localhost:11434"
)
```

## Development

### Setting Up Development Environment

1. Install development dependencies:

```bash
uv pip install -r requirements.txt
```

2. Run the main application:

```bash
python main.py
```

### Running Tests

Tests can be added in a `tests/` directory:

```bash
uv run pytest tests/
```

## Available Tools

### Weather Tool (`src/agents/tools/weather.py`)

Example tool for demonstrating agent capabilities. Can be extended to fetch real weather data.

```python
from agents.tools.weather import check_weather

result = check_weather("New York")
```

## Configuration

Key configuration files:

- **`pyproject.toml`**: Python project metadata and dependencies
- **`requirements.txt`**: Direct pip dependencies
- **`src/model/llm.py`**: LLM model configuration

## Environment Variables

You can set environment variables to customize behavior:

```bash
# Set Ollama base URL (default: http://localhost:11434)
export OLLAMA_BASE_URL=http://localhost:11434
```

## Troubleshooting

### Ollama Connection Error

**Problem**: `Connection refused` when connecting to Ollama

**Solution**:
1. Ensure Ollama is running: `ollama serve`
2. Check Ollama is accessible at `http://localhost:11434`
3. Verify the model is downloaded: `ollama list`

### Model Not Found

**Problem**: `Model not found` error

**Solution**:
1. Download the model: `ollama pull gpt-oss:120b-cloud`
2. Update `src/model/llm.py` with correct model name

### Import Errors

**Problem**: `ModuleNotFoundError`

**Solution**:
1. Ensure you're in the project root directory
2. Reinstall dependencies: `uv pip install -r requirements.txt`
3. Verify Python version: `python --version` (must be 3.13+)

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test your code
4. Submit a pull request

## License

[Add your license here]

## Support

For issues, questions, or suggestions, please open an issue on the repository.

## Resources

- [LangChain Documentation](https://docs.langchain.com)
- [Ollama Documentation](https://ollama.ai)
- [Python 3.13 Documentation](https://docs.python.org/3.13/)
