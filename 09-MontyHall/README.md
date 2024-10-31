# Monty Hall Problem

The **Monty Hall Problem** is a probability puzzle inspired by *Let’s Make a Deal*. The player chooses one of three doors, with a car behind one and goats behind the others. After choosing, the host reveals a goat behind a remaining door. The player then decides whether to stick with their choice or switch to the other unopened door. This simulation shows why switching statistically increases the chances of winning.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Monty Hall Problem** is a famous example of counterintuitive probability, where switching doors statistically increases the chances of winning the prize. This project simulates the problem, allowing players to observe the probability outcomes by choosing to either stick with or switch their initial choice.

## Features
- **Probability Simulation**: Run simulations to observe outcomes based on switching or staying with the initial door choice.
- **Interactive Gameplay**: Players can choose doors and decide whether to stick or switch.
- **Statistics Display**: See the statistical probability of winning by switching or staying.
- **Docker Support**: Run the simulation in a Docker container for compatibility across different systems.
- **Development Container**: Use Dev Containers for Visual Studio Code to ensure a consistent development environment.

## Installation
To set up the **Monty Hall Problem** project on your local machine, follow these steps:

1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 09-MontyHall
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Monty Hall Problem simulation using Docker, ensure Docker is installed, then use the following commands:

```bash
    docker build -t monty-hall
    docker run -it monty-hall
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts:

1. Select a door (1, 2, or 3) as your initial choice.
2. The host will open one of the remaining doors, revealing a goat.
3. Decide whether to stay with your original choice or switch to the other unopened door.
4. Observe the outcome and learn about the probability implications of your choice.

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.