class MemoriaVirtual:
    def __init__(self,tamanho_paginas):
        self.paginas = []
        self.tamanho_paginas = tamanho_paginas
        self.set_paginas()

    def set_paginas(self):
        for i in range(0,self.tamanho_paginas):
            self.paginas.append(i)