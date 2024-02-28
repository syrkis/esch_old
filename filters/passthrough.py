import sys
import re

def remove_passthrough(file_path):
    # Read the LaTeX file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the regex pattern to find and remove \passthrough{\lstinline!...!} 
    # while keeping the ... part inside \lstinline!...!
    pattern = re.compile(r'\\passthrough{\s*\\lstinline!(.*?)!\s*}')

    def replacement(match):
        # Extract the content inside \lstinline!...! and return it
        return '\\texttt{' + match.group(1) + '}'

    # Replace the content
    modified_content = pattern.sub(replacement, content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file.tex")
        sys.exit(1)

    remove_passthrough(sys.argv[1])
    print(f"Processed {sys.argv[1]} successfully.")
