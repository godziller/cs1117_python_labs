height = float(input('input height: '))
reboundNo = 0

while height >= 0.001:
    reboundHeight = height / 2
    height = reboundHeight
    reboundNo = reboundNo +1
    print(f"rebound number {reboundNo} is: {reboundHeight}")