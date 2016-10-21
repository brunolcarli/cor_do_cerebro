

class Brain():

    def __init__(self, tipo):
        self.tipo = tipo
        self.color = ''

        if self.tipo == "A":
            self.color = 'Amarelo'
        elif self.tipo == 'B':
            self.color = "Azul"
        elif self.tipo == 'C':
            self.color = 'Verde'
        elif self.tipo == "D":
            self.color = "Laranja"
