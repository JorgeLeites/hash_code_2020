import sys

# Read the file
input_file = sys.argv[1]

file = open(input_file, 'r')
first_line = file.readline().split(' ')
max_slices = int(first_line[0])
amount_of_pizzas = int(first_line[1])
pizzas = [int(pizza_slices) for pizza_slices in file.readline().split(' ')]
file.close()

# Do the math
max_values = [[0] for pizza in pizzas]
max_values.append([0])
for index in range(1, max_slices + 1):
    max_values[0].append(0)

for index in range(1, max_slices + 1):
    print(str(100 * index / max_slices) + '%')
    for pizza_number, pizza_slices in enumerate(pizzas):
        pizza_number += 1
        if pizza_slices > index:
            max_values[pizza_number].append(max_values[pizza_number - 1][index])
        else:
            value_with = max_values[pizza_number - 1][index - pizza_slices] + pizza_slices
            value_without = max_values[pizza_number - 1][index]
            max_value = max(value_with, value_without)
            max_values[pizza_number].append(max_value)

# Final results
selected_pizzas = []
def find_solution(pizza_index, amount_index):
    if pizza_index > 0 and amount_index > 0:
        pizza_slices = pizzas[pizza_index - 1]
        if pizza_slices <= amount_index:
            value_with = max_values[pizza_index - 1][amount_index - pizza_slices] + pizza_slices
            value_without = max_values[pizza_index - 1][amount_index]
            if value_with > value_without:
                selected_pizzas.append(pizza_index - 1)
                find_solution(pizza_index - 1, amount_index - pizza_slices)
            else:
                find_solution(pizza_index - 1, amount_index)
        else:
            find_solution(pizza_index - 1, amount_index)

find_solution(amount_of_pizzas, max_slices)
selected_pizzas.sort()
selected_pizzas = [str(selected_pizza) for selected_pizza in selected_pizzas]

# Write the output file
output_file = input_file[slice(-2)] + 'out'
file = open(output_file, 'w+')
file.write(str(len(selected_pizzas)) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
