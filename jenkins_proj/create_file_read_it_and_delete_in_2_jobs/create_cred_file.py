import os

def create_text_file(fileName):
    # Ensure the exists
    try:
        if not os.path.exists(fileName):
            with open(fileName,'w') as f:
                f.write('my name is ido bistry')
                f.close()
                return True
        print(f"An error occurred : file already exists")  
        os.remove(fileName)
        return False
    except :
        print(f"An error occurred when try to create file")
        return False
    

if not create_text_file('../my_credentials.txt'):
   raise( Exception('failed to create file') )
    
 