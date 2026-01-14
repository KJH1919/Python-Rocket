import time

# Define color constants using ANSI escape codes
GREEN_ON_BLACK = '\033[1;32;40m'
RESET = '\033[0m'
RED_ON_BLACK = '\033[1;31;40m' # for error messages

# Define fixed simulation constants
FIXED_ROCKET_DRY_MASS_KG = 500.0 # The structural weight of the rocket
FIXED_INITIAL_FUEL_MASS_KG = 2000.0 # The initial weight of the fuel
MASS_PER_ASTRONAUT_KG = 80.0 # Average mass including gear

# Default values for user inputs
DEFAULT_ASTRONAUTS = 3
DEFAULT_THRUST = 50000.0
DEFAULT_FUEL_BURN = 50.0
DEFAULT_TIME_STEP = 0.5
DEFAULT_SIM_DURATION = 120.0

def input_with_default(prompt, default, value_type=float):
    """Get user input with a default value. Press Enter to accept default."""
    user_input = input(f'{prompt} [{default}]: ').strip()
    if user_input == '':
        return value_type(default)
    return value_type(user_input)

def clear_screen():
    """Clears the terminal screen using ANSI escape codes."""
    print('\033[2J\033[H', end='')

def launch_animation():
    """Plays an EPIC multi-stage space adventure animation."""
    hide_cursor()
    
    # ===== STAGE 1: LAUNCH INTO SPACE =====
    width = 40
    height = 20
    rocket = [
        '    /\\    ',
        '   |==|   ',
        '   |  |   ',
        '   |  |   ',
        '   |  |   ',
        '   |  |   ',
        '   |==|   ',
        '   /||\\   ',
    ]
    flame_frames = ['  🔥🔥  ', ' 🔥🔥🔥 ', '🔥🔥🔥🔥']
    
    for y in range(height):
        clear_screen()
        for _ in range(height - y):
            print(' ' * width + '✨')
        for line in rocket:
            print(' ' * (width - 5) + line)
        print(' ' * (width - 5) + flame_frames[y % len(flame_frames)])
        time.sleep(0.12)
    
    print('\n' + GREEN_ON_BLACK + '🚀 LEAVING EARTH ATMOSPHERE... 🚀' + RESET)
    time.sleep(1.5)
    
    # ===== STAGE 2: SPACE TRAVEL TO MARS =====
    space_rocket = ['    🚀']
    for i in range(15):
        clear_screen()
        print('\n' * 3)
        print(GREEN_ON_BLACK + '        ═══ INTERPLANETARY TRAVEL ═══' + RESET)
        print('\n')
        stars = ''.join(['✨' if (i + j) % 4 == 0 else '  ' if (i + j) % 3 == 0 else ' ·' for j in range(25)])
        print('  ' + stars)
        print('  ' + stars[::-1])
        print('\n')
        trail = '· · · · ·' if i % 2 == 0 else ' · · · ·'
        print(' ' * (i * 3) + trail + ' 🚀💨')
        print('\n')
        print('  ' + stars)
        print('  ' + stars[::-1])
        print('\n')
        print(f'        Distance to Mars: {225 - (i * 15):,} million km')
        time.sleep(0.2)
    
    print('\n' + RED_ON_BLACK + '🔴 MARS APPROACH DETECTED 🔴' + RESET)
    time.sleep(1.5)
    
    # ===== STAGE 3: LANDING ON MARS =====
    mars_surface = [
        '🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴',
        '🏔️    🪨      🏔️    🪨      🏔️',
    ]
    
    for y in range(10, 0, -1):
        clear_screen()
        print('\n' * y)
        print('              /\\')
        print('             |==|')
        print('             |  |')
        print('             |==|')
        print('             🔥🔥' if y > 1 else '             💨💨')
        print('\n' * (10 - y))
        for line in mars_surface:
            print(line)
        time.sleep(0.2)
    
    clear_screen()
    print('\n' * 4)
    print('              /\\')
    print('             |==|')
    print('             |  |')
    print('             |==|')
    print('             ████')
    for line in mars_surface:
        print(line)
    print('\n' + GREEN_ON_BLACK + '🛬 SUCCESSFUL MARS LANDING! 🛬' + RESET)
    time.sleep(2)
    
    # ===== STAGE 4: ASTRONAUT MEETS ALIEN =====
    clear_screen()
    print('\n' + GREEN_ON_BLACK + '═══ FIRST CONTACT ═══' + RESET + '\n')
    print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
    print('')
    print('    🧑‍🚀                            👽')
    print('   /|\\                            /|\\')
    print('   / \\                            / \\')
    print('')
    print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
    print('\n   👽: "GREETINGS EARTHLING... PREPARE TO BE PROBED!"')
    time.sleep(2.5)
    
    # ===== STAGE 5: ASTRONAUT SHOOTS ALIEN =====
    clear_screen()
    print('\n' + RED_ON_BLACK + '═══ NOT TODAY, ALIEN! ═══' + RESET + '\n')
    print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
    print('')
    print('    🧑‍🚀 ―――――💥💥💥―――――――→  👽')
    print('   /|\\        PEW PEW!        /|\\')
    print('   / \\                        / \\')
    print('')
    print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
    print('\n   🧑‍🚀: "SAY HELLO TO MY LITTLE FRIEND!"')
    time.sleep(1.5)
    
    # Alien explosion
    for i in range(3):
        clear_screen()
        print('\n' + RED_ON_BLACK + '═══ ALIEN ELIMINATED ═══' + RESET + '\n')
        print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
        print('')
        explosions = ['💥', '🔥💥🔥', '✨💥✨']
        print('    🧑‍🚀                        ' + explosions[i])
        print('   /|\\                          ')
        print('   / \\                          ')
        print('')
        print('🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴')
        time.sleep(0.4)
    
    print('\n   🧑‍🚀: "GET REKT LMAOOO 😂"')
    time.sleep(2)
    
    # ===== STAGE 6: WORMHOLE APPEARS =====
    clear_screen()
    print('\n' + '\033[1;35;40m' + '═══ ANOMALY DETECTED ═══' + RESET + '\n')
    time.sleep(1)
    
    wormhole_frames = [
        ['        ○        '],
        ['       (○)       '],
        ['      ((○))      '],
        ['     (((○)))     '],
        ['    ((((○))))    '],
        ['   (((( ⭕ ))))   '],
        ['  ((((  🌀  )))) '],
        [' (((((  🌀  )))))'],
        ['((((((  🌀  ))))))'],
    ]
    
    for frame in wormhole_frames:
        clear_screen()
        print('\n' + '\033[1;35;40m' + '═══ WORMHOLE OPENING ═══' + RESET + '\n')
        print('\n' * 3)
        for line in frame:
            print('\033[1;35;40m' + '          ' + line + RESET)
        print('\n' * 3)
        time.sleep(0.3)
    
    print('\n   🧑‍🚀: "YOOO WHAT IS THAT?!"')
    time.sleep(1.5)
    
    # Astronaut enters wormhole
    for i in range(8):
        clear_screen()
        print('\n' + '\033[1;35;40m' + '═══ ENTERING WORMHOLE ═══' + RESET + '\n')
        print('\n' * 2)
        print('          ((((((  🌀  ))))))')
        spaces = ' ' * (10 + i * 2)
        if i < 7:
            print(spaces + '🧑‍🚀💨')
        else:
            print('           🧑‍🚀 → 🌀')
        print('\n' * 2)
        swirl = '~*~' * (i + 1)
        print('\033[1;35;40m' + '     ' + swirl + RESET)
        time.sleep(0.25)
    
    # Trippy wormhole travel
    trippy = ['🌀', '🌌', '✨', '💫', '⭐', '🔮', '💜', '🟣']
    for i in range(12):
        clear_screen()
        print('\n' + '\033[1;35;40m' + '═══ INTERDIMENSIONAL TRAVEL ═══' + RESET + '\n')
        for j in range(8):
            row = ''.join([trippy[(i + j + k) % len(trippy)] + ' ' for k in range(15)])
            print('  ' + row)
        print('\n        🧑‍🚀 AAAAAAHHHHH!!!')
        time.sleep(0.15)
    
    time.sleep(1)
    
    # ===== STAGE 7: ARRIVAL AT VIANNEY HIGH SCHOOL =====
    clear_screen()
    print('\n' + '\033[1;33;40m' + '═══ EXITING WORMHOLE ═══' + RESET + '\n')
    time.sleep(1)
    
    # Falling from sky
    for y in range(8):
        clear_screen()
        print('\n' * y)
        print('                    🧑‍🚀')
        print('                   💨💨')
        print('\n' * (8 - y))
        time.sleep(0.2)
    
    # Landing at Vianney
    clear_screen()
    print('\n' + '\033[1;33;40m' + '════════════════════════════════════════' + RESET)
    print('\033[1;33;40m' + '     WELCOME TO VIANNEY HIGH SCHOOL     ' + RESET)
    print('\033[1;33;40m' + '════════════════════════════════════════' + RESET)
    print('')
    print('              🏫🏫🏫🏫🏫')
    print('             |  VIANNEY  |')
    print('             | HIGH SCHOOL|')
    print('             |  ▓▓  ▓▓  |')
    print('             |  ▓▓  ▓▓  |')
    print('             |    🚪    |')
    print('        🌳   ████████████   🌳')
    print('      🌳🌳  ════════════════  🌳🌳')
    print('')
    print('                 🧑‍🚀')
    print('                /|\\')
    print('                / \\')
    print('')
    print('═══════════════════════════════════════')
    time.sleep(2)
    
    print('\n   🧑‍🚀: "Yo... is this... VIANNEY?!"')
    time.sleep(1.5)
    print('   🧑‍🚀: "I just shot an alien on Mars..."')
    time.sleep(1.5)
    print('   🧑‍🚀: "Went through a WORMHOLE..."')
    time.sleep(1.5)
    print('   🧑‍🚀: "And ended up at HIGH SCHOOL?!"')
    time.sleep(1.5)
    print('\n' + '\033[1;33;40m' + '   🔔 RING RING! Time for class! 📚' + RESET)
    time.sleep(2)
    
    # Final screen
    clear_screen()
    print('\n' * 3)
    print('\033[1;32;40m' + '╔══════════════════════════════════════════╗' + RESET)
    print('\033[1;32;40m' + '║                                          ║' + RESET)
    print('\033[1;32;40m' + '║   🚀 MISSION COMPLETE 🚀                 ║' + RESET)
    print('\033[1;32;40m' + '║                                          ║' + RESET)
    print('\033[1;32;40m' + '║   ✅ Launched from Earth                 ║' + RESET)
    print('\033[1;32;40m' + '║   ✅ Landed on Mars                      ║' + RESET)
    print('\033[1;32;40m' + '║   ✅ Eliminated hostile alien            ║' + RESET)
    print('\033[1;32;40m' + '║   ✅ Traversed wormhole                  ║' + RESET)
    print('\033[1;32;40m' + '║   ✅ Arrived at Vianney High School      ║' + RESET)
    print('\033[1;32;40m' + '║                                          ║' + RESET)
    print('\033[1;32;40m' + '║        🧑‍🚀 YOU ARE A LEGEND 🧑‍🚀           ║' + RESET)
    print('\033[1;32;40m' + '║                                          ║' + RESET)
    print('\033[1;32;40m' + '╚══════════════════════════════════════════╝' + RESET)
    print('\n' * 2)
    time.sleep(3)
    show_cursor()

