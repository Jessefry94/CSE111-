# # Loop to get user input (name and age of each family member)
# # Store each person in a dictionary
# # Store all people in a list
# # Save each name and age to a text file

# def main():
#     family = get_family()
#     save_my_family(family)

# def get_family():
#     continue_bool = 'Y'
#     family = []
#     while continue_bool == 'Y':
#         name = input('\nEnter name: ')
#         age = input('Enter age: ')
#         person = {'name': name, 'age': age}
#         family.append(person)
#         user_input = input('Continue? (Y/n) ') 
#         continue_bool = 'n' if user_input == 'n' else 'Y'

#         # if user_input == 'n':
#         #     continue_bool = 'n'
#         # else:
#         #     continue_bool = 'Y'

#     return family

# def save_my_family(family):
#     file = open('family.txt', 'w')
#     file.write('Here is a list of your family members.\n\n')
#     for person in family:
#         file.write(person['name'] + ' is ' + person['age'] + ' years old.\n')

# main()
# Loop to get user input (name and age of each family member)
# Store each person in a dictionary
# Store all people in a list
# Save each name and age to a text file

# stretch
# add a function to get the family members from a text file
# add a function to print the family members
# add a function to edit the a family member's name or age

def main():
    print_menu()
    user_input = input('Enter your choice: ')
    if user_input == '1':
        family = get_family()
        save_my_family(family)
    if user_input == '2':
        family = get_family_from_file()
        print_family(family)
    if user_input == '3':
        edit_family()
    if user_input == '4':
        print('Goodbye!')

def print_menu():
    print('1. Input family and save to file')
    print('2. See family members in a text file')
    print('3. Edit family members in text file')
    print('4. Exit')

def get_family():
    continue_bool = 'Y'
    family = []
    while continue_bool == 'Y':
        name = input('\nEnter name: ')
        age = input('Enter age: ')
        person = {'name': name, 'age': age}
        family.append(person)
        user_input = input('Continue? (Y/n) ') 
        continue_bool = 'n' if user_input == 'n' else 'Y'
    return family

def save_my_family(family):
    file = open('family.txt', 'w')
    file.write('Here is a list of your family members.\n\n')
    for person in family:
        file.write(person['name'] + ' is ' + person['age'] + ' years old.\n')

def get_family_from_file():
    file = open('family.txt', 'r')
    family = []
    for line in file:
        if line == 'Here is a list of your family members.\n' or line == '\n':
            continue
        else:
            name = line.split(' is ')[0]
            age = line.split(' is ')[1].split(' years old.')[0]
            person = {'name': name, 'age': age}
            family.append(person)
    return family

def print_family(family):
    for person in family:
        print(person['name'] + ' is ' + person['age'] + ' years old.')

def edit_family():
    family = get_family_from_file()
    print_family(family)
    name = input('Enter name of family member to edit: ')
    for person in family:
        if person['name'] == name:
            person['name'] = input('Enter new name: ')
            person['age'] = input('Enter new age: ')
            break
    save_my_family(family)

main()