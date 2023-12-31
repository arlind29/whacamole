import solara
from helpers import *
import time 
from time import sleep

####
# Reactive state variables
# initializing reactive variables, to be used to control game / back and front end 
state = get_init_state(how_many_moles=1)
points = solara.reactive(0)
time_spent = solara.reactive(0)
game_on = solara.reactive(True)

@solara.component
def Cell(cell_value): 
    """
    Draw a grid cell for the game

    Args:
        cell_value: cell value of type solara.reactive
    """
    def collect_points(cell_value): 
        if cell_value.value == "-": 
            if game_on.value:
                points.set(points.value - 5)
            return 
        cell_value.set("-")
        points.set(points.value + 1)
    solara.Button(cell_value.value, \
        on_click =lambda:  collect_points(cell_value),
        style= "font-size: 16pt"
    )
    
@solara.component    
def Grid(): 
    """Draw the whacamole grid 
    """
    global state
    for i in range(len(state)):
        with solara.Row(): 
            for j in range(len(state[0])):
                Cell(state[i][j])
    solara.Info(f"Time left : {time_spent.value}")    
    solara.Success(f"Points : {points.value}")    

@solara.component        
def Page(): 
    """
    Draw the app components
    """
    continue_thread, set_continue_thread = solara.use_state(False)
    
    def start(): 
        points.set(0)
        set_continue_thread(True)

    def stop(): 
        game_on.set(False)
        set_continue_thread(False)


    def refresh(): 
        refresh_state(state, how_many_moles=1)
        Grid()    
    
    def run_logic():
        game_on.set(True)
        start_time = time.time()
        print(f"Thread started")
        i = 0
        total_time = 60
        while(continue_thread): 
            sleep(1)
            time_spent_so_far = int(time.time() - start_time) 
            time_spent.set(total_time - time_spent_so_far)
            if i%2 == 0: 
                refresh()
            if (i+1)%total_time==0: 
                break 
            i += 1
        refresh_state(state, how_many_moles=0)            
        game_on.set(False)
        time_spent.set("Game stopped")
        print("Thread stopped")
    
    solara.use_thread(run_logic, dependencies=[continue_thread])
    
    solara.Title("Whac-a-mole")
    with solara.Sidebar(): 
        solara.Button("Start", on_click=start)
        solara.Button("Stop", on_click=stop)
    with solara.Column():
        Grid()
