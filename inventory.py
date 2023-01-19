
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product

        try:
            self.quantity = int(quantity)
        except ValueError:
            print(f"Error! Quantity not an integer for {product}")
            self.quantity = quantity 
        
        try:
            self.cost = int(cost)
        except ValueError:
            print(f"Error! cost not an integer for {product}")
            self.cost = cost

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost 

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        my_string = f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"
        return my_string

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:
        with open('inventory.txt', 'r') as file:
            lines = file.read().split("\n")

            #ignore the first line of the file, then take each line and split it into its attributes before creating a show object from the data
            lines = lines[1:]
            for line in lines:
                my_shoe = line.split(",")
                shoe_list.append(Shoe(my_shoe[0], my_shoe[1], my_shoe[2], my_shoe[3], my_shoe[4]))

    except FileNotFoundError:
        print("Error! File not found.")


def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    #capture the input variables for a new shoe from the user
    country = input("Enter the country: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    
    #infinite loop until 2 valid integers are entered
    while True:
        try:
            cost = int(input("Enter the cost: "))
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            "Error please enter a number for cost and quantity." 

    #create a new shoe object and it to the internal list 
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    #prepare the first line of text to add back to the file 
    try:
        with open('inventory.txt', 'r') as file:
            my_text = file.read().split("\n")

        my_list = []
        my_list.append(my_text[0])

        #build a list with all the shoes objects in string format 
        for my_shoe in shoe_list:
            my_list.append(str(my_shoe))

        with open('inventory.txt', 'w') as file:
            file.write("\n".join(my_list))
        
    except FileNotFoundError:
        print("Error! File not found.")
    

    

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for my_shoe in shoe_list:
        print(my_shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    #variables to keep track of the loqest quantity and the index in the list of that shoe
    lowest_quantity = shoe_list[0].quantity
    my_index = ""

    #loop through the whole list and find the lowest quantity shoe and it's index
    for i, my_shoe in enumerate(shoe_list):
        if my_shoe.quantity < lowest_quantity:
            lowest_quantity = my_shoe.quantity
            my_index = i
            

    print(f"The lowest quantity shoe is:    {shoe_list[my_index].product}")
    print(f"Quantity:                       {shoe_list[my_index].quantity}")

    #update the value of the shoe quantity in the shoe list
    while True:
        try:
            update = int(input("Enter the quantity of shoes to add to the stock: "))
            shoe_list[my_index].quantity += update
            break
        except ValueError:
            print("Error! Please enter an integer.")


    #read the file to get the first line, then add the updated shoe list onto the data and write it back to the file
    try:
        with open('inventory.txt', 'r') as file:
            my_text = file.read().split("\n")

        my_list = []
        my_list.append(my_text[0])

        for my_shoe in shoe_list:
            my_list.append(str(my_shoe))

        with open('inventory.txt', 'w') as file:
            file.write("\n".join(my_list))
        
    except FileNotFoundError:
        print("Error! File not found.")

    




def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    my_code = input("Please enter the shoe code to search for: ")

    for shoe in shoe_list:
        if shoe.code == my_code:
            print(f"Shoe found! \n{shoe}")
            return shoe

    print("Shoe not found.")
    return None




def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        print(f"The total value of {shoe.product} is {shoe.quantity * shoe.cost}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_qty = 0
    highest_shoe = None

    for shoe in shoe_list:
        if shoe.quantity > highest_qty:
            highest_qty = shoe.quantity
            highest_shoe = shoe
    print(f"The highest quantity shoe is {highest_shoe.product} with {highest_shoe.quantity}")
    print(f"{highest_shoe.product} is for sale.")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
selection = 0
read_shoes_data()

while selection != -1:
    print("Please select from one of the following options: ")
    print("1.) View all shoes")
    print("2.) Re-stock lowest quantity shoe")
    print("3.) Search for a shoe")
    print("4.) Display total values")
    print("5.) Find highest quantity shoe")
    print("6.) Add a new shoe")
    print("-1 to quit.")

    try:
        selection = int(input())
    except ValueError:
        print("Error! Please select from 1-5, or -1 to exit.")
        pass

    if selection == 1:
        view_all()
    elif selection == 2:
        re_stock()
    elif selection == 3:
        seach_shoe()
    elif selection == 4:
        value_per_item()
    elif selection == 5:
        highest_qty()
    elif selection == 6:
        capture_shoes()
    
    

