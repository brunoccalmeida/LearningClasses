def arithmetic_arranger(a_list, answers=False):

    list_of_elements = []
    file_handler = open('arithmetic_arranger.txt', 'w+')

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

    list_of_first_operands = list_of_elements[::3]
    # Creates a list with only the first operands
    if len(list_of_first_operands) > 5:
        return f'Error: Too many problems.'

    list_of_operators_and_second_operands = list_of_elements[:]
    for i in list_of_first_operands:
        list_of_operators_and_second_operands.remove(i)
        # Creates a list with only the operators and second operands

    list_of_second_operands = list_of_elements[2::3]
    # Creates a list with only the second operands
    for operand in list_of_first_operands+list_of_second_operands:
        if not str(operand).isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(str(operand)) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    list_of_operands_as_tuples = []

    for index in range(len(list_of_first_operands)):
        list_of_operands_as_tuples.append((list_of_first_operands[index], list_of_second_operands[index]))
        # Creates a list of tuples with the operands of each operation from the original list

    list_of_operands = list_of_elements[1::3]  # Grabs only the operators from the original list
    for operator in list_of_operands:
        if operator not in "+-":
            return f"Error: Operator must be '+' or '-'."

    list_of_operators_and_second_operands_as_tuples = []

    for index in range(len(list_of_second_operands)):
        list_of_operators_and_second_operands_as_tuples.append((list_of_operands[index],
                                                                list_of_second_operands[index]))
        # Creates a list of tuples with the operands of each operation

    for count, element in enumerate(list_of_first_operands):
        # Gets the width of the biggest operand; writes the operand on the line with extra spaces for
        # the operator and the next operation (2 spaces for operator and 4 for the next operation);
        # writes the last operand without the 4 extra spaces. Operands are right aligned
        width = len(str(max(list_of_operands_as_tuples[count])))
        if count == len(list_of_first_operands)-1:
            file_handler.write(f'{element:>{width + 2}}')
            continue
        file_handler.write(f'{element:>{width+2}}    ')
    file_handler.write('\n')

    for count, operand in enumerate(list_of_operators_and_second_operands_as_tuples):
        # writes the second line with the operator and second operand with a space between them and four
        # spaces to the next operation
        width = len(str(max(list_of_operands_as_tuples[count])))
        if count == len(list_of_operators_and_second_operands_as_tuples)-1:
            file_handler.write(f'{operand[0]:<{2}}{operand[1]:>{width}}')
            continue
        file_handler.write(f'{operand[0]:<{2}}{operand[1]:>{width}}    ')
    file_handler.write('\n')

    for count in range(len(list_of_operands_as_tuples)):
        # writes N "-" symbols depending on the width of the biggest operand of the operation
        width = len(str(max(list_of_operands_as_tuples[count])))
        if count == len(list_of_operands_as_tuples)-1:
            file_handler.write(f'{"":-^{width + 2}}')
            continue
        file_handler.write(f'{"":-^{width+2}}    ')
    file_handler.write('\n')

    list_of_all_elements_as_tuples = []

    for index in range(len(list_of_second_operands)):
        list_of_all_elements_as_tuples.append((list_of_first_operands[index], list_of_operands[index] ,list_of_second_operands[index]))
        # Creates a list of tuples with all the elements

    if answers:
        # writes the answer to file if requested by function call
        for count, element in enumerate(list_of_all_elements_as_tuples):
            width = len(str(max(list_of_operands_as_tuples[count])))
            if element[1] == "+":
                result_of_operation = element[0] + element[2]
            else:
                result_of_operation = element[0] - element[2]
            if count == len(list_of_all_elements_as_tuples)-1:
                file_handler.write(f'{result_of_operation:>{width + 2}}')
                continue
            file_handler.write(f'{result_of_operation:>{width+2}}    ')

    file_handler.close()

    with open('arithmetic_arranger.txt', 'r') as fh:
        # takes out extra lines
        whole_file = fh.read().rstrip()

    return whole_file


if __name__ == '__main__':
    arithmetic_arranger(['3 + 855', '988 + 40'], True)
