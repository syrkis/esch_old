import sys
import re

def add_allowframebreaks(file_path):
    # Read the LaTeX file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define the regex pattern to find frames, capturing existing options if present
    pattern = re.compile(r'\\begin{frame}(\[(.*?)\])?(?![^\[]*allowframebreaks)(.*?)(?=\\end{frame})', re.DOTALL)
    
    def replacement(match):
        before_options = match.group(1)  # Existing options including brackets
        options_content = match.group(2)  # The content of the options without brackets
        frame_content = match.group(3)
        
        # Check if the frame contains lstlisting, skip modification if true
        if 'begin{lstlisting}' not in frame_content and '[<+->]' not in frame_content:
            # If there were options, append allowframebreaks, otherwise create new option
            if before_options:
                new_options = f"[{options_content},allowframebreaks]"
            else:
                new_options = "[allowframebreaks]"
            return f'\\begin{{frame}}{new_options}' + frame_content
        else:
            return match.group(0)  # Return the original match if lstlisting is found
    
    # Replace the content
    modified_content = pattern.sub(replacement, content)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frames.py file.tex")
        sys.exit(1)
    
    add_allowframebreaks(sys.argv[1])
    print(f"Processed {sys.argv[1]} successfully.")
