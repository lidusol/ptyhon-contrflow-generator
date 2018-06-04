from path_generator import *

files = ["test_file_1.py", "test_file_2.py"]
for file in files:
    print(file)
    a = path_generator(file)
    a.print_path()
    print("\t/ ----------------------- /")

