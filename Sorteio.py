# Sorteio.stf
import random

participantes = [
    "MIN. ALEXANDRE DE MORAES",
    "MIN. CAROLINA DE TONI",
    "MIN. GILMAR MENDES"
]

def adicionar_participante(nome):
    """Adiciona um participante à lista."""
    if nome not in participantes:
        participantes.append(nome)
        print(f"{nome} foi adicionado com sucesso.")
    else:
        print(f"{nome} já está na lista.")

def remover_participante(nome):
    """Remove um participante da lista."""
    if nome in participantes:
        participantes.remove(nome)
        print(f"{nome} foi removido com sucesso.")
    else:
        print(f"{nome} não está na lista.")

def realizar_sorteio():
    """Realiza o sorteio entre os participantes."""
    if not participantes:
        print("Não há participantes para o sorteio.")
        return None
    vencedor = random.choice(participantes)
    print(f"O vencedor do sorteio é: {vencedor}")
    return vencedor
if __name__ == "__main__":
    print("Participantes iniciais:", participantes)
    realizar_sorteio()
