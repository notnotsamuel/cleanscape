# Cleanscape
![image](app/cleanscape.png | width=100))

Make your desktop clean again...  
Simple macOS menu bar application that helps to keep your desktop clean and organized. With just one click, it allows you to hide or unhide all files and folders on your desktop. It's built in Python using rumps lib (exposing Objective-C classes).

## Features

    🖥️ Clear your desktop in one click.
    👀 Easily toggle the visibility of your desktop files.
    🔔 Intuitive, non-intrusive menu bar application.
    🎛️ Easy to use - no complex settings or configurations.

## Installation

To use Cleanscape, download the latest release [here](https://github.com/notnotsamuel/cleanscape/releases/tag/v0.1). Unzip the file and move the `cleanscape.app` file to your Applications folder.  

## Building from source

If you want to build Cleanscape from source, you will need Python and py2app. Here's a quick start:

```python
https://github.com/notnotsamuel/cleanscape.git
cd cleanscape/app
pip install -r requirements.txt
python3 setup.py py2app
```

The built application will appear in the dist directory.
## Usage

After launching Cleanscape, you'll see a new icon in your menu bar. Click on the icon to access the controls:

    Click "Hide" to hide all files and folders on your desktop.
    Click "Show" to unhide all files and folders on your desktop.

## Contribution

All hacks approved !

## License

Cleanscape is released under the MIT License.