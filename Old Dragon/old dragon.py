import random

# --- CLASSE DADO ---
class Dado:
    def __init__(self, lados):
        self.lados = lados
    def rolar(self):
        return random.randint(1, self.lados)

# --- CLASSE PERSONAGEM ---
class Personagem:
    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        
    
    def mostrar_atributos(self):
        print("\n--- Atributos Finais do Personagem ---")
        print(f"Força:         {self.forca}")
        print(f"Destreza:      {self.destreza}")
        print(f"Constituição:  {self.constituicao}")
        print(f"Inteligência:  {self.inteligencia}")
        print(f"Sabedoria:     {self.sabedoria}")
        print(f"Carisma:       {self.carisma}")

    def gerar_atributos(self):
        atributos = []
        for _ in range(6):
            soma_da_rolagem = 0
            for _ in range(3):
                soma_da_rolagem += self.dado.rolar()
            atributos.append(soma_da_rolagem)
        return atributos    

# --- CLASSE DO PERSONAGEM CLÁSSICO ---

class Classico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "classico"
        self.dado = Dado(6)

    def mostrar_atributos(self):
        print("\nEstilo: Clássico")
        super().mostrar_atributos()
        
# --- CLASSE DO PERSONAGEM AVENTUREITO ---
class Aventureiro(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "aventureiro"
        self.dado = Dado(6)

    def gerar_atributos(self):
        atributos_rolados = []
        for _ in range(6):
            soma_da_rolagem = 0
            for _ in range(3):
                soma_da_rolagem += self.dado.rolar()
            atributos_rolados.append(soma_da_rolagem)
        return atributos_rolados
    
    def mostrar_atributos(self):
        print("\nEstilo: Aventureiro")
        super().mostrar_atributos()
      
# --- CLASSE DO PERSONAGEM HEROICO ---
class Heroico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = "heroico"
        self.dado = Dado(6)
    
    def gerar_atributos(self):
        atributos_rolados = []
        for _ in range(6):
            rolagens_individuais = []
            for _ in range(4):
                rolagens_individuais.append(self.dado.rolar())
            
            rolagens_individuais.remove(min(rolagens_individuais))
            soma_final = sum(rolagens_individuais)
            atributos_rolados.append(soma_final)
        return atributos_rolados
    
    def mostrar_atributos(self):
        print("\nEstilo: Heroico")
        super().mostrar_atributos()

# --- FUNÇÃO AUXILIAR DA MAIN ---

def permitir_distribuicao(valores_rolados):
  
    print(f"\nRolagens disponíveis: {sorted(valores_rolados)}")
    print("Agora, distribua esses valores entre os 6 atributos.")
    
    valores_disponiveis = sorted(valores_rolados)
    atributos_finais = []
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    for nome in nomes_atributos:
        while True:
            try:
                valor_str = input(f"Digite o valor para {nome} (disponíveis: {valores_disponiveis}): ")
                valor_int = int(valor_str)
                if valor_int in valores_disponiveis:
                    atributos_finais.append(valor_int)
                    valores_disponiveis.remove(valor_int)
                    break
                else:
                    print("Valor inválido ou já utilizado. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    return atributos_finais

# --- FUNÇÃO PRINCIPAL ---

def main():
    print("--- Gerador de Atributos de Personagem ---")
    estilo = input("Escolha o estilo de geração (classico, aventureiro, heroico): ").strip().lower()

    personagem = None

    if estilo == "classico":
        personagem = Classico()
    elif estilo == "aventureiro":
        personagem = Aventureiro()
    elif estilo == "heroico":
        personagem = Heroico()
    else:
        print("Estilo inválido.")
        return

    valores_gerados = personagem.gerar_atributos()
    
    atributos_finais = []
    if estilo == "classico":
        atributos_finais = valores_gerados
    else:
        atributos_finais = permitir_distribuicao(valores_gerados)
        
    if len(atributos_finais) != 6:
        print("\nOcorreu um erro na geração dos atributos.")
        return

    personagem.forca, personagem.destreza, personagem.constituicao, personagem.inteligencia, personagem.sabedoria, personagem.carisma = atributos_finais
    
    personagem.mostrar_atributos() 


if __name__ == "__main__":
    main()
