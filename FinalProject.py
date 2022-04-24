"""
This program calculates the total cost of a wholesale purchase given the
product title, product cost, and production quantity.
"""
__author__ = 'Rebecca Sheffey'


def test_integer_number():
    """tests if an input is a valid integer"""
    valid = "no"
    integer = 0
    while valid == "no":  # causes input request to repeat while the
        # input is invalid
        test_value = input()
        try:
            integer = (int(float(test_value)))  # tests if input can be
            # an integer
        except:
            print("That was not a valid number. Please try again.")
        else:
            if integer <= 0:
                print("You may not enter a negative value. Please try again.")
            elif integer != float(test_value):
                print("You must enter a whole number. Please try again.")
            else:
                valid = "yes"
    while valid == "yes":  # returns the valid input
        return integer  # returns the value as an integer


def test_float_number():
    """tests if an input is a valid float number"""
    valid = "no"
    float_number = 0
    while valid == "no":  # causes input request to repeat while the
        # input is invalid
        test_value = input()
        try:
            float_number = (float(test_value))  # tests if input is a float
        except:
            print("That was not a valid number. Please try again.")
        else:
            if float_number <= 0:
                print("You may not enter a negative value. Please try again.")
            else:
                valid = "yes"
    while valid == "yes":  # returns the valid input
        return float_number  # returns the value as a float


def test_word(word1, word2):
    """tests if an input is valid (valid inputs are word1 and word2)"""
    valid = "no"
    tested_word = 0
    while valid == "no":  # causes input request to repeat until a valid
        # input is given
        tested_word = input()
        if word1 == tested_word or word2 == tested_word:
            valid = "yes"
        else:
            print("That was not a valid response. Please try again.")
    while valid == "yes":  # returns the valid input
        return tested_word


def check_input(n):
    """Checks if the user has entered the proper input"""
    print("You have entered '" + str(n) + "'. Is this correct? Please enter "
                                          "'yes' or 'no'")
    return test_word("yes", "no")  # tests if the user entered yes or no


def def_product_title():
    """Determines the product title"""
    valid = "no"
    product_title = 0
    while valid == "no":  # causes input request to repeat until a valid
        # input is given
        product_title = input("Please enter a product title: ")
        test = check_input(product_title)  # checks if the user entered
        # the proper title
        if test == "yes":
            valid = "yes"
    while valid == "yes":
        return product_title


def def_product_cost_per_unit():
    """Determines the CPU of the product"""
    print("Please enter the estimated cost per unit of the product: ")
    product_cost = test_float_number()  # tests if the input is a valid number
    print("Please enter the estimated tax percentage(for 7%, enter '7'): ")
    tax = test_float_number() / 100  # tests if the input is a valid number and
    # divides by 100
    tax += 1  # adds 1 to tax
    return product_cost, tax  # returns both the product cost and tax


def def_smart_pricing():
    """
    Determines if a user would like to enable smart pricing as described below
    """
    print("Smart pricing will automatically decrease the cost of production "
          "based on the quantity being produced. 100+ units is 3% cheaper, "
          "500+ is 5% and 1000+ is 10%.\nWould you like to enable smart "
          "pricing? Please enter 'yes' or 'no'")
    smart_pricing = test_word("yes", "no")  # tests if the user entered yes
    # or no
    if smart_pricing == "yes":
        print("Smart pricing is now enabled.")
    return smart_pricing


def def_product_quantity(smart_pricing):
    """
    Determines the quantity of the product being bought and discount awarded
    """
    print("Please enter the number of units you would like produced: ")
    product_quantity = test_integer_number()  # tests if the input is
    # an integer
    if smart_pricing == "yes":  # determines the discount given from smart
        # pricing
        if product_quantity >= 1000:
            discount = .90
        elif product_quantity >= 500:
            discount = .95
        elif product_quantity >= 100:
            discount = .97
        else:
            discount = 1
    else:
        discount = 1
    return product_quantity, discount  # returns both the product quantity and
    # discount


def def_product_description():
    """Collects a product description"""
    product_description = input("Please enter a product description or press "
                                "enter to cancel: \n")
    if not product_description:  # returns a null value if the user presses
        # enter without an input
        return "empty"
    else:
        test = check_input(product_description)  # checks if the user entered
        # the proper description
        if test == "yes":
            return product_description


def calculate_cost(cpu, units, tax, smart_pricing, discount):
    """Calculates the total price with and without tax"""
    total_price_no_tax = 0
    total_price_with_tax = 0
    if smart_pricing != "yes":
        total_price_no_tax = cpu * units  # calculates the total price with tax
        total_price_with_tax = total_price_no_tax * tax  # calculates the
        # total price without tax
    elif smart_pricing == "yes":
        total_price_no_tax = cpu * units * discount  # calculates the total
        # price with tax
        total_price_with_tax = total_price_no_tax * tax  # calculates the total
        # price without tax
    return total_price_no_tax, total_price_with_tax  # returns the total price
    # with and without tax


def main():
    """The main function of the program"""
    print("Hello, welcome to this Program! It was designed to calculate the "
          "total cost of a wholesale purchase.\nYou may enter multiple items "
          "into the system; however, results will only be given for one "
          "product at a time.")
    print("To properly enter a product into the system, you will need a: "
          "product title, product cost, and production quantity.\nYou may "
          "choose to add a product description as well.")
    # welcome messages

    print("How many products would you like to enter?")
    number_of_products = test_integer_number()  # tests if the input
    # is an integer
    # determines the number of products the user would like to calculate
    # the price for

    for x in range(0, number_of_products):
        product_title = def_product_title()  # defines product title

        print("Would you like to enter a product description? Please enter "
              "'yes' or 'no'")
        description_preference = test_word("yes", "no")
        # determines if user would like to enter a product description

        if description_preference == "yes":
            product_description = def_product_description()
        else:
            product_description = "empty"
        # defines product description

        place_holder = def_product_cost_per_unit()  # placeholder for defining
        # product CPU and tax
        product_cost_per_unit = place_holder[0]
        tax = place_holder[1]

        smart_pricing = def_smart_pricing()  # determines if user would like
        # smart pricing

        place_holder = def_product_quantity(smart_pricing)  # placeholder for
        # defining product quantity and discount
        product_quantity = place_holder[0]
        discount = place_holder[1]

        place_holder = calculate_cost(product_cost_per_unit, product_quantity,
                                      tax, smart_pricing, discount)
        # placeholder for defining product cost with and without tax
        total_cost_no_tax = place_holder[0]
        total_cost_with_tax = place_holder[1]

        if product_description != "empty":
            print("Your project description for", product_title, "is: ",
                  product_description)
            # prints the product description if there is one

        print("If you were to purchase", format(product_quantity, '.0f'),
              product_title + ", it would cost $"
              + format(total_cost_no_tax, '.2f'), "without tax and $" +
              format(total_cost_with_tax, '.2f'),
              "with tax.\n")
        # prints the total price with and without tax


if __name__ == "__main__":
    main()
