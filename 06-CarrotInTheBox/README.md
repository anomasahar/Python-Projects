# Carrot-in-the-Box

The **Carrot-in-the-Box** project is a Python-based bluffing game designed for two human players. Each player is given a box, but only one box contains a carrot. The players must use their bluffing skills to decide whether to keep or swap boxes in hopes of ending up with the carrot.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
**Carrot-in-the-Box** is a strategic and interactive game where players try to outwit each other to win a carrot hidden in one of two boxes. One player looks in their box and decides to tell the truth or bluff about whether they have the carrot. The second player must then decide whether to keep their box or swap, aiming to secure the carrot.

## Features
- **Bluffing Gameplay**: Players engage in a fun and strategic bluffing game to win the carrot by swapping or keeping their box.
- **Two-Player Experience**: Supports two human players with turn-based gameplay.
- **Simple and Engaging**: Easy-to-understand rules make it accessible, yet it offers room for strategy and bluffing.
- **Docker Support**: Run the game in a Docker container for easy setup and platform compatibility.
- **Development Container**: Set up a consistent environment using Dev Containers for use with Visual Studio Code.


## Installation
To set up the **Carrot-in-the-Box** game on your local machine, follow these steps:
1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 06-CarrotInTheBox
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Carrot-in-the-Box using Docker, ensure Docker is installed, then use the following commands:
```bash
    docker build -t Carrot-in-the-box
    docker run -it Carrot-in-the-box
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the game and follow the on-screen prompts:

1. The first player will look inside their box and then tell the second player if they have the carrot or not.

2. The second player decides whether to keep their box or swap based on the first player's statement.

3. The game reveals the carrot's location, and the player with the carrot wins the round.

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.