import os

def replace_spaces_with_underscores(folder_path):
    for filename in os.listdir(folder_path):
        if ' ' in filename:
            new_filename = filename.replace(' ', '_')
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    # Get the current directory (where the script is located)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Perform the renaming operation
    replace_spaces_with_underscores(current_directory)
    
    # Wait for a key press before exiting
    input("Press Enter to exit...")
