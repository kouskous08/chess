from posi_f_b import *
while True:
	print("")
	print(f"b: {nomsetat_b}")
	print(f"p: {posi_blanc}")
	print("")
	print(f"n: {nomsetat_b}")
	print(f"p: {posi_noir}")
	print("")
	a=input("ficha li 3ad 7arek :  ")#a=ficha li 3ad 7arek
	
	if a in noms_b:
		ap=noms_b.index(a)
		if ap==0:#ap= position d ficha li 3ad 7ark f liste d nom
			a=p_b_1
		elif ap==1:
			a=p_b_2
		elif ap==2:
			a=p_b_3
		elif ap==3:
			a=p_b_4
		elif ap==4:
			a=p_b_5
		elif ap==5:
			a=p_b_6
		elif ap==6:
			a=p_b_7
		elif ap==7:
			a=p_b_8
		elif ap==8:
			a=t_b_1
		elif ap==9:
			a=t_b_2
		elif ap==10:
			a=c_b_1
		elif ap==11:
			a=c_b_2
		elif ap==12:
			a=f_b_1
		elif ap==13:
			a=f_b_2
		elif ap==14:
			a=r_b
		elif ap==15:
			a=R_b
		if a["symbole"]=="P":
			m_a=pion(a["position"][0],a["position"][1])#ma=mvm posible d ficha a wu f mwata3 hta li 3amrin
		elif a["symbole"]=="C":
			m_a=cheval(a["position"][0],a["position"][1])

		elif a["symbole"]=="T":
			m_a=tour(a["position"][0],a["position"][1])

		elif a["symbole"]=="F":
			m_a=fou(a["position"][0],a["position"][1])

		elif a["symbole"]=="R":
			m_a=reine(a["position"][0],a["position"][1])

		elif a["symbole"]=="RO":
			m_a=roi(a["position"][0],a["position"][1])
		while True:
			if m_a==None or m_a==[]:
				print("had ficha ma i mkenchi d 7arka")

				break
			else:
				print("hahoma les mvm possible:")
				print(m_a)
				n=int(input("khtar ra9m d mvm:(0 pour changer de piece) "))#n = position d mvm f la liste m_a
				if n == 0:
					break
				if len(m_a)>= int(n):
					mjoue=int(n)-1#mjoue= position d mvm f la liste m_a mais li ki fehma python
					a["position"]=m_a[mjoue]#kd reja3 position d a hiya position li khtar joueur
					print("")
					print(f"{a['Nom']} 3ando position {a['position']}")
					break
				else:
					print("had mvm ma kaynchi 3afak dakhal ra9m d mvm li khesek  ")
					

	
	
	else:
		print("ficha ma kaynachi")