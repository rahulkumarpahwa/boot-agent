import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    absolute_working_directory_path = os.path.abspath(working_directory)
    final_path = os.path.join(absolute_working_directory_path, file_path)
    final_path = os.path.normpath(final_path)
    
    if os.path.isdir(final_path) == True:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    valid_target_path = os.path.commonpath([absolute_working_directory_path, final_path]) == absolute_working_directory_path
    if valid_target_path == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    os.makedirs(os.path.dirname(final_path), exist_ok=True)
    
    with open(final_path, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'