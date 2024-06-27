# main.py
import subprocess
import random
import time
import sys

# Edit path's here if necessary
valvecmd_path = "./valvecmd.exe"
gmod_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\GarrysMod\\hl2.exe"

def run_command(command):
    """Execute the given command using valvecmd.exe."""
    cmd_line = [valvecmd_path, command]
    subprocess.run(cmd_line, check=True)
    # print(f"Executed command: {command}")

def action(command):
    """Simulate moving forward."""
    run_command(f"+{command}")
    time.sleep(random.uniform(0.01, 0.05))
    run_command(f"-{command}")

def start_game():
    """Starts the game with specified parameters before running the main script."""
    params = "-64bit -textmode -single_core -nojoy -low -nosound -sw -noshader -nopix -novid -nopreload -nopreloadmodels -multirun +connect rp.superiorservers.co"
    cmd_line = f'"{gmod_path}" {params}'
    try:
        subprocess.run(cmd_line, check=True, shell=True)
        print("Game started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start the game: {e}")

def main():
    movement_commands = ["forward", "back", "moveleft", "moveright", "jump", "duck", "attack"]
    last_poop_time = time.time()
    start_time = time.time()  # Track the start time
    last_print_time = start_time  # Track the last print time
    poop_count = 0  # Track the number of times say_poop has been executed

    while True:
        current_time = time.time()

        # Check if it's time to say /poop
        if current_time - last_poop_time >= 11:
            """Simulate saying /poop."""
            run_command("rp poop; echo Pooped!")
            last_poop_time = current_time
            poop_count += 1  # Increment the poop count

        # Perform a random movement action every second
        action(random.choice(movement_commands))
        time.sleep(1)

        # Print running time and poop count every minute
        if current_time - last_print_time >= 60:
            elapsed_time = current_time - start_time
            elapsed_days = int(elapsed_time // (24 * 3600))
            elapsed_hours = int((elapsed_time % (24 * 3600)) // 3600)
            elapsed_minutes = int((elapsed_time % 3600) // 60)
            sys.stdout.write(f"Script has been running for {elapsed_days} days {elapsed_hours} hours {elapsed_minutes} minutes. Poop count: {poop_count}    \r")
            sys.stdout.flush()
            last_print_time = current_time