def hide_cursor():
    """Hides the terminal cursor."""
    print('\033[?25l', end='')

def show_cursor():
    """Shows the terminal cursor."""
    print('\033[?25h', end='')

def crash_animation():
    """Plays a simple text-based crash animation."""
    hide_cursor()
    width = 40
    crash_frames = [
        [
            '  /\\  ',
            ' |XX| ',
            ' |  | ',
            ' |  | ',
            ' |==| ',
            ' ||  ',
            ' 💨  ',
        ],
        [
            '  /\\  ',
            ' |XX| ',
            ' |  | ',
            ' |==| ',
            ' ||  ',
            ' 💨💨 ',
        ],
        [
            '  💥  ',
            ' 💥💥 ',
            ' 💨💨💨 ',
        ],
    ]
    for frame in crash_frames:
        clear_screen()
        for line in frame:
            print(' ' * width + line)
        time.sleep(0.4)  # Slow down the crash animation
    print('\n' + RED_ON_BLACK + '💥 VEHICLE LOST 💥' + RESET)
    time.sleep(1.0)
    show_cursor()

def run_simulation():
    """Runs a simple Rocket Simulation where a craft lifts off based on user inputs."""
    print(f'{GREEN_ON_BLACK}Welcome to my Rocket Simulation!{RESET}')

    try:
        print('\n(Press Enter to accept default values shown in brackets)\n')
        astronaut_count_in = input_with_default('Enter the number of astronauts', DEFAULT_ASTRONAUTS, int)

        if astronaut_count_in < 0:
             print(f'{RED_ON_BLACK}Astronaut count cannot be negative. Exiting the simulation!{RESET}')
             return

        astronaut_mass = astronaut_count_in * MASS_PER_ASTRONAUT_KG
        initial_total_mass = FIXED_ROCKET_DRY_MASS_KG + FIXED_INITIAL_FUEL_MASS_KG + astronaut_mass

        print(f'\nConfiguration Summary:')
        print(f'- Astronauts on board: {astronaut_count_in} (Total Mass: {astronaut_mass:.1f} kg)')
        print(f'- Fixed Rocket Dry Mass: {FIXED_ROCKET_DRY_MASS_KG} kg')
        print(f'- Initial Fuel Mass: {FIXED_INITIAL_FUEL_MASS_KG} kg')
        print(f'- Total Initial Launch Mass: {initial_total_mass:.1f} kg\n')

        # Get remaining user inputs for simulation parameters (thrust is still variable)
        thrust_in = input_with_default('Enter your thrust (Newtons)', DEFAULT_THRUST)
        fuel_burn = input_with_default('Enter fuel burn rate (kg/s)', DEFAULT_FUEL_BURN)
        time_step = input_with_default('Enter time step duration (seconds)', DEFAULT_TIME_STEP)
        sim_dur = input_with_default('Enter max simulation duration (seconds)', DEFAULT_SIM_DURATION)

        # Validate inputs
        if thrust_in <= 0 or fuel_burn <= 0 or time_step <= 0 or sim_dur <= 0:
            print(f'{RED_ON_BLACK}All input values must be positive. Exiting the simulation!{RESET}')
            return
            
    except ValueError:
        # Handle non-numeric inputs
        print(f'{RED_ON_BLACK}Your input was invalid. Try Again!{RESET}')
        return

    # Initialize simulation variables
    gravity = 9.81 # m/s^2
    drag_coefficient = 0.05 # a simple constant for basic drag modeling
    takeoff_threshold_altitude = 10.0 # meters
    velocity = 0.0 # m/s
    altitude = 0.0 # meters
    current_mass = initial_total_mass # Start with total mass
    thrust = thrust_in
    sim_time = 0.0
    liftoff_achieved = False
    initial_fuel = FIXED_INITIAL_FUEL_MASS_KG # Track fuel separately to stop burn

    print(f'{GREEN_ON_BLACK}Starting Simulation...{RESET}')

    # Main simulation loop
    # Continue as long as time hasn't run out AND we still have *some* fuel (arbitrary low threshold for dry mass)
    while sim_time < sim_dur and current_mass > (FIXED_ROCKET_DRY_MASS_KG + astronaut_mass):
        # Calculate forces
        force_of_gravity = current_mass * gravity
        force_of_drag = drag_coefficient * velocity**2
        net_force = thrust - force_of_gravity - force_of_drag

        if current_mass <= 0:
            break # Should not happen with dry mass threshold but good practice

        acceleration = net_force / current_mass
        velocity += acceleration * time_step

        if velocity < 0:
            velocity = 0 # Prevent velocity from becoming negative
        
        altitude += velocity * time_step

        # Simulate fuel burn and corresponding changes in mass/thrust
        fuel_burned_in_step = fuel_burn * time_step
        if initial_fuel >= fuel_burned_in_step:
            current_mass -= fuel_burned_in_step
            initial_fuel -= fuel_burned_in_step
            # A simple thrust reduction model as fuel density changes or tanks empty
            thrust *= (1 - (fuel_burned_in_step / FIXED_INITIAL_FUEL_MASS_KG) * 0.1)
        else:
            # Out of fuel, stop burning/reducing mass/thrust
            fuel_burned_in_step = initial_fuel
            current_mass -= fuel_burned_in_step
            initial_fuel = 0
            thrust = 0 # Engine cut off

        if altitude >= takeoff_threshold_altitude and not liftoff_achieved:
            liftoff_achieved = True
            print(f'\n*** LIFTOFF ACHIEVED at T+{sim_time:.2f} seconds! ***\n')

        # Increment time
        sim_time += time_step

        # Print status every 10 seconds of simulation time
        if int(sim_time / time_step) % (10 / time_step) == 0:
            print(f'T+{sim_time:.2f}s | Alt: {altitude:.2f}m | Vel: {velocity:.2f} m/s | Mass: {current_mass:.2f}kg | Fuel Left: {initial_fuel:.2f}kg')

    # Output Results
    print('\n--- Simulation Summary ---')
    if liftoff_achieved and altitude > 0:
        print('Result: SUCCESS - The rocket successfully lifted off.')
        time.sleep(2)
        launch_animation()
    else:
        print('Result: FAILURE - The rocket did not achieve sustained liftoff.')
        time.sleep(2)
        crash_animation()
    print(f'Final Time: {sim_time:.2f} seconds')
    print(f'Final Altitude: {altitude:.2f} meters')
    print(f'Final Velocity: {velocity:.2f} m/s')
    print(f'Final Mass (dry mass + crew): {current_mass:.2f} kg')

if __name__ == '__main__' :
    run_simulation()