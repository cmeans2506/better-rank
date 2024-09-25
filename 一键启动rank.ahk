; 一键启动rank.ahk
; 把下面的这些变量改成你实际的路径

global java_path := "D:\Software\zulu21.30.15-ca-jdk21.0.1-win_x64\bin\javaw.exe"

global nbbot_path := "D:\MC\julti\Ninjabrain-Bot-1.4.3.jar"

global obs_path := "C:\Users\****\Desktop\myApp\OBS Studio.lnk"
global collection_name := "rank-2K"
global scene_name := "title"

global resize_path := "D:\MC\ahk\resize.ahk"
global tallMacro_path := "D:\MC\ahk\TallMacro.ahk"
global projectorName := "窗口投影（场景） - Mag"

global mmc_path := "D:\MC\MultiMC\MultiMC.exe"
global instance_id := "rank"
global minecraft_WinTitle := "Minecraft ahk_exe javaw.exe"
global max_wait_time := 30

Run, %java_path% -jar %nbbot_path%

Run, %obs_path% --collection %collection_name% --scene %scene_name%
WinWait, %projectorName%
Run, %tallMacro_path%
Run, %resize_path%

while (1){
    Run, %mmc_path% --launch %instance_id%
    WinWait, %minecraft_WinTitle%, , %max_wait_time%
    if (ErrorLevel == 0)
        break
    Process, Close, MultiMC.exe
    Process, WaitClose, MultiMC.exe
}
