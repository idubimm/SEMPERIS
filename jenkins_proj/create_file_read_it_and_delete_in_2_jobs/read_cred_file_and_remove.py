import os
import sys

filename = sys.argv[1]


def read_and_delete_file(filepath):
    # Check if the file exists
    if os.path.exists(filepath):
        # Open the file
        with open(filepath, 'r') as f:
            # Read and print the file content
            print(f.read())
        
        # Delete the file
        os.remove(filepath)
        print(f"The file {filepath} has been deleted.")
        return True
    else:
        print("The file does not exist.")
        raise "file does not exist - failed process"


read_and_delete_file('../my_credentials.txt')


