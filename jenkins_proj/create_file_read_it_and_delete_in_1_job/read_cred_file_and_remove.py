import os
import sys

FILE_NAME = sys.argv[1]


def read_and_delete_file(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # Open the file
        with open(filename, 'r') as f:
            # Read and print the file content
            print(f.read())
        
        # Delete the file
        os.remove(filename)
        print(f"The file {filename} has been deleted.")
        return True
    else:
        print("The file does not exist.")
        raise "file does not exist - failed process"


read_and_delete_file(FILE_NAME)

# http://192.168.10.128:9090/job/create_files_with_trigger/job/trigger_create_file/build?token=create_cred_file