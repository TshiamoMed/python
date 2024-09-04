# file_handling_assignment.py

def create_and_write_file(filename):
    """Create a new text file and write initial content to it."""
    try:
        with open(filename, 'w') as file:
            # Write three lines of text including a mix of strings and numbers
            file.write("This is the first line of text.\n")
            file.write("Here is the second line with a number: 1234.\n")
            file.write("And another line with mixed content: Python 3.9\n")
        print("File created and written successfully.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation and writing operation completed.")

def read_file(filename):
    """Read and display the contents of the file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading operation completed.")

def append_to_file(filename):
    """Append additional lines of text to the file."""
    try:
        with open(filename, 'a') as file:
            # Append three additional lines of text
            file.write("Appended line 1.\n")
            file.write("Another appended line.\n")
            file.write("Yet another line added.\n")
        print("Content appended successfully.")
        
        # Read and display the updated file content
        read_file(filename)
        
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending operation completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    create_and_write_file(filename)
    read_file(filename)
    append_to_file(filename)

