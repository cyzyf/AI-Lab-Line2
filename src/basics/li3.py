#函数练习

def greet(name, msg="Hi"):
    print(f"{msg} {name}")

def add(*args):
    return sum(args)

def show(name, **kwargs):
    print(name, kwargs)

greet("Amy")
print(add(1,2,3))
show("Bob", age=19, major="soft")
