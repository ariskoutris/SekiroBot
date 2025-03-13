import time
import sekiro


# Run this to begin the farm bot program.


def bot_start_timer(seconds):
    print(f"\n\nStarting Sekiro Farmer bot in {seconds} seconds.")
    print(" Set window focus to the game and exit any menus.")
    print(" View the README for instructions on setup.")
    for i in range(0, seconds):
        print(f" -- {i + 1}")
        time.sleep(1)
    print(" Proceeding with farmbot...")

def use_idol():
    ### If your computer loads faster or slower, you may need to change this setting.
    # Use a stopwatch to time using the idol - stop when game is fully loaded.
    # add about 3 seconds as it's a good time to alt tab and stop the script
    wait_time = 16
    print(" -- Using Idol.")
    sekiro.item_use()
    sekiro.menu_down()
    sekiro.menu_select()
    print(f" -- Waiting {wait_time} seconds for Loading Screen.")
    time.sleep(wait_time)
    
def bulwark_line_up():
    print(" -- Lining up with bulwark.")
    sekiro.camera_left(130)
    sekiro.walk_slow_start()
    sekiro.walk_forward(4)
    sekiro.walk_slow_stop()

def bulwark_jump():
    print(" -- Jumping over bulwark.")
    sekiro.walk_slow_start()
    sekiro.walk_forward_hold_start()
    sekiro.jump()
    time.sleep(1)
    sekiro.walk_slow_stop()
    time.sleep(.8)
    sekiro.walk_forward_hold_stop()

def ledge_jump():
    print(" -- Jumping from ledge.")
    sekiro.walk_forward_hold_start()
    time.sleep(.8)
    sekiro.jump()
    sekiro.walk_forward_hold_stop()
    sekiro.grapple_repeat_for(.5, 2)

def platform_grapple():
    print(" -- Grappling to platform.")
    sekiro.camera_right(135)
    sekiro.walk_forward(1)
    sekiro.camera_up(45)
    sekiro.grapple(2)

def first_enemy_approach():
    print(" -- Approaching first enemy.")
    sekiro.walk_slow_start()
    sekiro.walk_forward(.2)
    sekiro.walk_slow_stop()

def kill_and_collect():
    print(" -- Killing and collecting loot.")
    sekiro.camera_lock()
    sekiro.attack()
    time.sleep(1.6)
    sekiro.interact_hold(1.2)

def platform_drop_off():
    print(" -- Dropping off platform.")
    sekiro.walk_backwards(1)
    sekiro.toggle_stealth()
    time.sleep(.2)

def second_platform_drop_off():
    print(" -- Dropping off second platform.")
    sekiro.walk_forward(1.2)
    time.sleep(.3)

def second_enemy_approach():
    print(" -- Approaching second enemy.")
    sekiro.camera_lock()
    sekiro.walk_slow_start()
    sekiro.walk_forward(.8)
    sekiro.walk_slow_stop()
   
# farming location: "Ashina Outskirts - Outskirts Wall - Stairway" 
def farm_route_instructions_ashina_outskirts():
    use_idol()
    bulwark_line_up()
    bulwark_jump()
    ledge_jump()
    platform_grapple()
    first_enemy_approach()
    kill_and_collect()
    platform_drop_off()
    second_platform_drop_off()
    second_enemy_approach()
    kill_and_collect()

# farming location: "Ashina Castle - Upper Tower - Antechamber"
def farm_route_instructions_ashina_castle():
    use_idol()
    sekiro.walk_backwards(0.01)
    sekiro.camera_lock()
    sekiro.walk_forward_hold_start()
    sekiro.camera_left(40)
    time.sleep(0.7)
    sekiro.camera_right(105)
    time.sleep(0.5)
    sekiro.camera_left(20)
    sekiro.walk_slow_start()
    sekiro.camera_left(70)
    sekiro.walk_slow_stop()
    sekiro.camera_left(100)
    time.sleep(1.25)
    sekiro.attack()
    sekiro.walk_forward_hold_stop()
    sekiro.interact_hold(4)

def print_farm_report(run_count, elalpsed_time, final=False):
    money_per_rounnd = 256
    exp_per_round = 3156
    money_earned = run_count * money_per_rounnd
    experience_earned = run_count * exp_per_round
    if final:
        filler = 200*' '
        print(filler)
        print("---------- Farm Bot Report ----------")
        print(f" Runs Completed:\t{run_count}")
        print(f" Total XP Earned:\t{experience_earned}")
        print(f" Total Sen Earned:\t{money_earned}")
        print(f" Elapsed Time:\t\t{int(elalpsed_time/60)} minutes")
        print(f" XP Rate:\t\t{int(3600*experience_earned/elalpsed_time)} XP/hour")
        print(f" Sen Rate:\t\t{int(3600*money_earned/elalpsed_time)} sen/hour")
        print("-------------------------------------")
    else:
        print(f'Run {run_count} | XP Total: {experience_earned} | Sen Total: {money_earned} | {int(3600*experience_earned/elalpsed_time)} XP/hour | {int(3600*money_earned/elalpsed_time)} sen/hour', end='\r')


if __name__ == "__main__":
    bot_start_timer(5)
    start_time = time.perf_counter()
    run_counter = 0
    while True:
        try:
            farm_route_instructions_ashina_castle()
            elapsed_time = time.perf_counter() - start_time
            run_counter += 1
            print_farm_report(run_counter, elapsed_time)
        except KeyboardInterrupt:
            elapsed_time = time.perf_counter() - start_time
            print_farm_report(run_counter, elapsed_time, final=True)
            exit()