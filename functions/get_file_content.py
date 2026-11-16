import os

from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    absolute_working_directory_path = os.path.abspath(working_directory)
    final_path = os.path.join(absolute_working_directory_path, file_path)
    final_path = os.path.normpath(final_path)

    if os.path.isfile(final_path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    valid_target_path = os.path.commonpath([absolute_working_directory_path, final_path]) == absolute_working_directory_path
    if valid_target_path == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


    with open(final_path, "r") as f:
        content = f.read(MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
    return content