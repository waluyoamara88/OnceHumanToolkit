from generator.plugins.api import ApiPlugin
from generator.plugins.assets import AssetsPlugin
from generator.plugins.calculator import CalculatorPlugin
from generator.plugins.cli import CliPlugin
from generator.plugins.database import DatabasePlugin
from generator.plugins.planner import PlannerPlugin
from generator.plugins.scraper import ScraperPlugin
from generator.plugins.updater import UpdaterPlugin
from generator.plugins.website import WebsitePlugin

PLUGINS=[
    ApiPlugin(),
    AssetsPlugin(),
    CalculatorPlugin(),
    CliPlugin(),
    DatabasePlugin(),
    PlannerPlugin(),
    ScraperPlugin(),
    UpdaterPlugin(),
    WebsitePlugin()
]
