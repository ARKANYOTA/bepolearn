from Get import getkey
import os
import readlist
def ikey():
	key = getkey()
	if key=="\x03":
		exit()
	return key

size0 = os.get_terminal_size()[0]
size1 = os.get_terminal_size()[1]
def clear():
	print("\033[1;1H\033[2J", end ="")
	print()
clear()


listechar = []
alllistechar = ['b', 'é', 'p', 'o', 'è', '^', 'v', 'd', 'l', 'j', 'z', 'w', 'ç', 'm', 'n', 'r', 's', 't', 'c', ',', 'e', 'i', 'u', 'a', 'à', 'ê', 'y', 'x', '.', 'k', "'", 'q', 'g', 'h', 'f']

Rmenu = True
nb = 0
with open("read.txt") as f:
	mots = []
	for i in f.readlines():
		mots += [i.replace("\n","")]
while True:
	clear()
	#  Print Number
	print("^C: Exit program")
	print("^R: Option de génération")

	Tkey = ikey()
	if Tkey=="\x12": #  Ctrl R
		Rmenu = True
		while Rmenu:
			clear()
			#  Print Number
			print("^C: Exit program")
			print("^E: Exit option de génération")
			print("^G: Genérér la liste")
			print("^D: Print Liste")
			print("Number of char : ", end ="")
			
			if nb == 0:
				print("All")
			elif nb == 1:
				print("NoOne")
			else :
				print(nb)
			print("Liste des charactères : " + str(listechar))
			Rkey = ikey()
			if Rkey=="\x05":
				Rmenu = False
			elif Rkey=="\x07":
				readlist.read(listechar, long=nb)
			elif Rkey=="\x04":
				print("Read:")
				with open("read.txt") as fic:
					for i in fic.readlines():
						print(i.replace("\t", "").replace("\n", ""))
				input("\npress for pass:")
			elif Rkey=="\x1b[A":
				nb = (nb+1)%25
			elif Rkey=="\x1b[B":
				nb = (nb-1)%25
			else:
				if Rkey in alllistechar:
					if Rkey in listechar:
						del listechar[listechar.index(Rkey)]
					else:
						listechar += [Rkey]

			
			

























"""
print("\033[1;1H\033[2J", end ="")
Texte = [
"Un texte répond de façon plus ou moins pertinente à des critères qui en déterminent la qualité littéraire.", 
"On retient en particulier la structure d'ensemble, la syntaxe et la ponctuation,", 
"l'orthographe lexicale et grammaticale, la pertinence et la richesse du vocabulaire,",
"la présence de figures de style, le registre de langue et la fonction recherchée",
"(narrative, descriptive, expressive, argumentative, injonctive, poétique).", 
"C'est l'objet de l'analyse littéraire."
]
Copy = []
for i in range(len(Texte)):
	Copy +=[""]
for i in Texte:
	print(i+"\n\n")
Nombre_de_Ligne = 0

while True:
	key = gk()
	if key=='\x03':
		print("exit")
		exit()
	elif key=='\x1b[A': #  UP
		pass
	elif key=='\x1b[B': #  DOWN
		pass
	elif key=='\x1b[C': #  LEFT
		pass
	elif key=='\x1b[D': #  RIGHT
		pass
	elif key=='\x7f':
		Copy[Nombre_de_Ligne] = Copy[Nombre_de_Ligne][:-2]
		print("\033[{0};1H".format(Nombre_de_Ligne*2+2)+" "*os.get_terminal_size()[0])
	Copy[Nombre_de_Ligne] += key
	print("\033[{0};1H".format(Nombre_de_Ligne*2+2)+Copy[Nombre_de_Ligne])
	print(bytes(key, "utf-8"))



# >>> F([[j**2+i**2 for j in range(-6,6)] for i in range(-6,6)])

"""