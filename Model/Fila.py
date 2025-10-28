from Model.No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def push(self, processo):
        """ Método para inserir elementos na fila"""
        novo = No(processo)
        if self.eVazia():
            self.inicio = novo
        else:
            self.fim.set_proximo(novo)
        self.fim = novo
        self._tamanho += 1

    def pop(self):
        """ método para remover elemento da fila"""
        if self._tamanho > 0:
            elemento = self.inicio
            self.inicio = self.inicio.get_proximo()
            self._tamanho -= 1
            return elemento
        raise IndexError("Fila está vazia")

    
    
    def pop_inicio(self):
        if self.inicio is None:
            raise IndexError("Lista vazia")
        removido = self.inicio.data
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1  # se você mantém contador de tamanho
        return removido



    def peek(self):
        if self._tamanho > 0:
            elemento = self.inicio
            return elemento
        raise IndexError("Fila está vazia")

    def __len__(self):
        return self._tamanho

    def eVazia(self):
        return self._tamanho == 0