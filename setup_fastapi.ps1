$dirs = @(
    "app",
    "app\routers",
    "app\schemas",
    "app\services"
)

$files = @(
    "app\__init__.py",
    "app\main.py",
    "app\routers\__init__.py",
    "app\routers\prediction.py",
    "app\schemas\__init__.py",
    "app\schemas\request.py",
    "app\schemas\response.py",
    "app\services\__init__.py",
    "app\services\prediction_service.py"
)

$dirs | ForEach-Object {
    New-Item -ItemType Directory -Force $_ | Out-Null
}

$files | ForEach-Object {
    New-Item -ItemType File -Force $_ | Out-Null
}

Write-Host "FastAPI structure created successfully."