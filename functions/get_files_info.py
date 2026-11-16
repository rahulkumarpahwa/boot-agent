import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    if os.path.isdir(directory) == False:
        return f'Error: "{directory}" is not a directory'
    
    absolute_working_directory_path = os.path.abspath(working_directory)
    final_path = os.path.join(absolute_working_directory_path, directory)
    final_path = os.path.normpath(final_path)

    valid_target_path = os.path.commonpath([absolute_working_directory_path, final_path]) == absolute_working_directory_path
    if valid_target_path == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if valid_target_path:
        return f'Success: "{directory}" is within the working directory'