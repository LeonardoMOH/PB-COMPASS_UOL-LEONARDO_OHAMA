class Ordenadora:
    
    def __init__(self):
        self.listaBaguncada = []

    
    def ordenacaoCrescente(self, lista):
        self.listaBaguncada = lista
        self.listaBaguncada.sort()
        return self.listaBaguncada
    

    def ordenacaoDecrescente(self, lista):
        self.listaBaguncada = lista
        self.listaBaguncada.sort(reverse = True)
        return self.listaBaguncada


listaBaguncada = Ordenadora()
print(listaBaguncada.ordenacaoCrescente([3,4,2,1,5]))

print(listaBaguncada.ordenacaoDecrescente([9,7,6,8]))
