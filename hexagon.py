import turtle as tr

n = 6

def turtleDrawNgon(n):
    for i in range(n):
        tr.forward(50)
        tr.left(180 - ((n - 2) * 180) / n)

for i in range(n):
    tr.forward(50)
    tr.left(-(180 - ((n - 2) * 180) / n))
    turtleDrawNgon(n)



tr.done()