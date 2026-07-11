class Registry:

    def __init__(self):
        self.items=[]

    def register(self,obj):
        self.items.append(obj)
