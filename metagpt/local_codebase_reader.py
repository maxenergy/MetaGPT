#import os

def read_local_codebase(directory):
    "
    Reads files from the specified directory and returns their contents.
    Args:
    - directory (str): The path to the directory containing the codebase files.
    Returns:
    - dict: A dictionary with filenames as keys and file contents as values.
   "
    files_content = {}
    for filename in os.listdir(directory):
        if filename.endswith(".py"):  # Assuming Python codebase; this can be adjusted as needed
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            files_content[filename] = file.read()
    return files_content
