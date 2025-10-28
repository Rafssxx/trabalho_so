from Model.Fila import Fila

class MemoriaFisica:
    def __init__(self, tamanho_molduras):
        self.molduras = Fila()
        self.tamanho_molduras = tamanho_molduras  # capacidade total

    def get_capacidade_total(self):
        """Retorna a capacidade máxima de molduras."""
        return self.tamanho_molduras

    def get_tamanho_ocupado(self):
        """Retorna quantas molduras estão atualmente ocupadas."""
        return self.molduras.__len__()

    def adicionar_acesso(self, lista_acessos):
        for acesso in lista_acessos:
            self.molduras.push(acesso)
