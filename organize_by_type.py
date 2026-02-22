import os
import shutil

def organize_files_by_type():
    base_folder = os.getcwd()  # Runs inside current folder
    print(f"Organizing files inside: {base_folder}")
    
    for item in os.listdir(base_folder):
        item_path = os.path.join(base_folder, item)
        
        # Skip folders and the script itself
        if os.path.isdir(item_path) or item == os.path.basename(__file__):
            continue
        
        # Get file extension
        _, ext = os.path.splitext(item)
        
        if not ext:
            folder_name = "Others"
        else:
            folder_name = ext[1:].upper()  # Remove dot and capitalize
        
        target_folder = os.path.join(base_folder, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        
        destination = os.path.join(target_folder, item)
        
        try:
            shutil.move(item_path, destination)
            print(f"Moved: {item} → {folder_name}/")
        except Exception as e:
            print(f"Error moving {item}: {e}")
    
    print("Done organizing files.")

if __name__ == "__main__":
    organize_files_by_type()
