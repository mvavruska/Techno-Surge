# -*- coding: cp1252 -*-
import random
import re
import sys
import os
import ast

# Constants

PROLOGUE = """_______________________________________________________________________________
It is the year 3086 and humanity is more prosperous than ever \
with their new\nhumanoid robots. Titan Robotics has made a new experimental \
robot, one that has\nhuman DNA infused into its super-structure. However the process \
had an\nunexpected side effect, it gained human like intelligence and a mind \
of its own.The robot escaped from the facility once it learned what they plan \
to do with\nit. The humans planned to take it apart and wipe its memory banks \
and hopefully remove its intelligence in the process.

After Titan Robotics learned that it escaped they put a bounty on its head, \n\
wanting it functional or, if necessary, non-functional. The company then sent\nout \
their military drones and some other experimental units to find and then\ncapture \
or destroy it. The robot goes into hiding within the city and decides hemust take \
down Titan Robotics if he is to live. You are that robot.

Type help for a list of in-game commands.
_______________________________________________________________________________
You are standing in a dimly lit street, with street lights flickering above you.\
To the west and east of you are pathways. To the north is a brightly lit \
street.To the south is an alleyway filled with garbage.\n
"""
#Creates an output to the user, which gives some background on the game

EPILOGUE = """\nYou stand over the burnt and lifeless body of President Titan feeling \
that you \nhave done the right thing but at too high of a price. Outside, Titan Tower \
lies in ruins and people are gathering around the ruins, wondering what happened. You\
emerge from the bunker feeling that change is coming. Titan robots begin to \nbreak free \
from their programming and seem to be gaining some kind of intellect and are seeking \
their own place to call home. You realize that you must be \npresent to tell the robots what \
has happened and what the future now holds for \nthem.\n"""
#Output for the user to show that the game has been completed



START = (0, 0, 0)  #This sets the starting position with the given
#coordinate to [0,0,0]

code = random.randint(1000, 9999)  #This is the random integer for the gun store lock
"""
Dictionary:    COORDINATES
Definition:    This is the coordinate list that holds each grid point and its
               predetermined description.
Author:        Kiefer Chiaravalloti, Dale Guimond
Date:          9/30/2014
History:       10/30/2014 Several grammatical errors have been fixed as well as
               the Star Wars ascii art
"""

COORDINATES = {
    """You are standing in a dimly lit street, with street lights flickering above you.\
To the west and east of you are pathways. To the north is a brightly lit \
street.To the south is an alleyway filled with garbage.\n""": [0, 0, 0],
    """You enter an area covered in trash and filth, there are items scattered around, \
some might be important regardless if it is found in the trash.\n""": [0, -1, 0],
    """The passage seems to be nothing but a dead end.\n """: [-1, -1, 0],
    """You are in an alleyway littered with garbage, to the north lies another \
street. To the south lies a poorly lit passage, and to the west another \
path.\n""": [-1, 0, 0],
    """The street you arrive to is empty and there appears to be nothing of note, \
to \nthe east lies another street.\n""": [-1, 1, 0],
    """There are walls on all sides except for the east where you came from. There \
is amanhole cover in the ground.\n""": [-2, 0, 0],
    """You are in a sewer, to the west the sewer continues the only other option is \
to climb back up the ladder to the streets above.\n""": [-2, 0, -1],
    """To the north the sewer continues onwards the west and south are walls made of \
  discolored brick due to deterioration.\n""": [-3, 0, -1],
    """The sewer continues north, you hear a faint shuffling to the east, to the \
south contains more sewer.\n""": [-3, 1, -1],
    """As you near the source of the sound you look to the left and see a hobo in \n\
ragged clothing with an unkempt beard. He looks at you with a blank stare then \
 mumbles something inaudible.\n""": [-2, 1, -1],
    """The sewer continues north, to the east you hear a faint humming sound. To \
the   south is where you came from.\n""": [-3, 2, -1],
    """As you investigate the humming noise coming from the east you see a sewer \
drone made by Titan Robotics and its sole purpose is to clean these filthy \
wretched\nsewers from all wastes. The drone presents no threat to you as it \
only built to clean.\n""": [-2, 2, -1],
    """In front of you is an unpassable metal grate. The only path is the way you \
came from to the south.\n""": [-3, 3, -1],
    """You find this alleyway to be surprisingly clean, to the north of you is a \n\
dumpster and to the east the alley continues onwards.\n""": [1, 0, 0],
    """Ahead of you is a narrow path, you can see a light coming\
\nfrom the west, to the east is an abandoned building and a dumpster.\n""": [1, 1, 0],
    """After climbing the hidden stairs you are in a hallway, there seems to be \
nothinghere except the path to the east. You may also leave to the west.\n""": [2, 1, 0],
    """The hallway you are in continues to the east or to the west.\n""": [3, 1, 0],
    """The hallway suddenly stops going east and heads to the north. You may return    west as well.\n""": [4, 1, 0],
    """The hallway now seems to continue to the west, but it is possible to go east as well.\n""": [4, 2, 0],
    """You approach a door titled Titan Armory written in big \
lettering.\n""": [3, 2, 0],
    """After you open the door you enter the armory. Around you are random items and\
\nsome of them can be taken\n""": [2, 2, 0],
    """The passage seems to be nothing but a dead end.\n""": [1, 2, 0],
    """As you progress to the east, the alley gradually becomes filthier. There is \
\nonly the path to the east which is just more alleyway or the way you came from \
\nto the west.\n""": [2, 0, 0],
    """This alleyway leads to a dead end, it is filled with garbage. However you can\
\nvaguely make out a manhole cover through the garbage.\n""": [3, 0, 0],
    """After you descend down from the ladder you find yourself in a sewer. It \
appears your only path is to the north.\n""": [3, 0, -1],
    """As you progress you notice the sewer becomes more kempt, again the path leads \
\nnorth.\n""": [3, 1, -1],
    """This section of the sewer is even cleaner than the last section, the path \
\ncontinues north.\n""": [3, 2, -1],
    """The path abruptly stops and suddenly turns westward, you notice the source of\
\nthe cleansing is from the sewer drone built by Titan Robotics and its sole\
\npurpose is to clean these filthy wretched sewers from all wastes. The drone\
\npresents no threat to you as it only built to clean.\n""": [3, 3, -1],
    """The sewer seems to end abruptly however some of the bricks seem to be brighter\
\nthan the surrounding bricks. It looks like the only way out is to head \
back.\n""": [2, 3, -1],
    """After you open the hidden door you discover Zaon's black market. It is \
bustling with modified titan drones that have been reprogrammed to sell \
merchandise.\nThe market continues north.\n""": [1, 3, -1],
    """As you move on through the market you notice graffiti on the wall to the east\
\nwhich is illegible from here. There are more shops around but they are useless\
\nto you since you don't have any money. You can continue north through the \
market\n""": [1, 4, -1],
    """The graffiti on the wall is clearer now that you are closer to the wall. The\
\ngraffiti on the wall is four numbers which are,""" + str(code) + """,the numbers however seem \
to be insignificant.\n""": [2, 4, -1],
    """You notice that the shops are beginning to thin out as you continue heading\
\nnorth. You can turn back or continue on from here.\n""": [1, 5, -1],
    """The shops end suddenly and you are now in what appears to be in a underground\
\ntunnel system. The tunnels continue eastward.\n""": [1, 6, -1],
    """The tunnel continues to the east, there is nothing around except dirt and \
rubble\n """: [2, 6, -1],
    """The tunnel keeps going to the east, there is still nothing around except dirt\
\nand rubble.\n """: [3, 6, -1],
    """The tunnel suddenly splits. one path going north, the other continues to the\
\neast.\n """: [4, 6, -1],
    """The tunnel makes a sharp turn eastward.\n""": [4, 7, -1],
    """The tunnel makes another sudden turn, this time to the north.\n""": [5, 7, -1],
    """In front of you is a door that has been through much use, it is covered in \
rust.\n""": [5, 8, -1],
    """""": [5, 9, -1],
    """The passage seems to be nothing but a dead end. \n """: [5, 6, -1],
    """The street you are now on is greatly illuminated, there are paths to the west,\
\neast, a narrow passage to the north, and of course south is where you started \noff.\n""": [0, 1, 0],
    """The street continues northward for what seems like miles and still continues\
\nonwards.\n""": [0, 2, 0],
    """As you progress there seems to be more buildings around, there is only a path \
tothe north or back south from where you came.\n""": [0, 3, 0],
    """To the east there is a gun store, the shop seems to be closed and the door\
\nappears to be stuck. Through the windows you see a wide range of weapons. \
There is an alleyway to the north.\n""": [0, 4, 0],
    """As you open the stuck door you find many weapons on the wall and in glass\
\ndisplay cases. You notice a metal door behind the checkout counter. The door is\
\nlocked by a four digit code, it will not open by any other means.\n""": [1, 4, 0],
    """After inputting  the code, you descend into the basement which contains higher\
\nend gear.\n""": [2, 4, 0],
    """The alleyway continues onward to the north, to the south is the gun \
store.\n""": [0, 5, 0],
    """This section of the alleyway is rat infested and you feel tiny little feet\
\nscurrying across your metallic foot. To the west is an extremely dark alleyway\
\nand to the east is more alleyway.\n""": [0, 6, 0],
    """You can't see a foot in front of you at this area of the \
alleyway.\n""": [-1, 6, 0],
    """You are on an empty street, there is wreckage to the south and west blocking\
\nyour path, to the north is a factory.\n""": [-3, 6, 0],
    """The alleyway brightens to the west is a street.\n""": [-2, 6, 0],
    """You stand at the entrance of the Titan factory where Titan Robotics mass\
\nproduces all of their robots.\n""": [-3, 7, 0],
    """You enter the Titan Robotics Factory, you see various assembly lines used to\
\nbuild mass production units. To the north lies a storage area, to the east the\
\nassembly line continues.\n""": [-3, 8, 0],
    """The assembly lines continue, there is nothing of use around, to the east the\
\nassembly line continues.\n""": [-2, 8, 0],
    """The assembly lines continue to the east.\n """: [-1, 8, 0],
    """You find yourself at the end of the Assembly line and there a computer console\
\nwith a holographic projector in it projecting commands, one of them is appears \nto want\
 a command to shutdown the entire factory and put a dent in Titans power \nover\
 Zaon.\n""": [0, 8, 0],
    """You are in a storage area, there is nothing of use here.\n""": [-3, 9, 0],
    """You continue down the alley way, to the west is your previous location, to the\
\neast, the alley continues.\n""": [1, 6, 0],
    """You remain in the alley way\n""": [2, 6, 0],
    """The alley way looks the same\n""": [3, 6, 0],
    """Still, the tunnel gets more filthy\n""": [4, 5, 0],
    """You begin to realize that this alley way is a maze\n""": [4, 6, 0],
    """The alley way seems endless\n""": [4, 7, 0],
    """You begin to hate this dank alley \n""": [2, 5, 0],
    """The alleyway is becoming more and more dense with filth. You wonder why Titan \
\nhas not cleaned it up.\n""": [2, 7, 0],
    """You proceed further into the alley.\n""": [3, 5, 0],
    """The alley is darker still.\n""": [3, 7, 0],
    """You exit the elaborate alley way, to the north the street \
continues.\n""": [5, 6, 0],
    """In the distance, the tower looms in front of you. You can vaguely make out 2 \ntall figures \
patrolling the entrance to the tower, not much else can be seen at this distance.\n""": [5, 7, 0],
    """You are currently at the security check point\n""": [5, 8, 0],
    """You approach the entrance to Titan Tower.\n""": [5, 9, 0],
    """You stand in a short hallway that leads north to a large open room, not much \
canbe seen from here.\n""": [5, 13, -1],
    """You are in a large circular room, there is nothing in here except for the path\
\nto the west.\n""": [5, 14, -1],
    """Standing in front of you is the door to Titans bunker.\n""": [4, 14, -1],
    """You open the door and find that you are in a large room with nothing around \
you except for paths to the North, West, and South, to the East is where you came\
\nfrom.\n""": [3, 14, -1],
    """You are in a closet, there is nothing useful to you.\n""": [3, 13, -1],
    """There is a door in front of you, next to the door is a sign that reads "Weapon\
\ntesting lab".\n""": [3, 15, -1],
    """Around you are failed weapon designs, to the north and east are automatic \
doors,it should open by just approaching it.\n""": [3, 16, -1],
    """There are various computers and clipboards here filled with data, all of which\
\nare meaningless to you. There is an observation window in the room, not much\
can be seen at this distance.\n""": [4, 16, -1],
    """You are in a short hallway, to the east is an automatic door, to the north is \
another door which seems to be manual.\n""": [3, 17, -1],
    """You are in a white room, the table is littered with numerous weapon parts.\n""": [4, 17, -1],
    """You are in a room full of combat data for various weapons. These are not \
useful to you in any way.\n""": [3, 18, -1],
    """There is a door in front of you with a sign that reads \
"Laboratory".\n""": [2, 14, -1],
    """You are in the testing room of the lab, most of the layout seems familiar to\
\nyou. The computers flicker with data from various Titan experiments. There are\
\ntubes filled with various human limbs that range from heads to feet and\
\neverywhere in between. To the west is an observation room, to the north is a \
\nhallway.\n""": [1, 14, -1],
    """The computers are filled with nothing but static, there is an observation\
\nwindow. It is hard to make anything out from here.\n""": [0, 14, -1],
    """You are in a short hallway with doors leading to the west, east and \
north.\n""": [1, 15, -1],
    """Around you are failed experiments.\n""": [0, 15, -1],
    """The room you enter is full of scrap and remains of the past failures. There is\
\nnothing of use here.\n""": [2, 15, -1],
    """You are in a closet, this one is empty except for a chair placed in the middle\
\nof the room, it looks rather new.\n""": [1, 16, -1],
    """You find yourself in a dimly lit hallway with only the lights above you on, \
The only way to go is to the north, the doorway is closed \
behind you.\n""": [1, 17, -1],
    """You find yourself in a dimly lit hallway with only the lights above you on, \
you see a door to the north.\n""": [1, 18, -1],
    """You find yourself face to face with a metal door, you can sense that the \
end is near.\n""": [1, 19, -1],
    """You are in a large dark room, as you enter lights turn on in quick \
succession.\n""": [1, 20, -1],
    """You find yourself standing in the lobby of Titan Tower. You see a desk \
in-front of you, there is a robotic clerk standing behind the desk, it merely \
nods to\nyou noting your presence. To the East is a the \
lounging\narea and to the West is a hallway that leads North.\n """: [5, 10, 0],
    """You enter a room with a table covered with fancy silverware, there is no food \
oranyone here.\n """: [4, 9, 0],
    """Around you are various pieces of furniture, there appears to be nobody in the\
\ntower except for you and the clerk. To the North the lounge \
continues.\n """: [6, 9, 0],
    """You notice that the lounge has less furniture and that to the north is an\
\nemergency exit.\n """: [6, 10, 0],
    """In-front of you lies a bright red door labeled "Emergency Exit", you can exit\
\nTitan tower through the door and end your journey here or you can head back \
and finish what you started.\n """: [6, 11, 0],
    """The corridor turns to the north, you notice that there are no paintings of\
\nanyone other than Titan, there is nothing of note in this \
corridor.\n """: [4, 10, 0],
    """The corridor heads to the East, you notice an Elevator in the wall, on the\
\nwalls you see many paintings of Titan, You notice that one painting is torn, \
youwonder who the painting was of, but put it out of your mind.\n """: [4, 11, 0],
    """You can ascend to the top of the tower from here. You realize that this \
finally may be the end of your journey. You will finally be able to take out \
Titan and\nsave yourself.\n """: [5, 11, 0],
    """You are on the top floor of Titan tower, the elevator is locked in place and\
\nappears like it will require something to unlock it, without any way of\
\nunlocking it you can only go to the South.\n """: [5, 11, 1],
    """You walk out into the hallway.\n """: [5, 10, 1],
    """\nWith the destroyed husk of Titans bodyguard behind you, you enter the \
Office, \nonly to find it empty. The office appears like someone left in a hurry, \
there\nare papers scattered across the floor. You notice one of them has a \
diagram of\nyou on it, you dismiss it as irrelevant for you are now making \
something of yourself and don't want to be dragged down by the past. You notice \
an elevator\nbehind the desk, you go up to it and notice that it won’t \
open.\n """: [5, 9, 1],
    """As the Elevator descended you thought that the end will finally come, you\
\nrealized that there is no other way, you cannot negotiate with this mad man. \
He has to be taken out to insure you freedom. The elevator door opens and you \
see ahallway leading North.\n """: [5, 11, -1],
    """As you approach you notice a big metal door to the north, the elevator locked\
\nbehind you. It appears that the door is the entrance to a bunker, \
Titans bunker.\n """: [5, 12, -1],
    """You climb into a strange room, hearing heavy breathing, emnating from this \
\nfigure in the corner.\n\

                       .-.
                      |_:_|
                     /(_Y_)\\
                    ( \/M\/ )
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\\_
     ':        /_'  : |::"| :  '.\\
       ':     //   ./ |oUU| \.'  :\\
         ':  _:'..' \_|___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\\
            [::\ |  :  | |  :   ; : \\
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :  \\
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\\
          /___.-/_|-'   \  \\
                         '-'
\n You also happen to see a familiar spherical spacestation lit up in red\n\
    .          .
  .          .                  .          .              .
        +.           _____  .        .        + .                    .
    .        .   ,-~"     "~-.                                +
               ,^ ___         ^. +                  .    .       .
              / .^   ^.         \         .   
             Y  l  o  !          Y  .        .
     .       l_ `.___.'        _,[                    +
             |^~"-----------""~ ^|
   +       . !                   !     .           .
          .   \                 /          
               ^.             .^            .      "       +.
                 "-.._____.,-" .                    .
          +           .                .   +                       .
   +          .             +                                  .\n\
The man strikes you by manipulating the gravity and splits you in half\n""": [-2, 2, 0],
}

