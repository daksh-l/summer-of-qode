item = input("What item do we find in the list of fruits? ")
list1 = ["apple", "mango", "banana", "kiwi", "grapes", "strawberry", "blueberry", "kiwi"]


def check_list(list1, item):
    if item in list1:
        print("The item is there in the list!")
    else:
        print("The item is NOT there in the list!")


check_list(list1, item)