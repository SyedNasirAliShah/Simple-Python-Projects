import os

def rename_files_in_directory(directory, start_number=1):
    files = os.listdir(directory)
    i = start_number

    for file in files:
        file_extension = os.path.splitext(file)[1]
        new_filename = f"{i}{file_extension}"
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_filename)
        
        # Renaming the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_filename}'")
        
        i += 1

# calling the function

rename_files_in_directory("C:/Users/user/Pictures/Saved Pictures", start_number=1)
