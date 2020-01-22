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
selected_pizzas = []
total_sum = 0
for index in range(amount_of_pizzas - 1, -1, -1):
    slices_sum = total_sum + pizzas[index]
    if slices_sum <= max_slices:
        total_sum = slices_sum
        selected_pizzas.append(str(index))

print(total_sum)
selected_pizzas.reverse()

# Write the output file
output_file = input_file[slice(-2)] + 'out'
file = open(output_file, 'w+')
file.write(str(len(selected_pizzas)) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
