# List of folders
$folders = @(
    ".github/workflows",
    "app",
    "config",
    "data/raw",
    "data/processed",
    "data/external",
    "artifacts",
    "docs",
    "logs",
    "notebooks",
    "tests",
    "src/components",
    "src/config",
    "src/constants",
    "src/entity",
    "src/exception",
    "src/logger",
    "src/pipeline",
    "src/utils"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

# Files
$files = @(
    ".env.example",
    ".gitignore",
    "README.md",
    "src/__init__.py",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/external/.gitkeep",
    "artifacts/.gitkeep",
    "logs/.gitkeep"
)

foreach ($file in $files) {
    New-Item -ItemType File -Force -Path $file | Out-Null
}

Write-Host ""
Write-Host "===================================="
Write-Host " Project Structure Created Successfully!"
Write-Host "===================================="