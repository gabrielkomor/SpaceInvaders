# SpaceInvaders
Computer game based on the popular space invaders game

## Table of Contents
* [General info](#general-info)
* [Technologies Used](#technologies-used)
* [Setup pip](#setup-pip--requirementstxt)
* [Setup poetry](#setup-poetry)
* [Screenshots](#screenshots)
* [Game Controls](#game-controls)
* [Project Status](#project-status)
* [Sources](#sources)

## General info
I created a 2D game in Python, based on the classic Space Invaders. Thanks to this, I developed my skills in object-oriented programming and working with graphics and animations.

## Technologies Used
Project is created with:
* Python
* Pygame
* PyCharm Community Edition
* Gimp

## Setup (pip + requirements.txt)

1. Clone GitHub repozitory `git clone https://github.com/gabrielkomor/SpaceInvaders.git`

2. To run this project, create new empty project in PyCharm editor, copy all files and put command below in PyCharm terminal:

```shell
pip install -r .\requirements.txt
```

## Setup (poetry)

1. Clone GitHub repozitory `git clone https://github.com/gabrielkomor/SpaceInvaders.git`

2. Install poetry via command below (Windows)

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

3. Add poetry to environment variables (you can find `poetry.exe` in `...\AppData\Roaming\Python\Scripts`)

4. Install Python environment and dependencies using `poetry install` command

## Screenshots
### Sample screenshots from the game:
##### Beginning of the game
![Beginning of the game](example_screens/SpaceInvaders_1.jpg)
##### Game shop
![Game shop](example_screens/SpaceInvaders_2.jpg)
##### New opponents
![New opponents](example_screens/SpaceInvaders_3.jpg)
##### Final boss
![Final boss](example_screens/SpaceInvaders_4.jpg)

## Game Controls

### Movement:
- **Go left:** `A` key or left arrow key, or click on the left button on the game interface  
- **Go right:** `D` key or right arrow key, or click on the right button on the game interface  

### Shooting:
- **Press space** once or click on the bullet icon once on the game interface  

### Pause:
- **Press `P` key** or click on the pause button on the game interface  

### Buy in shop:
- Click on the sprocket on the game interface next to the upgrade you want to buy  

### Leave the shop:
- Click on the red icon with a door on the game interface  

### Game quit:
- **Press `Esc` key**  


## Project Status
Project is complete. I currently have no plans to further develop the game, as I have achieved the intended learning outcomes

## Sources
#### Game was based on the popular classic game of the same title.
#### Graphics used in game come from the website https://www.flaticon.com/
