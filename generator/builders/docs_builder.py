from generator.builders.base_builder import BaseBuilder

class DocsBuilder(BaseBuilder):

    NAME = "docs"

    def build(self):
        print("[BUILD]", self.NAME)
