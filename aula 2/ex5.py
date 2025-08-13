''' Sobrescrita de Métodos: Crie uma classe Animal com o método som() que imprime "O animal faz
um som". Crie classes Cachorro e Gato que herdam de Animal e sobrescreva o método som() para
imprimir sons específicos para cada animal'''

class Animal:          
    def som(self):
        print("O animal faz um som")
        
#sobrrescreve o método som da classe Animal
class Cachorro(Animal):
    def som(self):
        print("O cachorro late")


class Gato(Animal):
    def som(self):
        print("O gato mia")        

    
Animal().som()  
Cachorro().som() 
Gato().som()  
  
