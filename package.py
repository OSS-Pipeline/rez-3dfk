name = "3dfk"

version = "1.6.13"

authors = [
    "DNA Research"
]

description = \
    """
    Katana plugin for the 3Delight renderer.
    """

requires = [
    "3delight_core-{version}".format(version=str(version)),
    "cmake-3+",
    "katana-3.0+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "3dfk-{version}".format(version=str(version))

def commands():
    env.KATANA_RESOURCES.append("{root}/3DelightForKatana")
    env.DEFAULT_RENDERER.set("dl")
