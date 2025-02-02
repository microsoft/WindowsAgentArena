$scriptFolder = "\\host.lan\Data"

Import-Module (Join-Path $scriptFolder -ChildPath "setup-tools.psm1")

# Load the JSON configuration from the same folder as the current script
$config = Get-Content -Raw -Path (Join-Path $scriptFolder -ChildPath "agents.json") | ConvertFrom-Json

# Path to the Logs.txt file in the same folder as the script
$logFilePath = Join-Path -Path $PSScriptRoot -ChildPath "Logs.txt"

# Remove the Logs.txt file if it exists
if (Test-Path -Path $logFilePath -PathType Leaf) {
    Remove-Item -Path $logFilePath
}

# Iterate through each server repository and execute the setup script
foreach ($repo in $config.server_repositories) {
    $setupScriptPath = Join-Path -Path $scriptFolder -ChildPath "mm_agents"
    $setupScriptPath = Join-Path -Path $setupScriptPath -ChildPath $repo.name
    $setupScriptPath = Join-Path -Path $setupScriptPath -ChildPath $repo.setupscript

    try {
        if (Test-Path -Path $setupScriptPath -PathType Leaf) {
            Write-Host "Executing setup script for $($repo.name)..."
            powershell -ExecutionPolicy Bypass -File $setupScriptPath
            $successMessage = "Successfully executed setup script for $($repo.name)"
            Write-Host $successMessage
            $successMessage | Out-File -FilePath $logFilePath -Append
        } else {
            $notFoundMessage = "Setup script not found for $setupScriptPath."
            Write-Host $notFoundMessage
            $notFoundMessage | Out-File -FilePath $logFilePath -Append
        }
    } catch {
        $errorMessage = "Failed to execute setup script for $($repo.name): $($_.Exception.Message)"
        Write-Host $errorMessage
        $errorMessage | Out-File -FilePath $logFilePath -Append
    }
}