from generator.builders.base_builder import BaseBuilder

class CliBuilder(BaseBuilder):

    NAME = "cli"

    def build(self):
        print("[BUILD]", self.NAME)
