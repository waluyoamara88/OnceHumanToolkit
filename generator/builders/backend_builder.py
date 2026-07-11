from generator.builders.base_builder import BaseBuilder

class BackendBuilder(BaseBuilder):

    NAME = "backend"

    def build(self):
        print("[BUILD]", self.NAME)
