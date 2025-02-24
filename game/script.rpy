# Declare characters used by this game. The color argument colorizes the
# name of the character.
$ player_name: str = ""
define player = Character("[player_name]")

# characters
define bookstore_woman = Character("Marion") # Basically Izzie
define rude_woman = Character("Jen")
define rude_woman2 = Character("Pearl")
define s = Character("Sarah") # basically Sally
define j = Character("Judy") 

# choices
define book_seeking = None
define went_to_spiritual_meeting = False
# images
image eug_back = "images/eugene_bg.jpg"
image apt_back = "images/apartment.jpg"
image bookstore_back = "images/bookstore_bg.jpg"
image house_back = "images/house_bg.jpg"
image baleboostehs_back = "images/bale_bg.jpg"
image cred1 = "images/src1.jpg"
image cred2 = "images/src2.jpg"
image cred3 = "images/src3.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene eug_back:
        fit "cover"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # Intro sequence giving broad context
    "Eugene, 1984."

    "Lesbians are flocking to Eugene from all over the country. The area is a haven for them, with a lesbian sub-economy
    and vibrant social scene. There are lesbian-run forestry groups, food distribution companies, and more. Lesbian bookstores,
    bars, and sports create a sense of community."

    "There's also a major Jewish push for Soviet Jews to immigrate to America for fear of repression and economic needs. This formed a national
    Jewish political movement, along with much Jewish feminism and involvement in the gay and lesbian liberation movements."
    
    "Jewish women were occupying new spaces in the economy by working jobs. 
    Reform synagogues were slowly becoming more accepting of queer people, though many were still hostile."

    "In this context, you arrive in Eugene."


    # Get player name and process it
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Sarah"

    
    
    
    # Opening scene
    #FIXME the flow is bad here, try adding a black screen. Also friend before they left doesn't make sense. ANother screen before entering
    scene apt_back with fade:
        fit "cover"
    "(Your new apartment is small. The walls are bare, the mattress is on the floor, and the kitchen 
    has mismatched dishes from a thrift store. Outside, the sound of bicycles, birds, and occasional yelling drifts in through 
    the open window.)"

    "Eugene isn’t quite what you expected. It’s greener, quieter. The air smells like rain and something herbal, maybe patchouli. 
    You don’t know anyone yet, but that’s going to change."

    "(You glance at a list scrawled in your notebook—places to check out, recommended by a friend who visited before. 
    At the top: “Mother Kali’s Books – Women’s books, radical stuff.”)"

    scene bookstore_back with fade:
        fit "cover"
    "You enter Mother Kali’s Books, a small, dimly lit bookstore filled with the smell of old paper and incense. 
    A black cat dozes on the counter. Shelves are packed with books on feminism, poetry, spirituality, and revolution."

    "(A woman in her 40s, with silver-streaked hair and a gauzy shawl, looks up from behind the counter. This is Marion, the owner.)"
    
    bookstore_woman "You must be new."
    
    "(You nod.)"

    bookstore_woman "Figured. I know most folks around here."
    
    "(She gestures at the shelves)"
    
    bookstore_woman "Looking for something in particular?"

    menu:
        "Feminist books":
            "I'm looking for anything feminist."
            $ book_seeking = "feminist"
            jump book_choice
        
        "Socialist books":
            "I'm looking for some socialist works."
            $ book_seeking = "socialist"
            jump book_choice

        "Just looking around":
            "I'm not really sure, just browsing."
            $ book_seeking = "none"
            jump book_choice


label book_choice:
    if book_seeking == "feminist":
        bookstore_woman "We've got tons of feminist books! Take a look over there."
        "(She points to a corner overflowing with books.)"
        "(You pick up a few that seem interesting and read for half an hour.)"
        jump baleboostehs_suggestion
    elif book_seeking == "socialist":
        bookstore_woman "We've got tons of socialist books! There's the Marx corner."
        "(She points to a corner overflowing with books.)"
        bookstore_woman "And there's the more anarchist stuff over there."
        "(She points to a stack in the back.)"
        "(You walk to the Marx section and pick up a few that seem interesting. You sit and read for half an hour.)"
        jump baleboostehs_suggestion
    else:
        bookstore_woman "You might try some local Eugene history ones. Look over in that corner."
        "(She points to a spot in the back with a bunch of magazines. You walk over and grab one, browsing it on a couch.)"
        jump baleboostehs_suggestion

