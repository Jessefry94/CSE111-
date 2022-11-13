import random




def main():

    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers(numbers)

    print(numbers)

    append_random_numbers(numbers, 3)

    print(numbers)

   

    words_list = ['you', 'are', 'silly']

    print(words_list)

    append_random_words(words_list)

    print(words_list)

    append_random_words(words_list, 3)

    print(words_list)

   

def append_random_numbers(numbers_list, quantity = 1):

    for _ in range(quantity):

        numbers_list.append(round(random.uniform(1, 100), 1))



def append_random_words(words_list, quantity = 1):

    possibility = ['Parker', 'Chad', 'Jesse', 'MIKE']

   

    for _ in range(quantity):

        words_list.append(random.choice(possibility))



if __name__ == "__main__":

    main()