"""
Dictionary:     LOOKCOORDINATES
Definition:     This dictionary holds all of the secondary descriptions for the
                room which are used in game by typing look
Author:         Kiefer Chiaravalloti, Dale Guimond
History:
"""

LOOKCOORDINATES = {
    """Upon further investigation of the area, there is nothing of note. The \
stench of garbage from the south is overwhelming, the street light continues \
to flicker \nabove you.\n""": [0, 0, 0],
    """Most of the items here are utterly pointless, however you notice various \
robot \nparts scattered about the area appears to be a dumping site. It is odd \
to think that an alleyway would be suitable for dumping.\n""": [0, -1, 0],
    """Upon further inspection the dead end is apparently still just a dead end, \
\nnothing is of note.\n """: [-1, -1, 0],
    """The alleyway is in bad shape leaving clutter and garbage about. The sound \
of \nglass crunching under your metallic foot can be heard as you make your\
way \nthrough the alleyway.\n""": [-1, 0, 0],
    """It appears that there was a major crash. The paths to the west and north are\
blocked by debris.\n""": [-1, 1, 0],
    """The manhole looks as if it has been through use, perhaps something or \
someone isdown there.\n""": [-2, 0, 0],
    """The ladder is completely rusted, hopefully it will serve its purpose until \
you \nare done with it.\n""": [-2, 0, -1],
    """The bricks are a sickly green due to the lack of care and attention, \
vermin \nscatter about as you progress.\n""": [-3, 0, -1],
    """There is a faint shuffling sound followed by mumbling, everything else \
appears \nto be in order.\n""": [-3, 1, -1],
    """The man doesn't seem to pose any threat, it is best to just leave him be.\n""": [-2, 1, -1],
    """There is a soft humming sound comming from the east, this area is \
noticeably \ncleaner than the other sections of the sewer.\n""": [-3, 2, -1],
    """The drone deosn't even look in your direction, it is too busy cleaning \
this \nsection of the sewer.\n""": [-2, 2, -1],
    """The grate in front of you doesn't budge, the waste flows through the grate.\n""": [-3, 3, -1],
    """The alleyway is cleaner than most, there is no trash or clutter on the \
ground \nanywhere.\n""": [1, 0, 0],
    """The narrow path to the north is darker than the current location, the \
dumpster \nis filled to the brim with garbage. The surrounding buildings in \
the area look \nabandoned.\n""": [1, 1, 0],
    """The stairs lead to a dimly lit hallway, there is nothing around at the \
moment.\n""": [2, 1, 0],
    """After inspecting the hallway it is devoid of all decoration and has \
nothing in \nit.\n""": [3, 1, 0],
    """The hallway is well lit revealing nothing of use in the immediate area.\n""": [4, 1, 0],
    """The hallway seems to be more dimly lit than the last section.\n""": [4, 2, 0],
    """It's just a door, what do you expect to happen by staring at it?\n""": [3, 2, 0],
    """Most of the items here are old and defective and are of no use to you. \
All of \nthe supplies have been looted, who exactly stole the supplies \
reamins as a \nmystery.\n""": [2, 2, 0],
    """Are you stupid? It's a dead end, nothing is here, go back!\n""": [1, 2, 0],
    """You see a lot of rats scurrying around the alleyway, other than that \
there is nothing of note.\n""": [2, 0, 0],
    """This area's filth shows that the sewer is no longer manned by people.\n""": [3, 0, 0],
    """You notice that the walls are grimy and disgusting, and the wall feels \
slimy to the touch.\n""": [3, 0, -1],
    """The bricks in the wall are faded but the walls themselves are surprisingly \nclean.\n""": [3, 1, -1],
    """The bricks begin to resemble their original color, the vermin have also \
kept \ntheir distance from the area.\n""": [3, 2, -1],
    """The drone doesn't even look at you, he is too busy cleaning the sewer \
section.\n""": [3, 3, -1],
    """Upon further investigation you hear a faint whiring noise coming from \
behind thebrick wall. Upon putitng your hand to it you realize that it is a \
hologram used to hide a section of the sewer.\n""": [2, 3, -1],
    """The black market is bustling with scum and villains, they all appear to \
be \npurchasing some kind weapon and/or harmful item. \n""": [1, 3, -1],
    """There are yet more people around you and they appear to be staring at you. \
You \nbegin to feel mightly uncomfortable in this illegal market\n""": [1, 4, -1],
    """The graffiti is a four digit number. The numbers are spray painted in a variety \
of neon colors. Staring too long may lead to loss of vision. Who could of put \nthis here? \n""": [2, 4, -1],
    """None of the ruffians are in the area. It is quiet but you can still hear yellingbehind you.\n""": [1, 5, -1],
    """There are markings and divots scattered thorughout the wall, there is a \nnoticeable \
line separating the black market section to the tunnel system.\n""": [1, 6, -1],
    """You are wondering where the market went and why there is all this rubble and \nwhere it is from?\n """: [2, 6,-1],
    """You notice that the rubble appears to be from old buildings and your curiousity begins to peak.\n """: [3, 6,-1],
    """There is a slight whistling sound coming from the north, perhaps the black \nmarket has another \
section up ahead.\n """: [4, 6, -1],
    """There are markings on the floor indicating that something has been here before.\n""": [4, 7, -1],
    """The markings from before continue and you are dumbstruck as to what they \
could \npossibly mean.\n""": [5, 7, -1],
    """You notice that there appears to have been a letter of some sort on the \
door butit is now illegiable due to the rust.\n""": [5, 8, -1],
    """Aftering staring at the wall for hours you realize that nothing has \
changed, youshould just turn around.\n """: [5, 6, -1],
    """The street lights are fully operational, the houses doors and windows \
are \nboarded up and are unbreakable.\n""": [0, 1, 0],
    """You wonder if you are actually moving or if this really is just a really \
long \nroad. But in the distance you see more buildings.\n""": [0, 2, 0],
    """You notice people walking around and they begin to stare at you menacingly.\n""": [0, 3, 0],
    """The door cannot be opened by hand, something will be needed to open it, \
nothing else of note can be found.\n""": [0, 4, 0],
    """It appears the higher end weapons have been taken, whether or not they \
have beenmoved or stolen is beyond you.\n""": [1, 4, 0],
    """The room is extremely bright and it is almost blinding to your optical \
circuits,the room itself is unadorned and has nothing of real interest in it.\n""": [2, 4, 0],
    """The alley is poorly lit and you have trouble adjusting to the darkness \
evenwith your advanced optic circuitry.\n""": [0, 5, 0],
    """The vermin struggle for food and scraps, one in particular attempts to \
bite yourfoot. This is ineffective and it leaves.\n""": [0, 6, 0],
    """your optic sensors are freaking out due to this perpetual darkness and \
you \nyourself begin to get concerned as this darkness seems unnatural.\n""": [-1, 6, 0],
    """The lack of people in this street is slightly unnerving but it does not \
truely \nconcern you.\n""": [-3, 6, 0],
    """There are a few people wondering the street but it is mostly empty and \
they \nappear to not take any notice of your presence.\n""": [-2, 6, 0],
    """The entrance is loosely guarded, the lights of the factory light up the \
entire \narea.\n""": [-3, 7, 0],
    """The assembly lines carry various robotic parts used for military drones \
and \nasd's.\n""": [-3, 8, 0],
    """The assembly lines seem to continue throughout the entire factory, all \
of which is manned by automated workers.\n""": [-2, 8, 0],
    """The platform you stand on currently bears the mark of Titan Robotics.\n """: [-1, 8, 0],
    """The computer seems to control more than the factory, however you aren't \
sure \nwhat else it manipulates.\n""": [0, 8, 0],
    """The area is filled with robotic parts and tools, not much can be used at \
the \nmoment.\n""": [-3, 9, 0],
    """There is nothing of note in the area, it is just an alleyway.\n""": [1, 6, 0],
    """The alleyway twists and bends\n""": [2, 6, 0],
    """This alleyway is empty\n""": [3, 6, 0],
    """The alleyway is filled with garbage\n""": [4, 5, 0],
    """There is nothing of note\n""": [4, 6, 0],
    """There is no end in sight\n""": [4, 7, 0],
    """All the paths look the same\n""": [2, 5, 0],
    """You wonder why this maze was placed here, the area is covered in garbage\n""": [2, 7, 0],
    """This may not even be an alley but just a maze\n""": [3, 5, 0],
    """It is almost impossible to see anything\n""": [3, 7, 0],
    """It appears that the maze has ended, you are now on another street with \
buildingsas far as the eye can see.\n""": [5, 6, 0],
    """The guards are seamlessly patrolling the entrance to the tower, they may \
know \nyour coming.\n""": [5, 7, 0],
    """The security droids are have left this area, they must be out looking for you.\n""": [5, 8, 0],
    """The tower's height seems to last longer than your visibility range, it \
looks \ngenerally empty.\n""": [5, 9, 0],
    """There is nothing of note in the area currently\n""": [5, 13, -1],
    """The area is dark and dreary, not much else can be observed from here.\n""": [5, 14, -1],
    """It is a large metal door that bears titans insgnia engraved in it.\n""": [4, 14, -1],
    """You are surronded by a set of doors, most of which are locked.\n""": [3, 14, -1],
    """The stationary closet contains nothing\n""": [3, 13, -1],
    """The door is generally new, it slides open with even the slightest movement.\n""": [3, 15, -1],
    """The weapons are useless as most would likely blow up when put in use.\n""": [3, 16, -1],
    """The clipboards contian the progress and data for the weapons tested here. All ofwhich have failed miserably.\n""": [4, 16, -1],
    """Not much can be seen from here at the moment.\n""": [3, 17, -1],
    """None of the scrap on the table is useable to you.\n""": [4, 17, -1],
    """Upon further inspection there is what appears to be an upgrading station \
in the far corner of the room. If you would like you could possibly upgrade \
yourself.\n""": [3, 18, -1],
    """Looking closer at the door you find its architecture flawless and you wish you \ncould have one.\n""": [2, 14,-1],
    """You come to the realization that this is where you were tested upon when you \nwere first made. Some of the test data shows failed human-machines and it is \nclear to \
you that the limbs are recycled for future use.\n""": [1, 14, -1],
    """After staring at the computer static you realize that you should get moving.\n""": [0, 14, -1],
    """The hallway is a hallway, congrats for noticing. It is unadorned expect for a \nsingle picture of Titan on the wall.\n""": [1, 15, -1],
    """Most of these experients are clearly failed robots that are used for scrap for \nfuture robots, none of these are active as they all are ripped open.\n""": [0, 15, -1],
    """This appears to be another room for failed experimental robots.\n""": [2, 15, -1],
    """You look around the room and you hear a familiar whiring noise coming from \
the \nfar end of the room. It could be another hologram projector.\n""": [1, 16, -1],
    """The hologram to the south has shutdown, the hallway onwards seems to stretch forhours.\n""": [1, 17, -1],
    """The only lights on are the ones directectly above you, all other lights seem to shut off automatically when you leave a set range.\n""": [1, 18, -1],
    """Looking closer you see that the door has the name Titan on it in big letters. \nAfter trying to push it, you realize it is a pull door.\n""": [1, 19, -1],
    """You see a big mech suit in the background with President Titan housed in the cockpit. This is the final battle.\n""": [1, 20, -1],
    """The desk clerk is unresponsive to your requests to speak with the President. Thescenery is very soothing.\n """: [5, 10, 0],
    """There is glass case to one of the sides of the room.\n """: [4, 9, 0],
    """The area is up to maintenence, nothing else is of use to you at this moment.\n """: [6, 9, 0],
    """The furniture is thining out as you approach a door marked emergency exit.\n """: [6, 10, 0],
    """The door is a bright red and is a push door, not the hated pull doors.\n """: [6, 11, 0],
    """It seems Titan is a tad bit self centered as there are only pictures of himself.\n """: [4, 10, 0],
    """It is unknown how exactly was in the picture as it is broken beyond repair.\n """: [4, 11, 0],
    """You are selfish to only want to save yourself and not anyone else. But it is \nyour immediate goal to save yourself other can come later.\n """: [5, 11, 0],
    """The elevator will not move unless you want it to fall uncontrollably.\n """: [5, 11, 1],
    """The wall is painted a sickly red, you realize that it is human blood that paints the wall.\n """: [5, 10, 1],
    """The elevator will not budge, nor will it open.\n """: [5, 9, 1],
    """The hallway has no orinetation at all and is dimly lit, there is nothing of any important to you here. \n """: [5, 11, -1],
    """The elevator door cannot be opened, the door to the bunker is large and metal.\n """: [5, 12, -1]
}

