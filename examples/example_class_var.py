
class BaseVar:

    classvar = None


class DerivedClassA(BaseVar):

    def __init__(self):
        this_type = type(self)
        this_type.classvar = "DerivedClassA"
        return

class DerivedClassB(BaseVar):

    def __init__(self):
        this_type = type(self)
        this_type.classvar = "DerivedClassB"
        return


a = DerivedClassA()
b = DerivedClassB()

print(DerivedClassA.classvar)
print(DerivedClassB.classvar)
