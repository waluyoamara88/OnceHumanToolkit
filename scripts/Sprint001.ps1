$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===== OnceHumanToolkit Sprint001 ====="

$dirs = @(
"generator",
"generator/core",
"generator/builders",
"generator/plugins",
"generator/templates",
"generator/manifests",
"generator/config",
"generator/cli",
"generator/pipeline",

"app/api",
"app/core",
"app/models",
"app/schemas",
"app/repositories",
"app/services",
"app/workers",
"app/plugins",
"app/builders",

"tests",
"docs",
"assets",
"data",
"data/json",
"data/sqlite"
)

foreach($d in $dirs){
    New-Item -ItemType Directory -Force $d | Out-Null
}

$files=@(

"generator/build.py",

"generator/core/__init__.py",
"generator/core/engine.py",
"generator/core/builder.py",
"generator/core/context.py",
"generator/core/config.py",
"generator/core/logger.py",
"generator/core/filesystem.py",
"generator/core/plugin.py",
"generator/core/registry.py",
"generator/core/manifest.py",
"generator/core/renderer.py",
"generator/core/validator.py",
"generator/core/writer.py",
"generator/core/exceptions.py",

"generator/builders/__init__.py",
"generator/builders/base_builder.py",
"generator/builders/backend_builder.py",
"generator/builders/frontend_builder.py",
"generator/builders/database_builder.py",
"generator/builders/sqlite_builder.py",
"generator/builders/json_builder.py",
"generator/builders/assets_builder.py",
"generator/builders/api_builder.py",
"generator/builders/scraper_builder.py",
"generator/builders/calculator_builder.py",
"generator/builders/planner_builder.py",
"generator/builders/github_builder.py",
"generator/builders/docs_builder.py",
"generator/builders/cli_builder.py",
"generator/builders/updater_builder.py",
"generator/builders/website_builder.py",
"generator/builders/builder_registry.py",

"generator/plugins/__init__.py",
"generator/plugins/api.py",
"generator/plugins/assets.py",
"generator/plugins/calculator.py",
"generator/plugins/cli.py",
"generator/plugins/database.py",
"generator/plugins/planner.py",
"generator/plugins/scraper.py",
"generator/plugins/updater.py",
"generator/plugins/website.py",

"generator/config/__init__.py",
"generator/config/settings.py",
"generator/config/constants.py",
"generator/config/environment.py",

"generator/cli/__init__.py",
"generator/cli/main.py",
"generator/cli/build.py",
"generator/cli/init.py",
"generator/cli/update.py",
"generator/cli/doctor.py",
"generator/cli/clean.py",
"generator/cli/release.py",

"generator/pipeline/__init__.py",
"generator/pipeline/build_pipeline.py",
"generator/pipeline/test_pipeline.py",
"generator/pipeline/release_pipeline.py",

"generator/manifests/project.yaml",
"generator/manifests/modules.yaml",
"generator/manifests/plugins.yaml",
"generator/manifests/builders.yaml",

"generator/templates/readme.md.j2",
"generator/templates/github.yml.j2",
"generator/templates/fastapi.py.j2",
"generator/templates/nextjs.json.j2",
"generator/templates/sqlite.py.j2"
)

foreach($f in $files){
    $parent = Split-Path $f -Parent
    if($parent){
        New-Item -ItemType Directory -Force $parent | Out-Null
    }

    if(!(Test-Path $f)){
        New-Item -ItemType File -Force $f | Out-Null
    }
}

git add .
git commit -m "feat(generator): sprint001 initialize architecture"
git push

Write-Host ""
Write-Host "Sprint001 Complete"
tree generator /F
