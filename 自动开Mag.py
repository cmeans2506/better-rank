
# 自动开mag 1.1
# OBS居然自带timer_add, 我搞麻烦了
# OBS脚本添加了callback函数就不能随便在计时器里调用obs_frontend_set_current_scene，
# 否则会卡死,看网上的资料说是好像造成了死锁
# 开MAG的逻辑得重新写了
# 还加了个自动录制的功能，如果不需要就改成False

import obspython as obs
import pygetwindow as gw

minecraft_folders = [r"D:\MC\MultiMC\instances\SeedQueue\.minecraft"]
ranked_instance_name = "Minecraft* 1.16.1 - MCSR Ranked"
use_auto_recording = True

current_recording_active = False



def win_endswith(window_title):
    windows = gw.getAllTitles()
    return any(title.endswith(window_title) for title in windows)


def win_exist(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    return len(windows) > 0


def get_source(name):
    return obs.obs_get_source_by_name(name)


def release_source(source):
    obs.obs_source_release(source)


def switch_to_scene(scene_name):
    scene_source = get_source(scene_name)
    if scene_source == None:
        return False
    obs.obs_frontend_set_current_scene(scene_source)
    release_source(scene_source)
    return True


def auto_recording():
    is_instance_found = False
    for minecraft_folder in minecraft_folders:
        try:
            with open(minecraft_folder + r"\wpstateout.txt", 'r') as file:
                content = file.read()
                print(content)
                if content != "waiting":
                    is_instance_found = True
                    break
        except FileNotFoundError:
            obs.script_log(obs.LOG_WARNING, '文件未找到，可能是文件夹路径有误或者没有安装state-output模组')
    
    if win_exist(ranked_instance_name):
        is_instance_found = True
        
    global current_recording_active
    if is_instance_found:
        if not current_recording_active:
            obs.obs_frontend_recording_start()
            current_recording_active = True
    else:
        if current_recording_active:
            obs.obs_frontend_recording_stop()
            current_recording_active = False


def open_mag():
    if win_endswith("- Mag"):
        return
    scene_source = get_source('Mag')
    if scene_source == None:
        obs.script_log(obs.LOG_WARNING, '当前场景集合中没有Mag，请检查！')
    else:
        obs.obs_frontend_open_projector('Scene', -1, '', 'Mag')
        release_source(scene_source)


def script_load(settings):
    if use_auto_recording:
        obs.timer_add(auto_recording, 3000)
    # 2000指等待2秒，不要调得太低。调得越低，OBS在退出时卡死的概率越大
    # 恕我能力不足，不知如何修复这个bug
    obs.timer_add(open_mag, 2000)

