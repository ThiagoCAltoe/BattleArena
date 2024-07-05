import random

# Personagem: classe mãe
# Heroi: controlado pelo usuario
# Inimigo: Adversário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f'Nome: {self.__nome}\nVida: {self.__vida}\nNível: {self.__nivel}'

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano1 = self.__nivel * 1
        dano2 = self.__nivel * 2
        dano = random.randint(dano1, dano2)
        alvo.receber_dano(dano)
        print(f'{self.__nome} atacou {alvo.get_nome()} e causou {dano} de dano.')


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.__habilidade}\n'

    def ataque_especial(self, alvo):
        dano1 = self.get_nivel() * 2
        dano2 = self.get_nivel() * 5
        dano = random.randint(dano1, dano2)
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} usou {self.__habilidade} e causou {dano} de dano.')
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.__tipo}\n'

class Jogo:
    """Classe que controla o jogo"""
    def __init__(self) -> None:
        self.heroi = Heroi('Heroi', 100, 5, 'Super Força')
        self.inimigo = Inimigo('Morcego', 50, 3, 'Voador')

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print('Batalha iniciada!')
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input('Pressione enter para atacar...')
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")
            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print('Escolha inválida! Escolha novamente.')
        if self.heroi.get_vida() > 0:
            print('\nParabéns, Você venceu a batalha!')
        else:
            print('\nVocê foi derrotado!')

#criar istancia do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()
