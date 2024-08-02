import os

def read_all_files(directory):
    """
    Read all files in the src directory and its subdirectories.
    Exclude the src/lib/components/ui directory and its subdirectories.
    Return concatenated content of all files.
    """
    exclude_dir = os.path.join(directory, 'lib/components/ui')
    code_content = []
    for root, _, files in os.walk(directory):
        if exclude_dir in root:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code_content.append(f"File: {file_path}\n")
                    code_content.append(f.read())
                    code_content.append("\n" + "="*80 + "\n")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return ''.join(code_content)

def write_to_output(content, output_file):
    """
    Write content to output file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")

def main():
    src_directory = './src'
    output_file = 'printed.txt'
    
    try:
        all_code = read_all_files(src_directory)
        write_to_output(all_code, output_file)
        print(f"All code written to {output_file}")
    except Exception as e:
        print(f"Error processing files: {e}")

if __name__ == "__main__":
    main()
