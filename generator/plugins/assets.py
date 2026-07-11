from generator.plugins.base_plugin import BasePlugin

class AssetsPlugin(BasePlugin):

    NAME="assets"

    def register(self):
        print("[PLUGIN]",self.NAME)
