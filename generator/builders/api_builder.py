from generator.builders.base_builder import BaseBuilder

class ApiBuilder(BaseBuilder):

    NAME = "api"

    def build(self):
        print("[BUILD]", self.NAME)
