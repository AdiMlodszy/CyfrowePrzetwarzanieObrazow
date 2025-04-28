#!/usr/bin/env python
"""
Bulk Label Class Modifier

This script modifies class identifiers in YOLO format annotation files (.txt).
In YOLO format, each bounding box is represented as:
<class_id> <center_x> <center_y> <width> <height>
where all values except class_id are normalized between 0 and 1.

This script changes the class_id for all bounding boxes to a specified value
across multiple annotation files.
"""

import os

# Configuration constants
LABELS_FOLDER = "D:/CyfrowePrzetwarzanieObrazow/data/dataset/labels/train"
NEW_CLASS_ID = '0'

def change_labels(folder_path, new_Class_id='0'):
    """
    Change the class ID of all bounding boxes in YOLO format annotation files.
    
    Args:
        folder_path (str): Path to the folder containing annotation files
        new_Class_id (str): The new class ID to replace existing ones
    
    Returns:
        int: Number of files processed successfully
    """
    # Find all .txt files in the specified directory
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    print(f"Found {len(txt_files)} .txt files in {folder_path}.")
    
    files_processed = 0
    
    # Process each text file
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        
        # Read the original content
        with open(file_path, 'r') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            # Split each line into components
            parts = line.strip().split()
            
            # Verify the line has the expected YOLO format (5 values)
            if len(parts) == 5:
                # Replace the first element (class ID) with the new class ID
                parts[0] = new_Class_id
                new_lines.append(' '.join(parts))
            else:
                # Skip malformed lines
                print(f"Skipping line in {txt_file}: {line.strip()}")
                
        # Write the modified content back to the file
        with open(file_path, 'w') as f:
            f.write('\n'.join(new_lines))
        
        files_processed += 1
    
    print(f"Changed labels in {files_processed} files.")
    return files_processed
            
if __name__ == "__main__":
    # Execute the label changing function
    change_labels(LABELS_FOLDER, NEW_CLASS_ID)
    print("Labels changed successfully.")