import os

def delete_files_with_extension(root_directory, extension):
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                print("Deleting file:", file_path)
                os.remove(file_path)

# Specify the root directory where you want to delete the files
root_directory = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/sensor.community/temp'

# Specify the extension of files you want to delete
extension = '.gz'

# Call the function to delete the files
delete_files_with_extension(root_directory, extension)
