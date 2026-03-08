"""
Lab Assignment 2
Task: Copy a Python script into another file without including comments.
"""

# Prompt user for source and destination file names
source_file = input("Enter the source Python file name: ")
destination_file = input("Enter the destination file name: ")

# Copy content excluding comments
with open(source_file, "r") as src, open(destination_file, "w") as dest:
    for line in src:
        stripped_line = line.strip()
        # Write only non-comment lines
        if not stripped_line.startswith("#"):
            dest.write(line)

# Display results
print("\n--- Source File Content ---")
with open(source_file, "r") as src:
    print(src.read())

print("\n--- Destination File Content (without comments) ---")
with open(destination_file, "r") as dest:
    print(dest.read())