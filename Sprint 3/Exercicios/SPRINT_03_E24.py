class Ordenadora:
    
    
    def __init__(self, lista):
        self.listaBaguncada = lista

    
    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada
    

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse = True)
        return self.listaBaguncada


crescente = Ordenadora([3,4,2,1,5])
print(crescente.ordenacaoCrescente())
decrescente = Ordenadora([9,7,6,8])
print(decrescente.ordenacaoDecrescente())
