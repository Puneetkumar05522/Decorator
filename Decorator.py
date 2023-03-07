#Main function 
def num():
    print("Hello This is Puneet")

#Decorator function

def deco(arg):
    def inner():
        print("Before decorating function")
        arg()
        print("After Decorating function")
    return inner

result = deco(num)
result()
# Another Decorator programme
def super(arg):
    def inner(a, b):
        if a < b:
            a, b = b, a
        arg(a, b)
    return inner
@super
def sum(a, b):
    print(a+b)
sum(5, 5)