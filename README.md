# boot-agent

**boot-agent** is an AI-powered coding agent that can perform various file and directory operations through natural language commands. It connects to OpenRouter API to use free LLMs and provides a set of tools for directory navigation, file reading, file writing, and Python execution.

## Project Structure

```
boot-agent/
├── calculator/              # Example calculator directory
│   ├── main.py              # Calculator application
│   ├── tests.py             # Test file
│   ├── pkg/                 # Package directory
│   │   ├── __pycache__/
│   │   └── calculator.py
│   ├── lorem.txt            # Sample text file
│   └── README.md
├── functions/               # Core function implementations
│   ├── get_file_content.py  # Read file content
│   ├── get_files_info.py    # List directory contents
│   ├── run_python_file.py   # Execute Python files
│   └── write_file.py        # Write content to files
├── .venv/                   # Python virtual environment
├── .gitignore               # Git ignore rules
├── pyproject.toml           # Project configuration
├── main.py                  # Main entry point / chatbot
├── prompts.py               # System prompt for the AI
├── config.py                # Configuration constants
├── call_function.py         # Function dispatcher
├── tests/                   # Test files
│   ├── test_get_file_content.py
│   ├── test_get_files_info.py
│   ├── test_run_python_file.py
│   └── test_write_file.py
├── .env                     # Environment variables (API keys)
└── README.md                # This file
```

## Features

- **List files and directories** - View directory contents with file sizes and type information
- **Read file content** - Read file contents with automatic truncation at character limits
- **Execute Python files** - Run Python scripts and capture stdout/stderr output
- **Write files** - Create or overwrite files within the permitted working directory
- **AI-powered tool selection** - LLM automatically selects appropriate tools for tasks
- **Directory containment** - All operations are restricted to the working directory for safety
- **Verbose output** - Optional detailed logging of operations

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/boot-agent.git
   cd boot-agent
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Or using uv:
   uv sync
   ```

4. **Set up environment variables**
   Copy `.env` and add your OpenRouter API key:
   ```bash
   cp .env.example .env  # if available
   # Or edit .env directly:
   export OPENROUTER_API_KEY='your-api-key-here'
   ```

## Usage

### Basic Usage

Run the main chatbot with a user prompt:

```bash
uv run main.py "Your request here"
```

Example:
```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

### Available Commands

The agent supports natural language requests that trigger these operations:

| Operation | Description | Example |
|-----------|-------------|---------|
| `list directory` | List files in a directory | "List files in calculator/pkg" |
| `read file` | Read file content | "Read calculator/main.py" |
| `execute python` | Run a Python file | "Execute calculator/main.py with args 3+5" |
| `write file` | Write content to a file | "Write 'Hello World' to calculator/new.txt" |

### Verbose Mode

Enable verbose output to see detailed information about prompt tokens and tool calls:

```bash
uv run main.py "--verbose" "Your request here"
```

### Working Directory

All operations are relative to the project root directory. The agent will prevent access to files outside the permitted working directory for security.

## Configuration

- **`pyproject.toml`** - Project metadata, name, version, dependencies, and Python version requirements
- **`config.py`** - Contains `MAX_CHARS` constant (currently 10,000) for file content truncation
- **`.env`** - Environment variables, specifically `OPENROUTER_API_KEY`

### Dependencies

- `openai==2.44.0` - OpenAI client library (used for OpenRouter API)
- `python-dotenv==1.1.0` - Environment variable loading

## Testing

Run the existing test suite:

```bash
python -m unittest discover -v
# Or with uv:
uv run pytest
```

Tests cover:
- `test_get_file_content.py` - File reading operations
- `test_get_files_info.py` - Directory listing operations  
- `test_run_python_file.py` - Python execution operations
- `test_write_file.py` - File writing operations

## Security

- All file operations are restricted to the working directory
- Attempting to access files outside the working directory returns an error
- Directory traversal (e.g., `../`) is blocked
- File type validation is performed (e.g., only `.py` files can be executed)

## License

This project is licensed under the MIT License.

## Acknowledgements

- Built with OpenRouter API access to free LLM models
- Inspired by AI coding agent patterns

## Test: 

- Manually update calculator/pkg/calculator.py and change the precedence of the + operator to 3.
- Run the calculator app, to make sure it's now producing incorrect results: 
```bash
uv run calculator/main.py "3 + 7 * 2" 
``` 
(this should be 17, but because we broke it, it will return 20).

- Run your agent and ask it, "Fix the bug: 3 + 7 * 2 shouldn't be 20." as:
    
```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```