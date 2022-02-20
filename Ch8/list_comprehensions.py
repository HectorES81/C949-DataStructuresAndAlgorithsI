print(10/1) #convert int to float
#list comprehensions
#square root even and cube odd numbers
my_nums = list(range(1,11))

print(my_nums)
def sq_or_cubes(i):
    if(i%2 == 0):
        return i**2
    return i**3

sq_cubes = [sq_or_cubes(i) for i in my_nums]
print(sq_cubes)

weight_fluctuation = [.1, -.6, .4, 1.5, -.8, 0]

print("Only recorded weight gains: ", [i for i in weight_fluctuation if i > 0])
print("Only recorded weight loses: ", [i for i in weight_fluctuation if i < 0])
