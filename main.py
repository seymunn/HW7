def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        for y in range(1, num_columns + 1):
            res = operation(x, y)
            print(res, end='\t')
        print()


print_operation_table(lambda x, y: x * y)
