#Requires -Version 7.0
<#
.SYNOPSIS
    Deploys the statusline script from this repo to ~/.claude/ for runtime use.
.DESCRIPTION
    Copies statusline.py to the path the settings.json statusline command runs.

    The /statusline skill is deliberately NOT deployed: it is a project-level skill
    that ships with this repo under .claude/skills/statusline/, so it only loads in
    sessions working on the statusline. The claude-setup repo keeps its own copy,
    produced by that repo's sync script.
#>

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path $PSScriptRoot -Parent
$Claude   = Join-Path $env:USERPROFILE '.claude'

Copy-Item (Join-Path $RepoRoot 'statusline.py') (Join-Path $Claude 'statusline.py') -Force

Write-Host "Deployed statusline.py to $Claude"
