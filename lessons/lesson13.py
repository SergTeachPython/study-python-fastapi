import os

# curr_path_to_file = "f1/f2/f3/test.txt"
# curr_path_to_folder = curr_path_to_file[:curr_path_to_file.rfind("/")]
#
# if os.path.exists(curr_path_to_folder):
#     print("Directory exists")
#     with open(curr_path_to_file, "w") as myfile:
#         myfile.write("hello world from existing file")
# else:
#     print("Directory does not exist")
#     os.makedirs(curr_path_to_folder)
#     with open(curr_path_to_file, "w") as myfile:
#         myfile.write("hello world from new file")
# #
# with open("../test1.txt", "w") as myfile:
#     myfile.write('hello world')
#
def read_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def write_file_in_chunks(source_path, target_path, chunk_size=1024):
    with open(target_path, 'wb') as target_file:
        for chunk in read_file_in_chunks(source_path, chunk_size):
            target_file.write(chunk)

source_file = "myfile.txt"
target_file = "myfile_copy.txt"
current_chunk_size = 1024

write_file_in_chunks(source_file, target_file, current_chunk_size)
