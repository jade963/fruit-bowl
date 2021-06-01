def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)

def main():

    fruit_list = [
        ["apples", 2],
        ["pears", 0],
        ["oranges", 6],
        ["grapes", 72],
    ]
    review_fruit(fruit_list)

main()