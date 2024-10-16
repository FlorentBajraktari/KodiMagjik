[Setup]
AppName=Kodi Magjik
AppVersion=1.0
DefaultDirName={pf}\KodiMagjik
DefaultGroupName=KodiMagjik
OutputBaseFilename=KodiMagjik_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\KodiMagjik"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,KodiMagjik}"; Flags: nowait postinstall skipifsilent
