import os

def rename_files():
    # This line of code will go to files location and list all of them to put them in a new variable named all_files
    # You need to change the bellow directory with your folder directory containing your files
    all_files = os.listdir(r"C:\Users\hyg\Desktop\MSSD in Software Development\Toy programs\prank")
    
    # This will edit all files by deleting any number in their names using a for loop
    # Here also you need to change the bellow directory with your folder directory containing your files
    os.chdir("C:\Users\hyg\Desktop\MSSD in Software Development\Toy programs\prank")
    for file in all_files:
        print("Old name - " + file)
        print("New name - " + file.translate(None, "0123456789"))
        print(" ")
        os.rename(file, file.translate(None, "0123456789"))
    #return to the original directory
    os.chdir("C:\Users\hyg\Desktop\MSSD in Software Development\Toy programs")
rename_files()
