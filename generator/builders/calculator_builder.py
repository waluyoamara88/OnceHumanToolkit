from generator.builders.base_builder import BaseBuilder

class CalculatorBuilder(BaseBuilder):

    NAME = "calculator"

    def build(self):
        print("[BUILD]", self.NAME)
