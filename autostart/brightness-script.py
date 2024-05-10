import os  
import subprocess  


from gi.repository import Gtk as gtk  
from gi.repository import AppIndicator3 as appindicator  
from gi.repository import Notify as notify  


PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

class BrightnessController:
    def __init__(self):
        # Unique identifier for the indicator
        self.APPINDICATOR_ID = 'indicator-brightnesscontroller'
        # Get the primary display identifier
        self.primary_display = self.get_primary_display()
        
        # Creating a new AppIndicator with an icon
        self.indicator = appindicator.Indicator.new(self.APPINDICATOR_ID, os.path.abspath(PATH + 'brt.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        # Setting the status of the indicator to active
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        # Setting the menu for the indicator
        self.indicator.set_menu(self.build_menu())
        # Initializing the Notify library
        notify.init(self.APPINDICATOR_ID)
        
    def main(self):
        gtk.main()  # Start the GTK+ main loop

    def build_menu(self):
        menu = gtk.Menu()  # Creating a new GTK menu
        
        # Adding menu items for different brightness levels
        value = 10
        while value <= 100:
            item_myapp = gtk.MenuItem("%3d%%" % value)
            item_myapp.connect('activate', self.brightness, (float(value) / 100))
            menu.append(item_myapp)
            value += 10 
        
        # Adding a quit option to the menu
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all()  # Show all menu items
        return menu
    
    def brightness(self, widget, value):
        # Adjusting the brightness using xrandr command if primary display is available
        if self.primary_display:
            os.system(f"xrandr --output {self.primary_display} --brightness {value}")

    def get_primary_display(self):
        try:
            # Running xrandr command to list monitors
            output = subprocess.check_output(["xrandr", "--listmonitors"], universal_newlines=True)
            # Parsing the output to find the primary display
            for line in output.splitlines()[1:]:
                if "*" in line:
                    return line.split()[3]  # Returning the identifier of the primary display
        except subprocess.CalledProcessError:
            pass
        return None 

    def quit(self, widget):
        # Uninitializing the Notify library and quitting the GTK+ main loop
        notify.uninit()
        gtk.main_quit()

if __name__ == "__main__":
    # Creating an instance of BrightnessController and starting the main loop
    brightness_controller = BrightnessController()
    brightness_controller.main()
