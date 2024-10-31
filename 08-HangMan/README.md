# Hangman Game

**Hangman Game** is a classic word-guessing challenge where players try to reveal a hidden word by guessing letters. Each incorrect guess draws another part of the hangman. Guess the full word before the drawing is complete to win! This version includes animal-themed words (like "RABBIT" and "PIGEON") but can be customized with any word list.



## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Hangman Game** offers a fun and challenging experience as users try to guess a secret word letter by letter. Each incorrect letter guess reveals a new piece of the hangman drawing, creating suspense as the player aims to guess the word before running out of chances.


## Features
- **Word Guessing Challenge**: Guess the letters in a hidden word, one letter at a time.
- **Animal-Themed Words**: The default set of secret words consists of animal names like "RABBIT" and "PIGEON."
- **Hangman Visualization**: A part of the hangman drawing appears with each incorrect guess.
- **Customizable Word List**: Easily replace the default words with your own custom set.
- **Docker Support**: Run the game in a Docker container for ease of setup and compatibility across different platforms.
- **Development Container**: Set up a consistent development environment using Dev Containers for Visual Studio Code.


## Installation
To set up the **Hangman Game** on your local machine, follow these steps:
1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 08-HangMan
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Hangman Game using Docker, ensure Docker is installed, then use the following commands:

```bash
    docker build -t hangman
    docker run -it hangman
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts to guess the letters of a secret word.

1. The program will prompt you to enter a letter.
2. Each correct guess reveals part of the secret word.
3. For each incorrect guess, another part of the hangman is drawn.
4. Continue guessing until you either guess the complete word or the hangman drawing is complete.

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
