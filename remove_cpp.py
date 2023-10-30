import os

def delete_cpp_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".cpp"):
                file_path = os.path.join(root, filename)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

directory_path = r'./'

delete_cpp_files(directory_path)
