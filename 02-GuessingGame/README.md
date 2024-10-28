# Number Guessing Game Project

Welcome to the **Number Guessing Game Project**! This is a simple command-line game built using Python, where users try to guess a randomly generated number within a set range.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Number Guessing Game** demonstrates fundamental programming concepts, such as loops, user input handling, and control flow. This interactive game tests players' logic and luck by challenging them to guess a randomly generated number. This project is a great starting point for beginners learning about randomness and user interaction in Python.

## Features
- **Random Number Generation**: The game generates a random number within a specified range for the user to guess.
- **Guess Tracking**: Tracks the number of guesses taken to arrive at the correct answer.
- **User-Friendly Interface**: Simple command-line interface for easy interaction.
- **Error Handling**: Gracefully manages invalid input to enhance user experience.
- **Continuous Play Option**: Allows users to play multiple rounds without restarting the program.
- **Docker Support**: Easily run the game in a containerized environment using Docker.
- **Development Container**: Dev Container configuration for a consistent development setup.

## Installation
To set up the Number Guessing Game on your local machine, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anomasahar/Python-Projects.git
   ```

2. **Navigate into the Project Directory**:
    ```bash
    cd 02-GuessingGame
    ```

3. **Run the Project**
    ```bash
    python main.py
    ```

## Running with Docker
To run the calculator using Docker, ensure you have Docker installed, then use the following command:
```bash
    docker build -t guessing-game
    docker run -it guessing-game
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Once the game is running, follow the on-screen prompts to enter your guess for the randomly generated number. The program will let you know if your guess is too high or too low, helping you zero in on the correct answer. You can play additional rounds by following the prompts without restarting the game.

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.