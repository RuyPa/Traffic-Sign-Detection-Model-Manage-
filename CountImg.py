import os
import glob

def countFile(a):
# Define the directory path
    directory_path = a

    # List all files in the directory
    all_files = glob.glob(os.path.join(directory_path, '*'))

    # Filter for image files (e.g., .jpg, .png, .jpeg)
    image_extensions = ('.jpg', '.png')  # Add more extensions if needed
    image_files = [file for file in all_files if file.lower().endswith(image_extensions)]

    # Count the number of image files
    num_images = len(image_files)

    # Print the result
    print(f'The number of image files in the directory is: {num_images}')
    return num_images

# countFile("D:\\test flask cors\\data\\images\\train")
