class cadeira:
    tipoEstofado = ""
    qtdPernas = 0

    #utiliza um construtor para cada classe
    def __init__(self, tipoEstofado = "Pano", qtdPernas = 4): #cria um construtor
        self.tipoEstofado = tipoEstofado #self é para acessar os atributos da classe
        self.qtdPernas = qtdPernas

    def descricao(self):
        print("Esta cadeira de %s tem %d pernas." %(self.tipoEstofado, self.qtdPernas))
       

c1 = cadeira("veludo", 4) #usando o construtor para chamar a classe



c1.descricao()