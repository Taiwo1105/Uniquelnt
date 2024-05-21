# def read_integers_from_file(file_path):
#     """Read integers from a file, skipping invalid entries."""
#     integers = set()
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if line == '' or ' ' in line:
#                 continue
#             try:
#                 number = int(line)
#                 integers.add(number)
#             except ValueError:
#                 continue
#     return integers

# def sort_integers(integers):
#     """Sort integers without using built-in sort. Implements insertion sort."""
#     sorted_list = list(integers)
#     for i in range(1, len(sorted_list)):
#         key = sorted_list[i]
#         j = i - 1
#         while j >= 0 and key < sorted_list[j]:
#             sorted_list[j + 1] = sorted_list[j]
#             j -= 1
#         sorted_list[j + 1] = key
#     return sorted_list

# def write_integers_to_file(integers, file_path):
#     """Write sorted integers to a file, one integer per line."""
#     with open(file_path, 'w') as file:
#         for integer in integers:
#             file.write(f"{integer}\n")

# def processFile(inputFilePath, outputFilePath):
#     """Process file to read, sort and write unique integers."""
#     integers = read_integers_from_file(inputFilePath)
#     sorted_integers = sort_integers(integers)
#     write_integers_to_file(sorted_integers, outputFilePath)

# # Example usage:
# input_file_path = 'input.txt'
# output_file_path = 'output.txt'
# processFile(input_file_path, output_file_path)






def read_and_process_file(input_file_path):
    """ Read integers from file and return a sorted list of unique integers. """
    sorted_unique_integers = []
    with open(input_file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                sorted_unique_integers = custom_insert(sorted_unique_integers, num)
            except ValueError:
                continue  # Skip non-integer lines
    return sorted_unique_integers

def custom_insert(sorted_data, value):
    """ Insert value into sorted_data maintaining sorted order. """
    if value in sorted_data:
        return sorted_data  # Skip insertion if value already exists.
    for i in range(len(sorted_data)):
        if value < sorted_data[i]:
            sorted_data = sorted_data[:i] + [value] + sorted_data[i:]
            return sorted_data
    sorted_data.append(value)
    return sorted_data

def write_output_file(output_file_path, integers):
    """ Write each integer from the list to the file, one per line. """
    with open(output_file_path, 'w') as file:
        for integer in integers:
            file.write(f"{integer}\n")

def process_file(input_file_path, output_file_path):
    """ Process input file to generate an output file with sorted unique integers. """
    sorted_unique_integers = read_and_process_file(input_file_path)
    write_output_file(output_file_path, sorted_unique_integers)

# Example usage
input_file_path = 'input.txt'
output_file_path = 'output.txt'
process_file(input_file_path, output_file_path)
