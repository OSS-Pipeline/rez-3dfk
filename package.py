name = "3dfk"

version = "1.7.15"

authors = [
    "DNA Research"
]

description = \
    """
    Katana plugin for the 3Delight renderer.
    """

requires = [
    "3delight-{version}".format(version=str(version)),
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
    import os

    env.KATANA_RESOURCES.append(
        os.path.join(
            str(env.REZ_3DELIGHT_ROOT),
            "3DelightForKatana"
        )
    )
    env.DEFAULT_RENDERER.set("dl")
