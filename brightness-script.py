import os  
import subprocess  


from gi.repository import Gtk as gtk  
from gi.repository import AppIndicator3 as appindicator  
from gi.repository import Notify as notify  


PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

class BrightnessController:
    def __init__(self):
        self.APPINDICATOR_ID = 'indicator-brightnesscontroller'

        # Get the primary display 
        self.primary_display = self.get_primary_display()
        
        self.indicator = appindicator.Indicator.new(self.APPINDICATOR_ID, os.path.abspath(PATH + 'brt.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

        # Initializing Notify
        notify.init(self.APPINDICATOR_ID)
        
    def main(self):
        gtk.main()  

    def build_menu(self):
        menu = gtk.Menu()  
        
        # Adding different brightness levels
        value = 10
        while value <= 100:
            item_myapp = gtk.MenuItem("%3d%%" % value)
            item_myapp.connect('activate', self.brightness, (float(value) / 100))
            menu.append(item_myapp)
            value += 10 
        
        item_quit = gtk.MenuItem('Quit')
        item_quit.connect('activate', self.quit)
        menu.append(item_quit)

        menu.show_all() 
        return menu
    
    def brightness(self, widget, value):
        # Adjusting brightness lvl using xrandr command
        if self.primary_display:
            os.system(f"xrandr --output {self.primary_display} --brightness {value}")

    def get_primary_display(self):
        # Running xrandr command to list monitors
        try:
            output = subprocess.check_output(["xrandr", "--listmonitors"], universal_newlines=True)
            for line in output.splitlines()[1:]:
                if "*" in line:
                    return line.split()[3] 
        except subprocess.CalledProcessError:
            pass
        return None 

    def quit(self, widget):
        notify.uninit()
        gtk.main_quit()

if __name__ == "__main__":
    brightness_controller = BrightnessController()
    brightness_controller.main()
