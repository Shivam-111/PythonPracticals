Practocal 8 File Handling

# Lab Assignment 1: Copy file content in uppercase

# Ask user for source and destination file names
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

# Open source file in read mode and destination in write mode
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        dest.write(line.upper())

print("File copied successfully in uppercase!")
