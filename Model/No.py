class No:
    def __init__(self, data):
        self.data = data
        self.proximo = None
    
    def set_proximo(self, proximo):
        self.proximo = proximo

    def get_proximo(self):
        return self.proximo