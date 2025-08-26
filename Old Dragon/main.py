from personagem import Personagem
from raca import Raca
from classe import Classe
from elfo import Elfo
from gnomo import Gnomo
from halfling import Halfling
from humano import Humano
from meio_elfo import MeioElfo
from classico import Classico
from aventureiro import Aventureiro
from heroico import Heroico
from anao import Anao
from clerigo import Clerigo
from guerreiro import Guerreiro
from ladrao import Ladrao
from mago import Mago


def permitir_distribuicao(valores_rolados):
    print(f"\nRolagens disponíveis: {sorted(valores_rolados)}")
    print("Agora, distribua esses valores entre os 6 atributos.")

    valores_disponiveis = sorted(valores_rolados)
    atributos_finais = []
    nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    for nome in nomes_atributos:
        while True:
            try:
                valor = int(input(f"Digite o valor para {nome} (disponíveis: {valores_disponiveis}): "))
                if valor in valores_disponiveis:
                    atributos_finais.append(valor)
                    valores_disponiveis.remove(valor)
                    break
                else:
                    print("Valor inválido ou já utilizado. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    return atributos_finais

def mostrar_raca(personagem):

    print("\n\n")
    print(f"Raça: {personagem.raca.__class__.__name__}")
    print(f"Alinhamento: {personagem.raca.alinhamento}")
    print(f"Infravisao: {personagem.raca.infravisao}")
    print(f"Movimento: {personagem.raca.movimento}")

def mostar_classe(personagem):

    print("\n\n")
    print(f"Classe: {personagem.classe.__class__.__name__}")
    print(f"Armadura: {personagem.classe.armadura}")
    print(f"Armas: {personagem.classe.armas}")
    print(f"Itens magicos: {personagem.classe.intensMagigos}")


def main():
    print("--- Gerador de Atributos de Personagem ---")
    estilo = input("Escolha o estilo de geração (classico, aventureiro, heroico): ").strip().lower()


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
    

    if estilo == "classico":
        atributos_finais = valores_gerados
    else:
        atributos_finais = permitir_distribuicao(valores_gerados)
        
    if len(atributos_finais) != 6:
        print("\nOcorreu um erro na geração dos atributos.")
        return

    for nome_atributo, valor_atributo in zip(Personagem.atributos_nomes,atributos_finais):
        setattr(personagem, nome_atributo, valor_atributo )



    print("--- Escolha a Raça do Personagem ---")
    raca_personagem = input("[anao] [elfo] [gnome] [halfling] [humano] [meio-elfo] ").strip().lower()

    if raca_personagem == "anao":
        personagem.raca = Anao()
    elif raca_personagem == "elfo":
        personagem.raca = Elfo()
    elif raca_personagem == "gnomo":
        personagem.raca = Gnomo()
    elif raca_personagem == "halfling":
        personagem.raca = Halfling()
    elif raca_personagem == "humano":
        personagem.raca = Humano()
    elif raca_personagem == "meio-elfo":
        personagem.raca = MeioElfo()
    else:
        print("Raça inválida!")
        return

    personagem.mostrar_atributos()


    mostrar_raca(personagem)

    print("--- Escolha a Classe do Personagem ---")
    classe_personagem = input("[clerico] [guerreiro] [ladra] [mago] ").strip().lower()

    if classe_personagem == "clerico":
        personagem.classe = Clerigo()
    elif classe_personagem == "guerreiro":
        personagem.classe = Guerreiro()
    elif classe_personagem == "ladrao":
        personagem.classe = Ladrao()
    elif classe_personagem == "mago":
        personagem.classe = Mago()
    else:
        print("Classe inválida!")
        return

    mostar_classe(personagem)


if __name__ == "__main__":
    main()
