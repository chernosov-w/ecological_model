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
eat_color = (0, 255, 0)

W = 900
x1 = W//2
y1 = W//2
t0 = 0


N0 = 20*p
N = 1


tk = 400
tN = 10
V = 2.43
Em = 9

xn = 3*r
yn = 3*r


EAT = []

for k in range(N0):
	x = random.randint(0,W)
	y = random.randint(0,W)
	EAT.append(Eat(x,y,p,eat_color))


BAC = [Bac(x1,y1,r,bac_color,V)]

def char(obj):
	return [obj.H[0],obj.H[1],obj.H[2],obj.H[3]]

A = [char(EAT[0])]
B = [char(BAC[0])]
C = []
K = True

# функции

def way(eat,bac):
	dx = eat.H[0] - bac.H[0]
	dy = eat.H[1] - bac.H[1]
	d = (dx**2 + dy**2)**0.5
	if d!=0:
		Vx = (dx/d)*V
		Vy = (dy/d)*V
		Vx = int(math.floor(Vx))
		Vy = int(math.floor(Vy))


			
		return [Vx,Vy,d]
	else:
		return [0,0,0]

def sort(bac):
	dm = W
	z = 0
	for k in range(len(EAT)):
		w = way(EAT[k],bac)
		d = w[2]
		if dm>d:
			dm = d
			z = k

		else:
			continue
	dm = W
	return z 

def define(t):
	print(len(BAC))
	global A
	global B
	if (t%tN)==0:
		for k in range(N):
			x = random.randint(0,W)
			y = random.randint(0,W)
			EAT.append(Eat(x,y,p,eat_color))

	if len(EAT)!=0 and len(BAC)!=0:
		A = []
		B = []
		for k in range(len(BAC)):
			if k >= len(BAC):
				break
			j = BAC[k]
			l = sort(j)
			m = EAT[l]
			w = way(m,BAC[k])
			if w[2]==0:
				del(EAT[sort(BAC[k])])
				BAC[k].H[6] += 3

			if BAC[k].H[5]<tk:
				if BAC[k].H[6]>=Em:
					BAC[k].H[6]=0
					BAC.append(Bac(BAC[k].H[0]+xn,BAC[k].H[1]+yn,BAC[k].H[2],BAC[k].H[3],BAC[k].H[4]))

			else:
				del(BAC[k])



			for i in range(len(EAT)):
				A.append(char(EAT[i]))
			for j in range(len(BAC)):
				B.append(char(BAC[j]))

	else:
		if len(EAT)==0 and len(BAC)!=0:
			A = []
			w = [0,0,1]
			if BAC[0].H[5]<tk:
				if BAC[0].H[6]==Em:
					BAC.append(Bac(BAC[0].H[0]+xn,BAC[0].H[1]+yn,BAC[0].H[2],BAC[0].H[3]))
			else:
				del(BAC[0])

		elif len(BAC)==0 and len(EAT)!=0:
			B = []
			w = [0,0,1]
		else:
			A = []
			B = []
		w = [0,0,1]

def close(bac,k):
	for b in range(len(BAC)):
		b = b - 1
		l = way(bac,BAC[b])
		if b==k or l[2]>r:
			continue
		else:
			return [False,b]
	return [True, -1]

def DIFF(t):
	if len(EAT)!=0 and len(BAC)!=0:
		for k in range(len(BAC)):
			k = k - 1
			w = way(EAT[sort(BAC[k])],BAC[k])
			c = close(BAC[k],k)
			if c[0]:
				BAC[k].H[0] += w[0]
				BAC[k].H[1] += w[1]
				BAC[k].H[5] += 1
			else:
				BAC[k].H[0] += -2*w[0] - (BAC[c[1]].H[0] - BAC[k].H[0])
				BAC[k].H[1] += -2*w[1] - (BAC[c[1]].H[1] - BAC[k].H[1])
				BAC[k].H[5] += 1
	elif len(BAC)!=0:
		for k in range(len(BAC)):
			k = k - 1
			BAC[k].H[5] += 1
	define(t)