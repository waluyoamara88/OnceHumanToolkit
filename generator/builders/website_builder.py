from generator.builders.base_builder import BaseBuilder

class WebsiteBuilder(BaseBuilder):

    NAME = "website"

    def build(self):
        print("[BUILD]", self.NAME)