label baleboostehs_suggestion:
    "..."
    "(You get ready to leave and walk towards the door.)"

    "(Marion stops you.)"

    bookstore_woman "You might like a group I know. They meet every week—women’s spirituality, earth-based, goddess traditions, that kind of thing. 
    Real deep conversations. Might help you find your footing here."

    menu:
        "Accept":
            jump spiritual_group

        "Decline":
            jump walk_home

label spiritual_group:
    #FIXME intro
    scene house_bg with fade:
        fit "cover"
    "You join a circle of women in a candlelit room, sitting on the floor. You listen as they talk about energy, 
    past lives, and divine feminine power."
    
    "At first, it’s interesting. Some of it even feels familiar. But something is… off."

    "(The conversation shifts. A woman with long blonde hair sighs dramatically.)"


    rude_woman "It’s so sad how people get stuck in their old traditions. They don’t understand real spirituality."
    
    "(You stiffen.)"

    rude_woman2 "I had a friend who still did Jewish holidays. I told her, why would you want to be part of a patriarchal religion?"

    "(A few women nod. No one disagrees. No one looks at you.)"

    "You don’t say anything. Maybe they don’t mean it that way. Maybe they don’t even realize."

    "(The meeting ends, and you quitely leave, deciding not to return.)"

    "(As you walk outside, someone else from the meeting catches up to you - Sarah, a friendly, down-to-earth woman with
    frizzy hair and an easy smile.)"

    s "Not your thing, [player_name]?"
   
    "(She laughs)"

    s "Yeah, Jen can be a real schmuck."

    "(She hesitates)"

    s "You might like something else better. There’s a group—Jewish lesbian women, call themselves Baleboostehs. 
    It’s smaller, but it feels more… real."

    "She hands you a flyer with details about the group."

    s "Maybe I'll see you there?"

    $ went_to_spiritual_meeting = True
    jump baleboostehs_meeting

label walk_home:
    "(As you walk home from the bookstore, you spot a flyer tacked to a bulletin board outside a food co-op. 
    It’s handwritten, with doodles of Stars of David and candles.)"

    "“Baleboostehs: A gathering of Jewish lesbians. Community, culture, and connection. Potluck this Sunday—bring something to share.”"

    "You hesitate, not knowing what to expect. But you've got to try something if you want to make friends."
    
    "You reach out and grab the flyer."

    jump baleboostehs_meeting

label baleboostehs_meeting:
    scene baleboostehs_back with fade:
        fit "cover"
    "You look down at the flyer in your hand, confirming the small house you're looking at is the right one."

    "You knock on the door and are greeted by a shorter woman with short, curly gray hair."

    j "Are you here for Baleboostehs? Come in! I'm Judy."

    "(A cozy living room, dimly lit with candles. A table is covered in food—challah, kugel, a dish 
    someone calls their “grandmother’s secret recipe.” Laughter fills the space. Women are talking, leaning close, 
    telling stories. A menorah sits in the window.)"

    if went_to_spiritual_meeting:
        "(Sara, from the spiritual meeting the other day, turns around and smiles at you.)"
        s "Welcome [player_name]! Come join us!"
        "She pulls up a seat for you to sit by her."
    else:
        "(Judy pulls up a seat for you next to her at the table.)"

    #FIXME maybe add more stuff here or at least a transition
    jump time_skip

label time_skip:
    scene baleboostehs_back with fade:
        fit "cover"
    "Years later -- 1989"
    "The group has shrunk quite a bit. Some members moved away, some found new community in other spaces."
    "Some people have started going to synagogue again, now that the rabbis are more progressive."
    "You sit next to Sarah, a longtime member. She pours you some tea and gives a small smile, but she looks pensive."

    s "Feels quieter these days, huh? I guess that's how things go."

    "(You nod.)"

    "(Judy walks in.)"

    j "But we're still here, aren't we?"

    "A few more people enter. The group is smaller, but the warmth is still there. People pour grape juice into cups, and break off
    pieces of challah. The prayer begins:" 

    "'Baruch atah Adonai, Eloheinu melech ha-olam...'"

    "..."

    "As the night winds down, you step outside. The city lights glow, and you stroll along the sidewalk on your way home. 
    The future is uncertain, but one way or another you'll find your way."





label end:
    scene cred1:
        fit "cover"
    ""
    scene cred2:
        fit "cover"
    ""
    scene cred3:
        fit "cover"
    ""
    return
    # This ends the game.