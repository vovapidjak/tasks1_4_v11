import json
def sol(arr, n):
    temp = sorted(set(arr))

    return temp[:n]


with open('input.json') as inputfile:
    data = json.load(inputfile)
    arr = data["1"]
    n = data["2"]

result = sol(arr,n)

with open('output.json', 'w') as outfile:
    json.dump({"result": result}, outfile)