
import os
 
# Function to rename multiple files
def main():
   
    folder = "C:/Users/Carlos/Documents/Mascotas"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count + 1)}.jpg" # we cand add eny Sufix BEFORE and After {str(count)} / +1 is 1-N
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()