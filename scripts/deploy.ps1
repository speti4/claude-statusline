#Requires -Version 7.0
<#
.SYNOPSIS
    Deploys the statusline script from this repo to ~/.claude/ for runtime use.
.DESCRIPTION
    Copies statusline.py to the path the settings.json statusline command runs.

    The settings at the top of the script (STYLE, COLOR_SCHEME, SHOW_RATE_LIMITS,
    SHOW_PROFILE_TAG) are carried over from the copy already deployed, when there is
    one, so updating never resets them. A setting the old copy does not have keeps
    the new default.

    The /statusline skill is deliberately NOT deployed: it is a project-level skill
    that ships with this repo under .claude/skills/statusline/, so it only loads in
    sessions opened in this repo.
#>

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path $PSScriptRoot -Parent
$Claude   = Join-Path $env:USERPROFILE '.claude'
$Source   = Join-Path $RepoRoot 'statusline.py'
$Target   = Join-Path $Claude 'statusline.py'
$Settings = 'STYLE', 'COLOR_SCHEME', 'SHOW_RATE_LIMITS', 'SHOW_PROFILE_TAG'

$content = Get-Content $Source -Raw
$kept = @()
if (Test-Path $Target) {
    $old = Get-Content $Target -Raw
    foreach ($var in $Settings) {
        # Values are plain words; anything else is not a setting we recognise.
        $m = [regex]::Match($old, "(?m)^$var = `"([a-z0-9-]+)`"")
        if (-not $m.Success) { continue }
        $value   = $m.Groups[1].Value
        $pattern = [regex]"(?m)^$var = `"[^`"]*`""
        if ($pattern.IsMatch($content)) {
            $content = $pattern.Replace($content, "$var = `"$value`"", 1)
            $kept += $value
        }
    }
}

New-Item -ItemType Directory -Force $Claude | Out-Null
[IO.File]::WriteAllText($Target, $content, [Text.UTF8Encoding]::new($false))

if ($kept.Count) {
    Write-Host "Deployed statusline.py to $Claude (kept settings: $($kept -join ', '))"
} else {
    Write-Host "Deployed statusline.py to $Claude"
}
