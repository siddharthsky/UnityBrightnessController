<h1 align="center">
  <br>
  <a href="https://github.com/siddharthsky/UnityBrightnessController"><img src="https://i.imgur.com/aBvmgsh.png" alt="Unity Brightness Controller" width="100"></a>
  <br>
   Unity Brightness Controller
  <br>
</h1>

<h4 align="center">Brighten your Linux display effortlessly from the system tray.</h4>

<p align="center">
  <a href="https://github.com/siddharthsky/UnityBrightnessController/issues"><img src="https://img.shields.io/github/issues/siddharthsky/UnityBrightnessController"></a> 
  <a href="https://github.com/siddharthsky/UnityBrightnessController/stargazers"><img src="https://img.shields.io/github/stars/siddharthsky/UnityBrightnessController"></a>
  <a href="https://github.com/siddharthsky/UnityBrightnessController/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </a>
</p>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a> •
  <a href="#reason-for-creation">Reason for Creation</a> •
  <a href="#notes">Notes</a>
</p>

## Description
This is a simple Python script for controlling the brightness of a primary display in Linux using an AppIndicator. It allows users to adjust the brightness of their primary display through a dropdown menu in the system tray.

## Requirements
- Python 3.x
- Gtk3
- AppIndicator3

## Usage
1. **Download:** Download the zip file from the latest release of the repository.
2. **Extract:** Extract the contents of the zip file.
3. **Navigate:** Navigate to the extracted folder.
4. **Copy Files:** Copy the files to `/home/[username]/.config/autostart/` directory

    Note: Replace `[username]` with your actual username.

5. **Edit Desktop File:** Open the `brightness-controller.desktop` file in a text editor and modify the `Exec` line to point to the correct path of `brightness-script.py`. 
For example:
    ```
    Exec=python3 /home/[username]/.config/autostart/brightness-script.py
    ```

6. **Save Changes:** Save the changes to `brightness-controller.desktop`.

7. **Auto-Start:** Now, the brightness controller script will automatically run on startup.

This setup ensures that the brightness controller script runs automatically every time you log in. Adjustments to the brightness can be made through the dropdown menu in the system tray.

<!-- ## Menu Options
- The menu contains options for adjusting brightness levels from 10% to 100% in increments of 10%. -->

## Reason for Creation
The reason for creating this script is that there is no built-in brightness controller in Ubuntu Unity System tray. While many desktop environments provide native brightness controls, Unity lacks this feature. This script fills that gap by providing a simple yet effective way to adjust display brightness directly from the system tray.


## Notes
- This script assumes the usage of the `xrandr` command-line utility for adjusting display brightness. Ensure that `xrandr` is installed and available in your system's PATH. 
- This script may need to be run with elevated privileges to adjust display brightness, depending on your system configuration.

## License
This project is licensed under the [MIT License](LICENSE).


Feel free to contribute, report issues, or suggest improvements!

## Credits 
<a href="https://www.flaticon.com/free-icons/sun" title="sun icons">Sun icons created by Freepik - Flaticon</a>