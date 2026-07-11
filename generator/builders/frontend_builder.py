from generator.builders.base_builder import BaseBuilder

class FrontendBuilder(BaseBuilder):

    NAME = "frontend"

    def build(self):
        print("[BUILD]", self.NAME)
