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
max_values = [{'slices': 0, 'pizzas': [False for pizza in pizzas]}]

for index in range(1, max_slices + 1):
    candidate_values = max_values[index-1].copy()
    for pizza_number, pizza_slices in enumerate(pizzas):
        if pizza_slices > index:
            break  # The list of pizzas is in non descendent order,
                   # so if we find one that doesn't fit, we can stop checking

        # We have to find a set of selected pizzas that doesn't contain the current one
        valid_index = index - pizza_slices
        found_index = False
        while not found_index and index >= 0:
            if max_values[valid_index]['pizzas'][pizza_number]:
                valid_index -= 1
            else:
                found_index = True

        if found_index:
            current_slices = max_values[valid_index]['slices'] + pizza_slices
            if current_slices > candidate_values['slices']:
                candidate_values['slices'] = current_slices
                candidate_values['pizzas'] = max_values[valid_index]['pizzas'][:]
                candidate_values['pizzas'][pizza_number] = True
    max_values.append(candidate_values)

# Final results
total_pizzas = 0
selected_pizzas = []
for index, selected_pizza in enumerate(max_values[max_slices]['pizzas']):
    if selected_pizza:
        selected_pizzas.append(str(index))
        total_pizzas += 1

# Write the output file
output_file = input_file[slice(-2)] + 'out'
file = open(output_file, 'w+')
file.write(str(total_pizzas) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
