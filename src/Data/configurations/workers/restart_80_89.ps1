# restart_80_89.ps1
# Restarts the focused 80-89 band fill run using Worker H.
#
# Worker H uses a top-quarter displacement-maximising strategy with a vast
# design space (billions of unique rotation keys) and a >99% hit rate in the
# 80-89 score band.
#
# Termination:
#   - Orchestrator exits when all H slots hit 3 consecutive all-duplicate batches
#   - OR database reaches 300 GB (MAX_DB_GB limit in orchestrator.py)
#
# Target: 3,400,000 unique rows in the 80-89 band
#
# Usage:
#   .\restart_80_89.ps1
#   .\restart_80_89.ps1 | Tee-Object -FilePath orchestrator_h.log

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "Starting focused 80-89 fill (Worker H) at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
python -u orchestrator.py --workers H,H2,H3,H4
Write-Host "Orchestrator exited at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
