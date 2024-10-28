# Calculator Project

Welcome to the Calculator Project! This is a simple command-line calculator built using Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Calculator is designed to demonstrate basic programming concepts, including functions, user input handling, and control flow. It provides an interactive interface for users to perform calculations quickly and easily. This project serves as a foundation for beginners to understand how to implement logic and handle user input in Python.

## Features
- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **User-Friendly Interface**: Simple command-line interface for easy interaction.
- **Error Handling**: Handles invalid input gracefully to improve user experience.
- **Continuous Operation**: Allows users to perform multiple calculations without restarting the program.
- **Docker Support**: Easily deploy the calculator in a containerized environment using Docker.
- **Development Container**: A Dev Container configuration is provided for a consistent development environment.

## Installation
To set up the Calculator on your local machine, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anomasahar/Python-Projects.git
   ```

2. **Navigate into the Project Directory**:
    ```bash
    cd 01-Calculator
    ```

3. **Run the Project**
    ```bash
    python main.py
    ```

## Running with Docker
To run the calculator using Docker, ensure you have Docker installed, then use the following command:
```bash
    docker build -t calculator
    docker run -it calculator
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Once the calculator is running, follow the on-screen prompts to enter numbers and select the desired operation. The results will be displayed immediately after the calculation. To perform another calculation, simply follow the prompts again without needing to restart the program. 

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.