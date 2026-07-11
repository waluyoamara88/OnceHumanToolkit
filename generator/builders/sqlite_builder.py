from generator.builders.base_builder import BaseBuilder

class SqliteBuilder(BaseBuilder):

    NAME = "sqlite"

    def build(self):
        print("[BUILD]", self.NAME)
