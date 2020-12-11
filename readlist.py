def read(L, long=0,readfile="liste_francais.txt" , writefile="read.txt"):
	fr = open(readfile, "rb")
	fw = open(writefile, "w")
	ai = fr.readlines()
	for a in ai:
		#print(a.decode("ascii", "replace"))
		if k(a.decode("utf-8", "replace").replace("\n","").replace("\r",""), L, long):
			fw.write(a.decode("utf-8", "replace").replace("\n","").replace("\r","")+"\n")
	fr.close()
	fw.close()


def k(m, L, long=0):
	for i in m:
		if i not in L:
			return False
	if long==0:
		return True
	elif long==len(m):
		return True
	else:
		return False
