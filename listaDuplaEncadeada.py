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

	def remover(self, dado):
        """ Remove um no da lista. """
        # O no atual eh o primeiro no da lista
        no_atual = self.head
 
        # Vamos procurar pelo dado que queremos remover
        # Equanto o no atual for valido
        while no_atual is not None:
            # Verifica se eh o dado que estamos buscando
            if no_atual.dado == dado:
                # Se o dado que estamos buscando esta no primeiro no
                # da lista, nao temos anterior
                if no_atual.prev is None:
                    # A cabeca 'aponta' para o proximo no da lista
                    self.head = no_atual.next
                    # E o anterior do proximo no aponta para None
                    no_atual.next.prev = None
                else:
                    # Exemplo: Removendo o valor 5
                    # ... <---> | 2 | <---> | 5 | <---> | 12 | <---> ...
                    #
                    # O proximo do valor 2 passa a apontar para o 12 e
                    # o anterior do valor 12 passa a apontar para o 2
                    #                     ---------------
                    # ... <---> | 2 | <---|--- | 5 | ---|---> | 12 | <---> ... 
                    no_atual.prev.next = no_atual.next
                    no_atual.next.prev = no_atual.prev

            # Se nao eh o no que estamos buscando va para o proximo
            no_atual = no_atual.next


lista= Lista()
for i in range (5):
	lista.append(i)

print(lista.head, "\n", lista, "\n", lista.tail)

#lista.remove()

#print(lista)

#lista.remove()

#print(lista)


			