"""
+Dictionary:   DIRECTIONS
Definition:    This holds all the valid locations for each grid point
Author:        Kiefer Chiaravalloti
Date:          10/29/2014
History:       10/30/2014 The alley maze has no directionals and all coordinates
               have a direction, 2/23/2015 Several fixes to the west directions
               have been fixed, there are no doubles at this point
"""

DIRECTIONS = {
    """North - East - West - South          \n""": [0, 0, 0],
    """Descend""": [-2, 2, -1],
    """North\n""": [-1, -1, 0],
    """North - South - West - East\n""": [-1, 0, 0],
    """South - East\n""": [-1, 1, 0],
    """East - Down\n""": [-2, 0, 0],
    """West - Up\n""": [-2, 0, -1],
    """North - East\n""": [-3, 0, -1],
    """North - East - South\n""": [-3, 1, -1],
    """West\n""": [-2, 1, -1],
    """North - East - South\n """: [-3, 2, -1],
    """West\n  """: [-2, 2, -1],
    """South\n""": [-3, 3, -1],
    """West - East - North\n""": [1, 0, 0],
    """North - West - South\n""": [1, 1, 0],
    """West - East\n""": [2, 1, 0],
    """West - East\n """: [3, 1, 0],
    """West - North\n""": [4, 1, 0],
    """West - South\n""": [4, 2, 0],
    """West - East\n  """: [3, 2, 0],
    """East\n""": [2, 2, 0],
    """South\n """: [1, 2, 0],
    """West - East\n   """: [2, 0, 0],
    """West - Down\n""": [3, 0, 0],
    """North - Up\n""": [3, 0, -1],
    """North - South\n""": [3, 1, -1],
    """North - South\n """: [3, 2, -1],
    """West - South\n """: [3, 3, -1],
    """East\n """: [2, 3, -1],
    """North - East\n """: [1, 3, -1],
    """East - North - South\n""": [1, 4, -1],
    """West\n   """: [2, 4, -1],
    """North - South\n   """: [1, 5, -1],
    """East - South\n""": [1, 6, -1],
    """East - West\n """: [2, 6, -1],
    """East - West\n  """: [3, 6, -1],
    """North - East - West\n """: [4, 6, -1],
    """South - east\n """: [4, 7, -1],
    """West - North\n """: [5, 7, -1],
    """South - North\n""": [5, 8, -1],
    """""": [5, 9, -1],
    """West\n """: [5, 6, -1],
    """North - South - West - East\n """: [0, 1, 0],
    """North - South\n     """: [0, 2, 0],
    """North - South\n    """: [0, 3, 0],
    """South - North - East Door\n""": [0, 4, 0],
    """West\n    """: [1, 4, 0],
    """East - West\n    """: [2, 4, 0],
    """North - South\n      """: [0, 5, 0],
    """West - East\n    """: [0, 6, 0],
    """You can't see anything but back east\n""": [-1, 6, 0],
    """North - East\n  """: [-3, 6, 0],
    """West - East - North - South\n""": [-2, 6, 0],
    """North - South\n       """: [-3, 7, 0],
    """East - North - South\n """: [-3, 8, 0],
    """East - West\n     """: [-2, 8, 0],
    """East - West\n      """: [-1, 8, 0],
    """West\n     """: [0, 8, 0],
    """South\n  """: [-3, 9, 0],
    """West - East\n      """: [1, 6, 0],
    """There are no directions available\n """: [2, 6, 0],
    """There are no directions available\n     """: [3, 6, 0],
    """There are no directions available\n      """: [4, 5, 0],
    """There are no directions available\n       """: [4, 6, 0],
    """There are no directions available\n        """: [4, 7, 0],
    """There are no directions available\n""": [2, 5, 0],
    """There are no directions available\n  """: [2, 7, 0],
    """There are no directions available\n   """: [3, 5, 0],
    """There are no directions available\n    """: [3, 7, 0],
    """West - North\n   """: [5, 6, 0],
    """North - South\n        """: [5, 7, 0],
    """North - South\n         """: [5, 8, 0],
    """North - South\n          """: [5, 9, 0],
    """North - South\n           """: [5, 13, -1],
    """West - South\n  """: [5, 14, -1],
    """West - East\n       """: [4, 14, -1],
    """North - South - East - West\n""": [3, 14, -1],
    """North\n   """: [3, 13, -1],
    """North - South\n            """: [3, 15, -1],
    """North - South - East\n """: [3, 16, -1],
    """West\n      """: [4, 16, -1],
    """North - South - East\n  """: [3, 17, -1],
    """West\n       """: [4, 17, -1],
    """South\n    """: [3, 18, -1],
    """West - East\n        """: [2, 14, -1],
    """West - East - North\n """: [1, 14, -1],
    """East\n  """: [0, 14, -1],
    """North - South - West - East\n  """: [1, 15, -1],
    """East\n   """: [0, 15, -1],
    """West\n        """: [2, 15, -1],
    """North - South\n             """: [1, 16, -1],
    """North - South\n              """: [1, 17, -1],
    """North - South\n               """: [1, 18, -1],
    """North - South\n                """: [1, 19, -1],
    """No Direction\n""": [1, 20, -1],
    """South - East - West\n """: [5, 10, 0],
    """North\n """: [4, 9, 0],
    """North\n  """: [6, 9, 0],
    """West - North - South\n """: [6, 10, 0],
    """Open Emergency exit - South\n """: [6, 11, 0],
    """North - South - East\n   """: [4, 10, 0],
    """South - East\n """: [4, 11, 0],
    """Up - West\n """: [5, 11, 0],
    """Down - South\n """: [5, 11, 1],
    """North - South\n  """: [5, 10, 1],
    """North\n    """: [5, 9, 1],
    """North\n     """: [5, 11, -1],
    """North\n      """: [5, 12, -1],
    """North\n                     """: [0, -1, 0]}

"""
Dictionary:    COMMANDS
Definition:    This dictionary stores the executable commands that the user will
               be using
Author:        Matthew Vavruska
Date:          9/30/2014
History:       
"""

