# Math Quiz with Dice

The **Math Quiz** program generates a quick-paced arithmetic challenge where players add up the numbers rolled on two to six dice. The dice are displayed as ASCII art at random positions on the screen, adding a fun, visual twist to the game.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Math Quiz** is more than just a flash card app; it rolls two to six dice, and players must add the dice values as quickly as possible. Each dice roll is drawn with ASCII art at random places on the screen, adding a visual twist that makes math practice engaging and interactive.


## Features
- **Dice Roll Simulation**: Rolls between two and six dice per game.
- **Timed Challenge**: Encourages quick mental math as you add the dice values.
- **ASCII Art Display**: Draws dice faces at random positions, making each round unique.
- **Interactive Gameplay**: Designed to be both a math quiz and visual game.


## Installation
To set up the **Math Quiz** project on your local machine, follow these steps:

1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 10-DiceMath
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Math Quiz simulation using Docker, ensure Docker is installed, then use the following commands:

```bash
    docker build -t dice-math
    docker run -it dice-math
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts:

1. The program will roll between two and six dice.
2. Add the numbers shown on the dice and enter your answer as quickly as possible.
3. Check your result and try to beat your best time!

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

