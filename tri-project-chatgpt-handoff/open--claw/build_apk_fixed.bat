@echo off
set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.16.8-hotspot
set ANDROID_HOME=C:\Users\ynotf\AppData\Local\Android\Sdk
set PATH=%JAVA_HOME%\bin;%ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools;%PATH%

echo Java Home: %JAVA_HOME%
echo Android Home: %ANDROID_HOME%

cd /d "D:\github\open--claw\vendor\openclaw\apps\android"
echo Current directory: %CD%

echo Testing Java...
java -version

echo.
echo Building APK...
gradlew.bat assembleDebug

echo.
echo Build complete!
dir app\build\outputs\apk\debug\
pause