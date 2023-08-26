import os
import shutil

# Define the source directory where images and annotations are located
source_directory = "data/video_images"

# Define the destination directories for images and annotations
image_destination = "images"
annotation_destination = "annotations"

# Create the destination directories if they don't exist
os.makedirs(image_destination, exist_ok=True)
os.makedirs(annotation_destination, exist_ok=True)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if filename.lower().endswith((".jpg", ".png")):
        # Move images to the image destination directory
        image_source_path = os.path.join(source_directory, filename)
        image_destination_path = os.path.join(image_destination, filename)
        shutil.move(image_source_path, image_destination_path)
    elif filename.lower().endswith(".xml"):
        # Move annotations to the annotation destination directory
        annotation_source_path = os.path.join(source_directory, filename)
        annotation_destination_path = os.path.join(annotation_destination, filename)
        shutil.move(annotation_source_path, annotation_destination_path)

print("Separation complete!")