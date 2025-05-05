import os
import tarfile


# Set the directory where the .tar files are located
directory_path = "<path_to_the_directory>"

# Function to extract all .tar.gz files in the specified directory
def extract_all_tar_files(directory):
    # List all files in the specified directory
    for filename in os.listdir(directory):
        print(filename)
        # Check if the file is a .tar.gz file
        if filename.endswith(".tar.gz"):
            # Construct the full path to the tar file
            tar_path = os.path.join(directory, filename)
            # Remove the last 7 characters ('.tar.gz') from the filename to get the folder name
            folder_name = filename[:-7]  
            # Construct the full path for the extraction folder
            extract_path = os.path.join(directory, folder_name)
            print(extract_path)
            
            # Create the folder if it doesn't exist
            os.makedirs(extract_path, exist_ok=True)
            
            # Open and extract the tar file
            with tarfile.open(tar_path, 'r') as tar:
                # Extract all contents to the specified folder
                tar.extractall(path=extract_path)
                print(f"Extracted {filename} to {extract_path}")

# Call the function to extract all .tar.gz files in the specified directory
extract_all_tar_files(directory_path)
print("finished")

# Function to delete all files in the specified directory that are not .tar.gz files
def delete_non_tar_gz_files(directory):
    # List all files in the specified directory
    for filename in os.listdir(directory):
        # Construct the full path to the file
        file_path = os.path.join(directory, filename)
        
        # Check if the file is not a .tar.gz file
        if not filename.endswith(".tar.gz") and os.path.isfile(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"Deleted {filename}")

# Call the function to delete non .tar.gz files in the specified directory
delete_non_tar_gz_files(directory_path)
