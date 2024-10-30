# Encryption Project

The **Encryption Project** is a Python-based program that lets users encrypt and decrypt messages by shifting letters in the alphabet. This ancient encryption method, used by Julius Caesar, shifts each letter over by a specified key. For example, with a key of 3, A becomes D, B becomes E, etc. This program allows for easy message encryption and decryption.



## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Running with Docker](#running-with-docker)
- [Using the Development Container](#using-the-development-container)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The **Encryption Project** is a Python program that lets users encrypt and decrypt messages based on the Encryption. It’s a simple yet powerful demonstration of text-based encryption using a key to shift letters within the alphabet.


## Features
- **Encryption and Decryption**: Encrypt messages by shifting letters a specified number of places, then decrypt them by shifting back.
- **Customizable Shift Key**: Users can specify any number for the shift, allowing flexible encryption.
- **Docker Support**: Run the project in a containerized environment with Docker for easy setup.
- **Development Container**: Set up a consistent environment with a Dev Container configuration for use in VS Code.

## Installation
To set up the Encryption Project on your local machine, follow these steps:
1. **Clone the Repository**:
   
    ```bash
    git clone https://github.com/anomasahar/Python-Projects.git
    ```

2. **Navigate into the Project Directory**:

    ```bash
    cd 05-Encryption
    ```

3. **Run the Project**:
    
    ```bash
    python main.py
    ```

## Running with Docker
To run the Encryption Project using Docker, ensure Docker is installed, then use the following commands:
```bash
    docker build -t blackjack-game
    docker run -it blackjack-game
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and follow the prompts to either encrypt or decrypt a message. Enter the shift key, and the program will transform your message accordingly.


## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.