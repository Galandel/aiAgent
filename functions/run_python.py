import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    # Future enhancement: Could add args parameter to pass command-line arguments
    # to the executed Python file: run_python_file(working_dir, file_path, args=None)

    try:
        output = subprocess.run(["python", target_file], 
                                capture_output=True, text=True, 
                                timeout=30, cwd=abs_working_dir)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    parts = [f"Ran: {file_path}"]

    if output.stdout:
        parts.append(f'STDOUT: {output.stdout.strip()}')
    if output.stderr:
        parts.append(f'STDERR: {output.stderr.strip()}')
    if output.returncode != 0:
        parts.append(f'Process exited with code {output.returncode}')

    if len(parts) == 1:
        return "No output produced."
    else:
        return '\n'.join(parts)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            # "args": types.Schema(
            #     type=types.Type.ARRAY,
            #     items=types.Schema(
            #         type=types.Type.STRING,
            #         description="Optional arguments to pass to the Python file.",
            #     ),
            #     description="Optional arguments to pass to the Python file.",
            # ),
        },
        required=["file_path"],
    ),
)