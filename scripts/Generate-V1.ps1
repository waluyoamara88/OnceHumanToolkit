$ErrorActionPreference="Stop"
$root=Split-Path -Parent $PSScriptRoot
$dirs=@(
"backend","frontend","database","data","assets","docs","tests","tools",
".github",".github\workflows",
"generator","generator\builders","generator\core","generator\templates","generator\config"
)
foreach($d in $dirs){New-Item -ItemType Directory -Force -Path (Join-Path $root $d)|Out-Null}
python generator\build.py
