import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    absolute_working_directory_path = os.path.abspath(working_directory)
    final_path = os.path.join(absolute_working_directory_path, directory)
    final_path = os.path.normpath(final_path)

    if os.path.isdir(final_path) == False:
        return f'Error: "{directory}" is not a directory'


    valid_target_path = os.path.commonpath([absolute_working_directory_path, final_path]) == absolute_working_directory_path
    if valid_target_path == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


    if valid_target_path:
        if final_path == absolute_working_directory_path:
            directory = "current"
            
        output = f"Result for {directory} directory:\n"
        list= os.listdir(final_path)
        list = sorted(list)
        for file_name in list:
            file_path = os.path.join(final_path, file_name)
            output += f"  - {file_name}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return output
    

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}