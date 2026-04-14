@echo off
echo Setting up Java environment...
set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot
set PATH=%JAVA_HOME%\bin;%PATH%

echo Java version:
java -version

echo.
echo Building Android APK...
cd /d "D:\github\open--claw\vendor\openclaw\apps\android"
gradlew.bat assembleDebug

echo.
echo Build complete! APK should be in app\build\outputs\apk\debug\
pause