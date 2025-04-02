import os

folderPath = r"C:\Users\pc\Desktop\computer"
counter = 1

for filename in os.listdir(folderPath):
    old_path = os.path.join(folderPath, filename)  # Full path of the existing file

    # Extracting file extension
    file_extension = os.path.splitext(filename)[1]

    # Creating new file name with extension
    new_filename = f"my-text{counter}{file_extension}"
    new_path = os.path.join(folderPath, new_filename)

    os.rename(old_path, new_path)  # Rename file
    counter += 1  # Increment counter
