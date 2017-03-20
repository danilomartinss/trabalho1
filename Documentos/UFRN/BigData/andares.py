import numpy as np

def andares():
	andar = input ("Digite em qual andar deseja comecar: ")
	if andar > 0:
		return andar
	else:
		print "Digite numero de andar valido"
		return andares()

def rola_dado():
	return np.random.permutation(np.arange(1, 7))[1]

def sobe_desce(dice_number, andar):
	if dice_number <= 2 and andar > 0:
		andar -= 1
	elif dice_number > 2 and dice_number <= 5:
		andar += 1
	else:
		andar = andar + rola_dado()
	return andar

def probabilidade_andar0(andar):
	desceu = np.random.random(1)
	if desceu < 0.001:
		andar = 0
	return andar

andar = andares()
print andar

def Rounds(andar):
	Round = []
	for i in range(0, 100):
		andar = sobe_desce(rola_dado(), andar)
		Round.append(andar)
		andar = probabilidade_andar0(andar)
		Round[i] = andar
	return Round

print(Rounds(andar))

Games = []
for j in range(0,500):
	text = "Jogo " + str(j+1) + ": "
	Games.append(text)
	Games.append(Rounds(andar))

print Games