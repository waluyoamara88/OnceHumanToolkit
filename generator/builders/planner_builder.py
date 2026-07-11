from generator.builders.base_builder import BaseBuilder

class PlannerBuilder(BaseBuilder):

    NAME = "planner"

    def build(self):
        print("[BUILD]", self.NAME)
