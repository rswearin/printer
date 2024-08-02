import os

def read_all_files(target_directories, excluded_directories, excluded_file_types):
    """
    Read all files in the specified directories and their subdirectories.
    Exclude specified directories and file types.
    Return concatenated content of all files.
    """
    code_content = []
    for directory in target_directories:
        for root, _, files in os.walk(directory):
            if any(excluded_dir in root for excluded_dir in excluded_directories):
                continue
            for file in files:
                if any(file.endswith(ext) for ext in excluded_file_types):
                    continue
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
    # Set all parameters here
    target_directories = ['./src']
    excluded_directories = ['lib/components/ui']
    excluded_file_types = ['.css']
    output_file = './printed.txt'
    
    try:
        all_code = read_all_files(target_directories, excluded_directories, excluded_file_types)
        write_to_output(all_code, output_file)
        print(f"All code written to {output_file}")
    except Exception as e:
        print(f"Error processing files: {e}")

if __name__ == "__main__":
    main()
