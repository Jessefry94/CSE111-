import csv


def main():
    # Index of the product_id, product_name, product_cost column
    # in the products.csv file.
    PRODUCT_ID_INDEX = 0
    # PRODUCT_NAME_INDEX = 1
    # PRODUCT_COST_INDEX = 2
    
    # REQUEST_PRODUCT_ID_INDEX = 0
    # REQUEST_PRODUCT_QUANTITY = 1

    # Read the contents of the products.csv into a
    # compound dictionary named product_id_dict. Use
    # the phone numbers as the keys in the dictionary.
    product_id_dict = read_dict("products.csv", PRODUCT_ID_INDEX)

    # Print the dentists compound dictionary.
    print(product_id_dict)

    with open("request.csv", "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            for products in product_id_dict:
                if row_list[0] == products:
                    print(f'{product_id_dict[products][1]}: {row_list[1]} @ {product_id_dict[products][2]}')

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
    # Create an empty dictionary that will
    # store the data from the CSV file.
    product_id_dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        with open(filename,'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
                key = row_list[0]
                product_id_dictionary[key] = row_list

    # Return the dictionary.
    return product_id_dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()