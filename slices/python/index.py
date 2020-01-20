import sys
import numpy as np

# Read the file
input_file = sys.argv[1]

file = open(input_file, 'r')
first_line = file.readline().split(' ')
max_slices = int(first_line[0])
amount_of_pizzas = int(first_line[1])
pizzas = np.array([int(pizza_slices) for pizza_slices in file.readline().split(' ')], dtype=np.uint32)
file.close()

# Do the math
max_values = np.empty((max_slices + 1, amount_of_pizzas + 1), dtype=np.uint32)
for index in range (0, max_slices + 1):
    max_values[index][0] = 0
for index in range (0, amount_of_pizzas + 1):
    max_values[0][index] = 0

for slices in range (1, max_slices + 1):
    for pizza_index in range (1, amount_of_pizzas + 1):
        slices_without_pizza = max_values[slices][pizza_index - 1]
        max_values[slices][pizza_index] = slices_without_pizza
        amount_of_slices = pizzas[pizza_index - 1]
        if amount_of_slices <= slices:
            slices_with_pizza = amount_of_slices + max_values[slices - amount_of_slices][pizza_index - 1]
            if (slices_with_pizza > slices_without_pizza):
                max_values[slices][pizza_index] = slices_with_pizza

# Final results
selected_pizzas = []
def find_solution(slices, pizza_index):
    if slices > 0 and pizza_index > 0:
        amount_of_slices = pizzas[pizza_index - 1]
        slices_without_pizza = max_values[slices][pizza_index - 1]
        slices_with_pizza = amount_of_slices + max_values[slices - amount_of_slices][pizza_index - 1]
        if amount_of_slices > slices or slices_without_pizza > slices_with_pizza:
            find_solution(slices, pizza_index - 1)
        else:
            selected_pizzas.append(str(pizza_index - 1))
            find_solution(slices - amount_of_slices, pizza_index - 1)

find_solution(max_slices, amount_of_pizzas)
selected_pizzas.sort()

# Write the output file
output_file = input_file[slice(-2)] + 'out'
file = open(output_file, 'w+')
file.write(str(len(selected_pizzas)) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
