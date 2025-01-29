import os
import subprocess
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

class BrightnessController:
    def __init__(self):
        self.APPINDICATOR_ID = "indicator-brightnesscontroller"
        self.ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brt.svg")
        self.primary_display = self.get_primary_display()

        self.indicator = appindicator.Indicator.new(
            self.APPINDICATOR_ID, self.ICON_PATH, appindicator.IndicatorCategory.SYSTEM_SERVICES
        )
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

        notify.init(self.APPINDICATOR_ID)

        if not self.primary_display:
            notify.Notification.new("Brightness Controller", "Error: No primary display detected!", None).show()

    def main(self):
        gtk.main()

    def build_menu(self):
        """Builds the dropdown menu for brightness control."""
        menu = gtk.Menu()

        for value in range(10, 110, 10):  # Generates 10%, 20%, ... 100%
            item = gtk.MenuItem(label=f"{value}%")
            item.connect("activate", self.set_brightness, value / 100.0)
            menu.append(item)

        item_quit = gtk.MenuItem(label="Quit")
        item_quit.connect("activate", self.quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def set_brightness(self, widget, value):
        """Adjusts screen brightness using xrandr."""
        if self.primary_display:
            command = f"xrandr --output {self.primary_display} --brightness {value}"
            try:
                subprocess.run(command, shell=True, check=True)
                notify.Notification.new("Brightness Controller", f"Brightness set to {int(value * 100)}%", None).show()
            except subprocess.CalledProcessError:
                notify.Notification.new("Brightness Controller", "Failed to adjust brightness!", None).show()

    def get_primary_display(self):
        """Retrieves the name of the primary display."""
        try:
            output = subprocess.check_output(["xrandr", "--listmonitors"], universal_newlines=True)
            for line in output.splitlines()[1:]:  # Skipping the first line
                if "*" in line:
                    return line.split()[3]  # Extracting display name
        except subprocess.CalledProcessError:
            return None
        return None

    def quit(self, widget):
        """Closes the application."""
        notify.uninit()
        gtk.main_quit()

if __name__ == "__main__":
    BrightnessController().main()
