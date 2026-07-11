from generator.builders.base_builder import BaseBuilder

class DatabaseBuilder(BaseBuilder):

    NAME = "database"

    def build(self):
        print("[BUILD]", self.NAME)
