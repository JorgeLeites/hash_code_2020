import sys

# Read the file
input_file = sys.argv[1]

file = open(input_file, 'r')
first_line = file.readline().split(' ')
max_slices = int(first_line[0])
amount_of_pizzas = int(first_line[1])
pizzas = [int(pizza_slices) for pizza_slices in file.readline().split(' ')]
file.close()

max_values = [{'previous_answer': None, 'added_pizza': None}]

# Helper functions


def containsPizza(pizza, index):
    if max_values[index]['previous_answer'] == None:
        return False
    if max_values[index]['added_pizza'] == pizza:
        return True
    return containsPizza(pizza, max_values[index]['previous_answer'])


def sumSlices(index):
    if max_values[index]['previous_answer'] == None:
        return 0
    previous_slices = sumSlices(max_values[index]['previous_answer'])
    pizza_slices = 0
    if max_values[index]['added_pizza'] != None:
        pizza_slices = pizzas[max_values[index]['added_pizza']]
    return previous_slices + pizza_slices


# Do the math
for index in range(1, max_slices + 1):
    print(str(100 * index / max_slices) + '%')
    candidate_values = {'previous_answer': index - 1, 'added_pizza': None}
    candidate_slices = sumSlices(index - 1)
    for pizza_number, pizza_slices in enumerate(pizzas):
        if pizza_slices > index:
            break  # The list of pizzas is in non descendent order,
            # so if we find one that doesn't fit, we can stop checking

        # We have to find a set of selected pizzas that doesn't contain the current one
        valid_index = index - pizza_slices
        found_index = False
        while not found_index and index >= 0:
            if containsPizza(pizza_number, valid_index):
                valid_index -= 1
            else:
                found_index = True

        if found_index:
            current_slices = sumSlices(valid_index) + pizza_slices
            if current_slices > candidate_slices:
                candidate_values['previous_answer'] = valid_index
                candidate_values['added_pizza'] = pizza_number
                candidate_slices = current_slices
    max_values.append(candidate_values)

# Final results
total_pizzas = 0
selected_pizzas = []
index = max_slices
while max_values[index]['previous_answer'] != None:
    if max_values[index]['added_pizza'] != None:
        total_pizzas += 1
        selected_pizzas.append(str(max_values[index]['added_pizza']))
    index = max_values[index]['previous_answer']

# Write the output file
output_file = input_file[slice(-3)] + '_pointers.out'
file = open(output_file, 'w+')
file.write(str(total_pizzas) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
