# Project #3 : Help Mac Gyver to get out !  
  
The aim of this student project is to create a 2D maze where the famous Mac Gyver will be trapped.  
To escape, he will have to pick-up 3 objects with whom he will create a syringe in order to fall the guardian asleep.  
  
## Installation of the game
### Prerequisites  
  
1. This program runs on __Python__.    
To install it, see the official website :  www.python.org  

2. You will also need __Git__ on your computer. See : https://git-scm.com/book/en/v2/Getting-Started-Installing-Git    
    
3. Before running the game installation, I recommend you to create a virtual environment with __venv__.    
    
- Run your shell on your destination file.    
- Create you virtual environment with this command :    
`python3 -m venv name_of_your_virtual_environment` 
*Example :* 
`python3 -m venv venv`  
- Activate your virtual environment with this command :    
`source name_of_your_virtual_environment/bin/activate`  
*Example :*  
`source venv/bin/activate`  
  
### Installing  
  
To download the project :  
`git clone https://github.com/mblnv/P3_mac_gyver.git`

Then move to the new file 'P3_mac_gyver'
`cd P3_mac_gyver`

And finally, to install the dependencies :  
`python3 -m pip install -r requirements.txt`
(On Mac OS X, you might encounter some issues and might need to install Pygame manually :
`python3 -m pip install pygame==2.0.0.dev6`
For more, see the documentation : https://www.pygame.org/wiki/GettingStarted )

### Running  
  
To launch the game :  
`python3 __main__.py`

### Closing

To quit your virtual environment :
`deactivate name_of_your_virtual_environment`
*Example :*
`deactivate venv`

## About the game

### Architecture of the project  

When the program is launched, a new game is created.  
  
From this new game, a map is created.  
  
The sprites are displayed according to their type, as described in the 'map.txt' file.  
  
Then, the player (Mac Gyver) can be moved with the arrow keys.  
  
If the player pick-up the 3 objects displayed randomly on the floor and then face the guardian, he wins.  
  
If the player faces the guardian with less than 3 objects, then he dies.  
  
In both cases, the game has to be closed and launched again to start a new game.  
  
### Tree of the files
 
origin/   
|-- .gitignore   
|-- __ main __.py   
|-- map.txt  
|-- README.md   
|-- requirements.txt  
|-- game/   
|&nbsp;&nbsp;&nbsp;&nbsp;|-- __ init __.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- game.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- items.py  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- structure.py  
|-- images/  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- floor.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- guardian.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- mac_gyver.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- wall.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- you_die.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- you_win.png  
|&nbsp;&nbsp;&nbsp;&nbsp;|-- objects/  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- ether.png  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- needle.png  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- syringe.png  
  
### Author 
 
Ombeline  
  
Student @ OpenClassrooms