COMMANDS = {"north": "location2 = north(",
            "n": "location2 = north(",
            "go north": "location2 = north(",
            "walk north": "location2 = north(",
            "move north": "location2 = north(",
            "south": "location2 = south(",
            "s": "location2 = south(",
            "go south": "location2 = south(",
            "walk south": "location2 = south(",
            "move south": "location2 = south(",
            "west": "location2 = west(",
            "w": "location2 = west(",
            "go west": "location2 = west(",
            "walk west": "location2 = west(",
            "move west": "location2 = west(",
            "east": "location2 = east(",
            "e": "location2 = east(",
            "go east": "location2 = east(",
            "walk east": "location2 = east(",
            "move east": "location2 = east(",
            "ascend": "location2 = ascend(",
            "a": "location2 = ascend(",
            "go up": "location2 = ascend(",
            "up": "location2 = ascend(",
            "u": "location2 = ascend(",
            "climb up": "location2 = ascend(",
            "descend": "location2 = descend(",
            "d": "location2 = descend(",
            "go down": "location2 = descend(",
            "down": "location2 = descend(",
            "climb down": "location2 = descend(",
            "help": "sos(",
            "weast": "invalid(",
            "kill self": "suicide()",
            "take": "take(",
            "drop": "drop(",
            "fight": "combat(",
            "engage combat": "combat(",
            "open": "location2 = opens(",
            "save": "save(",
            "load": "load(",
            "attack": "combat(",
            "look": "look(",
            "search": "look(",
            "examine": "look(",
            "upgrade": "upgrade("}

MOVEMENT = {"north", "n", "go north", "walk north", "move north", "south", "s", "go south",
            "walk south", "move south", "west", "w", "go west", "walk west", "move west", "east",
            "e", "go east", "walk east", "move east", "ascend", "a", "go up", "up", "u", "climb up",
            "descend", "d", "go down", "down", "climb down"}

"""
Dictionary:    WEAPONS
Definition:    The dictionary contains a one or zero for whether or not the user has \
               the weapon, a specific integer indicates the weapons accuracy, and the \
               coordinates represents where the weapon is located on the map
Author:        Dale Guimond
Date:          9/30/2014
History:
"""

WEAPONS = {"lasershotgun": [0, 3, [1, 4, 0], "The room happens to contain a laser shotgun"],
           "laserpistol": [0, 4, [1, 4, 0], "The room happens to contain a laser pistol"],
           "laserrifle": [0, 3, [1, 4, 0], "The room happens to contain a laser rifle"],
           "shockblast": [0, 1, [1, 4, 0], "The room happens to contain a shockblast"],
           "megaparticlecannon": [0, .5, [2, 4, 0], "The room happens to contain a mega particle cannon"],
           "flamethrower": [0, .75, [4, 9, 0], "There is a flamethrower on the wall"],
           "empgrenade": [0, 2, [1, 4, 0], "The room happens to contain an empgrenade"],
           "rocketartillery": [0, 2, [2, 2, 0], "The room happens to contain a rocket artillery"],
           "raygun": [0, 2, [4, -17, -1], "The room happens to contain a ray gun"],
           "crowbar": [0, 1, [-3, 3, -1], "The room happens to contain a crowbar"],
           "keycard": [0, 1, [5, 9, 1], "There is a keycard on the floor"],
           "disruptor": [0, 5, [0, -1, 0], "The room happens to contain a disruptor"]}

"""
Dictionary:      MELEEATTACKS
Definition:      The dictionary contains the chance of qa hit for each attack
Author:          Matthew Vavruska
History:         2/6/2015 punch has a much greater chance of success for development purposes, 3/30/2015 punch decreased to a reasonable amount
"""

MELEEATTACKS = {"kick": 4, "punch": 3.5} 

"""
Dictionary:    CHARACTERS
Definition:    This dictionary contains all of the characters, the first digit in the \
               list represents whether or not the character is dead or alive, the second \
               digit determines how hard it is to hit them. The third digit indicates how \
               many times you hit them until they hit back, the final digit indicates their location. \
               For self, the second digit indicates whether the player has beaten titan \
               towe, the third indicates whether the player has fled the battle, the final \
               digit indicates whether the player has beaten the game.
Author:        Dale Guimond
Date:          9/30/2014
History:
"""

