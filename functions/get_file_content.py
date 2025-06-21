import os
from google.genai import types
from config import MAX_CHARS

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
    
    with open(target_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    if len(file_content_string) == MAX_CHARS:
        file_content_string = file_content_string +  f'[...File "{file_path}" truncated at 10000 characters]'
    
    return(file_content_string)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)