# rank场景切换.py
# 把minecraft_folder的值改成你rank实例的文件夹路径

import obspython as obs


minecraft_folder = r"D:\MC\MultiMC\instances\rank\.minecraft"
current_scene = ""


def get_source(name):
    return obs.obs_get_source_by_name(name)


def release_source(source):
    obs.obs_source_release(source)


def switch_to_scene(scene_name):
    global current_scene
    if current_scene == scene_name:
        return True
    current_scene = scene_name
    scene_source = get_source(scene_name)
    if scene_source == None:
        return False
    obs.obs_frontend_set_current_scene(scene_source)
    release_source(scene_source)
    return True


def switch_scene_on_ranked_mode():
    try:
        with open(minecraft_folder + r"\wpstateout.txt", 'r') as file:
            content = file.read()
            if content.startswith("inworld"):
                switch_to_scene("inworld")
            else:
                switch_to_scene("title")
    except FileNotFoundError:
        obs.script_log(obs.LOG_WARNING, '文件未找到，可能是文件夹路径有误或者没有安装state-output模组')


def script_load(settings):
    obs.timer_add(switch_scene_on_ranked_mode, 500)

