import os
import rumps

class DesktopHideShowApp(object):
    def __init__(self):
        self.app = rumps.App("Desktop Manager")
        self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.set_up_menu()
        self.app.icon = 'bar_icon.png'

    def set_up_menu(self):
        hide_button = rumps.MenuItem(title="Hide", callback=self.hide)
        show_button = rumps.MenuItem(title="Show", callback=self.show)
        self.app.menu = [hide_button, show_button]

    def hide(self, _):
        os.system(f'chflags hidden {self.desktop_path}/*')

    def show(self, _):
        os.system(f'chflags nohidden {self.desktop_path}/*')

    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = DesktopHideShowApp()
    app.run()

