import os

def rename_files():
    # This line of code will go to files location and list all of them to put them in a new variable named all_files
    # You need to change the bellow directory with your folder directory containing your files
    all_files = os.listdir(r"C:\This_Is_Just_A_Sample_Directory")
    
    # This will edit all files by deleting any number in their names using a for loop
    # Here also you need to change the bellow directory with your folder directory containing your files
    os.chdir("C:\This_Is_Just_A_Sample_Directory")
    for file in all_files:
        print("Old name - " + file)
        print("New name - " + file.translate(None, "0123456789"))
        print(" ")
        os.rename(file, file.translate(None, "0123456789"))
    # You need to return to the original directory using the chdir() function from the os module
    # Just replace the bellow "your original directory" with your actual original directory
    os.chdir("put your original directory here")

rename_files()
