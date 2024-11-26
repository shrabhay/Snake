# Snake Game
## Description
This project is a simple implementation of the classic Snake game using Python and the `turtle` module. The game consists of a snake that grows longer as it eats food while avoiding walls and collisions with its own body. The goal is to achieve the highest possible score.

---

## Project Overview

The project includes the following components:

* **snake.py**: Contains the Snake class that controls all the snake-related functionality, such as movement, growth, 
and collision detection.
* **food.py**: Contains the Food class responsible for creating and managing the food the snake eats. The food appears at random positions on the screen.
* **scoreboard.py**: Manages the display of the player's score and handles the game-over message.
* **snake-game.py**: The main script that runs the game, bringing together the Snake, Food, and Scoreboard components. It listens for player input to control the snake and runs the game loop.

---

## How to Play

* Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.
* The objective is to eat the blue food that appears at random positions on the screen. Each time the snake eats food, it grows in length, and the score increases by 1.
* The game ends if the snake hits the wall or collides with its own body.

---

## Features

* **Snake Movement**: The snake moves continuously and changes direction based on user input.
* **Food Generation**: The food is randomly placed on the screen, and the snake grows in size each time it eats the food.
* **Scoreboard**: Displays the current score at the top of the screen and shows a "GAME OVER" message when the game ends.
* **Game Over Detection**: The game detects when the snake collides with the wall or its own body and ends the game.

---

## Requirements

* Python 3.x
* `turtle` module (usually pre-installed with Python)

---

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/shrabhay/Snake.git
   ```

2. Navigate to the project directory:
    ```shell
    cd Snake
    ```

3. Run the game:
    ```shell
    python3 snake-game.py
    ```

---

## Code Breakdown
### `snake.py`
Defines the `Snake` class, which controls all the snake-related functions, including movement, growing when eating food, and checking for collisions with itself and the walls.

### `food.py`
Defines the `Food` class, which creates food at random positions and allows the snake to eat it. The food is represented by a blue circle.

### `scoreboard.py`
Defines the `Scoreboard` class, which keeps track of the player's score and displays a game-over message when the game ends.

### `snake-game.py`
The main game loop, where the game is initialized and controlled. It listens for keyboard input to control the snake's direction and handles the game’s core logic, including collisions, score updates, and game over conditions.

---

## Contributing
If you would like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Contributions are always welcome!

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
The game is built using Python's built-in turtle graphics library.
Special thanks to the creators of the turtle module for making this possible!
