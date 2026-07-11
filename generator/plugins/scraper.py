from generator.plugins.base_plugin import BasePlugin

class ScraperPlugin(BasePlugin):

    NAME="scraper"

    def register(self):
        print("[PLUGIN]",self.NAME)
