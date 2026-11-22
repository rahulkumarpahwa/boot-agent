import os, subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    absolute_working_directory_path = os.path.abspath(working_directory)
    final_path = os.path.join(absolute_working_directory_path, file_path)
    final_path = os.path.normpath(final_path)
        
    if os.path.isfile(final_path) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if file_path.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file'
        
    valid_target_path = os.path.commonpath([absolute_working_directory_path, final_path]) == absolute_working_directory_path
    if valid_target_path == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    
    command = ["python", final_path]
    if args is not None:
        command.extend(args)
    
    completed_process = subprocess.run(command, capture_output=True, check=True, text=True, timeout=30)

    if completed_process.returncode != 0:
        return f"Error: Process exited with code {completed_process.returncode}"
    
    if completed_process.stderr != "":
        return f"STDERR: executing Python file: {completed_process.stderr}"
    
    if completed_process.stderr == "" and completed_process.stdout == "":
        return "No output produced"
    
    return f"STDOUT: {completed_process.stdout}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory and returns its stdout, stderr, or an error message",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional command-line arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}   