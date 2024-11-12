import os
import shutil

def folder_synchronizer(source_folder, replica_folder):
    # Folder verifications
    if not os.path.exists(source_folder):
        print(f"The source folder does not exist.\nPath: '{source_folder}'")
        return
    if not os.path.exists(replica_folder):
        print(f"The replica folder does not exist.\nPath: '{replica_folder}'")
        return
    
    for root, dirs, files in os.walk(source_folder):
        #Create the path in the replica folder using the relative path from the source folder
        relative_path = os.path.relpath(root, source_folder)
        replica_path = os.path.join(replica_folder, relative_path)
        
        #If it doesnt exist, creates one
        if not os.path.exists(replica_path):
            os.makedirs(replica_path)

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_folder, file)

            if (not os.path.exists(replica_file) or os.path)
        

