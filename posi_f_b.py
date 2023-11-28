#l = [  0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ] hado ar9am li 3andom 3ala9a b li ta7t bihom 0 f liste lowla hiya A wu tania hiya 1
L_x= [ "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" ]
c_x= [ 355 , 455 , 555 , 655 , 755 , 855 , 955 ,1055 ]
L_y= [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" ]
c_y =[ 900 , 800 , 700 , 600 , 500 , 400 , 300 , 200 ]
# x y = homa  coordone d le plan d  table d les echec
#L = liste
#p = position za3ma dik 7arf chmen martaba 3ando f la liste
#e = element d la liste
#mvm = mouvement kfx ki mken d f7ark la piece
#c = coordone dans la zone

pion_v=1
fou_v=2
cheval_v=3
tour_v=5
reine_v=10
roi_v=100
def place_pleine_a(pp):#pp place pleine	a=ami
	a=p_b_1["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")

	a=p_b_2["position"]		
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_3["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_4["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_5["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_6["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_7["position"]
	if a in pp:
		pp.remove(a)		
		print(f"mota3 {a} 3amra (pion biat)")
	a=p_b_8["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (pion biat)")
	a=t_b_1["position"]
	if a in pp:
		pp.remove(a)		
		print(f"mota3 {a} 3amra (tour biat)")
	a=t_b_2["position"]
	if a in pp:
		pp.remove(a)		
		print(f"mota3 {a} 3amra (tour biat)")
	a=f_b_1["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (fou biat)")
	a=f_b_2["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (fou biat)")
	a=c_b_1["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (cheval biat)")
	a=c_b_2["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (cheval biat)")
	a=r_b["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (reine biat)")
	a=R_b["position"]
	if a in pp:
		pp.remove(a)
		print(f"mota3 {a} 3amra (roi biat )")	

	return(pp)

def place_pleine_e(pp):#pp place pleine	e=enemi
	if p_n_1["position"] in pp:
		print(f"mota3 {p_n_1['position']} 3amra (pion k7al)")
			
	if p_n_2["position"] in pp:
		print(f"mota3 {p_n_2['position']} 3amra (pion k7al)")
	
	if p_n_3["position"] in pp:
		print(f"mota3 {p_n_3['position']} 3amra (pion k7al)")

	
	if p_n_4["position"] in pp:
		
		print(f"mota3 {p_n_4['position']} 3amra (pion k7al)")
	
	if p_n_5["position"] in pp:
		
		print(f"mota3 {p_n_5['position']} 3amra (pion k7al)")
	
	if p_n_6["position"] in pp:
		print(f"mota3 {p_n_6['position']} 3amra (pion k7al)")
	
	if p_n_7["position"] in pp:
		
		print(f"mota3 {p_n_7['position']} 3amra (pion k7al)")
	
	if p_n_8["position"] in pp:
		
		print(f"mota3 {p_n_8['position']} 3amra (pion k7al)")
	
	if t_n_1["position"] in pp:	
		print(f"mota3 {t_n_1['position']} 3amra (tour k7al)")
	
	if t_n_2["position"] in pp:
				
		print(f"mota3 {t_n_2['position']} 3amra (tour k7al)")
	
	if f_n_1["position"] in pp:
		
		print(f"mota3 {f_n_1['position']} 3amra (fou k7al)")
	
	if f_n_2["position"] in pp:
		
		print(f"mota3 {f_n_2['position']} 3amra (fou k7al)")
	
	if c_n_1["position"] in pp:
		
		print(f"mota3 {c_n_1['position']} 3amra (cheval k7al)")
	
	if c_n_2["position"] in pp:
		
		print(f"mota3 {c_n_2['position']} 3amra (cheval k7al)")
	
	if r_n["position"] in pp:
		
		print(f"mota3 {r_n['position']} 3amra (reine k7al)")
	
	if R_n["position"] in pp:
		
		print(f"mota3 {R_n['position']} 3amra (roi k7al)")	

	return(pp)


p_b_1 = {
    "Nom": "pion1",
    "symbole": "P",
    "position": ["A", "2"],
    "etat": "v"
}

p_b_2 = {
    "Nom": "pion2",
    "symbole": "P",
    "position": ["B", "2"],
    "etat": "v"
}

p_b_3 = {
    "Nom": "pion3",
    "symbole": "P",
    "position": ["C", "2"],
    "etat": "v"
}

p_b_4 = {
    "Nom": "pion4",
    "symbole": "P",
    "position": ["D", "2"],
    "etat": "v"
}

p_b_5 = {
    "Nom": "pion5",
    "symbole": "P",
    "position": ["E", "2"],
    "etat": "v"
}

p_b_6 = {
    "Nom": "pion6",
    "symbole": "P",
    "position": ["F", "2"],
    "etat": "v"
}

p_b_7 = {
    "Nom": "pion7",
    "symbole": "P",
    "position": ["G", "2"],
    "etat": "v"
}

p_b_8 = {
    "Nom": "pion8",
    "symbole": "P",
    "position": ["H", "2"],
    "etat": "v"
}

t_b_1 = {
    "Nom": "tour1",
    "symbole": "T",
    "position": ["A", "1"],
    "etat": "v"
}

t_b_2 = {
    "Nom": "tour2",
    "symbole": "T",
    "position": ["H", "1"],
    "etat": "v"
}

c_b_1 = {
    "Nom": "cheval1",
    "symbole": "C",
    "position": ["B", "1"],
    "etat": "v"
}

c_b_2 = {
    "Nom": "cheval2",
    "symbole": "C",
    "position": ["G", "1"],
    "etat": "v"
}

f_b_1 = {
    "Nom": "fou1",
    "symbole": "F",
    "position": ["C", "1"],
    "etat": "v"
}

f_b_2 = {
    "Nom": "fou2",
    "symbole": "F",
    "position": ["F", "1"],
    "etat": "v"
}

r_b = {
    "Nom": "reine",
    "symbole": "R",
    "position": ["D", "1"],
    "etat": "v"
}

R_b = {
    "Nom": "roi",
    "symbole": "RO",
    "position": ["E", "1"],
    "etat": "v"
}


p_n_1 = {
    "Nom": "pion1",
    "symbole": "P",
    "position": ["A", "7"],
    "etat": "v"
}

p_n_2 = {
    "Nom": "pion2",
    "symbole": "P",
    "position": ["B", "7"],
    "etat": "v"
}

p_n_3 = {
    "Nom": "pion3",
    "symbole": "P",
    "position": ["C", "7"],
    "etat": "v"
}

p_n_4 = {
    "Nom": "pion4",
    "symbole": "P",
    "position": ["D", "7"],
    "etat": "v"
}

p_n_5 = {
    "Nom": "pion5",
    "symbole": "P",
    "position": ["E", "7"],
    "etat": "v"
}

p_n_6 = {
    "Nom": "pion6",
    "symbole": "P",
    "position": ["F", "7"],
    "etat": "v"
}

p_n_7 = {
    "Nom": "pion7",
    "symbole": "P",
    "position": ["G", "7"],
    "etat": "v"
}

p_n_8 = {
    "Nom": "pion8",
    "symbole": "P",
    "position": ["H", "7"],
    "etat": "v"
}

t_n_1 = {
    "Nom": "tour1",
    "symbole": "T",
    "position": ["A", "8"],
    "etat": "v"
}

t_n_2 = {
    "Nom": "tour2",
    "symbole": "T",
    "position": ["H", "8"],
    "etat": "v"
}

c_n_1 = {
    "Nom": "cheval1",
    "symbole": "C",
    "position": ["B", "8"],
    "etat": "v"
}

c_n_2 = {
    "Nom": "cheval2",
    "symbole": "C",
    "position": ["G", "8"],
    "etat": "v"
}

f_n_1 = {
    "Nom": "fou1",
    "symbole": "F",
    "position": ["C", "8"],
    "etat": "v"
}

f_n_2 = {
    "Nom": "fou2",
    "symbole": "F",
    "position": ["F", "8"],
    "etat": "v"
}

r_n = {
    "Nom": "reine",
    "symbole": "R",
    "position": ["D", "8"],
    "etat": "v"
}

R_n = {
    "Nom": "roi",
    "symbole": "RO",
    "position": ["E", "8"],
    "etat": "v"
}

f_noirs=[
    p_n_1, p_n_2, p_n_3, p_n_4, p_n_5, p_n_6, p_n_7, p_n_8,
    t_n_1, t_n_2, c_n_1, c_n_2, f_n_1, f_n_2, r_n, R_n
]
f_blancs = [
	p_b_1, p_b_2, p_b_3, p_b_4, p_b_5, p_b_6, p_b_7, p_b_8, t_b_1, t_b_2, c_b_1, c_b_2, f_b_1, f_b_2, r_b, R_b]

posi_blanc=[p["position"] for p in f_blancs]
posi_noir=[p["position"] for p in f_noirs]
posi_noir_list=[]
for p in posi_noir:
	Lxn=L_x.index(p[0])
	Lyn=L_y.index(p[1])
	posi_noir_list.append([Lxn,Lyn])


def pion(xpr,ypr):#pr=principale

	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	nouv_posi=[]

	if yp==1:
		mvm_y=[yp+1,yp+2]
	elif yp != 1 :
		mvm_y=[yp+1]
	
	for y_e in mvm_y:#y_e = element d y li kayn f liste mvm_y
		y=L_y[y_e]
		x=L_x[xp]
		nouv_posi.append([x,y])
	place_pleine_a(nouv_posi)
	ya=L_y[yp+1]
	if yp==1 and [x,ya] not in nouv_posi:
		y=L_y[yp+2]
		p=[x,y]
		nouv_posi.remove(p)
	mvm_kill_possible=[[xp-1,yp+1],[xp+1,yp+1]]
	if xp-1==-1:
		mvm_kill_possible.remove(mvm_kill_possible[0])
	elif xp+1==8:
		mvm_kill_possible.remove(mvm_kill_possible[1])
	mvm_kill=[]
	for n in mvm_kill_possible:
		mvm_kill.append([L_x[n[0]],L_y[n[1]]])

	for b in mvm_kill:
		if b in posi_noir:
			print(f"i mkenlek dakol ficha li f {b}")
			nouv_posi.append(b)
	if [L_x[xp],L_y[yp+1]] in posi_noir:
		nouv_posi.remove([L_x[xp],L_y[yp+1]])
	

	return nouv_posi

def cheval(xpr,ypr):
	
	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	
	mvm=[
		[xp-1,yp+2],
		[xp-1,yp-2],
		[xp+1,yp+2],
		[xp+1,yp-2],
		[xp+2,yp+1],
		[xp+2,yp-1],
		[xp-2,yp+1],
		[xp-2,yp-1]
		]
	nouv_posi=[]
	
	for e in mvm:
		if e[0]>=0 and e[0]<=7 and e[1]>=0 and e[1]<=7 :
			x=L_x[e[0]]
			y=L_y[e[1]]
			nouv_posi.append([x,y])
	place_pleine_a(nouv_posi)

	return nouv_posi

def fou(xpr,ypr):
	
	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	nb=[1,2,3,4,5,6,7]
	nouv_posi=[]
	nouv_posi_a=[]
	for a in nb:
		mvm=[
			[xp+a,yp+a],
			[xp+a,yp-a],
			[xp-a,yp+a],
			[xp-a,yp-a]
		]
		for e in mvm:
			if e[0]>=0 and e[0]<=7 and e[1]>=0 and e[1]<=7 :
				x=L_x[e[0]]  
				y=L_y[e[1]]
				nouv_posi.append([x,y])
				nouv_posi_a.append([x,y])

	place_pleine_a(nouv_posi)
	for c in nouv_posi_a:
		if c not in nouv_posi and c in nouv_posi_a:
			for a in nb:
				cx=L_x.index(c[0])
				cy=L_y.index(c[1])
				if [xp+a,yp+a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+b
							ypc=yp+b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp+a,yp-a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+b
							ypc=yp-b							
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp-a,yp+a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp-b
							ypc=yp+b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp-a,yp-a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp-b
							ypc=yp-b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])

	return nouv_posi

def tour(xpr,ypr):

	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	nb=[1,2,3,4,5,6,7]
	nouv_posi=[]
	nouv_posi_a=[]
	
	for a in nb:
		mvm=[
			[xp+a,yp+0],
			[xp-a,yp+0],
			[xp+0,yp+a],
			[xp+0,yp-a]
		]
		for e in mvm:
			if e[0]>=0 and e[0]<=7 and e[1]>=0 and e[1]<=7 :
				x=L_x[e[0]]
				y=L_y[e[1]]
				nouv_posi.append([x,y])	
				nouv_posi_a.append([x,y])
	place_pleine_a(nouv_posi)
	for c in nouv_posi_a:
		if c not in nouv_posi and c in nouv_posi_a:
			for a in nb:
				cx=L_x.index(c[0])
				cy=L_y.index(c[1])
				if [xp+a,yp+0]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+b
							ypc=yp+0
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp-a,yp+0]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp-b
							ypc=yp+0							
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp+0,yp+a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+0
							ypc=yp+b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp+0,yp-a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+0
							ypc=yp-b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])			
	return nouv_posi

