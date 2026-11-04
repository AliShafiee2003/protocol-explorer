@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo ========================================================
echo    کاوشگر تعاملی پروتکل‌های اینترنت (نسخه فارسی)
echo    Protocol Explorer - Persian Edition
echo ========================================================
echo.

where python >nul 2>nul
if %errorlevel% equ 0 (
    python serve.py
    goto end
)

echo پایتون در سیستم یافت نشد، تلاش برای اجرا با Node...
where npx >nul 2>nul
if %errorlevel% equ 0 (
    start http://localhost:8000
    npx --yes serve -l 8000
    goto end
)

echo خطا: پایتون یا Node.js در سیستم یافت نشد.
pause

:end
