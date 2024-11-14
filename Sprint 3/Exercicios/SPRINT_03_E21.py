class Passaro:
    
    def __init__(self):
        pass

    def voar(self):
        return print("Voando...")

    
    def som(self):
        return print(f"{self.__class__.__name__} emitindo som ...")


class Pardal(Passaro):
        
    def __init__(self):
        super().__init__()
        return print("Pardal")

    
    def som_pardal(self):
        return print("Piu Piu")



class Pato(Passaro):
  
    def __init__(self):
        super().__init__()
        return print("Pato")

    
    def som_pato(self):
        return print("Quack Quack")

pato = Pato()
pato.voar()
pato.som()
pato.som_pato()

pardal = Pardal()
pardal.voar()
pardal.som()
pardal.som_pardal()