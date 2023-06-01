from setuptools import setup
import os
import plistlib

APP = ['cleanscape.py']
DATA_FILES = ['bar_icon.png']
OPTIONS = {
    'includes': ['rumps'],
    'argv_emulation': True,
    'iconfile': 'cleanscape.icns',
    'plist': {
        'LSUIElement': True,
        'CFBundleName': 'cleanscape',
        'CFBundleDisplayName': 'cleanscape',
        'CFBundleGetInfoString': "Make your desktop clean again",
        'CFBundleIdentifier': "com.notnotsamuel.osx.cleanscape",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, Samuel Compagnon, All hacks approved"
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

