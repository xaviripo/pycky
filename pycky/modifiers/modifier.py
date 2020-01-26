class Modifier:
    def __init__(self):
        self.classes = {}
    def modifier(self, cls):
        def inner(func):
            self.classes[cls] = func
            return func
        return inner
    def __call__(self, arg):
        for cls in self.classes:
            if type(arg) is cls:
                return self.classes[cls](arg)
        raise Exception("{} not registered for modifier {}".format(
            repr(type(arg)), repr(self)
        ))

# fa = Modifier()

# @fa.modifier(int)
# def f(a):
#     print("int!")

# @fa.modifier(str)
# def f(a):
#     print("str!")

# fa("a")
# fa(1)
# fa("a")

# print(f.classes)