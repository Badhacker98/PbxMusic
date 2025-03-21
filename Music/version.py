import platform
import time

from pyrogram import __version__ as pyro_version
from pytgcalls.__version__ import __version__ as pytgcalls_version

# versions dictionary
__version__ = {
    "Pbx Music": "3.0.0",
    "Python": platform.python_version(),
    "Pyrogram": pyro_version,
    "PyTgCalls": pytgcalls_version,
}

# store start time
__start_time__ = time.time()
