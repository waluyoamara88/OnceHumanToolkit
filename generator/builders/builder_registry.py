from generator.builders.backend_builder import BackendBuilder
from generator.builders.frontend_builder import FrontendBuilder
from generator.builders.database_builder import DatabaseBuilder
from generator.builders.sqlite_builder import SqliteBuilder
from generator.builders.json_builder import JsonBuilder
from generator.builders.api_builder import ApiBuilder
from generator.builders.assets_builder import AssetsBuilder
from generator.builders.scraper_builder import ScraperBuilder
from generator.builders.calculator_builder import CalculatorBuilder
from generator.builders.planner_builder import PlannerBuilder
from generator.builders.website_builder import WebsiteBuilder
from generator.builders.docs_builder import DocsBuilder
from generator.builders.github_builder import GithubBuilder
from generator.builders.cli_builder import CliBuilder
from generator.builders.updater_builder import UpdaterBuilder

BUILDERS = [
    BackendBuilder(),
    FrontendBuilder(),
    DatabaseBuilder(),
    SqliteBuilder(),
    JsonBuilder(),
    ApiBuilder(),
    AssetsBuilder(),
    ScraperBuilder(),
    CalculatorBuilder(),
    PlannerBuilder(),
    WebsiteBuilder(),
    DocsBuilder(),
    GithubBuilder(),
    CliBuilder(),
    UpdaterBuilder()
]
