from generator.plugins.base_plugin import BasePlugin

class PlannerPlugin(BasePlugin):

    NAME="planner"

    def register(self):
        print("[PLUGIN]",self.NAME)
