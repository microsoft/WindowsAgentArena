Dim scriptFolder, pythonScriptFile, pythonServerPort
scriptFolder = "\\host.lan\Data"
pythonScriptFile = scriptFolder & "\server\main.py"
pythonServerPort = 5000

' Start the Caddy reverse proxy in a non-blocking manner
CreateObject("WScript.Shell").Run "cmd /c caddy reverse-proxy --from :9222 --to :1337", 0, False

' Start the WinArena server
CreateObject("WScript.Shell").Run "cmd /c py """ & pythonScriptFile & """ --port " & pythonServerPort, 0, False
