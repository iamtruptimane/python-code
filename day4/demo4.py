#collection (list = [])

def func1():
    numbers = [1,2,3,4,5]

    print(numbers)
    print(f"type of numbers = {type(numbers)}")
    print(f"number of values in numbers = {len(numbers)}")

    for value in numbers:
         print(f"value = {value}")

    index_positions = [0, 1, 2, 3, 4]
    for index in index_positions:
        print(f"value at {index} = {numbers[index]}")

func1()


