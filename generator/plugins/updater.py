from generator.plugins.base_plugin import BasePlugin

class UpdaterPlugin(BasePlugin):

    NAME="updater"

    def register(self):
        print("[PLUGIN]",self.NAME)
