# defining functions
def hello_world():
    print("hello world")


hello_world()


def square_it(number):
    return number ** 2


print(square_it(3))


def tip_cal(subtotal):
    tax_amt = subtotal * .18  # tax_amt CANNOT be used outside of def
    return tax_amt


def total_bill (bill_amt):
    total = bill_amt + tip_cal(bill_amt)
    print("your total bill is %d" % total)


total_bill(1000000000000)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) **2
    answer = inside ** 0.5 # this is a square root
    return answer


print(distance(0, 0, 3, 4))


def pythagorean (a, b):
    C = a ** 2 + b ** 2
    solution = C ** .5
    return solution


print(pythagorean(5, 12))