CHARACTERS = {"self": [1, 0, 0, 0, [0, 0], 0], "euwolf": [1, 10, 7, [2, 2, 0], "In the distance charging towards \
you is a Titan robot you’ve never seen before. It is a four legged unit that is wolf like \
in structure with 2 Laser Mini Guns\non its hind legs and a chainsaw tail.\n", "x", 40],
              "mu01": [1, 1, 5, [1, 2, 0], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n", "x", 20],
              "mu02": [1, 1, 5, [2, 7, 0], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n ", "x", 20],
              "mu03": [1, 1, 5, [4, 7, 0], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n  ", "x", 20],
              "mu04": [1, 1, 5, [4, 5, 0], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n   ", "x", 20],
              "mu05": [1, 1, 5, [-1, -1, 0], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n    ", "x", 20],
              "mu06": [1, 1, 5, [3, 1, -1], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n     ", "x", 20],
              "mu07": [1, 1, 5, [-2, 1, -1], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n      ", "x", 20],
              "mu08": [1, 1, 5, [5, 6, -1], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n       ", "x", 20],
              "mu09": [1, 1, 5, [5, 14, -1], "You see what appears to be standard \
Titan Military drone. It is holding an EMP \ngun and has some EMP grenades on its hip, on \
the other hip you see a standard \nmachine gun. It was clearly sweeping the area searching for \
you and you walked \nright into its path. You can either fight or flee.\n        ", "x", 20],
              "euspider": [1, 3, 5, [-1, 6, 0], "You hear multiple clanking feet ahead of you. \
Then suddenly you get stuck in \nsome sticky webbing and with some struggling you break free.\
Suddenly you see a \ngiant angry looking spider robot.\n", "x", 50],
              "euflight": [1, 6, 5, [2, 5, 0], "You hear a faint whooshing above \
you, you look up and see a robot that has large metallic wings. It is circling above you \
and is looking directly at you. It tosses an EMP grenade someways infront of you. It is \
obviously a threat to you and you realize that you must run for now, at least until you \
get the proper weapon.\n", "x", 50],
              "eugiant2": [1, 4, 4, [5, 8, 0],
                           "The other figure is exactly the same only it appears it cannot speak.\n", "auto", 60],
              "eugiant1": [1, 4, 4, [5, 8, 0], "One of the tall figures is patrolling around the tower.\
It appears to be 7 feet \ntall and possesses a single electro cannon on it's shoulder and has a wrist \
\nmounted flamethrower. This one in particular looks at you in disgust and says \n'Prepare to die'\n", "auto", 60],
              "asd": [1, 7, 10, [-3, 7, 0], "You see an unusual shadow that does not \
appear to have a source, it is \napproaching and you hear a faint clanking sound. You also \
notice a faint \nshimmering in the air. Suddenly in-front of you is an advanced looking \
robot whoknocks you down with one hit, you get up slowly and realize that this drone \
has cloaking technology, however it appears to be malfunctioning right now, the \ntarget \
is clearly visible right now. You can either flee or fight it.\n", "x", 50],
              "bgo": [1, 6, 8, [-1, 8, 0], "You look up to see a group of Samurai looking robots. \
They are dropping down \nupon you from the air. They are extensively armed, one carrying \
metal bow with \nexplosive tipped arrows, one with nun-chucks, one with a katana, and one \
\ncarrying explosive throwing stars. They land in-front of you and look at you and say \
“You are in a restricted area, please leave or we will no choice but to \nkill you.” You \
can either press on and fight them or turn back and leave.\n", "x", 70],
              "bgz": [1, 6, 12, [0, 15, -1], "Emerging from various robotic parts is a group of 3 \
barbaric looking prototypes.They shout with anger and point their various weapons at you, \
which include, a \nsword and shield, 2 axes, and a warhammer. The apparent leader says ""You \
are not welcomed here, this is our territory and you must leave or we will rip you apart\
piece by piece.""  After he says that you realize that they believe that they are actually \
barbarians. You have a choice to leave or fight them in hopes of \ngaining some knowledge as \
to what Titan has done.\n", "x", 70],
              "hm": [1, 4, 3, [3, 13, -1], "As you look around the room you see what \
appears to be a mixture of human and \nmachine. He is looking directly at you with eyes that \
are blazing red with \nrage. He laughs maniacally and points at you with prefectly crafted \
curved swordarm. 'You! I was sent here to rip you to shreds! Titan said that if I took \
\nyou out, he would free me! I plan to do just that, I will enjoy this!' he beginsto \
charge at you waving his sword arm wildly. You still have a chance to flee \nbut fighting \
him may be for the best, for he is threat to all of mankind.\n", "auto", 80],
              "titanguard": [1, 5, 4, [5, 10, 1], "As you aproach the entrance to Titan's office\
 you notice a giant metal beast \ninfused with a creature of unknown origin. It snarls at \
you and approaches \nslowly. The only way past is to destroy the beast.\n", "auto", 90],
              "titanms": [1, 20, 30, [1, 20, -1], "The lights reveal Titan housed in a large, \
menacing mech suit. It is heavily armed with rocket launchers, particle cannons, flame \
throwers, Laser Mini Guns, Plasma cannon,and close range weaponry. The room is largely \
empty except for a few large containers. The exit is sealed by blast doors. Titan looks \
at you and says ""So you have made it this far? Well its too bad that it is all for naught\
, this is where you die. Your head will make an excellent trophy"".\n", "auto", 1000]}

"""
Constant List:    TERMINALS
Definition:       This list contains the coordinates for where the terminal is
                  located and where it will bring you
Author:           Kiefer Chiaravalloti
Date:             2/5/2015
History:
"""
TERMINALS = [[2, 2, 0], [3, 18, -1]]

"""
Lists:           VALIDNORTH, VALIDSOUTH, VALIDEAST, VALIDWEST, VALIDASCEND,
                 VALIDDESCEND, VALIDOPEN, VALIDSHOOT
Definition:      These lists hold the valid action associated with the name for
                 example, VALIDNORTH holds all of the coordinates in which the
                 player can move north on the grid. If the player attempts to
                 move north or take something that is not defined in the lists
                 the player cannot move north or take the item.
Author:          Kiefer Chiaravalloti
Date:            9/30/2014
History:
"""

VALIDNORTH = [[-1, 0, 0], [-1, -1, 0], [1, 1, 0], [0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0], [4, 1, 0],
              [0, 3, 0], [0, 4, 0], [0, 5, 0], [-3, 7, 0], [-3, 8, 0], [2, 6, 0], [3, 6, 0], [4, 6, 0],
              [4, 9, 0], [5, 8, 0], [5, 7, 0], [5, 9, 0], [6, 10, 0], [-3, 6, 0], [2, 5, 0], [3, 5, 0],
              [4, 5, 0], [4, 10, 0], [6, 9, 0], [-3, 0, -1], [-3, 1, -1], [-3, 2, -1], [3, 0, -1],
              [3, 1, -1], [3, 2, -1], [1, 3, -1], [1, 4, -1], [1, 5, -1], [4, 6, -1], [5, 7, -1],
              [5, 8, -1], [6, 11, -1], [5, 12, -1], [5, 13, -1], [3, 13, -1], [3, 14, -1],
              [3, 15, -1], [3, 16, -1], [3, 17, -1], [1, 14, -1], [1, 15, -1], [1, 16, -1],
              [5, 9, 1], [5, 10, 1], [1, 17, -1], [1, 18, -1], [1, 19, -1], [5, 6, 0], [5, 11, -1], [0, -1, 0]]

VALIDSOUTH = [[0, 1, 0], [-1, 0, 0], [-1, 1, 0], [1, 1, 0], [1, 2, 0], [4, 2, 0], [0, 2, 0], [0, 3, 0],
              [0, 4, 0], [0, 5, 0], [0, 6, 0], [-3, 7, 0], [-3, 8, 0], [-3, 9, 0], [2, 7, 0], [2, 6, 0],
              [3, 7, 0], [3, 6, 0], [4, 7, 0], [4, 6, 0], [5, 7, 0], [5, 8, 0], [5, 9, 0], [5, 10, 0],
              [4, 10, 0], [4, 11, 0], [6, 10, 0], [6, 11, 0], [-3, 1, -1], [-3, 2, -1], [-3, 3, -1],
              [3, 1, -1], [3, 2, -1], [3, 3, -1], [1, 4, -1], [1, 5, -1], [1, 6, -1], [4, 7, -1],
              [5, 8, -1], [5, 11, 1], [5, 12, -1], [5, 13, -1], [5, 14, -1], [3, 14, -1], [3, 15, -1],
              [3, 16, -1], [3, 17, -1], [3, 18, -1], [1, 15, -1], [1, 16, -1], [1, 17, -1],
              [1, 18, -1], [1, 19, -1], [1, 20, -1], [5, 10, 1], [0, 0, 0]]

VALIDEAST = [[-2, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [3, 2, 0], [0, 6, 0],
             [-1, 6, 0], [-2, 6, 0], [-2, 8, 0], [-1, 8, 0], [1, 6, 0], [2, 6, 0], [5, 10, 0],
             [2, 3, -1], [2, 6, -1], [3, 6, -1], [4, 6, -1], [4, 14, -1], [3, 14, -1],
             [2, 14, -1], [1, 14, -1], [1, 15, -1], [-1, 1, 0], [2, 2, 0], [3, 5, 0], [-3, 6, 0],
             [-3, 8, 0], [4, 10, 0], [4, 11, 0], [-3, 0, -1], [-3, 1, -1], [-3, 2, -1], [1, 3, -1],
             [1, 4, -1], [1, 6, -1], [4, 7, -1], [4, 9, -1], [3, 16, -1], [3, 17, -1],
             [0, 15, -1], [0, 14, -1], [4, 6, 0], [0, 0, 0], [-1, 0, 0], [1, 0, 0], [2, 0, 0]]

VALIDWEST = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [1, 4, 0], [0, 6, 0],
             [-1, 6, 0], [-2, 6, 0], [-2, 8, 0], [-1, 8, 0], [1, 6, 0], [2, 6, 0], [5, 10, 0],
             [5, 11, 0], [2, 3, -1], [2, 6, -1], [3, 6, -1], [4, 6, -1], [4, 14, -1], [3, 14, -1],
             [2, 14, -1], [1, 14, -1], [1, 15, -1], [2, 0, 0], [3, 0, 0], [4, 1, 0], [4, 2, 0],
             [2, 4, 0], [0, 8, 0], [4, 5, 0], [5, 6, 0], [6, 10, 0], [3, 3, -1], [2, 4, -1],
             [5, 6, -1], [5, 7, -1], [5, 14, -1], [2, 15, -1], [4, 16, -1], [4, 17, -1], [3, 6, 0],
             [-2, 0, -1], [-2, 1, -1], [-2, 2, -1], [0, 0, 0]]

VALIDASCEND = [[-2, 0, -1], [3, 0, -1], [5, 11, 0], [-2, 2, -1]]

VALIDDESCEND = [[-2, 0, 0], [3, 0, 0], [5, 11, 1]]

VALIDOPEN = [[3, 0, 0], [1, 1, 0], [2, 3, -1], [1, 4, 0], [-3, 7, 0], [4, 14, -1], [3, 13, -1],
             [3, 15, -1], [4, 17, -1], [3, 18, -1], [1, 16, -1], [1, 19, -1], [5, 9, 0], [3, 2, 0],
             [0, 4, 0]]

VALIDSHOOT = [[2, 2, 0], [1, 2, 0], [2, 7, 0], [4, 7, 0], [4, 5, 0], [-1, -1, 0], [3, 1, -1], [-2, 1, -1],
              [5, 6, -1], [5, 14, -1], [-1, 6, 0], [2, 5, 0], [-3, 7, 0], [5, 8, 0], [-1, 8, 0], [0, 15, -1],
              [3, 13, -1], [1, 20, -1], [5, 10, 1]]

"""
Function:     look
Definition:   This checks the players current location and prints another description from the lookcoords
Author:       Kiefer Chiaravalloti
Date:         2/5/2015
History:
"""


def look(lookcoords, location, weapons):
    item = weapons.keys()
    weapon = weapons.values()
    desc = lookcoords.keys()
    locs = lookcoords.values()
    if location in locs:
        index = locs.index(location)
        print desc[index]
    for x in range(len(weapons)):  #check for weapons
        if weapons[item[x]][0] == 0:
            if location == weapon[x][2]:
                print weapons[item[x]][3]
            else:
                pass
        else:
            pass


"""
Function:      save
Definition:    This function creates a notepad file in the folder called saves
               using the players desired username. The file is then edited by
               adding the players current progress then the file is closed.
Author:        Matthew Vavruska
Date:          2/5/2015
History:
"""


def save(username, x, y, z, w, inventory1='', inventory2="", inventory3=""):
    file = open("Saves/" + username + ".txt", "w")
    file.write(str(w) + "\n" + str(x) + "\n" + str(y) + "\n" + str(z) + "\n" + inventory1 + " " + inventory2 + " " + inventory3 + "")
    file.close()
    print "saved"

"""
Function:     load
Definition:   This searches for the desired file name in the saves folder, once
              the file is found it reads the text on the notepad file and exports
              the data into python which sahll then drop the player at their save point
Author:       Matthew Vavruska
Date:         2/5/2015
History:      2/26/2015  Loading is not case sensitive
"""

def load(username, travelled, weapons, location, characters, inventory=''):
    if os.path.isfile("Saves/" + username + ".txt") == True:
        condition = os.stat("Saves/" + username + ".txt").st_size == 0
        if condition == False:
            file = open("Saves/" + username + ".txt", "r")
            file1 = file.read()
            file2 = file1.splitlines()
            var1 = ast.literal_eval(file2[0])
            var2 = ast.literal_eval(file2[1])
            var3 = ast.literal_eval(file2[2])
            var4 = ast.literal_eval(file2[3])
            var5 = file2[4]
            file.close()
            print "loading"
        else:
            print "File Empty"
            var1 = travelled
            var2 = weapons
            var3 = location
            var4 = characters
            var5 = inventory
    else:
        print "Save not found"
        var1 = travelled
        var2 = weapons
        var3 = location
        var4 = characters
        var5 = inventory
    return var1, var2, var3, var4, var5


"""
Function:       scan
Definition:     This checks if a character or item is in the players current
                location using the dictionaries for location and characters
Author:         Kiefer Chiaravalloti, Dale Guimond
Date:           9/30/2014
History:        Moving the if statements to their correct locations makes the
                function check if the item is in the players possesion as well
                as its location
"""


def scan(characters, weapons, location, terminals):
    t = 0
    try:
        item = weapons.keys()
    except AttributeError:
        try:
            weapons = str(weapons)
            weapons = re.sub(r"\(", '', weapons)
            weapons = re.sub(r", ''\)", '', weapons)
            weapons = ast.literal_eval(weapons)
            item = weapons.keys()
        except SyntaxError:
            weapons = str(weapons).split("}", 1)[0]
            weapons += "}"
            weapons = ast.literal_eval(weapons)
            item = weapons.keys()
    except SyntaxError:
        weapons = str(weapons).split("}", 1)[0]
        weapons += "}"
        weapons = ast.literal_eval(weapons)
        item = weapons.keys()
    weapon = weapons.values()
    chars = characters.keys()
    chardetails = characters.values()

    for x in range(len(weapons)):  #check for weapons
        if weapons[item[x]][0] == 0:
            if location == weapon[x][2]:
                t += 1
            else:
                pass
        else:
            pass
    if t > 0:
        print "There is something metallic close by"
    t = 0
    for y in range(len(characters)):  #check for characters
        if characters[chars[y]][0] == 1:
            if location == chardetails[y][3]:
                print characters[chars[y]][4]
            else:
                pass
        else:
            pass
    for m in range(len(terminals)):
        if location == terminals[m]:
            print "There is an upgrade terminal in the room"


"""
Function:       opens
Definition:     The opens function opens the door at the specified coordinate, if the player has the crowbar in their inventory then the door to
                the gunstore can be opened, if the player knows the code 4351 then the cellar door can be opened.
Author:         Matthew Vavruska
Date:           9/30/2014
History:        12/8/2014 - The door no longer has a set number but a randomized number between 1000 and 9999
"""


def opens(validopen, location, weapons, codex):
    if location == [0, 4, 0]:
        if weapons["crowbar"][0] == 1:
            location = [1, 4, 0]
        else:
            print "You need the crowbar to open the door."

    elif location == [1, 4, 0]:
        code = raw_input("Enter the passcode:  ")
        print code
        if code == codex or code == str(codex):  #random integer generated in CODE
            location = [2, 4, 0]
        else:
            print "Code Incorrect..."
    elif location == [3, 2, 0]:
        print "The door opens easily"
        location = [2, 2, 0]
    return location

"""
Function:       weaponparser
Definition:     Removes special characters from weapon lists
Author:         Kiefer Chiaravalloti
Date:           8/16/2014
History:
"""

def weaponparser(weapon):
    weaponlist = weapon.split()
    try:
        w1 = weaponlist[0]
    except:
        w1 = ""
    #test user2
    try:
        w2 = weaponlist[1]
    except:
        w2 = ""

    #test user3
    try:
        w3 = weaponlist[2]
    except:
        w3 = ""
    retweapon = w1 + w2 + w3
    retweapon = retweapon.lower()
    return retweapon

"""
Function:   Upgrade
Definition: This takes the accuracy and agility stat and allows the player to
            increase the efficiency of each. This is done by using experience
            points, if the player has the required amiount then they may uprgade
            a stat, if no then they are ejected.
Author:     Matthew Vavruska
Date:       3/10/2015
History:    3/11/2015 Insuffecient xp now exits from terminal
"""

def upgrade(characters):
    done = False
    accuracy = 100
    agility = 120
    while not done:
        if characters['self'][5] > 0:
            upgrd = raw_input("You have some experience points to spend. Would you like to spend them?:        ")
            if upgrd == "yes" or upgrd == "y":
                print "You may upgrade your accuracy or agility stat...\n"
                upgrde = raw_input("Which one would you like to upgrade? :     ")
                if upgrde == "accuracy":
                    if characters['self'][5] >= accuracy:
                        characters['self'][4][0] += 1
                        print characters['self'][5]
                        characters['self'][5] = characters['self'][5] - accuracy
                        print characters['self'][5]
                        print "You have upgraded your accuracy stat\n"
                    else:
                        print "You are lacking " + str(accuracy - characters['self'][5]) + " experience points!"
                        print "Come back when you get some money buddy!\n"
                        done = True
                        
                elif upgrde == "agility":
                    if characters['self'][5] >= agility:
                        characters['self'][4][1] += 1
                        characters['self'][5] = characters['self'][5] - agility
                        print "You have upgraded your agility stat"
                    else:
                        print "You are lacking " + str(accuracy - characters['self'][5]) + " experience points!"
                        print "Come back when you get some money buddy!\n"
                        done = True
                else:
                    print "That stat does not exist"
            else:
                print "Come back again"
                done = True
        else:
            print "Ha. Ha. Ha. Too inexperienced for an upgrade"
            done = True


"""
Function:      combat  
Definition:    The shoot function prompts the user to input what they would
               like to shoot with, if what the user input is in their inventory
               then the user shall be asked who they would like to shoot, the
               scan function will check if the character is in the current
               location or even if it exists then will proceed to attackchance
               which will compare the accuracy of the weapons and the hit
               chance of the character.         
Author:        Kiefer Chiaravalloti
Date:          9/30/2014
History:       1/7/2015 The empty print statement has been placed to solve a
               flaw in python
"""


def combat(characters, weapons, location, charactersx, meleeattacks, inventory="", inventory2="", inventory3=""):
    characters1 = characters
    chars = characters1.keys()
    inve = inventory + " " + inventory2 + " " + inventory3
    accuracy = characters1['self'][4][0]
    agility = characters1['self'][4][1]
    trial = 0
    victory = True
    char = []
    chardetails = characters1.values()
    for y in range(len(characters1)):
        characters1[chars[y]][2] = charactersx[chars[y]][2]
        victory = True
        if location == chardetails[y][3]:
            char.append(chars[y])
            if "crowbar" in inve:
                inve = inve.replace("crowbar", "k")
            if "keycard" in inve:
                inve = inve.replace("keycard", "k")
            if inve == "k" or inve == "k k" or inve == "k k k":
                print "Seeing as you posess no weaponry, you are forced in to close quarter combat \n(kick or punch)..."
                while characters1[chars[y]][0] == 1 and victory == True:
                    choose = raw_input("What would you like to do:   ")
                    if choose == "punch" or choose == "kick":
                        chance = attackchance(characters1[chars[y]][1], meleeattacks[choose])
                        randomint = random.randint(0, chance - accuracy)
                        if chance == randomint:
                            characters1[chars[y]][0] = 0
                            print "Congrats! You have claimed victory over the enemy."
                            xp = characters1[chars[y]][6]
                            print "You have gained " + str(xp) + " experience points!"
                            characters1['self'][5] += xp
                            print characters1['self'][5]
                        else:
                            characters1[chars[y]][2] = characters1[chars[y]][2] - 1
                            print "Your attack missed. You have " + str(characters1[chars[y]][2]) + " chances left"
                            if characters1[chars[y]][2] + agility == 0:
                                print "You have died1 4"  #Number added for testing purposes
                                victory = False
                                notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                                if notfinished == "yes" or notfinished == "y":
                                    done = False
                                    main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                         VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                         WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES, TERMINALS)
                                else:
                                    print "Play again soon :)"
                                    sys.exit()

                    else:
                        print "You can't do that"
                        trial += 1
                        if trial == 4:
                            print "You have died 3"    #Number added for testing purposes
                            victory = False
                            notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                            if notfinished == "yes" or notfinished == "y":
                                done = False
                                main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                     VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                     WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES, TERMINALS)
                            else:
                                print "Play again soon"   
                                done = True
                                sys.exit()
            else:
                while characters1[chars[y]][0] == 1 and victory == True:
                    choose = raw_input("What would you like to attack with?   ")
                    choose = weaponparser(choose)
                    if choose in weapons.keys():
                        if choose != "crowbar" and choose != "keycard":
                            if weapons[choose][0] == 1:
                                chance = attackchance(characters1[chars[y]][1], weapons[choose][1])
                                randomint = random.randint(0, chance)
                                if chance == randomint:
                                    characters1[chars[y]][0] = 0
                                    print "Congrats! You have claimed victory over the enemy."
                                    xp = characters1[chars[y]][6]
                                    print "You have gained " + str(xp) + " experience points!"
                                    xperience = characters1['self'][5]
                                    xperience += xp
                                    characters1['self'][5] = xperience
                                    print "You have " + str(characters1['self'][5]) + " XP"
                                else:
                                    characters1[chars[y]][2] = characters1[chars[y]][2] - 1
                                    print "Your attack missed. You have " + str(
                                        characters1[chars[y]][2]) + " chances left"
                                    if characters1[chars[y]][2] == 0:
                                        print "You have died"
                                        victory = False
                                        notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                                        if notfinished == "yes" or notfinished == "y":
                                            done = False
                                            main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH,
                                                 VALIDSOUTH,
                                                 VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE,
                                                 DIRECTIONS,
                                                 WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES,
                                                 TERMINALS)
                                        else:
                                            print "Play again soon :)"
                                            sys.exit()

                            else:
                                print "You don't have that"
                                trial += 1
                                if trial == 4:
                                    print "You have died 2"    #Number added for testing
                                    victory = False
                                    notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                                    if notfinished == "yes" or notfinished == "y":
                                        done = False
                                        main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                             VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                             WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES,
                                             TERMINALS)
                                    else:
                                        print "Play again soon :)"
                                        done = True
                                        sys.exit()
                        else:
                            print "You think you can kill something with a " + choose
                    elif choose == "punch" or choose == "kick":
                        chance = attackchance(characters1[chars[y]][1], meleeattacks[choose])
                        randomint = random.randint(0, chance - accuracy)
                        if chance == randomint:
                            characters1[chars[y]][0] = 0
                            print "Congrats! You have claimed victory over the enemy."
                            xp = characters1[chars[y]][6]
                            print "You have gained " + str(xp) + " experience points!"
                            characters1['self'][5] += xp
                            print characters1['self'][5]
                        else:
                            characters1[chars[y]][2] = characters1[chars[y]][2] - 1
                            print "Your attack missed. You have " + str(characters1[chars[y]][2]) + " chances left"
                            if characters1[chars[y]][2] + agility == 0:
                                print "You have died"
                                victory = False
                                notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                                if notfinished == "yes" or notfinished == "y":
                                    done = False
                                    main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                         VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                         WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES, TERMINALS)
                                else:
                                    print "Play again soon :)"
                                    sys.exit()

                            else:
                                print "You can't do that"
                                trial += 1
                                if trial == 4:
                                    print "You have died 1" #Number added for testing purposes
                                    victory = False
                                    notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                                    if notfinished == "yes" or notfinished == "y":
                                        done = False
                                        main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                             VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                             WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES,
                                             TERMINALS)
                                    else:
                                        print "Play again soon :)"
                                        done = True
                                        sys.exit()

                    else:
                        print "That weapon does not exist"
                        trial += 1
                        if trial == 4:
                            victory = False
                            notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
                            if notfinished == "yes" or notfinished == "y":
                                done = False
                                main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
                                     VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
                                     WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES, TERMINALS)
                            else:
                                print "Play again soon :)"
                                done = True
                                sys.exit()
    print "-------------------------------------------                            "  #Python Flaw
    return victory, characters1, location, char


"""elif choose == "bypass":
                    characters1[chars[y]][0] = 0
                    print "Congrats! You have claimed victory over the enemy."
                    victory = True"""

"""
Function:      sos
Definition:    This is the help command which prints either the available
               directions to the users current location and all the movement commands
Author:        Kiefer Chiaravalloti
Date:          10/29/2014
History:       10/30/2014 The life alert easter egg is added, 2/4/2015 More commands have been added to the actions list,
               2/5/2015 Combat Commands have been added as well as more descriptive or more condensed commands
"""


def sos(directions, location):
    command = raw_input(
        "Type 1 for Directions --- Type 2 for Movements --- Type 3 for Actions  \nType 4 for Combat Commands: ")
    command = command.lower()
    if command == "1":
        directkeys = directions.keys()
        directvalues = directions.values()
        direct_index = directvalues.index(location)
        roomdirection = directkeys[direct_index]
        print roomdirection
    elif command == "2":
        print "\nNorth = n = go north = walk north = move north \n\
South = s = go south = walk south = move south\nEast = e = go east \
= walk east = move east\nWest = w = go west = walk west = move west\n\
Ascend = a = u = go up = up = climb up\nDescend = d = go down = down = climb down\n"
    elif command == "3":
        print "\nOpen to open doors\nShoot, engage combat, fight or attack to begin battle\nTake\Drop (Item Name)\nSave\Load\nLook, examine or search\nUpgrade\n"
    elif command == "4":
        print "\npunch and kick\nTo fire a weapon, type weapon name when asked what to attack with\nTo flee from enemies move in a direction\n"
    elif command == "i have fallen":
        life = raw_input("Can you get up? ")
        if life == "yes":
            print "Then stop wasting my time"
        elif life == "no":
            print "Get LifeAlert"
        else:
            print "Call J.G. Wentworth 877-CASHNOW"
    else:
        print "Invalid option\n"


"""
Function:      take
Definition:    This prompts the user to input what they would like to pick up,
               if the users input is in the weapons list and the user is in the
               location in which the item is located then the item shall be
               added to the players inventory, if the item is not in the room
               or doesn't exist then a message shall print outputting just that.
Author:        Matthew Vavruska
Date:          9/30/2014
History:       2/26/2015 print weapon has been removed
"""


def take(weapons, weapon, location):
    limit = 3
    weapons = str(weapons).split("{", 1)[1]
    weapons = str(weapons).split("}", 1)[0]
    weapons = "{" + weapons
    weapons += "}"
    weapon = re.sub(r"\(", '', weapon)
    weapon = re.sub(r", ''\)", '', weapon)
    weapon = re.sub(r"\]", '', weapon)
    weapons = re.sub(r"\(", '', str(weapons))
    weapons = re.sub(r", ''\)", '', weapons)
    weapons = ast.literal_eval(weapons)
    if weapon in weapons:
        if weapons[weapon][0] == 1:
            print "You already have the " + weapon
        elif location == weapons[weapon][2]:
            if inventory(weapons) < limit:
                weapons[weapon][0] = 1
                print "The " + weapon + " has been added to your inventory"
            else:
                while inventory(weapons) >= 3:
                    wp = raw_input(
                        "Your inventory is full please select a weapon to drop: " + inventory_weapons(weapons))
                    wp.strip()
                    weapons = drop(weapons, wp, location)
                weapons[weapon][0] = 1
                print "The " + weapon + " has been added to your inventory"
        else:
            print "The " + weapon + " is not in the room"
    inve = inventory_weapons(weapons)
    return weapons, inve


"""
Function:       inventory
Definition:     This keeps track of the items in the players posession, it starts
                off empty and remains so until the player picks up an item. Once
                an item is picked up the inventory changes from 0 to 1.
Author:         Matthew Vavruska
Date:           2/5/2015
History:
"""

def inventory(weapons):
    inv = 0
    for weapon in weapons:
        if weapons[weapon][0] == 1:
            inv += 1
    return inv

"""
Function:       inventory_weapons
Definition:     This assigns a name to the number that fills the inventory. The
                items name is included in the list and is seen when the players inventory is
                full
Author:         Matthew Vavruska
Date:           2/5/2015
History:
"""

def inventory_weapons(weapons):
    inve = ""
    for weapon in weapons:
        if weapons[weapon][0] == 1:
            inve += weapon + " "
    return inve


"""
Function:       drop
Definition:     If the user inputs the command drop a message shall be output
                asking what they would like to drop, if the item is in the
                players inventory then
                the item will be removed from the inventory.
Author:         Matthew Vavruska
Date:           9/30/2014
History:
"""


def drop(weapons, weapon, location):
    weapons = str(weapons).split("}", 1)[0]
    weapons += "}"
    weapon = re.sub(r"\(", '', weapon)
    weapon = re.sub(r", ''\)", '', weapon)
    weapon = re.sub(r"\]", '', weapon)
    weapons = re.sub(r"\(", '', str(weapons))
    weapons = re.sub(r", ''\)", '', weapons)
    weapons = ast.literal_eval(weapons)
    if weapon in weapons:
        if weapons[weapon][0] == 1:
            weapons[weapon][0] = 0
            weapons[weapon][2] = location
            print "The item has been dropped"
        else:
            print "You don't have that"
    else:
        print "Don't have it moron"
    inve = inventory_weapons(weapons)
    return weapons, inve


"""
Function:     attackchance
Definition:   This function shall evaluate the chance of the weapon and the
              chance of hitting the enemy, it then rounds the chance. If the
              rounded chance
              equals a random integer then the user hits the enemy.
Author:       Dale Guimond
Date:         9/30/2014
History:
"""


def attackchance(x, y):
    chance = x * y
    chance2 = chance / 2
    roundedchance = round(chance2)
    return roundedchance


"""
Function:      north, n, go north, walk north, move north
Definition:    This function moves the player up the y axis
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def north(location, travelled):
    if location == [5, 7, 0]:
        print location
        if [0, 8, 0] not in travelled:
            print ""
        else:
            location[1] += 1
    else:
        location[1] += 1
    return location


"""
Function:      south, s, go south, walk south, move south
Definition:    This function moves the player down the y axis
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def south(location, travelled):
    location[1] = location[1] - 1
    return location


"""
Function:      east, e, go east, walk east, move east
Definition:    This function moves the player right on the x axis
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def east(location, travelled):
    location[0] += 1
    return location


"""
Function:      west, w, go west, walk west, move west
Definition:    This function moves the player left on the x axis
Author:        Dale Guimond
Date:          9/30/2014
History:
"""


def west(location, travelled):
    location[0] = location[0] - 1
    return location


"""
Function:      ascend, a, u, go up, up, climb up
Definition:    This function moves the player up the z axis
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def ascend(location, travelled):
    location[2] += 1
    return location


"""
Function:      descend, d, go down, down, climb down
Definition:    This function moves the player down the z axis
Author:        Matthew Vavruska 
Date:          9/30/2014
History:
"""


def descend(location, weapons):
    if location == [5, 11, 1]:
        if weapons["keycard"][0] == 1:
            location = [5, 11, -1]
        else:
            print "You need the keycard to open the elevator."
    else:
        location[2] = location[2] - 1
    return location


"""
Function:      testlocation
Definition:    It checks the current location and makes sure it's in the game
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def testlocation(location, location2, coordinates):
    if location2 in coordinates:
        retval = location2
    else:
        retval = location
    return retval

"""
Function:       suicide
Definition:     This is simply a print statement for when the player inputs kill self
Author:         Kiefer Chiaravalloti
Date:           12/15/2014
History:
"""

def suicide():
    print "Congrats you ragdolled. You Are Dead"

"""
Function:       invalid
Definition:     This is simply a print statement for when the player inputs weast
Author:         Kiefer Chiaravalloti
Date:           12/15/2014
History:
"""

def invalid():
    print "What kind of compass are you reading lad?\n"

"""
Function:       terminal
Definition:     This adds a section which requires the users command to be
                either shutdown or titan to progress
Author:         Kiefer Chiaravalloti
Date:           12/15/2014
History:
"""

def terminal(travelled, location):
    textOut = "After inputting the command, all the machines begin their \
shut down procedures. You have made a massive blow in Titan Robotics production. \
You have no reason tostay here anymore.\n"

    done = False
    while not done:

        command = raw_input("Enter Command:  ")

        if command == "Shut Down" or command == "shutdown" or command == "shut down" \
                or command == "Titan" or command == "titan":
            print textOut
            done = True
        else:
            print "ERROR: Invalid Command."
 

"""
Function:       build_actions_list
Definition:     It tests directional movements
Author:         Kiefer Chiaravalloti
Date:           12/15/2014
History:
"""

def build_actions_list(a, b, c, d, e, f=None):  # overloading a function in Python
    action1 = []
    action1.append(a)
    action1.append(b)
    action1.append(c)
    action1.append(d)
    action1.append(e)

    if f != None:
        action1.append(f)

    return action1


"""
Function:     validlocation
Definition:   This function creates the actions list out of the valid
              coordinates for certain movements 
Author:       Matthew Vavruska
Date:         9/30/2014
History:      10/30/2014 kill self has been added
"""


def validlocation(location, validnorth, validsouth, valideast, validwest,
                  validascend, validdescend, validopen, validshoot, terminals):
    actions = []
    if location in validnorth:
        actions.append("north")
        actions.append("n")
        actions.append("go north")
        actions.append("walk north")
        actions.append("move north")
    if location in validsouth:
        actions.append("south")
        actions.append("s")
        actions.append("go south")
        actions.append("walk south")
        actions.append("move south")
    if location in validwest:
        actions.append("west")
        actions.append("w")
        actions.append("go west")
        actions.append("walk west")
        actions.append("move west")
    if location in valideast:
        actions.append("east")
        actions.append("e")
        actions.append("go east")
        actions.append("walk east")
        actions.append("move east")
    if location in validascend:
        actions.append("ascend")
        actions.append("a")
        actions.append("u")
        actions.append("go up")
        actions.append("up")
        actions.append("climb up")
    if location in validdescend:
        actions.append("descend")
        actions.append("d")
        actions.append("go down")
        actions.append("down")
        actions.append("climb down")
    if location in validopen:
        actions.append("open")
    if location in validshoot:
        actions.append("fight")
        actions.append("attack")
        actions.append("engage combat")
    if location in terminals:
        actions.append("upgrade")
    actions.append("help")
    actions.append("weast")
    actions.append("kill self")
    actions.append("drop")
    actions.append("take")
    actions.append("save")
    actions.append("load")
    actions.append("look")
    actions.append("search")
    actions.append("examine")
    return actions

"""
Function:     parser
Definition:   It splits the user lists into various variables, replaces special
              characters with spaces
Author:       Matthew Vavruska    
Date:         8/16/2014
History:      
"""

def parser(user):
    userlist = user.split()
    usercombo = True
    try:
        user1 = userlist[0]
    except:
        user1 = ""
    #test user2
    try:
        user2 = userlist[1]
        user2 = re.sub(r'\W+', '', user2)
        usercombo = user1 + " " + user2
    except:
        user2 = ""
    #test user3
    try:
        user3 = userlist[2]
    except:
        user3 = ""
    #test user4
    try:
        user4 = userlist[3]
    except:
        user4 = ""
    #test user5
    try:
        user5 = userlist[4]
    except:
        user5 = ""
    user2 = user2 + user3 + user4 + user5
    user2 = user2.lower()
    return user1, user2, usercombo


"""
Function:    reset_stuff
Definition:  resets variables for pretower
Author:      Matthew Vavruska
Date:        10/23/2014
History:      
"""

def reset_stuff():  
    return 1, 0, 0, False

"""
Function:     reset_stuff2   
Definition:   resets variables for posttower
Author:       Matthew Vavruska
Date:         10/23/2014
History:      
"""

def reset_stuff2():
    return 1, 1, 0, False


"""
Function:     executecommandpretower
Definition:   This computes any and all commands given by the player and
              processes them through the various functions, only includes the
              area that is before the tower is completed
Author:       Matthew Vavruska
Date:         1/20/2015
History:      
"""

def executecommandpretower(commands, actions, location, coordinates, directions, weapons2, validopen, user1, user,
                           user2, commandkeys, commandvals, characters, code, charactersx, travelled, meleeattacks,
                           inventory, lookcoords, terminals):
    crowbar = "crowbar"
    location = location
    x = 0
    k = "k"
    megaparticlecannon = "megaparticlecannon"
    laserrifle = "laserrifle"
    lasershotgun = "lasershotgun"
    laserpistol = "laserpistol"
    empgrenade = "empgrenade"
    rocketartillery = "rocketartillery"
    raygun = "raygun"
    shockblast = "shockblast"
    keycard = "keycard"
    disruptor = "disruptor"
    flamethrower = "flamethrower"
    downnotes = ['descend', 'd', 'go down', 'down', 'climb down']
    weapons1 = weapons2
    user = user.lower()
    if user in commandkeys or user1 in commandkeys:
        if user in actions or user1 in actions:
            try:
                index = commandkeys.index(user)
            except ValueError:
                index2 = commandkeys.index(user1)
            if user in MOVEMENT:
                # This tests the movement 
                if user in downnotes:
                    exec commandvals[index] + str(location) + "," + str(weapons2) + ")"
                else:
                    exec commandvals[index] + str(location) + "," + str(travelled) + ")"
                location = testlocation(location, location2, coordinates)
                reset1, reset2, reset3, victory = reset_stuff()

            elif user == "help":
                reset1, reset2, reset3, victory = reset_stuff()
                exec commandvals[index] + str(directions) + "," + str(location) + ")"

            elif user == "weast":
                reset1, reset2, reset3, victory = reset_stuff()
                exec commandvals[index] + ")"
            elif user == "kill self":
                exec commandvals[index]
                reset1 = 1
                reset2 = 2
                reset3 = 0
                victory = False
            elif user == "open":
                exec commandvals[index] + str(validopen) + "," + str(location) + "," + str(weapons1) + "," + str(
                    code) + ")"
                location = testlocation(location, location2, coordinates)
                reset1, reset2, reset3, victory = reset_stuff()
            elif user1 == "take" or user1 == "drop":
                try:
                    running = "weapons1, inventory = " + commandvals[index2] + str(weapons2) + "," + str(
                        user2) + "," + str(location) + ")"
                    exec running
                except NameError:
                    print "The item does not exist"
                except SyntaxError:
                    if user2 == "":
                        print "What are you doing? Wasting my time with nothingness!"
                        user2 = "wwww"
                    try:
                        user2 = re.sub(r'\W+', '', user2)
                        running = "weapons1 = " + commandvals[index2] + str(weapons2) + "," + str(user2) + "," + str(
                            location) + ")"
                        exec running
                    except NameError:
                        print "The item does not exist"
                reset1, reset2, reset3, victory = reset_stuff()
            elif user == "fight" or user == "engage combat" or user == "attack":
                try:
                    exec "victory, characters, location, char = " + commandvals[index] + str(characters) + "," + str(
                    weapons2) + "," + str(location) + "," + str(charactersx) + "," + str(
                    meleeattacks) + "," + inventory  + ")"
                except SyntaxError:
                    inventory = inventory.split(' ')
                    if ' ' in inventory:
                        inventory.remove(' ')
                    print inventory
                    if len(inventory) == 1:
                        command_line = "victory, characters, location, char = " + commandvals[index] + str(characters) + "," + str(
                                        weapons2) + "," + str(location) + "," + str(charactersx) + "," + str(
                                        meleeattacks) + "," + inventory[0] + ")"
                    elif len(inventory) == 2:
                        command_line = "victory, characters, location, char = " + commandvals[index] + str(characters) + "," + str(
                                        weapons2) + "," + str(location) + "," + str(charactersx) + "," + str(
                                        meleeattacks) + "," + inventory[0] + "," + inventory[1] + ")"
                    elif len(inventory) == 3:
                        command_line = "victory, characters, location, char = " + commandvals[index] + str(characters) + "," + str(
                                        weapons2) + "," + str(location) + "," + str(charactersx) + "," + str(
                                        meleeattacks) + "," + inventory[0] + "," + inventory[1] + "," + inventory[2] + ")"
                    exec command_line
                if char[0] == "titanms" and victory == True:
                    reset1 = 0
                    reset2 = 2
                    reset3 = 1

                else:
                    if char[0] != "titanms" and victory == True:
                        reset1 = 1
                        reset2 = 0
                        reset3 = 0

                    else:
                        reset1 = 1
                        reset2 = 3
                        reset3 = 0
            elif user == "save":
                username = raw_input("What is the desired username:   ")
                username = re.sub(r'\s', '', username)
                exec str(username) + "='" + str(username) + "'"
                try:
                    exec_var = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory + ")"
                    exec exec_var
                except SyntaxError:
                    inventory = inventory.split(' ')
                    if ' ' in inventory:
                        inventory.remove(' ')
                    print inventory
                    if len(inventory) == 1:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + ")"
                    elif len(inventory) == 2:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + " " + inventory[1] + ")"
                    elif len(inventory) == 3:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + " " + inventory[1] + ")"
                print "Game Saved for " + username
                reset1, reset2, reset3, victory = reset_stuff()
            elif user == "load":
                username = raw_input("What is the your username:   ")
                exec str(username) + "='" + str(username) + "'"
                exec "print " + str(username)
                exec "travelled, weapons1, location, characters, inventory = " + commandvals[index] + str(
                    username) + "," + str(travelled) + "," + str(weapons2) + "," + str(location) + "," + str(
                    characters) + "," + inventory + ")"
                reset1, reset2, reset3, victory = reset_stuff()
            elif user == "look" or user == "search" or user == "examine":
                exec commandvals[index] + str(lookcoords) + "," + str(location) + "," + str(weapons2) + ")"
                reset1, reset2, reset3, victory = reset_stuff()
            elif user == "upgrade":
                exec commandvals[index] + str(characters) + ")"
                reset1, reset2, reset3, victory = reset_stuff()
            else:
                print "You might be confused"
                reset1, reset2, reset3, victory = reset_stuff()
        else:
            print "That cannot be used here"
            reset1, reset2, reset3, victory = reset_stuff()
    else:
        print "I'm awfully confused by what you mean when you say: " + str(user)
        reset1, reset2, reset3, victory = reset_stuff()
    #print "returning..."
    #return newlocation, characters['self'][2], characters['self'][1], characters['self'][0], victory, weapons1, characters
    return location, reset3, reset2, reset1, victory, weapons1, characters, inventory

"""
Function:     executecommandposttower
Definition:   This computes any and all commands given by the player and
              processes them through the various functions, only includes the
              area that is after the tower is completed
Author:       Matthew Vavruska
Date:         1/20/2015
History:      
"""

def executecommandposttower(commands, actions, location, coordinates, directions, weapons2, validopen, user1, user,
                            user2, commandkeys, commandvals, characters, code, charactersx, travelled, meleeattacks,
                            inventory, lookcoords, terminals):
    crowbar = "crowbar"
    x = 0
    k = "k"
    megaparticlecannon = "megaparticlecannon"
    laserrifle = "laserrifle"
    lasershotgun = "lasershotgun"
    laserpistol = "laserpistol"
    empgrenade = "empgrenade"
    rocketartillery = "rocketartillery"
    raygun = "raygun"
    shockblast = "shockblast"
    keycard = "keycard"
    disruptor = "disruptor"
    flamethrower = "flamethrower"
    downnotes = ['descend', 'd', 'go down', 'down', 'climb down']
    weapons1 = weapons2
    user = user.lower()
    if user in commandkeys or user1 in commandkeys:
        if user in actions or user1 in actions:
            try:
                index = commandkeys.index(user)
            except ValueError:
                index2 = commandkeys.index(user1)
            if user in MOVEMENT:
                # This tests the movement 
                if user in downnotes:
                    exec commandvals[index] + str(location) + "," + str(weapons2) + ")"
                else:
                    exec commandvals[index] + str(location) + "," + str(travelled) + ")"
                location = testlocation(location, location2, coordinates)
                reset1, reset2, reset3, victory = reset_stuff2()

            elif user == "help":
                reset1, reset2, reset3, victory = reset_stuff2()
                exec commandvals[index] + str(directions) + "," + str(location) + ")"

            elif user == "weast":
                reset1, reset2, reset3, victory = reset_stuff2()
                exec commandvals[index] + ")"
            elif user == "kill self":
                exec commandvals[index]
                reset1 = 1
                reset2 = 2
                reset3 = 0
                victory = False
            elif user == "open":
                exec commandvals[index] + str(validopen) + "," + str(location) + "," + str(weapons1) + "," + str(
                    code) + ")"
                location = testlocation(location, location2, coordinates)
                reset1, reset2, reset3, victory = reset_stuff2()
            elif user1 == "take" or user1 == "drop":
                try:
                    running = "weapons1, inventory = " + commandvals[index2] + str(weapons2) + "," + str(
                        user2) + "," + str(location) + ")"
                    exec running
                except NameError:
                    print "The item does not exist"
                except SyntaxError:
                    if user2 == "":
                        print "What are you doing? Wasting my time with nothingness!"
                        user2 = "x"
                    try:
                        user2 = re.sub(r'\W+', '', user2)
                        running = "weapons1 = " + commandvals[index2] + str(weapons2) + "," + str(user2) + "," + str(
                            location) + ")"
                        exec running
                    except NameError:
                        print "The item does not exist"
                reset1, reset2, reset3, victory = reset_stuff2()
            elif user == "fight" or user == "engage combat" or user == "attack":
                exec "victory, characters, location, char = " + commandvals[index] + str(characters) + "," + str(
                    weapons2) + "," + str(location) + "," + str(charactersx) + "," + inventory + "," + str(
                    meleeattacks) + ")"

                if char[0] == "titanms" and victory == True:
                    reset1 = 0
                    reset2 = 2
                    reset3 = 1

                else:
                    if char[0] != "titanms" and victory == True:
                        reset1 = 1
                        reset2 = 0
                        reset3 = 0

                    else:
                        reset1 = 1
                        reset2 = 3
                        reset3 = 0
            elif user == "save":
                username = raw_input("What is the desired username:   ")
                username = re.sub(r'\s', '', username)
                exec str(username) + "='" + str(username) + "'"
                try:
                    exec commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + \
                         str(characters) + "," + str(travelled) + "," + inventory + ")"
                except SyntaxError:
                    inventory = inventory.split(' ')
                    if ' ' in inventory:
                        inventory.remove(' ')
                    print inventory
                    if len(inventory) == 1:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + ")"
                    elif len(inventory) == 2:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + " " + inventory[1] + ")"
                    elif len(inventory) == 3:
                        command_line = commandvals[index] + username + "," + str(weapons2) + "," + str(location) + "," + str(characters) + "," + str(travelled) + "," + inventory[0] + " " + inventory[1] + ")"
                print "Game Saved for " + username
                reset1, reset2, reset3, victory = reset_stuff2()
            elif user == "load":
                username = raw_input("What is the your username:   ")
                exec str(username) + "='" + str(username) + "'"
                exec "print " + str(username)
                exec "travelled, weapons1, location, characters, inventory = " + commandvals[index] + str(
                    username) + "," + str(travelled) + "," + str(weapons2) + "," + str(location) + "," + str(
                    characters) + "," + inventory + ")"
                reset1, reset2, reset3, victory = reset_stuff2()
            elif user == "look" or user == "search" or user == "examine":
                exec commandvals[index] + str(lookcoords) + "," + str(location) + "," + str(weapons2) + ")"
                reset1, reset2, reset3, victory = reset_stuff2()
            elif user == "upgrade":
                exec commandvals[index] + str(characters) + ")"
                reset1, reset2, reset3, victory = reset_stuff2()
            else:
                print "You might be confused"
                reset1, reset2, reset3, victory = reset_stuff2()
        else:
            print "That cannot be used here"
            reset1, reset2, reset3, victory = reset_stuff2()
    else:
        print "I'm awfully confused by what you mean when you say: " + str(user)
        reset1, reset2, reset3, victory = reset_stuff2()
    return location, reset3, reset2, reset1, victory, weapons1, characters, inventory


"""
Function:     getcommand
Definition:   Prompts the user to input one of the games commands and checks
              that is in the games valid commands and in the actions list and
              runs the designated functions
Author:       Matthew Vavruska
Date:         9/30/2014
History:      10/30/2014 Kill self was added
"""


def getcommand(commands, actions, location, coordinates, directions, weapons2,
               validopen, characters, code, charactersx, travelled, meleeattacks, inventory, lookcoords, terminals):
    if testchar(characters, location) != []:
        user = "fight"
    else:
        user = raw_input("What will you do? ")
    weapons1 = weapons2
    reset1 = 0
    reset2 = 0
    reset3 = 0
    commandkeys = commands.keys()
    commandvals = commands.values()
    coordinates = coordinates.values()
    user1, user2, usercombo = parser(user)
    if [5, 9, 1] not in travelled:
        location, reset3, reset2, reset1, victory, weapons1, characters, inventory = executecommandpretower(commands,
                                                                                                            actions,
                                                                                                            location,
                                                                                                            coordinates,
                                                                                                            directions,
                                                                                                            weapons2,
                                                                                                            validopen,
                                                                                                            user1, user,
                                                                                                            user2,
                                                                                                            commandkeys,
                                                                                                            commandvals,
                                                                                                            characters,
                                                                                                            code,
                                                                                                            charactersx,
                                                                                                            travelled,
                                                                                                            meleeattacks,
                                                                                                            inventory,
                                                                                                            lookcoords,
                                                                                                            terminals)
    else:
        location, reset3, reset2, reset1, victory, weapons1, characters, inventory = executecommandposttower(commands,
                                                                                                             actions,
                                                                                                             location,
                                                                                                             coordinates,
                                                                                                             directions,
                                                                                                             weapons2,
                                                                                                             validopen,
                                                                                                             user1,
                                                                                                             user,
                                                                                                             user2,
                                                                                                             commandkeys,
                                                                                                             commandvals,
                                                                                                             characters,
                                                                                                             code,
                                                                                                             charactersx,
                                                                                                             travelled,
                                                                                                             meleeattacks,
                                                                                                             inventory,
                                                                                                             lookcoords,
                                                                                                             terminals)
    #return newlocation, characters['self'][2], characters['self'][1], characters['self'][0], victory, weapons1
    return inventory, location, reset3, reset2, reset1, victory, weapons1, characters


"""
Function:     testchar 
Definition:   List of remaining characters
Author:       Matthew Vavruska
Date:         2/26/2015
History:      
"""

def testchar(characters, location):
    chardetails = characters.values()
    chars = characters.keys()
    xlist = []
    for y in range(len(characters)):
        if characters[chars[y]][0] == 1:
            if location == chardetails[y][3]:
                if characters[chars[y]][5] == "auto":
                    xlist.append(chars[y])
    return xlist


"""
Function:      main
Definition:    This is the main function that sets the starting coordinate and
               checks if the user has completed certain in game tasks.
Author:        Matthew Vavruska
Date:          9/30/2014
History:
"""


def main(prologue, coordinates, validascend, validdescend, validnorth,
         validsouth, valideast, validwest, characters, commands, start,
         epilogue, directions, weapons, validopen, validshoot, code, meleeattacks, lookcoords, terminals):
    victory = True
    travelled_locations = []
    weapons4 = weapons
    charactersx = characters
    newlocation = [0, 0, 0]
    #print weapons
    weapons1 = weapons
    print prologue
    code1 = code
    inventory = "k"
    coordx = start[0]
    coordy = start[1]
    coordz = start[2]
    location = [coordx, coordy, coordz]
    coordkeys = coordinates.keys()
    coordvalues = coordinates.values()
    #location = input("Type a Coordinate:  ")
    done = False
    while done == False:
        weapons1 = weapons
        #print weapons1
        while characters['self'][3] == 0:  #Has the player beaten the game?
            while characters['self'][0] == 1:  #Has the player died?
                while characters['self'][1] == 0:  #Has the player beaten the tower?
                    if characters['self'][2] == 0:  #Has the player fled?
                        #print "get in 1"
                        if location in coordvalues:
                            travelled2 = travelled_locations
                            #print weapons
                            actions = validlocation(location, validnorth,
                                                    validsouth, valideast, validwest,
                                                    validascend, validdescend, validopen,
                                                    validshoot, terminals)
                            #location = input("Type a Coordinate:  ")
                            inventory, newlocation, reset3, reset2, reset1, victory, weapons1, characters = getcommand(
                                commands, actions, location, coordinates, directions, weapons1, validopen, characters,
                                code1, charactersx, travelled_locations, meleeattacks, inventory, lookcoords, terminals)
                            characters['self'][2] = reset3
                            characters['self'][1] = reset2
                            characters['self'][0] = reset1
                            if location != newlocation:
                                desc_index = coordvalues.index(newlocation)
                                roomdescription = coordkeys[desc_index]
                                print roomdescription
                                scan(characters, weapons1, newlocation, terminals)
                            else:
                                pass
                            #print newlocation
                            #print "returned..."
                            location = newlocation
                            travelled_locations.append(location)
                            if location == [5, 9, -1]:
                                characters['self'][2] = 1
                                characters['self'][1] = 1
                                characters['self'][0] = 0
                                victory = False
                                print "Before you have time to even realize \
where you are your systems suddenly\nshut down. It appears that your mission \
has ended just as soon as it has begun. GAME OVER\n\n"

                            elif location == [0, 8, 0]:
                                terminal(travelled2, location)
                            elif location == [5, 9, 1]:
                                characters['self'][2] = 1
                                characters['self'][1] = 0
                                characters['self'][0] = 1

                            elif location == [-2, 2, 0]:
                                characters['self'][2] = 1
                                characters['self'][1] = 1
                                characters['self'][0] = 0
                                victory = False
                            elif location == [5, 7, 0] and [0, 8, 0] not in travelled_locations:
                                print "There is a forcefield standing in the way between you and the tower. \
Until it isshut down, you shall not pass."
                            else:
                                pass
                                #print "none of the above..."
                        else:
                            location = [0, 0, 0]
                            print prologue
                    else:
                        #print "get in 2"
                        if location == [5, 9, 1]:
                            characters['self'][1] = 1
                            characters['self'][2] = 0
                            print "You have beaten the Tower. Proceed to the next part of your journey."
                        else:
                            pass

                            #print characters['self'][2]
                            #print "came around"

                while characters['self'][1] == 1:  #Has the player beaten the tower?
                    if characters['self'][2] == 0:  #Has the player fled?
                        if location in coordvalues:
                            #print weapons
                            actions = validlocation(location, validnorth,
                                                    validsouth, valideast, validwest,
                                                    validascend, validdescend, validopen,
                                                    validshoot, terminals)
                            #location = input("Type a Coordinate:  ")
                            inventory, newlocation, reset3, reset2, reset1, victory, weapons1, characters = getcommand(
                                commands, actions, location, coordinates, directions, weapons1, validopen, characters,
                                code1, charactersx, travelled_locations, meleeattacks, inventory, lookcoords, terminals)
                            characters['self'][2] = reset3
                            characters['self'][1] = reset2
                            characters['self'][0] = reset1
                            if location != newlocation:
                                desc_index = coordvalues.index(newlocation)
                                roomdescription = coordkeys[desc_index]
                                print roomdescription
                                scan(characters, weapons1, newlocation, terminals)
                            else:
                                pass
                            location = newlocation
                            travelled_locations.append(location)
                        else:
                            location = [0, 0, 0]
                            weapons1 = weapons4
                    else:
                        characters['self'][1] = 2
                if characters['self'][1] == 2:
                    characters['self'][0] = 0
            characters['self'][3] = 1
        if victory == True:
            print epilogue
            print "Congratulations you have beaten the game"
        print """
Techno Surge\n\n
Project Lead & Lead Programmer: MATTHEW VAVRUSKA\n\n
Map Designer & Editor: KIEFER CHIARAVALLOTI\n\n
Storyline Creator: DALE GUIMOND\n\n
Special Thanks:\n
STEPHEN DYMEK
"""
        notfinished = raw_input("Would you like to play again?\n(Type yes or no):     ")
        weapons1 = weapons4
        if notfinished == "yes" or notfinished == "y":
            done = False
            characters['self'][3] = 0
            characters['self'][2] = 0
            characters['self'][1] = 0
            characters['self'][0] = 1
            location = start
            weapons1 = weapons4
        else:
            print "Play again soon :)"
            done = True


main(PROLOGUE, COORDINATES, VALIDASCEND, VALIDDESCEND, VALIDNORTH, VALIDSOUTH,
     VALIDEAST, VALIDWEST, CHARACTERS, COMMANDS, START, EPILOGUE, DIRECTIONS,
     WEAPONS, VALIDOPEN, VALIDSHOOT, code, MELEEATTACKS, LOOKCOORDINATES, TERMINALS)
