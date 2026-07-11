from generator.builders.base_builder import BaseBuilder

class GithubBuilder(BaseBuilder):

    NAME = "github"

    def build(self):
        print("[BUILD]", self.NAME)
