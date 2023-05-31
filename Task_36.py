# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(1, num_rows + 1):
        print(*list(map(lambda x: operation(x, i), range(1, num_columns + 1))))

print_operation_table(lambda x, y: x * y)
