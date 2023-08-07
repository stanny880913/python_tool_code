import shutil
import random
import string
import os

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def copy_files(source_file, destination_folder, num_copies=1000):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    for i in range(1, num_copies + 1):
        # Generate a random string to use as the new filename
        random_string = generate_random_string()

        # Get the file extension from the source file
        _, extension = os.path.splitext(source_file)

        # Construct the new filename using the random string and original extension
        new_filename = f"{random_string}{extension}"

        # Join the source file path with the destination folder and new filename
        destination_file = os.path.join(destination_folder, new_filename)

        # Copy the source file to the destination folder with the new filename
        shutil.copy(source_file, destination_file)

if __name__ == "__main__":
    source_file = "/media/stannyho/ssd/Pseudo_Lidar_V2/data/calib/calib.txt"
    destination_folder = "/media/stannyho/ssd/Pseudo_Lidar_V2/data/calib"
    num_copies = 12609

    copy_files(source_file, destination_folder, num_copies)
