class No:
	def __init__(self, valor):
		self.dado=valor
		self.next=None
		self.prev=None
		
class Lista:
	def __init__(self):
		self.head=None
		self.tail=None

	def __str__(self):
		iterador = self.head
		texto ="["
		while iterador is not None:
			if iterador.prev is None and iterador.next is None:
				texto += f"No: {str(iterador.prev)} {str(iterador.dado)} {str(iterador.next)}"

			if iterador.prev is None and iterador.next is not None:
				texto += f"No: {str(iterador.prev)} {str(iterador.dado)} {str(iterador.next.dado)}"

			if iterador.prev is not None and iterador.next is None:
				texto += f"No: {str(iterador.prev.dado)} {str(iterador.dado)} {str(iterador.next)}"

			if iterador.prev is not None and iterador.next is not None:
				texto += f"No: {str(iterador.prev.dado)} {str(iterador.dado)} {str(iterador.next.dado)}"

			if iterador.next is not None:
				texto += "\n "
			iterador = iterador.next	
		texto += "]"
		return texto
		
	def append(self, valor):
		if self.head is None:
			self.head=self.tail=No(valor)
		else:
			self.tail.next=no=No(valor)
			no.prev=self.tail
			self.tail=self.tail.next

	#def remove (self):
	#	self.tail.prev=self.tail
	#	self.tail.prev=None		

lista= Lista()
for i in range (10):
	lista.append(i)

print(lista)

lista.remove()

print(lista)

lista.remove()

print(lista)


			