import sys

# Read the files
input_file = sys.argv[1]
output_file = input_file[slice(-2)] + 'out'

file = open(input_file, 'r')
first_line = file.readline().split(' ')
max_slices = int(first_line[0])
amount_of_pizzas = int(first_line[1])
pizzas = [int(pizza_slices) for pizza_slices in file.readline().split(' ')]
file.close()

file = open(output_file, 'r')
amount_selected_pizzas = int(file.readline())
selected_pizzas = [int(pizza) for pizza in file.readline().split(' ')]
file.close()

# Do the math
selected_slices = 0
for index in range(0, amount_selected_pizzas):
    selected_slices += pizzas[selected_pizzas[index]]

missing_slices = max_slices - selected_slices
percentage = 100 * selected_slices / max_slices

# Print the results
print('Maximum slices: {}'.format(max_slices))
print('Selected slices: {}'.format(selected_slices))
print('Missing slices: {}'.format(missing_slices))
print('Success percentage: {}%'.format(percentage))
