###############
#task1
###################

with open("lines_data.txt", "w") as f:
    for num in range(1, 1001):
        f.write(f"Entry {num}: Sample text here.\n")

line_count = 0
with open("lines_data.txt", "r") as f:
    for line in f:
        if line.strip():
            line_count += 1

print(f"Total non-empty lines: {line_count}")

###############
#task2
###################

with open("numbered_output.txt", "w") as f:
    for line_num in range(1, 18):
        if line_num == 2:
            f.write("Position 2: Number is 2\n")
        elif line_num == 8:
            f.write("Position 8: Number is 8\n")
        elif line_num == 10:
            f.write("Position 10: Number is 10\n")
        elif line_num == 13:
            f.write("Position 13: Number is 13\n")
        elif line_num == 17:
            f.write("Position 17: Number is 17\n")
        else:
            f.write(f"Position {line_num}: No specific number here.\n")

print("File created with numbers on the specified positions.")

###############
#task3
###################

file1 = 'source1.txt'
file2 = 'source2.txt'
output_file = 'merged_output.txt'

combined_content = []

with open(file1, 'r') as f1:
    content1 = f1.read()
    combined_content.append(content1)

with open(file2, 'r') as f2:
    content2 = f2.read()
    combined_content.append(content2)

merged_content = '\n'.join(combined_content)

with open(output_file, 'w') as output:
    output.write(merged_content)

print(merged_content)

###############
#task4
###################
def is_reverse(text1, text2):
    cleaned_text1 = ''.join(char.lower() for char in text1 if char.isalnum())
    cleaned_text2 = ''.join(char.lower() for char in text2 if char.isalnum())
    return cleaned_text1 == cleaned_text2[::-1]


def find_reverse_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        any_reverses_found = False

        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                if is_reverse(lines[i].strip(), lines[j].strip()):
                    print(f"'{lines[i].strip()}' and '{lines[j].strip()}' are reverses of each other.")
                    any_reverses_found = True

        if not any_reverses_found:
            print("No reverse lines found.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")


if __name__ == "__main__":
    file_name = 'reverse_test.txt'

    sample_data = [
        "madam\n",
        "racecar\n",
        "hello\n",
        "level\n",
        "world\n"
    ]

    with open(file_name, 'w') as file:
        file.writelines(sample_data)

    find_reverse_lines(file_name)

###############
#task5
###################

def partition_file_by_lines(source_file, lines_per_file=10):
    try:
        with open(source_file, 'r') as file:
            all_lines = file.readlines()

        total_lines_count = len(all_lines)
        total_files = (total_lines_count + lines_per_file - 1) // lines_per_file

        for index in range(total_files):
            start = index * lines_per_file
            end = start + lines_per_file
            chunk = all_lines[start:end]

            new_file_name = f'chunk_output_{index + 1}.txt'

            with open(new_file_name, 'w') as new_file:
                new_file.writelines(chunk)

            print(f'Created: {new_file_name} containing lines {start + 1} to {min(end, total_lines_count)}')

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")

if __name__ == "__main__":
    source_file_name = 'task5.txt'
    partition_file_by_lines(source_file_name)



###############
#task6
###################

def clean_file(input_path, output_path):
    try:
        with open(input_path, 'r') as file:
            all_lines = file.readlines()

        filtered_lines = [line for line in all_lines if line.strip()]

        with open(output_path, 'w') as file:
            file.writelines(filtered_lines)

        print(f'Successfully wrote {len(filtered_lines)} non-empty lines to "{output_path}".')

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_file_path = 'data_input.txt'
    output_file_path = 'cleared_output.txt'

    clean_file(input_file_path, output_file_path)
