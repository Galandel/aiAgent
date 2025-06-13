import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    # print(f"Abs path: {abs_working_dir}")
    # print(f"working dir: {working_directory}")
    target_dir = abs_working_dir
    if directory:
        # print(f"directory: {directory}")
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):

            filepath = os.path.join(target_dir, filename)

            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


# def get_files_info(working_directory, directory=None):
#     items = os.listdir(working_directory)
#     directories = [item for item in items if os.path.isdir(os.path.join(working_directory, item))]

#     for directory in directories:
#         item_subdir = os.listdir(os.path.join(working_directory, directory))
#         for item in item_subdir:
#             items.append(item)

#     if directory and not directory == '.':
#         if directory.startswith("/") or directory.startswith("../"):
#             return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

#         if directory in items and directory not in directories:
#             return f'Error: "{directory}" is not a directory'
    
#     return_string = ""
#     for item in items:
#         size = os.path.getsize(os.path.join(working_directory, item))
#         is_dir = os.path.isdir(os.path.join(working_directory, item))
#         return_string += f"- {item}: file_size={size} bytes, is_dir={is_dir}\n"

#     return return_string
           
