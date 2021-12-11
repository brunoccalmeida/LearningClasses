def arithmetic_arranger(a_list, answers=False):

    list_of_elements = []

    for item in a_list:
        # Iterates through the string list and returns a list of all its elements, converting the strings to integers,
        # when possible
        elements = item.split()
        for element in elements:
            try:
                element = int(element)
            except:
                pass
            list_of_elements.append(element)

    list_of_first_elements = list_of_elements[::3]
    # Creates a list with only the first operands

    list_of_operands_and_second_elements = list_of_elements[:]
    for i in list_of_first_elements:
        list_of_operands_and_second_elements.remove(i)
        # Creates a list with only the operators and second operands

    list_of_second_elements = list_of_elements[2::3]
    # Creates a list with only the second operands

    list_of_operands_as_tuples = []

    for index in range(len(list_of_first_elements)):
        list_of_operands_as_tuples.append((list_of_first_elements[index], list_of_second_elements[index]))
        # Creates a list of tuples with the operands of each operation

    list_of_operands = list_of_elements[1::3]
    list_of_operands_and_second_elements_as_tuples = []

    for index in range(len(list_of_second_elements)):
        list_of_operands_and_second_elements_as_tuples.append((list_of_operands[index], list_of_second_elements[index]))
        # Creates a list of tuples with the operands of each operation

    for count, element in enumerate(list_of_first_elements):
        width = len(str(max(list_of_operands_as_tuples[count])))
        print(f'{element:>{width+2}}', end="    ")
    print()

    for count, operand in enumerate(list_of_operands_and_second_elements_as_tuples):
        width = len(str(max(list_of_operands_as_tuples[count])))
        print(f'{operand[0]:<{2}}{operand[1]:>{width}}', end="    ")
    print()

    for count in range(len(list_of_operands_as_tuples)):
        width = len(str(max(list_of_operands_as_tuples[count])))
        print(f'{"":-^{width+2}}', end="    ")
    print()

    list_of_all_elements_as_tuples = []

    for index in range(len(list_of_second_elements)):
        list_of_all_elements_as_tuples.append((list_of_first_elements[index], list_of_operands[index] ,list_of_second_elements[index]))
        # Creates a list of tuples with all the elements

    if answers:
        for count, element in enumerate(list_of_all_elements_as_tuples):
            width = len(str(max(list_of_operands_as_tuples[count])))
            if element[1] == "+":
                result_of_operation = element[0] + element[2]
            else:
                result_of_operation = element[0] - element[2]

            print(f'{result_of_operation:>{width+2}}', end="    ")


if __name__ == '__main__':
    arithmetic_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    arithmetic_problems2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    arithmetic_arranger(arithmetic_problems, True)
    print("\n"*2)
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
