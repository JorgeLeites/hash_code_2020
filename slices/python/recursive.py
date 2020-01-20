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
def find_solution(slices, pizza_index):
    print(slices, pizza_index)
    if slices > 0 and pizza_index > 0:
        amount_of_slices = pizzas[pizza_index - 1]
        solution_without_pizza = find_solution(slices, pizza_index - 1)
        if (amount_of_slices > slices):
            return solution_without_pizza
        solution_with_pizza = find_solution(slices - amount_of_slices, pizza_index - 1)
        solution_with_pizza['pizzas'].append(str(pizza_index - 1))
        solution_with_pizza['slices'] += amount_of_slices
        if solution_with_pizza['slices'] > solution_without_pizza['slices']:
            return solution_with_pizza
        else:
            return solution_without_pizza
    else:
        return {'pizzas': [], 'slices': 0}

solution = find_solution(max_slices, amount_of_pizzas)
print(solution['slices'])
selected_pizzas = solution['pizzas']
selected_pizzas.sort()

# Write the output file
output_file = input_file[slice(-2)] + 'out'
file = open(output_file, 'w+')
file.write(str(len(selected_pizzas)) + '\n')
file.write(' '.join(selected_pizzas))
file.close()
