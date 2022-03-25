class pessoa: #criar classe
    nome = "" #atributo da classe
    idade = 0 #atributo da classe

    #utiliza um construtor para a classe
    def __init__(self, nome = "", idade = 0): #cria um construtor
        self.nome = nome #self é para acessar os atributos da classe
        self.idade = idade #self é para acessar os atributos da classe

    def fazAniversario(self): #cria um metodo
        self.idade += 1 #determina o que o metodo faz

p1 = pessoa() #chamando a classe sem construtor
p1.nome = "Cristina" #determinar os atributos da classe
p1.idade = 44 #determinar os atributos da classe

p2 = pessoa("Jose", 88) #usando o construtor para chamar a classe
print("%s tem %d anos de idade."%(p2.nome,p2.idade)) #exibindo a mensagem na tela
p2.fazAniversario() #usando o método da classe
print("%s tem %d anos de idade."%(p2.nome,p2.idade)) #exibindo a mensagem na tela
