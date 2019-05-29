from random import randint

class Host():

	def __init__(self):
		self.name = input("Indique su nombre para comenzar:  ")
		#self.name = "a"

	def wellcome(self):
		"""
		Da mensaje de bienvenida y una breve descripción sobre que consiste el juego.
		"""	
		msg = "Bienvenid@ %s, en el siguiente juego usted debe pensar un número de 4 cifras (sin repetirse) y el ordenador adivinará cual es la cifra que eligió.\nIndicar cuantas cifras son correctas y cuantas regular(correctas pero en otra posición)." % self.name.upper()
		print(msg)

class Guess(Host):

	def find_regulars(self):
		"""
		Define que cifras componen el número elegido por el usuario mediante un proceso lógico de descarte.

		El proceso consiste en dividir las cifras del 0 al 9 en 2 grupos de 4 cifras(1234 y 7890) y otro grupo de
		2 cifras que se forma por omisión(56), cubriendo así las 10 cifras posibles. El usuario indicará
		cuantas cifras correctas hay en cada grupo, a partir de la información brindada se generan nuevos
		grupos de números hasta poder identificar los correctos y descartar el resto.

		Obtiene una lista de 4 integers correctos y otra de 6 descartados.

		Si el usuario proporciona datos incorrectos y no se logra obtener las 4 cifras imprime error.
		"""

		ok = []
		no = []
		conjuntos = [1234,7890]
		conjuntos2 = [1235, 1236]
		conjuntos21 = [4563,4562]
		#conjuntos22 = [5890,6890]
		conjuntos23 = [5678,5679]		
		conjuntos3 = [8905, 8906]
		conjuntos31 = [7568, 7569]
		#conjuntos32 = [5321, 6321]
		conjuntos33 = [5643,5642]	
		conjuntos4 = [1235,5643,2456]	
		conjuntos41 = [6890, 5678,5679]
		conjuntos5 = [1237,9043,2407]
		conjuntos51 = [3890, 1078,2179]

		q = int(input("Su número es el %d?\nCifras OK:   "% conjuntos[0])) + int(input("Cifras REGULAR: "))
		q2 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos[1])) + int(input("Cifras REGULAR: "))
		## si la suma de ambos grupos da 4 --> 5 y 6 se descartan.		
		if 	q + q2 == 4: no.extend([5,6])
		
		## q + q2 == 3: definir 5 y 6 a partir del grupo con menos positivos(conjuntos[0]).
		if q == 1 and q2 == 2:
			q3 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos2[0])) + int(input("Cifras REGULAR: "))
			q4 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos2[1])) + int(input("Cifras REGULAR: "))
			# el mayor va a contener al positivo (5 o 6).		
			if q3 > q4: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			## defino positivos del 1 al 4
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 4 es negativo.				
			if q3 + q4 == 3: 
				no.append(4)
				q5 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos21[0])) + int(input("Cifras REGULAR: "))
				if q5 == 2: 
					ok.append(3)
					no.extend([1,2])
				elif q5 == 1:
					q6 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos21[1])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(2)
						no.extend([1,3])
					else:
						ok.append(1)
						no.extend([2,3])
			# si no hay otro positivo, 4 es positivo, 1 2 y 3 negativos.			
			elif q3 + q4 == 1: 
				ok.append(4)
				no.extend([1,2,3])
			## habiendo definido 5, 6 y los positivos entre 1 y 4 defino positivos entre 7 y 0
			if 5 in ok: conjuntos22 = 5890
			elif 6 in ok: conjuntos22 = 6890
			
			q7 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos22)) + int(input("Cifras REGULAR: "))
			if q7 == 3: 
				no.append(7)
				q8 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos23[0])) + int(input("Cifras REGULAR: "))
				if q8 == 1:
					no.append(8)
					ok.extend([9,0])
				elif q8 == 2:
					ok.append(8)
					q12 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos23[1]) + int(input("Cifras REGULAR: ")))
					if q9 == 2:
						ok.append(9)
						no.append(0)
			elif q7 == 2: 
				ok. append(7)
				q8 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos23[0])) + int(input("Cifras REGULAR: "))
				if q8 == 3:
					ok.append(8)
					no.extend([9,0])
				elif q8 == 2:
					q9 = int(input("Su número es el %d?\nCifras OK:  "% conjuntos23[1])) + int(input("Cifras REGULAR: "))
					if q9 == 3:
						ok.append(9)
						no.extend([8,0])
					elif q9 == 2:
						ok.append(0)
						no.extend([8,9])
		## q + q2 == 3: definir 5 y 6 a partir del grupo con menos positivos(conjuntos[1]).
		elif q == 2 and q2 == 1:
			q13 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos3[0])) + int(input("Cifras REGULAR: "))
			q14 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos3[1])) + int(input("Cifras REGULAR: "))
			# el mayor va a contener al positivo (5 o 6).			
			if q13 > q14: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			## defino positivos del 7 al 0
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 7 es negativo.					
			if q13 + q14 == 3: 
				no.append(7)
				q15 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos31[0])) + int(input("Cifras REGULAR: "))
				if q15 == 2: 
					ok.append(8)
					no.extend([9,0])
				elif q15 == 1:
					q16 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos31[1])) + int(input("Cifras REGULAR: "))
					if q16 == 2:
						ok.append(9)
						no.extend([8,0])
					else:
						ok.append(0)
						no.extend([8,9])
			# si no hay otro positivo, 7 es positivo.			
			elif q13 + q14 == 1: 
				ok.append(7)
				no.extend([8,9,0])
			## habiendo definido 5, 6 y los positivos entre 7 y 0 defino positivos entre 1 y 4
			if 5 in ok: conjuntos32 = 5321
			elif 6 in ok: conjuntos32 = 6321

			q17 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos32)) + int(input("Cifras REGULAR: "))
			if q17 == 3: 
				no.append(4)
				q18 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos33[0])) + int(input("Cifras REGULAR: "))
				if q18 == 1:
					no.append(3)
					ok.extend([2,1])
				elif q18 == 2:
					ok.append(3)
					q19 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos33[1])) + int(input("Cifras REGULAR: "))
					if q19 == 2:
						ok.append(2)
						no.append(1)
			elif q17 == 2: 
				ok. append(4)
				q18 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos33[0])) + int(input("Cifras REGULAR: "))
				if q18 == 3:
					ok.append(3)
					no.extend([2,1])
				elif q18 == 2:
					q19 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos33[1])) + int(input("Cifras REGULAR: "))
					if q19 == 3:
						ok.append(2)
						no.extend([3,1])
					elif q19 == 2:
						ok.append(1)
						no.extend([3,2])
		
		## q == 3 and q2 == 1.
		elif q == 3 and q2 == 1:
			#defino grupo con 1 positivo
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[0])) + int(input("Cifras REGULAR: "))
			if q3 == 0:
				ok.append(7)
				no.extend([8,9,0])
			elif q3 == 1:
				no.append(7)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[1])) + int(input("Cifras REGULAR: "))
				if q4 == 1:
					ok.append(8)
					no.extend([9,0])
				elif q4 == 0:
					no.append(8)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[2])) + int(input("Cifras REGULAR: "))
					if q5 == 1:
						ok.append(9)
						no.append(0)
					elif q5 == 0:
						ok.append(0)
						no.append(9)
			#defino grupo con 3 positivos
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[0])) + int(input("Cifras REGULAR: "))
			if q4 == 3:
				no.append(4)
				ok.extend([1,2,3])
			elif q4 == 2:
				ok.append(4)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[1])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(3)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(2)
						no.append(1)
					elif q6 == 1:
						ok.append(1)
						no.append(2)
				elif q5 == 1:
					no.append(3)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(2)
						no.append(1)
					elif q6 == 1:
						ok.append(1)
						no.append(2)
		## q == 1 and q2 == 3.
		elif q == 1 and q2 == 3:
			#defino grupo con 1 positivo
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[0])) + int(input("Cifras REGULAR: "))
			if q4 == 0:
				ok.append(4)
				no.extend([1,2,3])
			elif q4 == 1:
				no.append(4)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[1])) + int(input("Cifras REGULAR: "))
				if q5 == 1:
					ok.append(3)
					no.extend([1,2])
				elif q5 == 0:
					no.append(3)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q6 == 1:
						ok.append(2)
						no.append(1)
					elif q6 == 0:
						ok.append(1)
						no.append(2)
			#defino grupo con 3 positivos
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[0])) + int(input("Cifras REGULAR: "))
			if q3 == 3:
				no.append(7)
				ok.extend([8,9,0])
			elif q3 == 2:
				ok.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[1])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(8)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(9)
						no.append(0)
					elif q6 == 1:
						ok.append(0)
						no.append(9)
				elif q5 == 1:
					no.append(8)
					ok.extend([9,0])
		## q == 3 and q2 == 0.
		elif q == 3 and q2 == 0:
			no.extend([7,8,9,0])
			#defino 5 y 6.
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos3[0])) + int(input("Cifras REGULAR: "))
			if q3 == 1:
				ok.append(5)
				no.append(6)
			else:
				ok.append(6)
				no.append(5)
			#defino grupo con 3 positivos
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[0])) + int(input("Cifras REGULAR: "))
			if q4 == 3:
				no.append(4)
				ok.extend([1,2,3])
			elif q4 == 2:
				ok.append(4)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[1])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(3)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(2)
						no.append(1)
					elif q6 == 1:
						ok.append(1)
						no.append(2)
				elif q5 == 1:
					no.append(3)
					ok.extend([1,2])
		## q == 3 and q2 == 0.
		elif q == 0 and q2 == 3:
			no.extend([1,2,3,4])		
			#defino 5 y 6.
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[0])) + int(input("Cifras REGULAR: "))
			if q3 == 1:
				ok.append(5)
				no.append(6)
			else:
				ok.append(6)
				no.append(5)
			#defino grupo con 3 positivos
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[0])) + int(input("Cifras REGULAR: "))
			if q3 == 3:
				no.append(7)
				ok.extend([8,9,0])
			elif q3 == 2:
				ok.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[2])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(0)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[1])) + int(input("Cifras REGULAR: "))
					if q6 == 3:
						ok.append(8)
						no.append(9)
					elif q6 == 2:
						ok.append(9)
						no.append(8)
				elif q5 == 1:
					no.append(0)
					ok.extend([8,9])

		## q == 2 and q2 == 0.
		elif q == 2 and q2 == 0:
			ok.extend([5,6])
			no.extend([7,8,9,0])
			## defino positivos del 1 al 4.
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[0])) + int(input("Cifras REGULAR: "))
			#si en 123 hay 1 positivo, 4 es positivo
			if q3 == 1:
				ok.append(4)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[1])) + int(input("Cifras REGULAR: "))
				if q4 == 2:
					ok.append(3)
					no.extend([1,2])
				elif q4 == 1:
					no.append(3)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[2])) + int(input("Cifras REGULAR: "))
					if q5 == 2:
						ok.append(2)
						no.append(1)
					elif q5 == 1:
						ok.append(1)
						no.append(2)
			#si en 123 hay 2 positivos, 4 es negativo
			elif q3 == 2:
				no.append(4)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[1])) + int(input("Cifras REGULAR: "))
				if q4 == 0:
					ok.extend([1,2])
					no. append(3)
				elif q4 == 1:
					ok.append(3)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos5[2])) + int(input("Cifras REGULAR: "))
					if q5 == 1:
						ok.append(2)
						no.append(1)
					elif q5 == 0:
						ok.append(1)
						no.append(2)
		## q == 0 and q2 == 2.
		elif q == 0 and q2 == 2:
			ok.extend([5,6])
			no.extend([1,2,3,4])
			## defino positivos del 7 al 0.
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[0])) + int(input("Cifras REGULAR: "))
			#si en 890 hay 1 positivo, 7 es positivo
			if q4 == 1:
				ok.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[1])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(8)
					no.extend([9,0])
				elif q5 == 1:
					no.append(8)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(9)
						no.append(0)
					elif q6 == 1:
						ok.append(0)
						no.append(9)
			#si en 890 hay 2 positivos, 7 es negativo
			elif q4 == 2:
				no.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[1])) + int(input("Cifras REGULAR: "))
				if q5 == 0:
					ok.extend([9,0])
					no. append(8)
				elif q5 == 1:
					ok.append(0)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos51[2])) + int(input("Cifras REGULAR: "))
					if q6 == 1:
						ok.append(9)
						no.append(8)
					elif q6 == 0:
						ok.append(8)
						no.append(9)
		## q == 1 q2 ==1.
		elif q == 1 and q2 == 1:
			ok.extend([5,6])
			##defino primer grupo
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[0])) + int(input("Cifras REGULAR: "))
			if q4 == 1:
				ok.append(4)
				no.extend([1,2,3])
			elif q4 == 2:
				no.append(4)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[1])) + int(input("Cifras REGULAR: "))
				if q5 == 3:
					ok.append(3)
					no.extend([1,2])
				elif q5 == 2:
					no.append(3)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q6 == 3:
						ok.append(2)
						no.append(1)
					elif q6 == 2:
						ok.append(1)
						no.append(2)
			#defino segundo grupo
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[0])) + int(input("Cifras REGULAR: "))
			if q3 == 1:
				ok.append(7)
				no.extend([8,9,0])
			elif q3 == 2:
				no.append(7)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[1])) + int(input("Cifras REGULAR: "))
				if q4 == 3:
					ok.append(8)
					no.extend([9,0])
				elif q4 == 2:
					no.append(8)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[2])) + int(input("Cifras REGULAR: "))
					if q5 == 3:
						ok.append(9)
						no.append(0)
					elif q5 == 2:
						ok.append(0)
						no.append(9)

		## q == 2 q2 == 2. 
		elif q == 2 and q2 == 2:
			## defino positivos del 1 al 4.
			q3 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[0])) + int(input("Cifras REGULAR: "))
			#si en 123 hay 1 positivo, 4 es positivo
			if q3 == 1:
				ok.append(4)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[1])) + int(input("Cifras REGULAR: "))
				if q4 == 2:
					ok.append(3)
					no.extend([1,2])
				elif q4 == 1:
					no.append(3)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q5 == 2:
						ok.append(2)
						no.append(1)
					elif q5 == 1:
						ok.append(1)
						no.append(2)
			#si en 123 hay 2 positivos, 4 es negativo
			elif q3 == 2:
				no.append(4)
				q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[1])) + int(input("Cifras REGULAR: "))
				if q4 == 0:
					ok.extend([1,2])
					no. append(3)
				elif q4 == 1:
					ok.append(3)
					q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos4[2])) + int(input("Cifras REGULAR: "))
					if q5 == 1:
						ok.append(2)
						no.append(1)
					elif q5 == 0:
						ok.append(1)
						no.append(2)
			## defino positivos del 7 al 0.
			q4 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[0])) + int(input("Cifras REGULAR: "))
			#si en 890 hay 1 positivo, 7 es positivo
			if q4 == 1:
				ok.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[1])) + int(input("Cifras REGULAR: "))
				if q5 == 2:
					ok.append(8)
					no.extend([9,0])
				elif q5 == 1:
					no.append(8)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[2])) + int(input("Cifras REGULAR: "))
					if q6 == 2:
						ok.append(9)
						no.append(0)
					elif q6 == 1:
						ok.append(0)
						no.append(9)
			#si en 890 hay 2 positivos, 7 es negativo
			elif q4 == 2:
				no.append(7)
				q5 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[1])) + int(input("Cifras REGULAR: "))
				if q5 == 0:
					ok.extend([9,0])
					no. append(8)
				elif q5 == 1:
					ok.append(8)
					q6 = int(input("Su número es el %d?\nCifras OK:   "% conjuntos41[2])) + int(input("Cifras REGULAR: "))
					if q6 == 1:
						ok.append(9)
						no.append(0)
					elif q6 == 0:
						ok.append(0)
						no.append(9)
		## q == 4 or q2 == 4.
		elif q == 4 :
			ok.extend([1,2,3,4])
			no.extend([7,8,9,0])
		elif q2 == 4: 
			ok.extend([7,8,9,0])
			no.extend([1,2,3,4])

		if len(ok) != 4: 
			print("Error: Ha ingresado un valor equivocado.")

		self.ok = ok
		self.no = no

	def make_int(self, b):
		"""
		A partir de una lista de integers los concatena para formar un solo número.
		"""
		integer = ""
		j = []
		try:
			# Transforma lista anidada a lista simple si es necesario.
			a = len(b[0])
			if a == 1:
				for i in range(1,4):
					b[0] += b[i]
				for i in b[0]:
					j.append(i)
			b = j
		except: pass

		# Contatena lista en un solo integer.
		self.integer = int(integer.join(map(str,b)))
		return self.integer

	def end_game(self):
		"""
		Devuelve el número obtenido y da un mensaje de finalización.
		"""
		#print(self.hit)
		return print("FELICITACIONES SU NÚMERO ES %d\n(En caso de no ser correcto verifique las respuestas por favor)" % self.make_int(self.hit))

	def find_number(self):
		"""
		A partir de las cifras obtenidas con find_regulars() se pregunta al usuario que cifras están OK en
		una serie de candidatos que permite definir cual es la posición correcta de cada cifra para encontrar
		el número final. 

		Solamente solicita las cifras OK ya que las regulares fueron obtenidas de la función find_regulars().

		Si el usuario proporciona datos incorrectos imprime error.
		"""

		self.hit = ["","","",""]
		self.dismiss = [[],[],[],[]]
		suggest = [self.ok[0],self.no[1],self.no[0],self.ok[3]]
		suggest2 = [self.no[2],self.no[3],self.no[1],self.ok[3]]
		#suggest3 = [self.no[3],self.ok[1],self.ok[2],self.no[0]] no
		suggest4 = [self.no[4],self.no[2],self.ok[2],self.no[5]] #10
		suggest5 = [self.ok[3],self.no[1],self.no[0],self.ok[0]]
		suggest6 = [self.no[3],self.no[4],self.no[0],self.ok[0]]
		suggest7 = [self.no[4],self.ok[0],self.ok[3],self.no[5]]
		suggest8 = [self.no[1],self.no[2],self.ok[3],self.no[3]]
		suggest9 = [self.no[0],self.ok[3],self.no[2],self.no[5]] #14
		suggest10 = [self.no[0],self.no[2],self.ok[2],self.no[1]] #4
		suggest11 = [self.no[3],self.ok[2],self.no[2],self.no[0]]
		suggest12 = [self.no[3],self.ok[0],self.no[5],self.no[0]] #13
		suggest13 = [self.no[3],self.ok[0],self.no[2],self.no[0]] #12
		suggest14 = [self.no[2],self.ok[3],self.no[1],self.no[0]] #9
		suggest15 = [self.ok[1],self.no[1],self.no[0],self.no[5]]

		#verifico números de los extremos [0]xx[3].
		q1 = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest)))
		# si 1: verifico cual es correcto.
		if q1 == 1:
			#verifico última cifra.
			q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest2)))
			# si 1: posición[3] == cifra[3].
			if q == 1:
				self.hit[3] = self.ok[3]
				self.dismiss[0].append([self.ok[0]])
				# verifico si cifra[0] in posición[1] or cifra[0] in posición[2].
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest13)))
				
				# si 1: posición[1] == cifra[0].
				if q == 1:
					self.hit[1] = self.ok[0]
					self.dismiss[2].append([self.ok[0]])
					# definidas posiciones [3] y [1] verifico [0] y [2].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
					if q == 1:
						self.hit[2] = self.ok[2]
						self.hit[0] = self.ok[1]
						self.end_game()
					elif q == 0:
						self.hit[0] = self.ok[2]
						self.hit[2] = self.ok[1]
						self.end_game()
						
				# si 0: posición[2] == cifra[3].
				elif q == 0:
					self.hit[2] = self.ok[0]
					self.dismiss[1].append(self.ok[0])
					# definidas posiciónes [0] y [2] verifico [1] y [3].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest11)))
					if q == 1:
						self.hit[1] = self.ok[2]
						self.hit[0] = self.ok[1]
						self.end_game()
					elif q == 0:
						self.hit[0] = self.ok[2]
						self.hit[1] = self.ok[1]
						self.end_game()
			# si 0: posición[0] == cifra[0].
			elif q == 0:
				self.hit[0] = self.ok[0]
				self.dismiss[3].append([self.ok[3]])
				# verifico si cifra[3] in posición[1] or cifra[3] in posición[2].
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest9)))
				
				# si 1: posición[1] == cifra[3].
				if q == 1:
					self.hit[1] = self.ok[3]
					self.dismiss[2].append([self.ok[3]])
					# definidas posiciones [0] y [1] verifico [2] y [3].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
					if q == 1:
						self.hit[2] = self.ok[2]
						self.hit[3] = self.ok[1]
						self.end_game()
					elif q == 0:
						self.hit[3] = self.ok[2]
						self.hit[2] = self.ok[1]
						self.end_game()
						
				# si 0: posición[2] == cifra[3].
				elif q == 0:
					self.hit[2] = self.ok[3]
					self.dismiss[1].append([self.ok[3]])
					# definidas posiciónes [0] y [2] verifico [1] y [3].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest11)))
					if q == 1:
						self.hit[1] = self.ok[2]
						self.hit[3] = self.ok[1]
						self.end_game()
					elif q == 0:
						self.hit[3] = self.ok[2]
						self.hit[1] = self.ok[1]
						self.end_game()

		# si 0: verifico números de los extremos [3]xx[0].
		elif q1 == 0:
			q2 = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest5)))
			if q2 == 1:
				#verifico última cifra
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest6)))
				if q == 1:
					self.hit[3] = self.ok[0]
					self.dismiss[0].append([self.ok[3]])

					# verifico si cifra[3] in posición[1] or cifra[3] in posición[2].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest14)))
					
					# si 1: posición[1] == cifra[3].
					if q == 1:
						self.hit[1] = self.ok[3]
						self.dismiss[2].append([self.ok[3]])
						# definidas posiciones [0] y [1] verifico [2] y [3].
						q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
						if q == 1:
							self.hit[2] = self.ok[2]
							self.hit[0] = self.ok[1]
							self.end_game()
						elif q == 0:
							self.hit[0] = self.ok[2]
							self.hit[2] = self.ok[1]
							self.end_game()
							
					# si 0: posición[2] == cifra[3].
					elif q == 0:
						self.hit[2] = self.ok[3]
						self.dismiss[1].append([self.ok[3]])
						# definidas posiciónes [3] y [2] verifico [0] y [1].
						q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest11)))
						if q == 1:
							self.hit[1] = self.ok[2]
							self.hit[0] = self.ok[1]
							self.end_game()
						elif q == 0:
							self.hit[0] = self.ok[2]
							self.hit[1] = self.ok[1]
							self.end_game()
				elif q == 0:
					self.hit[0] = self.ok[3]
					self.dismiss[3].append([self.ok[0]])

					# verifico si cifra[0] in posición[1] or cifra[0] in posición[2].
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest12)))
					# si 1: posición[1] == cifra[0].
					if q == 1:
						self.hit[1] = self.ok[0]
						self.dismiss[2].append([self.ok[0]])
						# definidas posiciones [0] y [1] verifico [2] y [3].
						q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
						if q == 1:
							self.hit[2] = self.ok[2]
							self.hit[3] = self.ok[1]
							self.end_game()
						elif q == 0:
							self.hit[3] = self.ok[2]
							self.hit[2] = self.ok[1]
							self.end_game()
							
					# si 0: posición[2] == cifra[0].
					elif q == 0:
						self.hit[2] = self.ok[0]
						self.dismiss[1].append([self.ok[3]])
						# definidas posiciónes [0] y [2] verifico [1] y [3].
						q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest11)))
						if q == 1:
							self.hit[1] = self.ok[2]
							self.hit[3] = self.ok[1]
							self.end_game()
						elif q == 0:
							self.hit[3] = self.ok[2]
							self.hit[1] = self.ok[1]
							self.end_game()
			# si 2: posición[0] y [3] ok. verifico posiciones centrales.
			elif q2 == 2:
				self.hit[0] = self.ok[3]
				self.hit[3] = self.ok[0]
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
				if q == 1:
					self.hit[2] = self.ok[2]
					self.hit[1] = self.ok[1]
					self.end_game()
				elif q == 0:
					self.hit[2] = self.ok[1]
					self.hit[1] = self.ok[2]
					self.end_game()
		
		# si 2: posición[0] y [3] ok. verifico posiciones centrales.
		elif q1 == 2:
				self.hit[0] = self.ok[0]
				self.hit[3] = self.ok[3]
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest10)))
				if q == 1:
					self.hit[2] = self.ok[2]
					self.hit[1] = self.ok[1]
					self.end_game()
				elif q == 0:
					self.hit[2] = self.ok[1]
					self.hit[1] = self.ok[2]
					self.end_game()
		
		# si [0] y [3] negativo en extremos, verifico en cifras centrales.
		if q1 == 0 and q2 == 0:
			#q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest7)))
			#if q == 1:
				#verifico [2] cifra.
				q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest8)))

				# si 1: posición[2] == cifra[3] and posición[1] == cifra[0]
				if q == 1:
					self.hit[2] = self.ok[3]
					self.dismiss[1].append([self.ok[3]])
					self.hit[1] = self.ok[0]
					self.dismiss[2].append([self.ok[0]])

					#definidas posiciones [1] y [2] verifico [0] y [3]
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest15)))
					if q == 1:
						self.hit[0] = self.ok[1]
						self.hit[3] = self.ok[2]
						self.end_game()
					elif q == 0:
						self.hit[3] = self.ok[1]
						self.hit[0] = self.ok[2]
						self.end_game()

				# si 0: posición[2] == cifra[0] and posición[1] == cifra[3]
				elif q == 0:
					self.hit[2] = self.ok[0]
					self.dismiss[2].append([self.ok[3]])
					self.hit[1] = self.ok[3]
					self.dismiss[1].append([self.ok[0]])

					#definidas posiciones [1] y [2] verifico [0] y [3]
					q = int(input("Su número es el %d?\nCifras OK:   "% self.make_int(suggest15)))
					if q == 1:
						self.hit[0] = self.ok[1]
						self.hit[3] = self.ok[2]
						self.end_game()
					elif q == 0:
						self.hit[3] = self.ok[1]
						self.hit[0] = self.ok[2]
						self.end_game()

		#print(self.hit)
		for i in self.hit:
			if isinstance(i,int) == False:
				print("Error: Ha ingresado un valor equivocado.")
				break
	

def main():
    comenzar = Guess()
    comenzar.wellcome()
    comenzar.find_regulars()
    try:
    	comenzar.find_number()
    except: pass

if __name__ == "__main__":
	main()

