import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    # print(f"Target File: {target_file}")
    
    # check if file is outside of working directory
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check if file path is a valid file
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # read in 10,000 characters
    MAX_CHARS = 10_000
    
    with open(target_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    if len(file_content_string) == MAX_CHARS:
        file_content_string = file_content_string +  f'[...File "{file_path}" truncated at 10000 characters]'
    
    return(file_content_string)

