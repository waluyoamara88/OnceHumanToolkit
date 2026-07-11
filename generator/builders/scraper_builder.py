from generator.builders.base_builder import BaseBuilder

class ScraperBuilder(BaseBuilder):

    NAME = "scraper"

    def build(self):
        print("[BUILD]", self.NAME)
