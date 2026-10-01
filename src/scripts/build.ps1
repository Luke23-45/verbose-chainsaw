#Requires -Version 5.1
<#
.SYNOPSIS
    Builds the LaTeX proposal or thesis into an isolated build directory.

.DESCRIPTION
    All intermediate artifacts (.aux, .bbl, .blg, .log, .out, .toc, .lof, .lot)
    are written to docs/src/build/<target>/ instead of polluting the source tree.

    Run from anywhere; paths resolve relative to this script.

.EXAMPLE
    .\build.ps1
    Builds the proposal (default target).

.EXAMPLE
    .\build.ps1 -Target thesis -Clean
    Wipes build/thesis, then rebuilds the thesis from scratch.

.EXAMPLE
    .\build.ps1 -Target proposal -Engine xelatex
    Uses XeLaTeX (needed for Unicode/Nepali fonts).

.NOTES
    Layout expected:
        docs/src/<target>/main.tex
        docs/src/build/<target>/   (created, git-ignorable)
#>

[CmdletBinding()]
param(
    [ValidateSet('proposal', 'thesis')]
    [string] $Target = 'proposal',

    [ValidateNotNullOrEmpty()]
    [string] $File = 'main',

    [ValidateSet('pdflatex', 'xelatex', 'lualatex')]
    [string] $Engine = 'pdflatex',

    [ValidateRange(1, 5)]
    [int] $Passes = 3,

    [switch] $NoBibTeX,
    [switch] $Clean,
    [switch] $OpenPdf,
    [switch] $ContinueOnError
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# --- Path resolution ---------------------------------------------------------

$SrcRoot   = Split-Path -Parent $PSScriptRoot
$ProjectIn = Join-Path $SrcRoot $Target
$BuildOut  = Join-Path (Join-Path $SrcRoot 'build') $Target
$MainTex   = Join-Path $ProjectIn "$File.tex"
$LogFile   = Join-Path $BuildOut "$File.log"
$PdfFile   = Join-Path $BuildOut "$File.pdf"

function Write-Step { param([string] $Message)
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Write-Fail { param([string] $Message)
    Write-Host "!!! $Message" -ForegroundColor Red
}

# --- Preconditions -----------------------------------------------------------

if (-not (Test-Path -LiteralPath $MainTex)) {
    Write-Fail "No main file at: $MainTex"
    exit 1
}

if (-not (Get-Command $Engine -ErrorAction SilentlyContinue)) {
    Write-Fail "'$Engine' not found on PATH. Install MiKTeX/TeX Live and add it to PATH."
    exit 1
}

$BibFiles = @(Get-ChildItem -LiteralPath $ProjectIn -Filter '*.bib' -File -ErrorAction SilentlyContinue)
$UseBib   = (-not $NoBibTeX) -and ($BibFiles.Count -gt 0) -and
            (Get-Command bibtex -ErrorAction SilentlyContinue) -ne $null

# --- Build directory ---------------------------------------------------------

if ($Clean -and (Test-Path -LiteralPath $BuildOut)) {
    Write-Step "Cleaning $BuildOut"
    Remove-Item -LiteralPath $BuildOut -Recurse -Force
}

if (-not (Test-Path -LiteralPath $BuildOut)) {
    New-Item -ItemType Directory -Path $BuildOut -Force | Out-Null
}

Write-Host ''
Write-Host "  target : $Target" -ForegroundColor White
Write-Host "  source : $MainTex" -ForegroundColor White
Write-Host "  output : $BuildOut" -ForegroundColor White
Write-Host "  engine : $Engine   passes: $Passes   bibtex: $UseBib" -ForegroundColor White
Write-Host ''

# --- Runner ------------------------------------------------------------------

function Invoke-Stage {
    param(
        [Parameter(Mandatory)][string] $Name,
        [Parameter(Mandatory)][string] $Exe,
        [Parameter(Mandatory)][string[]] $Arguments,
        [string] $WorkingDirectory = $ProjectIn
    )

    Write-Step $Name
    Push-Location $WorkingDirectory
    try {
        # TeX writes harmless notices (MiKTeX update nag) to stderr; keep them
        # out of PowerShell's error stream but capture the real exit code.
        $ErrorActionPreference = 'Continue'
        & $Exe @Arguments 2>&1 | Out-Null
        $code = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = 'Stop'
        Pop-Location
    }
    return $code
}

function Test-LogHasErrors {
    if (-not (Test-Path -LiteralPath $LogFile)) { return $false }
    return [bool] (Select-String -LiteralPath $LogFile -Pattern '^!' -Quiet)
}

function Show-LogTail {
    if (-not (Test-Path -LiteralPath $LogFile)) { return }
    Write-Host ''
    Write-Host '--- last 25 log lines ---' -ForegroundColor DarkGray
    Get-Content -LiteralPath $LogFile -Tail 25 | ForEach-Object {
        Write-Host "  $_" -ForegroundColor DarkGray
    }
}

# --- Pass 1 ------------------------------------------------------------------

$texArgs = @(
    '-interaction=nonstopmode'
    '-file-line-error'
    '-output-directory', $BuildOut
    $File
)

$failed = $false

for ($pass = 1; $pass -le $Passes; $pass++) {

    if ($failed) { break }

    $code = Invoke-Stage -Name "LaTeX pass $pass of $Passes" -Exe $Engine -Arguments $texArgs
    if ($code -ne 0 -or (Test-LogHasErrors)) {
        if ($ContinueOnError) {
            Write-Host "    pass $pass reported problems, continuing (-ContinueOnError)" -ForegroundColor Yellow
        }
        else {
            $failed = $true
            Write-Fail "LaTeX pass $pass failed."
            break
        }
    }

    if ($UseBib -and $pass -eq 1) {
        # BibTeX must run inside the build dir so the .bbl lands there too,
        # while BIBINPUTS still points back at the source folder for *.bib.
        $savedBib = $env:BIBINPUTS
        $savedBst = $env:BSTINPUTS
        try {
            $env:BIBINPUTS = "$ProjectIn;$SrcRoot;;"
            $env:BSTINPUTS = "$ProjectIn;$SrcRoot;;"
            $code = Invoke-Stage -Name 'BibTeX' -Exe 'bibtex' `
                                  -Arguments @($File) -WorkingDirectory $BuildOut
            if ($code -ne 0) {
                if ($ContinueOnError) {
                    Write-Host '    bibtex reported problems, continuing' -ForegroundColor Yellow
                }
                else {
                    $failed = $true
                    Write-Fail 'BibTeX failed.'
                    break
                }
            }
        }
        finally {
            $env:BIBINPUTS = $savedBib
            $env:BSTINPUTS = $savedBst
        }
    }
}

# --- Result ------------------------------------------------------------------

Write-Host ''

if ($failed) {
    Show-LogTail
    Write-Fail "Build failed. See: $LogFile"
    exit 1
}

if (-not (Test-Path -LiteralPath $PdfFile)) {
    Show-LogTail
    Write-Fail "No PDF produced at: $PdfFile"
    exit 1
}

$warnings = @(Select-String -LiteralPath $LogFile -Pattern 'LaTeX Warning|Underfull|Overfull' -ErrorAction SilentlyContinue).Count

# pdflatex wraps "Output written on ... (12 pages," across lines, so the
# pattern must tolerate newlines inside the span.
$pages = $null
$raw   = [System.IO.File]::ReadAllText($LogFile)
$pageMatch = [regex]::Match($raw, 'Output written on[\s\S]{0,400}?\((\d+)\s+pages')
if ($pageMatch.Success) { $pages = $pageMatch.Groups[1].Value }

Write-Host "OK  $Target -> $PdfFile" -ForegroundColor Green
if ($pages)    { Write-Host "    pages    : $pages" -ForegroundColor Green }
if ($warnings) { Write-Host "    warnings : $warnings (typographic, non-fatal)" -ForegroundColor DarkYellow }

if ($OpenPdf) { Start-Process -FilePath $PdfFile }

exit 0