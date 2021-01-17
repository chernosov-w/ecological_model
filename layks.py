import math
import random
# классы

class Bac:
	"""docstring for ClassName"""
	t_eat = 0
	E = 0
	x = 0
	y = 0
	r = 0
	c = 0
	V = 0
	def __init__(self,x,y,r,c,V,t_eat=0,E=1):
		self.x = x
		self.y = y
		self.r = r
		self.c = c
		self.V = V
		self.H = [x,y,r,c,V,t_eat,E]
class Lay:
	"""docstring for ClassName"""
	t_eat = 0
	E = 0
	x = 0
	y = 0
	r = 0
	c = 0
	V = 0
	def __init__(self,x,y,r,c,V,t_eat=0,E=1):
		self.x = x
		self.y = y
		self.r = r
		self.c = c
		self.V = V
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
bg_color = (255, 255, 255)
bac_color = (0, 0, 255)
lay_color = (255,0,0)
eat_color = (0, 255, 0)

W = 900
x1 = W//2
y1 = W//2
t0 = 0


N0 = 10*p
N = 3*p


tk = 400
tkl = 500
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


BAC = [Bac(x1,y1,r,bac_color,V)]
LAY = [Lay(x1 + W//2, y1 + W//2, r, lay_color, V*2)]

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
	if T:
		return Bac(bac[k].H[0]+xn,bac[k].H[1]+yn,bac[k].H[2],bac[k].H[3],bac[k].H[4])
	else:
		return Lay(bac[k].H[0]+xn,bac[k].H[1]+yn,bac[k].H[2],bac[k].H[3],bac[k].H[4])


def decide(eat, bac, T):
	global A
	global B
	global C
	global K
	a = []
	b = []
	if T:
		tmax = tk
		wmin = p
		Emin = Em
		if len(bac)==0:
			print([len(BAC),len(LAY)])
			K=False
			print("FINISH")
			return
	else:
		tmax = tkl
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



	else:
		if len(eat)==0 and len(bac)!=0:
			w = [0,0,1]
			for k in range(len(bac)):
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
	print([len(BAC),len(LAY)])
	#добавление еды
	if (t%tN)==0:
		for k in range(N):
			x = random.randint(0,W)
			y = random.randint(0,W)
			EAT.append(Eat(x,y,p,eat_color))

	decide(EAT,BAC,True)

	if BAC==[] and LAY == []:
		print("FINISH")
		K = False

	decide(BAC,LAY,False)



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