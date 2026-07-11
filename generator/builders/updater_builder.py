from generator.builders.base_builder import BaseBuilder

class UpdaterBuilder(BaseBuilder):

    NAME = "updater"

    def build(self):
        print("[BUILD]", self.NAME)
