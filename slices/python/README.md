## Memoization

The `memoization` algorithm returns an optimum solution for the dataset.
It outputs a file on the same directory than the input file with the extension `.out`.

**Use:**

```shell
python3 memoization.py <file_path>
```

**Example:**

```shell
python3 memoization.py ../data_sets/a_example.in
```

⚠️ **Warning:** the amount of memory used is `O(n * w)`, with n being the number of pizzas
and w the maximum number of slices. **Do not use with big datasets**
(`d_quite_big.in` and `e_also_big.in`).

## Add biggest

This algorithm gives an approximate answer. In an average dataset the ammount of missing
slices will be smaller than the amount of slices of the smallest pizza. For the big datasets
this is good enough.

**Use:**

```shell
python3 add_biggest.py <file_path>
```

**Example:**

```shell
python3 add_biggest.py ../data_sets/a_example.in
```

## Analyze results

This file will log information about the given solutions.
This information is:

- Maximum slices: the maximum amount of slices allowed on the solution.
- Selected slices: the sum of the slices of the selected pizzas.
- Missing slices: the slices that were not selected (maximum slices - selected slices).
- Success percentage: the percentage of selected slices over maximum slices.

**Use:**

```shell
python3 analyze_solution.py <file_path>
```

**Example:**

```shell
python3 analyze_solution.py ../data_sets/a_example.in
```
