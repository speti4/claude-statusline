#Requires -Version 7.0
<#
.SYNOPSIS
    Deploys statusline files from this repo to ~/.claude/ for runtime use.
.DESCRIPTION
    Copies statusline.py and skill files to their expected locations
    under the Claude Code home directory.
#>

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path $PSScriptRoot -Parent
$Claude   = Join-Path $env:USERPROFILE '.claude'
$count    = 0

# --- Main script ---
Copy-Item (Join-Path $RepoRoot 'statusline.py') (Join-Path $Claude 'statusline.py') -Force
$count++

# --- Skill files ---
$skillDest = Join-Path $Claude 'skills' 'statusline'
if (-not (Test-Path $skillDest)) {
    New-Item -ItemType Directory -Path $skillDest -Force | Out-Null
}
Copy-Item (Join-Path $RepoRoot 'skills' 'statusline' '*') $skillDest -Force
$count += (Get-ChildItem (Join-Path $RepoRoot 'skills' 'statusline') -File).Count

Write-Host "Deployed $count files to $Claude"
