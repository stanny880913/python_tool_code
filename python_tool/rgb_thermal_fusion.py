import cv2
import os


# Set the paths to the directories containing RGB and thermal images
rgb_folder = '/home/stannyho/Downloads/rgb/'
thermal_folder = '/home/stannyho/Downloads/thermal/'
output_folder = '/home/stannyho/Downloads/'

# Get the list of file names in the folders
rgb_files = os.listdir(rgb_folder)
thermal_files = os.listdir(thermal_folder)

# Iterate through the files and perform the fusion
for i, rgb_file in enumerate(rgb_files):
    # Load RGB and thermal images
    rgb_image = cv2.imread(os.path.join(rgb_folder, rgb_file))
    thermal_file = thermal_files[i]
    thermal_image = cv2.imread(os.path.join(
        thermal_folder, thermal_file), cv2.IMREAD_GRAYSCALE)

    # Check if the images are loaded correctly
    if rgb_image is None or thermal_image is None:
        print(f"Error loading {rgb_file} or {thermal_file}")
        continue

    # Normalize thermal image to 0-255 range
    thermal_image = cv2.normalize(thermal_image, None, 0, 255, cv2.NORM_MINMAX)

    # thermal_image = cv2.resize(
    #     thermal_image, (rgb_image.shape[1], rgb_image.shape[0]))

    # Convert thermal image to a 3-channel grayscale image
    thermal_image = cv2.cvtColor(thermal_image, cv2.COLOR_GRAY2RGB)
    thermal_image = cv2.applyColorMap(thermal_image, cv2.COLORMAP_JET)


    # Combine RGB and thermal images using weighted addition
    fusion_image = cv2.addWeighted(rgb_image, 0.6, thermal_image, 0.4, 0)

    # Write the fusion image to the output folder
    output_file = os.path.join(output_folder, rgb_file)
    cv2.imwrite(output_file, fusion_image)

    # Print the shapes of the images
    print(
        f"{rgb_file}: {rgb_image.shape}, {thermal_file}: {thermal_image.shape[:2]}, fusion: {fusion_image.shape}")
