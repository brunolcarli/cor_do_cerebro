from cerebro import Brain

class User():

    def __init__(self):
        self.nome = ''
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.brain_color = ''

    def calcular(self):
        '''Essa função calcula o resultado e retorna o tipo'''
        tipos = {
            'A': self.a,
            'B': self.b,
            'C': self.c,
            'D': self.d
        }

        total = tipos['A'] + tipos['B'] + tipos['C'] + tipos['D']

        if total != 120:  # o total tem que ser 120
            print("Total incorreto: %i" % (total))
        else:
            maior = max(tipos.values())  # ver qual dos tipos recebeu mais pontos

            for key, value in tipos.items():  # Mostra o resultado
                if value == maior:
                    return (key)  # Essa função retorna a chave que corresponde a cor do cerebro
                    # guarde essa função em uma variavel e use como argumento da classe cerebro


    def get_user_brain(self):
        tipo = self.calcular()
        this_brain = Brain(tipo)
        self.brain_color = this_brain.color

    def muda_nome(self, nome):
        self.nome = nome

    def add_value(self, a, b, c, d):
        self.a += a
        self.b += b
        self.c += c
        self.d += d

    def reset_value(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

