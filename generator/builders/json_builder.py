from generator.builders.base_builder import BaseBuilder

class JsonBuilder(BaseBuilder):

    NAME = "json"

    def build(self):
        print("[BUILD]", self.NAME)
