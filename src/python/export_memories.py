import os
import shutil

def export_memories(dest_path):
    src_dir = 'data/memories/'
    files = os.listdir(src_dir)
    for file in files:
        if file.endswith('.db'):
            shutil.copy(os.path.join(src_dir, file), dest_path)
            print(f'Exported {file} to {dest_path}')

if __name__ == "__main__":
    dest_path = '/path/to/destination/'  # Replace with the actual destination path
    export_memories(dest_path)
