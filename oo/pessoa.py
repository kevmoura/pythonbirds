class Pessoa:
    olhos =2
       
    def __init__(self,*filhos,nome=None,idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__=='__main__':
    renzo = Pessoa('Renzo')
    luciano = Pessoa(renzo,nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome='Ramalho'
#__dict__apresenta todos os atributos criados no __init__ e os atributos dinâmicos (exemplo sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(luciano.olhos)
    print(renzo.olhos)