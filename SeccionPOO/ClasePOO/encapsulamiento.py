class A():
    def __init__(self):
        self.contador = 0  # 1

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador


class B():
   def __init__(self):
        self.__contador = 0  # 1

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

a = A()
a.incrementar()
a.incrementar()
print(a.cuenta())
print(a.contador)

b = B()
b.incrementar()
b.incrementar()
print(b.cuenta())
print(b._B__contador)
