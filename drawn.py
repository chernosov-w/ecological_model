# здесь подключаются модули

import pygame as pg
import math
import sys
import temp as p

#prog - сохранение численности популяции на одном уровне
#popul - популяционные волны
#evol - естественный отбор в жестких условиях
#layks  - хищники
#antiby - отравление окружающей среды
#temp - глобальное потепление

# здесь определяются константы,

FPS = 120
t = 0
bg_color = p.bg_color

WIN = (1200, 900)



# классы и функции


#рисование круга и квадрата
def drawn(x,y,R,C,T): 
	#x0,y0 - начальные координаты
	#R - размер
	#C - цвет ( (r,g,b) )
	#T - тип (0 - еда, 1 - бактерия)
	if T:
		pg.draw.circle(win,C,(int(math.floor(x)),int(math.floor(y))),int(R/2))
	else:
		pg.draw.rect(win,C,(int(math.floor(x)),int(math.floor(y)),R,R))

#полная отрисовка
def DRAW():
	win.fill(bg_color)
	A = p.A
	B = p.B
	C = p.C
	for i in range(len(A)):
		drawn(A[i][0],A[i][1],A[i][2],A[i][3], False)
	for j in range(len(B)):
		drawn(B[j][0],B[j][1],B[j][2],B[j][3], True)
	for k in range(len(C)):
		drawn(C[k][0],C[k][1],C[k][2],C[k][3], True)

#полное изменение
def DIFF(t):
	p.DIFF(t)



# здесь происходит инициация, создание объектов

pg.init()

win = pg.display.set_mode(WIN)

pg.display.set_caption("Evolution")

clock = pg.time.Clock()



# главный цикл
while p.K:

   	# задержка
	clock.tick(FPS)

	#игровое время
	t = t + 1

	# цикл обработки событий
	for i in pg.event.get():
		if i.type == pg.QUIT:
			sys.exit()
 
	# --------
	DRAW()
	DIFF(t)
	# --------

	# обновление экрана
	pg.display.update()
