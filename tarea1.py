from random import randint

class User():

	def __init__(self):
		self.name = input("Indique su nombre para comenzar:  ")

	def userNum(self):
		"""
		Solicita al usuario el número que elige como candidato.
		Debe ser un número de 4 cifras y distintas entre si o de lo contrario volverá a solicitarlo.
		"""
		self.user_num = int(input("Indique un número de 4 cifras:"))
		while len(str(self.user_num)) != 4:
			self.user_num = int(input("Número inválido.\nIndique un número de 4 cifras:"))
		for i in range(len(str(self.user_num))):
			for j in range(i+1,len(str(self.user_num))):
				while str(self.user_num)[i] == str(self.user_num)[j]:
					self.user_num = int(input("Número inválido: ninguna cifra debe repetirse.\nIndique un número de 4 cifras:"))
class Host(User):

	def wellcome(self):
		"""
		Da mensaje de bienvenida y una breve descripción sobre que consiste el juego.
		"""		
		msg = "Bienvenid@ %s, en el siguiente juego usted debe adivinar cual es el número de 4 cifras que ha pensado el ordenador(ninguna se repite). Se le indicará si hay cifras OK y si hay cifras REGULAR (en una posición incorrecta)." % self.name.upper()
		print(msg)

	def host_num(self):
		"""
		Genera un número aleatorio de 4 cifras no repetidas que el usuario deberá adivinar.
		"""
		random = randint(1023, 9876)
		random = list(map(int, str(random)))
		while random[0] == random[1] or random[0] == random[2] or random[0] == random[3] or random[1] == random[2] or random[1] == random[3] or random[2] == random[3]:
			random = randint(1023, 9876)
			random = list(map(int, str(random)))
		num = ""
		self.num = int(num.join(map(str,random)))
		
class Guess(Host):

	def guess(self):
		"""
		Compara el número generado por el ordenador con el número propuesto por el usuario.
		Retorna al usuario una pista sobre cuantas cifras son correctas y cuantas regular.
		"""
		self.ok = 0
		self.reg = 0	
		
		self.user_num = list(map(int, str(self.user_num)))
		self.num = list(map(int, str(self.num)))

		# Verifica números OK.
		for i in range(4):
			if self.user_num[i] == self.num[i]: self.ok +=1

		# Verifica números regular.
		if self.user_num[0] != self.num[0] and self.user_num[0] == self.num[1] or self.user_num[0] == self.num[2] or self.user_num[0] == self.num[3]: self.reg +=1
		if self.user_num[1] != self.num[1] and self.user_num[1] == self.num[0] or self.user_num[1] == self.num[2] or self.user_num[1] == self.num[3]: self.reg +=1
		if self.user_num[2] != self.num[2] and self.user_num[2] == self.num[0] or self.user_num[2] == self.num[1] or self.user_num[2] == self.num[3]: self.reg +=1
		if self.user_num[3] != self.num[3] and self.user_num[3] == self.num[0] or self.user_num[3] == self.num[1] or self.user_num[3] == self.num[2]: self.reg +=1

		# Indica una pista sobre cuantas cifras son correctas y cuantas regular.
		self.hint = "%d números OK | %d números REGULAR" % (self.ok,self.reg)
		print(self.hint)

	def win(self):
		"""
		Verifica si el número propuesto por el usuario es el correcto.
		En caso de adivinar retorna un mensaje de  finalización. De lo contrario solicita un nuevo número.
		"""
		if self.ok < 4:
			self.userNum()
			empty_var = ""
			self.num = int(empty_var.join(map(str,self.num)))
			self.guess()
			self.win()
		else: return print("¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!")


def main():
    comenzar = Guess()
    comenzar.wellcome()
    comenzar.host_num()
    comenzar.userNum()
    comenzar.guess()
    comenzar.win()


if __name__ == "__main__":
	main()
