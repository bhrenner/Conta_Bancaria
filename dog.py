class Dog:
    especies = "Canis familiaris"
    def __init__(self, nome, idd, raca):
        self.nome = nome
        self.idd = idd
        self.raca = raca
        pass
    #def descricao(self):
    def __str__(self):
        return f'{self.nome} tem {self.idd} anos'
    
    def lingua(self, som):
        return f'{self.nome} disse: {som}'

    pass

class Pincher(Dog):
    def lingua(self, som='auaua auaua'):
        return f'{self.nome} diz {som}'
    pass

class Viralata(Dog):
    def lingua(self, som='Arf'):
        return super().lingua(som)
    pass

class Bulldog(Dog):
    
    pass

belinha = Pincher("Belinha", 15, 'Pincher')
max = Viralata("Max", 12, 'Vira-lata')
sabrina = Bulldog("Sabrina", 6, 'Labrador')
titico = Viralata('Titico', 5, 'Vira-lata')
layka = Dog('Laika', 8, 'Pastor-alemão')
#belinha.especies = "Cachorro" 
#belinha.lingua('Auau Auau')
#max.lingua('Bual Bual')
sabrina.lingua('Woof woof woof')
#titico.lingua('Rhrhhrhrhrhrh')
#layka.lingua('Auuuuuuu')

#print(belinha, max, sabrina, titico, layka)

print(belinha.especies)
print(belinha.lingua())

print(sabrina.lingua('Woof'))
print(max.lingua())
#print(type(belinha))
#print(belinha.nome, belinha.idd, belinha.especies)
#print(max.nome, max.idd, max.especies)