class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá! %s' %(id(self))

if __name__ == '__main__':
    nezio = Pessoa(nome='Nézio')
    luciano = Pessoa(nezio, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    Pessoa.olhos = 3
    del luciano.olhos
    print(luciano.__dict__)
    print(nezio.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(nezio.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(nezio.olhos))