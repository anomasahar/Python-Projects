# Factorization Program

The **Factorization Program** is a Python-based tool that allows users to enter a positive whole number and receive its factors. It also determines whether the number is prime or composite based on the factors found.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Factorization Program** is a simple yet powerful utility that helps users identify the factors of a given number. Users can enter a positive whole number, and the program will display all factors, as well as indicating whether the number is prime (only two factors) or composite (more than two factors).

## Features
- **Factor Identification**: Calculates and displays all factors of the given number.
- **Prime and Composite Detection**: Informs the user whether the number is prime or composite based on the factors found.
- **User Input Validation**: Ensures only valid positive whole numbers are accepted.
- **Docker Support**: Run the program in a Docker container for easy setup and compatibility across different platforms.
- **Development Container**: Set up a consistent development environment using Dev Containers for Visual Studio Code.

## Installation
To set up the **Factorization Program** on your local machine, follow these steps:
1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 07-Factorization
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Factorization Program using Docker, ensure Docker is installed, then use the following commands:
```bash
    docker build -t factorization
    docker run -it factorization
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts to enter a positive whole number. The program will then display its factors and indicate whether the number is prime or composite.

1. Enter a positive whole number to factor.
2. The program will display all factors and state if the number is prime or composite.

## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

