# Blackjack Game Project

Welcome to the **Blackjack Game Project**! This project is a fun way to play Blackjack, also known as 21, directly in the console using ASCII art to represent the cards. The goal is for players to get as close to 21 points as possible without exceeding it. The program uses images drawn with text characters, making it both a visual and interactive experience.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Blackjack Game Project** is a Python program that allows users to play Blackjack through a console-based interface. Using ASCII art, the game visually represents each card, creating an engaging text-based gaming experience.

## Features
- **Card Game Mechanics**: Classic Blackjack rules where the objective is to reach 21 points without going over.
- **ASCII Art Representation**: Uses American Standard Code for Information Interchange (ASCII) art to visually display the playing cards in the console.
- **User Interaction**: Players can decide to "hit" or "stand" based on their current score.
- **Docker Support**: Easily run the project in a containerized environment with Docker.
- **Development Container**: Set up a consistent environment with a Dev Container configuration for use in VS Code.

## Installation
To set up the Blackjack Game Project on your local machine, follow these steps:
1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 04-CardsGame
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Blackjack Game Project using Docker, ensure Docker is installed, then use the following commands:
```bash
    docker build -t blackjack-game
    docker run -it blackjack-game
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts to play Blackjack. Use the options to "hit" or "stand" as you try to reach 21 points without exceeding it. The cards are displayed in ASCII art for an engaging console experience.


## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.