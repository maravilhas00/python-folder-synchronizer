import os
import shutil
import time
from datetime import datetime


def log_entries(message):
    with open(log_file, "a") as log_file:
        timestamp=datetime.now().strftime("%H:%M:%S %D-%m-%Y")
        log_file.write(f"[{timestamp}] {message}\n")


def check_for_valid_folder(message):
    while True:
        folder_path=input(message)
        if os.path.exists(folder_path):
            return folder_path
        else:
            print("Please submit a valid folder path.")


def folder_synchronizer(source_folder, replica_folder, log_file_path):
    #Synchronize the files from source to the replica
    for root, dirs, files in os.walk(source_folder):
        #Create the path in the replica folder using the relative path from the source folder
        relative_path=os.path.relpath(root, source_folder)
        replica_path=os.path.join(replica_folder, relative_path)
        
        #If it doesnt exist, creates one
        if not os.path.exists(replica_path):
            os.makedirs(replica_path)

        for file in files:
            source_file=os.path.join(root, file)
            replica_file=os.path.join(replica_path, file)

            #If the file doesnt exist on the replica or the version on the source is recent, proceed to copy the file
            if (not os.path.exists(replica_file) or os.path.getmtime(source_file)>os.path.getmtime(replica_file)):
                shutil.copy2(source_file, replica_file)
        
    #Delete files in replica that are not in the source
    for root, dirs, files in os.walk(replica_folder, topdown=False):
        #While running the files, it will pass the relative path of the file of the file to verify if it exists in the source and afterwards delete in replica if it doesnt
        relative_path=os.path.relpath(root, replica_folder)
        source_path=os.path.join(source_folder, relative_path)

        #Verification if the file exists on the source
        for file in files:
            replica_file=os.path.join(root, file)
            source_file=os.path.join(source_path, file)
            if not os.path.exists(source_file):
                #Delete file on replica
                os.remove(replica_file)

        #Verification if the folder exists on the source
        for dir in dirs:
            replica_sub_folder=os.path.join(root, dir)
            source_sub_folder=os.path.join(source_path, dir)
            if not os.path.exists(source_sub_folder):
                #Delete folder on replica
                shutil.rmtree(replica_sub_folder)


source_folder=check_for_valid_folder("Enter the Source folder path: ")
replica_folder=check_for_valid_folder("Enter the Replica folder path: ")
log_file_path=check_for_valid_folder("Enter the path for the log file: ")
refresh_timer=int(input("Refresh timer in seconds: "))




#replica_folder="C:/xampp/htdocs/Replica"
#log_file_path="C:/xampp/htdocs/Logs"
#source_folder="C:/xampp/htdocs/Source"



while True:
    folder_synchronizer(source_folder, replica_folder, log_file_path)
    print(f"Synchronization complete. Waiting for {refresh_timer} seconds...")
    time.sleep(refresh_timer)