class A():
    def mensaje(self):
        print("Esta es la clase A")

    def primera(self):
        print("Estamos dentro de la clase A")


class B():
    def mensaje(self):
        print("Esta es la clase B")

    def segunda(self):
        print("Estas dentro de la clase B")


class C(B, A):
    pass


c = C()
c.primera()
c.segunda()
