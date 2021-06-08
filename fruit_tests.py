def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

def review_fruit(L):
    for x in L:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)

def print_with_indices(L):
    for i in range((0), len(L)):
        print("{} : {}".format(i,L[i]))

def add_fruit(L):
    print_with_indices(L)
    my_index = get_integer("Please enter the index number of the fruit you would like to add to: ")
    add_amount = get_integer("Please enter the amount of fruit you would like to add: ")
    new_amount = L[my_index][1] + add_amount
    L[my_index][1] = new_amount
    print("The amount of {} in the bowl has been increased to {}".format(L[my_index][0], new_amount))

def subtract_fruit(L):
    print_with_indices(L)
    my_index = get_integer("Please enter the index number of the fruit you would like to subtract from: ")
    subtract_amount = get_integer("Please enter the amount of fruit you would like to remove: ")
    new_amount = L[my_index][1] - subtract_amount
    L[my_index][1] = new_amount
    print("The amount of {} in the bowl has been decreased to {}".format(L[my_index][0], new_amount))

def new_fruit(L):
    new_name = get_string("Please enter the name of the new fruit you'd like to add: ")
    new_quantity = get_integer("Please enter the amount of fruit you'd like to add: ")
    new_fruit = [new_name, new_quantity]
    L.append(new_fruit)

def main():

    fruit_list = [
        ["apples", 2],
        ["pears", 0],
        ["oranges", 6],
        ["grapes", 72],
    ]

    my_menu = '''
    A: Review bowl contents
    B: End the program
    C: Add more fruit to the bowl
    D: Remove fruit from the bowl
    E: Add a different kind of fruit to the bowl
    '''

    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please enter your choice from the menu: ")
        if choice == "A":
            review_fruit(fruit_list)
        elif choice == "B":
            print("Program has ended")
            run = False
        elif choice == "C":
            add_fruit(fruit_list)
        elif choice == "D":
            subtract_fruit(fruit_list)
        elif choice == "E":
            new_fruit(fruit_list)
        else:
            print("Unrecognised input, please try again")
            return main()
    review_fruit(fruit_list)

main()