$ErrorActionPreference="Stop"

$packages=@(
"items",
"weapons",
"armor",
"mods",
"recipes",
"resources",
"deviants",
"bosses",
"npcs",
"memetics",
"territories",
"thermal",
"assets",
"database",
"api",
"website"
)

foreach($p in $packages){

    $path="app\models\$p.py"

    if(!(Test-Path $path)){

@"
class $([CultureInfo]::InvariantCulture.TextInfo.ToTitleCase($p)):
    pass
"@ | Set-Content $path -Encoding UTF8

    }

}

git add .
git commit -m "feat(models): initialize domain models"
git push
