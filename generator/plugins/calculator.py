from generator.plugins.base_plugin import BasePlugin

class CalculatorPlugin(BasePlugin):

    NAME="calculator"

    def register(self):
        print("[PLUGIN]",self.NAME)
