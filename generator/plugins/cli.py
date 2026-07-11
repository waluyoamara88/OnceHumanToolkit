from generator.plugins.base_plugin import BasePlugin

class CliPlugin(BasePlugin):

    NAME="cli"

    def register(self):
        print("[PLUGIN]",self.NAME)
