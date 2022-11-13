import csv


def main():
    # Index of the student_id number column
    # in the students.csv file.
    STUDENT_ID_INDEX = 0

    # Read the contents of the students.csv into a
    # compound dictionary named students_id_dict. Use
    # the students_id numbers as the keys in the dictionary.
    student_id_dict = read_dict("students.csv", STUDENT_ID_INDEX)

    # Print the students_id compound dictionary.
    print(student_id_dict)

    i_number = input("Enter student I-Number: ")

    student_found = False
    for key in student_id_dict:
        if i_number == key:
            print(student_id_dict[key])
            student_found = True
    if student_found == False:
        print("No such student")            
       
            
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_id_dict = {}
    with open(filename,'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[0]
            student_id_dict[key] = row_list[1]
            #name = row_list[1]
            #student_id_dict = 
            
    return student_id_dict
    


main()