from generator.plugins.base_plugin import BasePlugin

class DatabasePlugin(BasePlugin):

    NAME="database"

    def register(self):
        print("[PLUGIN]",self.NAME)
