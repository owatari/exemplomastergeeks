class Soldado:
    def __init__(self, nome, vida, nacao, forca) -> None:
        self.nome = nome
        self.vida = vida
        self.nacao = nacao
        self.forca = forca

    def lutar(self, enemy):
        self.perderVida(enemy.forca)
        enemy.perderVida(self.forca)

        if (enemy.vida <= 0) and (self.vida > 0):
            print('Voce venceu')
        elif (enemy.vida <= 0) and (self.vida <= 0):
            print('Empatou')
        elif (self.vida <= 0) and (enemy.vida > 0):
            print('Voce venceu')
        
    def perderVida(self, damage):
        self.vida -= damage

    def regenerarVida(self):
        self.vida += 10

    def __str__(self) -> str:
        return f"O soldado {self.nome} tem {self.vida} de vida."

soldier1 = Soldado("Elementar", 100, "Brasil", 13)
print(soldier1)
soldier2 = Soldado("Juarez", 100, "Argentina", 11)
print(soldier2)

print("-"*30)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
soldier1.lutar(soldier2)
print(soldier1)
print(soldier2)