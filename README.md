# LAS-Randomizer
A randomizer for The Legend of Zelda: Link's Awakening remake.

This repository is a **modded version of the original randomizer made by Owen that adds some features**

**Latest modded release is available here** : https://github.com/ProfessorLaw/LAS-Randomizer/releases/latest

## Main changes currently in testing phase

- TBD

## Feature and changes added to the main version

- **Chest Size & Texture** : You can choose between normal, size matching content and texture matching content chests !
- **Extra consumable drops** : Bombs, Magic Powder and Arrows will drop from grass if this setting is enable
- **Starting Dungeon Items** : You can now choose to start with nothing, Maps & Compass, or Maps, Compass & Beaks as dungeon items!
- **Perfect ending** : You can force the perfect ending to show at the end of the game even if you get a game over.
- **Open Mabe** : This setting allows you to get out of the village without any items. This opens access to Beach, Woods & Plains (3 to 4 locations)
- **Quick Mode** : This setting makes most boss intro skipped, textbox skips and faster animations. **This is still a work in progress !**

**More to come in the future !**
### Donate:

If you want to support my additions on this randomizer, feel free to buy me a coffee ! 

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P77VZ2L)

Note: Owen being the main maintainer of the randomizer, I suggest you to support him too if you like his work !

## Information
This randomizes all the items in the game so that every playthrough is unique. It also aims to add quality of life changes, such as skipping cutscenes, or adding options that make the game more open-world.

**Logic**:
- Basic: No glitches or advanced tricks, although 2 tile jumps are included. Recommended for beginners.
- Advanced: Skews and bomb arrows will be added to logic.
- Glitched: Adds some glitches to logic that will not result in being softlocked.
- Hell: Adds more glitches to logic that can result in softlocks.
- None: Throws all logic out the window. Seeds will likely be unbeatable.

Please note that while most things are functional, there is a possibility of the logic resulting in softlocks. This will be especially true with the glitched logics. If this does happen, dying and selecting the Save + Quit option will respawn you back at Marin's house.

## How to play:
Please refer to the setup wiki: https://github.com/Owen-Splat/LAS-Randomizer/wiki/Setup-Instuctions

## Discord Server
Join the Discord server to talk about the randomizer, ask questions, or even set up races!  
The Discord also contains some more detailed information about the current state of the randomizer, including known issues and what is shuffled.

https://discord.com/invite/rfBSCUfzj8

## Credits:
- [Owen-Splat](https://github.com/Owen-Splat/LAS-Randomizer) for being the main maintainer of the randomizer and helped me a lot to get started with it !
- Glan: Created the original early builds of the randomizer found here: https://github.com/la-switch/LAS-Randomizer
- j_im: Created the original tracker for the randomizer
- Br00ty: Maintains and updates the tracker for newer randomizer versions
- theboy181: Blur removal patch

### Special Thanks:
- To everyone who has reported bugs or given feedback and suggestions. This randomizer would not be where it is today without our community.

## Running from source:
**NOTE**: This is for advanced users or those helping with the development of this randomizer.

If you want to run from source, then you need to clone this repository and make sure you have Python 3.8+ installed

Open the folder in a command prompt and install dependencies by running:
`py -3.8 -m pip install -r requirements.txt` (on Windows)
`python3 -m pip install -r requirements.txt` (on Mac)
`python3 -m pip install $(cat requirements.txt) --user` (on Linux)

Then run the randomizer with:
`py -3.8 randomizer.py` (on Windows)
`python3 randomizer.py` (on Mac)
`python3 randomizer.py` (on Linux)

If you are using a different version of Python, change the commands to include your version instead

Once you have installed all the requirements, there is an included **build.bat** file. Run that (you can just enter `build` in the terminal) and it will automatically enter the commands to create a build. Once again, if you are using a different version of Python, you will need to edit this file to match your version
