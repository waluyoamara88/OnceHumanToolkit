from generator.builders.base_builder import BaseBuilder

class AssetsBuilder(BaseBuilder):

    NAME = "assets"

    def build(self):
        print("[BUILD]", self.NAME)
