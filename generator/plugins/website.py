from generator.plugins.base_plugin import BasePlugin

class WebsitePlugin(BasePlugin):

    NAME="website"

    def register(self):
        print("[PLUGIN]",self.NAME)
