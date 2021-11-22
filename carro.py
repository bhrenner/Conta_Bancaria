class carro:
    def __init__(self, cor, km):
        self.cor = cor
        self.km = km

    def __str__(self):
       return f'\nO carro {self.cor} tem {self.km} km rodado.' 

carro_azul = carro(cor='Azul', km=20_000)
carro_vermelho = carro(cor='Vermelho', km=30_000)

#print(carro_azul, carro_vermelho)
for carro in (carro_vermelho, carro_azul):
    print(f'O carro {carro.cor} tem {carro.km} km rodado.')