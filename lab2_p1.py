# Warren Green
# 006314031

# A function that reads content from a file
def read_file():

    file =open('students.csv', 'r')
    print(file.read())

read_file()