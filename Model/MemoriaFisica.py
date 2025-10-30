from Model.Fila import Fila


class MemoriaFisica:
    def __init__(self, tamanho_molduras):
        self.molduras = Fila()
        self.tamanho_molduras = tamanho_molduras

    def get_capacidade_total(self):
        """Retorna a capacidade máxima de molduras."""
        return self.tamanho_molduras

    def get_tamanho_ocupado(self):
        """Retorna quantas molduras estão atualmente ocupadas."""
        return len(self.molduras)

    def contem(self, pagina):
        """Verifica se a página já está presente na memória física."""
        atual = self.molduras.inicio
        while atual is not None:
            if atual.data == pagina:
                return True
            atual = atual.get_proximo()
        return False

    def inserir(self, pagina):
        """Insere a página na fila (assume que há espaço). Retorna True se inseriu."""
        if self.get_tamanho_ocupado() < self.get_capacidade_total():
            self.molduras.push(pagina)
            return True
        return False

    def substituir_fifo(self, pagina):
        """Substitui a página mais antiga (FIFO) pela nova e retorna a removida."""
        removido = self.molduras.pop_inicio()
        self.molduras.push(pagina)
        return removido

    def listar_molduras(self):
        """Retorna uma lista com as páginas presentes na memória, em ordem FIFO (do início ao fim)."""
        elems = []
        atual = self.molduras.inicio
        while atual is not None:
            elems.append(atual.data)
            atual = atual.get_proximo()
        return elems

    def adicionar_acesso(self, lista_acessos):
        for acesso in lista_acessos:
            self.molduras.push(acesso)
