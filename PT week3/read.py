def read_and_modify_file():
    """
    Reads a file, modifies its content, and writes the modified version to a new file.
    Handles errors if the file does not exist or cannot be read.
    """
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.readlines()  # Read all lines from the file

        # Modify the content (example: convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"File has been successfully modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You do not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
