# product = 1
# for n in range(1, 10):
#     product = product * n
# print(product)

def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x, to_celcius(x))