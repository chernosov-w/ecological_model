import math
import random


# классы



class Bac:
	"""docstring for ClassName"""
	global tk0
	t_eat = 0
	tk = 400
	E = 0
	x = 0
	y = 0
	r = 0
	c = 0
	V = 0
	def __init__(self,x,y,r,c,V,t_eat,E,tk):
		self.x = x
		self.y = y
		self.r = r
		self.c = c
		self.V = V
		self.tk = tk
		self.H = [x,y,r,c,V,t_eat,E]
class Lay:
	"""docstring for ClassName"""
	global tkl0
	t_eat = 0
	tk = 500
	E = 0
	x = 0
	y = 0
	r = 0
	c = 0
	V = 0
	def __init__(self,x,y,r,c,V,t_eat,E,tk):
		self.x = x
		self.y = y
		self.r = r
		self.c = c
		self.V = V
		self.tk = tk
		self.H = [x,y,r,c,V,t_eat,E]


class Eat:
	"""docstring for ClassName"""
	E = 0
	x = 0
	y = 0
	r = 0
	c = 0
	def __init__(self, x,y,r,c,E=1):
		self.x = x
		self.y = y
		self.r = r
		self.c = c
		self.E = E
		self.H = (x,y,r,c,E)

# переменные и объекты

p = 3
r = 4*p

bg_color = [255, 255, 255]
bac_color = (0, 0, 255)
lay_color = (255,0,0)
eat_color = (0, 255, 0)

W = 900
x1 = W//2
y1 = W//2
t0 = 0


tk0 = 400
tkl0 = 500


tJ = 1000
sT = 4

N0 = 10*p
N = p


tN = 5
V = 2.43
Em = 9
Eml = 10


xn = 3*r
yn = 3*r


EAT = []

for k in range(N0):
	x = random.randint(0,W)
	y = random.randint(0,W)
	EAT.append(Eat(x,y,p,eat_color))


BAC = [Bac(x1,y1,r,bac_color,V,0,1, tk0)]
LAY = [Lay(x1 + W//2, y1 + W//2, r, lay_color, V*2, 0, 1, tkl0)]

def char(obj):
	return [obj.H[0],obj.H[1],obj.H[2],obj.H[3]]

A = [char(EAT[0])]
B = [char(BAC[0])]
C = [char(LAY[0])]
K = True

# функции

def way(eat,bac):
	dx = eat.H[0] - bac.H[0]
	dy = eat.H[1] - bac.H[1]
	d = (dx**2 + dy**2)**0.5
	if d!=0:
		Vx = (dx/d)*V
		Vy = (dy/d)*V
		#Vx = int(math.floor(Vx))
		#Vy = int(math.floor(Vy))


			
		return [Vx,Vy,d]
	else:
		return [0,0,0]

def sort(bac_n,eat):
	dm = W
	z = 0
	for k in range(len(eat)):
		w = way(eat[k],bac_n)
		d = w[2]
		if dm>d:
			dm = d
			z = k

		else:
			continue
	return z 

def initi(T,bac,k):
	global tk0
	global tkl0
	if T:
		return Bac(bac[k].H[0]+xn,bac[k].H[1]+yn,bac[k].H[2],bac[k].H[3],bac[k].H[4],0,1,tk0)
	else:
		return Lay(bac[k].H[0]+xn,bac[k].H[1]+yn,bac[k].H[2],bac[k].H[3],bac[k].H[4],0,1,tkl0)


def decide(eat, bac, T, t):
	global A
	global B
	global C
	global K
	a = []
	b = []
	Tsr = 0
	if T:
		wmin = p
		Emin = Em
		if len(bac)==0:
			print([len(BAC),len(LAY)])
			K=False
			print("FINISH")
			return
	else:
		wmin = r
		Emin = Eml
		if len(eat)==0:
			print([len(BAC),len(LAY)])
			K=False
			print("FINISH")
			return
	if len(eat)!=0 and len(bac)!=0:
		for k in range(len(bac)):
			if k >= len(bac):
				break
			if (t%sT == 0) and (t>tJ):
				bac[k].tk -= 1

			tmax = bac[k].tk
			Tsr += tmax
			w = way(eat[sort(bac[k],eat)],bac[k])


			if w[2]<=wmin:
				del(eat[sort(bac[k],eat)])
				bac[k].H[6] += 3




			if bac[k].H[5]<tmax:
				if bac[k].H[6]>=Emin:
					bac[k].H[6]=0
					bac.append(initi(T,bac,k))

			else:
				del(bac[k])



			for i in range(len(eat)):
				a.append(char(eat[i]))
			for j in range(len(bac)):
				b.append(char(bac[j]))
		if len(b)!=0 and (t%100==0):
			if T:
				print(tk0)
			else:
				print(tkl0)


	else:
		if len(eat)==0 and len(bac)!=0:
			w = [0,0,1]
			for k in range(len(bac)):
				if k >= len(bac):
					break
				tmax = bac[k].tk
				if bac[k].H[5]<tmax:
					if bac[k].H[6]==Emin:
						bac.append(initi(T,bac,k))
				else:
					del(bac[k])
			for j in range(len(bac)):
				b.append(char(bac[j]))

		elif len(bac)==0 and len(eat)!=0:
			for i in range(len(eat)):
				a.append(char(eat[i]))
			w = [0,0,1]
		w = [0,0,1]
	if T:
		A = a
		B = b
	if not(T):
		B = a
		C = b





def define(t):
	global K
	global tk0
	global tkl0
	global bg_color
	print([len(BAC),len(LAY)])
	#добавление еды
	if (t%tN)==0:
		for k in range(N):
			x = random.randint(0,W)
			y = random.randint(0,W)
			EAT.append(Eat(x,y,p,eat_color))
	if t>tJ and t%sT==0:
		tk0 -= 1
		tkl0 -= 1
		if t%(3*sT)==0:
			bg_color[1] = bg_color[1] - 1 
			bg_color[2] = bg_color[2] - 1
	decide(EAT,BAC,True, t)

	if BAC==[] and LAY == []:
		print("FINISH")
		K = False

	decide(BAC,LAY,False, t)



def close(bac_n,bac,k):
	for b in range(len(bac)):
		b = b - 1
		l = way(bac_n,bac[b])
		if b==k or l[2]>r:
			continue
		else:
			return [False,b]
	return [True, -1]

def velos(eat,bac):
	if len(eat)!=0 and len(bac)!=0:
		for k in range(len(bac)):
			k = k - 1
			w = way(eat[sort(bac[k],eat)],bac[k])
			c = close(bac[k],bac,k)
			if c[0]:
				bac[k].H[0] += w[0]
				bac[k].H[1] += w[1]
				bac[k].H[5] += 1
			else:
				bac[k].H[0] += -2*w[0] - (bac[c[1]].H[0] - bac[k].H[0])
				bac[k].H[1] += -2*w[1] - (bac[c[1]].H[1] - bac[k].H[1])
				bac[k].H[5] += 1
	elif len(bac)!=0:
		for k in range(len(bac)):
			k = k - 1
			bac[k].H[5] += 1

def DIFF(t):
	print(t)
	velos(BAC,LAY)
	velos(EAT,BAC)

	define(t)
