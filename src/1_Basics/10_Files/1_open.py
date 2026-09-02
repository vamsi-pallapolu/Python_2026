"""
Opening files in python

"""
from pathlib import Path

current_file = Path(__file__)
print(f"Current file path:{current_file}")

current_dir = Path(__file__).resolve().parent
data_file = current_dir/"data_file1.txt"
print(f"{type(data_file)}")

# Creating and Opening files
try:
    file = open(data_file, 'w') # By default read mode 
except FileNotFoundError as e:
    print("Error occured while opening the file:",e)
finally:
    file.close()

# Reading from files
data_file = current_dir/"data_file.txt"
try:
    file = open(data_file, 'r')
    data = file.read()
    print(f"Type of data:{type(data)}")
    for line in data:
        print(line, end='')
    print()
except FileNotFoundError as e:
    print(e)
finally:
    file.close()


# appending to files
data_file = current_dir/"append_file.txt"
try:
    file = open(data_file, 'a')
    file.write('Appending a line\n')
    file.write('Appendinf another line')
except FileNotFoundError as e:
    print(e)
# finally:

# What happens
#  if we don't close the file
data_file = current_dir/"append_file.txt"

with open(data_file, 'r') as file:
    for line in file.read():
        print(line, end='')




