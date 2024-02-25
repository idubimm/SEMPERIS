import os
import sys

FILE_NAME = sys.argv[1]
CONTENT = sys.argv[2]

def create_text_file(fileName,content):
    # Ensure the exists
    try:
        if not os.path.exists(fileName):
            with open(fileName,'w') as f:
                f.write(content)
                f.close()
                return True
        print(f"An error occurred : file already exists")  
        os.remove(fileName)
        return False
    except :
        print(f"An error occurred when try to create file")
        return False
    

if not create_text_file(FILE_NAME,CONTENT):
   raise( Exception(f'failed to create file {FILE_NAME}') )
    
 