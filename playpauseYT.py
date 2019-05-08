import os
import commands
import keyboard

def main():
    found = False
    tab_count = commands.getoutput(
        "osascript -e 'tell application \"Google Chrome\" to count every tab of front window'")
    for i in range(1, int(tab_count)+1):
        current_tab = commands.getoutput(
            "osascript -e 'tell application \"Google Chrome\" to get URL of tab " + str(i) + " of front window'")
        if "www.youtube.com/watch?v" in current_tab:
            found = True
            c = i
            break

    if found == True:
        yt = commands.getoutput("osascript -e' tell application \"Chrome\" to (tab " + str(c) + " of front window)'")
        os.system("osascript -e 'tell application \"Google Chrome\" to tell "+yt+" to execute javascript \"document.getElementsByClassName(\\\"ytp-play-button ytp-button\\\")[\\\"0\\\"].click();\"'")

def execute():
    while True:
        if keyboard.is_pressed('f8'):
            main()

execute()