def reine(xpr,ypr):

	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	nb=[1,2,3,4,5,6,7]
	nouv_posi=[]
	nouv_posi_a=[]
	for a in nb:
		mvm=[
			[xp+a,yp+0],#mvm de la tour
			[xp-a,yp+0],
			[xp+0,yp+a],
			[xp+0,yp-a],
			[xp+a,yp+a],#mvm  du fou
			[xp+a,yp-a],
			[xp-a,yp+a],
			[xp-a,yp-a]
		]
		for e in mvm:
			if e[0]>=0 and e[0]<=7 and e[1]>=0 and e[1]<=7 :
				
				x=L_x[e[0]]
				y=L_y[e[1]]
				nouv_posi.append([x,y])
				nouv_posi_a.append([x,y])
	place_pleine_a(nouv_posi)
	for c in nouv_posi_a:
		if c not in nouv_posi and c in nouv_posi_a:
			for a in nb:
				cx=L_x.index(c[0])
				cy=L_y.index(c[1])
				if [xp+a,yp+a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+b
							ypc=yp+b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp+a,yp-a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp+b
							ypc=yp-b							
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp-a,yp+a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp-b
							ypc=yp+b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if [xp-a,yp-a]==[cx,cy]:
					for b in nb:
						if b>a:
							xpc=xp-b
							ypc=yp-b
							if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
								x=L_x[xpc]
								y=L_y[ypc]
								if [x,y] in nouv_posi:
									nouv_posi.remove([x,y])
				if c not in nouv_posi and c in nouv_posi_a:
					for a in nb:
						cx=L_x.index(c[0])
						cy=L_y.index(c[1])
						if [xp+a,yp+0]==[cx,cy]:
							for b in nb:
								if b>a:
									xpc=xp+b
									ypc=yp+0
									if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
										x=L_x[xpc]
										y=L_y[ypc]
										if [x,y] in nouv_posi:
											nouv_posi.remove([x,y])
						if [xp-a,yp+0]==[cx,cy]:
							for b in nb:
								if b>a:
									xpc=xp-b
									ypc=yp+0							
									if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
										x=L_x[xpc]
										y=L_y[ypc]
										if [x,y] in nouv_posi:
											nouv_posi.remove([x,y])
						if [xp+0,yp+a]==[cx,cy]:
							for b in nb:
								if b>a:
									xpc=xp+0
									ypc=yp+b
									if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
										x=L_x[xpc]
										y=L_y[ypc]
										if [x,y] in nouv_posi:
											nouv_posi.remove([x,y])
						if [xp+0,yp-a]==[cx,cy]:
							for b in nb:
								if b>a:
									xpc=xp+0
									ypc=yp-b
									if xpc>=0 and xpc<=7 and ypc>=0 and ypc<=7 :
										x=L_x[xpc]
										y=L_y[ypc]
										if [x,y] in nouv_posi:
											nouv_posi.remove([x,y])	
	return nouv_posi

def roi(xpr,ypr):
	xp=L_x.index(xpr)
	yp=L_y.index(ypr)
	mvm=[
		[xp+1,yp+0],
		[xp-1,yp+0],
		[xp+0,yp+1],
		[xp+0,yp-1],
		[xp+1,yp+1],
		[xp+1,yp-1],
		[xp-1,yp+1],
		[xp-1,yp-1]
	]
	nouv_posi=[]

	for e in mvm:
		if e[0]>=0 and e[0]<=7 and e[1]>=0 and e[1]<=7 :
			x=L_x[e[0]]
			y=L_y[e[1]]
			nouv_posi.append([x,y])
	place_pleine_a(nouv_posi)
	return nouv_posi

def posi_c(x,y):
	xp=L_x.index(x)
	yp=L_y.index(y)
	xc=c_x[xp]
	yc=c_y[yp]
	return xc,yc

noms_b=[]
nomsetat_b=[]
nomsetat_n=[]
for a in f_blancs:
	noms_b.append(a["Nom"])
for a in f_blancs:
	nomsetat_b.append(f"{a['Nom']} ({a['etat']})")
for a in f_noirs:
	nomsetat_n.append(f"{a['Nom']} ({a['etat']})")	


	






