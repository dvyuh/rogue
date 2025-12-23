#import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)
#warnings.filterwarnings("ignore", category=FutureWarning)
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80 #screen width
    screen_height = 50 #screen height
    player_x = int(screen_width / 2) #player x coord
    player_y = int(screen_height / 2) #player y coord


    tileset = tcod.tileset.load_tilesheet("asset.png", 32, 8, tcod.tileset.CHARMAP_TCOD,
    )# this shows which font to use. the assest.png file

    event_handler = EventHandler()# instance of EventHandler. used here to recieve events

    with tcod.context.new_terminal( #this is what creates the new menu
        screen_width,
        screen_height,
        tileset=tileset,
        title="rogue",
        vsync=False,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        #console creation numpy access arrays as y,x .. the order f changes it to [x,y]
        
        while True: #gmaeplay loop
            root_console.print(x=player_x, y=player_y, string="@") #print player at x and y
            context.present(root_console) # this updates the screen
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action,MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
