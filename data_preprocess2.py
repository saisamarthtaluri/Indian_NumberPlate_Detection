import os
import shutil

# Define the source directory where folders with images and annotations are located
source_directory = "data/State-wise_OLX"

# Define the base destination directory for images and annotations
base_destination = "data/state-wise-processed"

# Create the base destination directory if it doesn't exist
os.makedirs(base_destination, exist_ok=True)

# Iterate through subdirectories in the source directory
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)
    
    if os.path.isdir(folder_path):
        # Create destination directories for this folder
        image_destination = os.path.join(base_destination, folder_name, "images")
        annotation_destination = os.path.join(base_destination, folder_name, "annotations")
        
        os.makedirs(image_destination, exist_ok=True)
        os.makedirs(annotation_destination, exist_ok=True)
        
        # Iterate through files in the current subdirectory
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".jpg", ".png")):
                # Move images to the image destination directory
                image_source_path = os.path.join(folder_path, filename)
                image_destination_path = os.path.join(image_destination, filename)
                shutil.move(image_source_path, image_destination_path)
            elif filename.lower().endswith(".xml"):
                # Move annotations to the annotation destination directory
                annotation_source_path = os.path.join(folder_path, filename)
                annotation_destination_path = os.path.join(annotation_destination, filename)
                shutil.move(annotation_source_path, annotation_destination_path)

print("Separation complete!")
