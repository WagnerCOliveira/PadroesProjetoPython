class University(type):

    def __call__(cls, *args, **kwargs):
        print(f'==== Estes são os arqgumentos: {args}')
        return type.__call__(cls, *args, **kwargs)


class Geek(metaclass=University):
    def __int__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

obj = Geek(42, 23)

print(obj)