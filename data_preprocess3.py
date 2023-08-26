import os
import shutil

# Define the source directory where the original dataset is located
source_directory = "data/state-wise-processed"

# Define the destination directory for the new organized dataset
destination_directory = "new"

# Create the destination directories if they don't exist
os.makedirs(destination_directory, exist_ok=True)
os.makedirs(os.path.join(destination_directory, "images"), exist_ok=True)
os.makedirs(os.path.join(destination_directory, "annotations"), exist_ok=True)

# Iterate through subdirectories in the source directory
for category_name in os.listdir(source_directory):
    category_path = os.path.join(source_directory, category_name)
    
    if os.path.isdir(category_path):
        image_source = os.path.join(category_path, "images")
        annotation_source = os.path.join(category_path, "annotations")
        
        # Move images and annotations to the destination directories
        for filename in os.listdir(image_source):
            image_source_path = os.path.join(image_source, filename)
            image_destination_path = os.path.join(destination_directory, "images", filename)
            shutil.copy(image_source_path, image_destination_path)
        
        for filename in os.listdir(annotation_source):
            annotation_source_path = os.path.join(annotation_source, filename)
            annotation_destination_path = os.path.join(destination_directory, "annotations", filename)
            shutil.copy(annotation_source_path, annotation_destination_path)

print("Reorganization complete!")
