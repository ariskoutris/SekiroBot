import pydirectinput
import time
import sekiro

# instructions -- needs to go in a requirements or readme
    # install python
    # unlock the right game portion of sekiro
    # setup keybinds
    # setup idol on bar and set camera speed properly


def countdown(seconds):
    print(f"\n\nStarting Sekiro Farmer bot in {seconds} seconds. Set window focus to the game and exit any menus.")
    for i in range(0, seconds):
        print(i + 1)
        time.sleep(1)
    print("\nProceeding with farmbot...\n")

def use_idol():
    ### If your computer loads faster or slower, you may need to change this setting.
    # Just time how long it takes for your computer to load in and be ready and put that in here.
    wait_time = 18
    print("Using Idol.")
    sekiro.item_use()
    pydirectinput.press('down')
    pydirectinput.press('enter')
    print(f"Waiting {wait_time} seconds for Loading Screen.")
    time.sleep(wait_time)

def prepare_jump():
    print("Preparing Jump.")
    sekiro.camera_left(90)
    sekiro.walk_forward(.5)

def jump_and_grapple():
    print("Performing jump and grapple.")
    sekiro.jump()
    time.sleep(.2)
    sekiro.grapple()
    time.sleep(1.8)

def drop_from_ledge():
    print("Dropping from ledge.")
    # stealth on
    sekiro.toggle_stealth()
    # line up to walk off behind enemy
    sekiro.camera_left(45)
    # walk forward slowly off ledge
    sekiro.walk_slow_start()
    sekiro.walk_forward(2.8)
    sekiro.walk_slow_stop()

def kill_and_collect():
    print("Killing and collecting loot.")
    # turn to face enemy's back
    sekiro.camera_right(135)
    # walk forward minimal amount to line up kill
    sekiro.walk_slow_start()
    sekiro.walk_forward(.1)
    sekiro.walk_slow_stop()
    sekiro.camera_lock()
    # main attack button to 1-hit kill, wait for death animation
    sekiro.attack()
    time.sleep(1.6)
    # collect item
    sekiro.interact_hold(1.2)


if __name__ == "__main__":
    countdown(5)
    counter = 0
    while True:
        use_idol()
        prepare_jump()
        jump_and_grapple()
        drop_from_ledge()
        kill_and_collect()
        counter += 1
        print(f" -- Farm bot has killed {counter} time(s). --")