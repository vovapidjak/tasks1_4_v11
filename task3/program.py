class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def is_overlaps(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 < (self.r + other.r)**2

    def to_json(self):
        return {
            "x": self.x,
            "y": self.y,
            "r": self.r
        }




def sol(circles):
    j = {}
    Circle(**j)
    not_overlaping_circles = []
    for i in range(len(circles)):
        is_overlaping = False
        for j in range(i, len(circles)-1):
            if circles[i].is_overlaps(circles[j]):
                is_overlaping = True
                break
        if not is_overlaping:
            not_overlaping_circles.append(circles[i])
    return not_overlaping_circles

with open('input.json') as inputfile:
    arr = json.load(inputfile)

newarr = sol(arr)

with open('output.json', 'w') as outfile:
    json.dump(newarr, outfile)