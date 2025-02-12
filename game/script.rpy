# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
$ player_name: str = ""
define player = Character("[player_name]")
define e = Character("Eileen")
image eug_back = "images/eugene_bg.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene eug_back:
        # zoom 1.0  # Ensure the image is scaled correctly
        # xalign 0.5  # Center horizontally
        # yalign 0.5  # Center vertically
        fit "cover"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # Get player name and process it
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "test"

    # Greet player
    e "Hi [player_name]"
    menu:

        "What should I do?"

        "Eat a bagel":
            jump bagel

        "Eat a donut":
            jump donut
    
    # This ends the game.

label bagel:
    "Eating a bagel"


label donut:
    "Eating a donut"


    return
