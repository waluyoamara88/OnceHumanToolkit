from generator.plugins.base_plugin import BasePlugin

class ApiPlugin(BasePlugin):

    NAME="api"

    def register(self):
        print("[PLUGIN]",self.NAME)
