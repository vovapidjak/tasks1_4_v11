import json

def sol(arr):
    rows = len(arr)
    cols = len(arr[0])

    exclude_rows = []
    exclude_cols = []

    for i in range(rows):
        row_elements = set(arr[i])
        if len(row_elements) == 1:
            exclude_rows.append(i)

    for j in range(cols):
        column_elements = set(arr[i][j] for i in range(rows))
        if len(column_elements) == 1:
            exclude_cols.append(j)

    new_arr = [[arr[i][j] for j in range(cols) if j not in exclude_cols]\
               for i in range(rows) if i not in exclude_rows]

    return new_arr

with open('input.json') as inputfile:
    arr = json.load(inputfile)

newarr = sol(arr)

with open('output.json', 'w') as outfile:
    json.dump(newarr, outfile)

