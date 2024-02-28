import sys
import re

def inject_content_after_header(markdown_file, inject_file):
    # Read the original Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        content = md_file.read()
    
    if 'bio: true' not in content:
        return
    
    # Find the end of the YAML header
    header_end_idx = content.find('---', content.find('---') + 3) + 3
    
    if header_end_idx == 2:  # No second '---' found, indicating no proper YAML header
        print("No valid YAML header found. Ensure the file has a correctly formatted header.")
        sys.exit(1)
    
    # Read the content to inject
    with open(inject_file, 'r', encoding='utf-8') as inj_file:
        inject_content =  inj_file.read() + '\n\n---\n\n'
    
    # Inject the content right after the header
    new_content = content[:header_end_idx] + '\n\n' + inject_content + '\n\n' + content[header_end_idx:]
    
    # Write the modified content back to the original file
    with open(markdown_file, 'w', encoding='utf-8') as md_file:
        md_file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inject_md.py target_markdown_file.md")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    inject_file = '/Users/syrkis/code/press/docs/bio.md'
    
    inject_content_after_header(markdown_file, inject_file)
    print(f"Injected content into {markdown_file} successfully.")
