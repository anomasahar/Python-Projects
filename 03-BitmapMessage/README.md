# Bitmap Message Project

Welcome to the **Bitmap Message Project**! This project is a unique way to display custom messages by using a bitmap, a 2D image with only two possible colors for each pixel, in the console. The program replaces specific characters in a multiline string bitmap with the user’s input message, creating a pixelated, graphical representation of the text.

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
The **Bitmap Message Project** is a Python program that displays user messages in a pixelated style based on a 2D bitmap template. Spaces remain blank, while other characters are replaced by the user’s input, creating a unique text-based image.


## Features
- **Multiline Bitmap**: Uses a customizable 2D bitmap string to control how the message is displayed.
- **User-Defined Messages**: Users can input any message they like, which will be rendered in the bitmap.
- **Binary Pixel Representation**: Simple system where each pixel is either blank or filled with a character from the message.
- **Docker Support**: Easily run the project in a containerized environment with Docker.
- **Development Container**: Set up a consistent environment with a Dev Container configuration for use in VS Code.

## Installation
To set up the Bitmap Message Project on your local machine, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anomasahar/Python-Projects.git
   ```

2. **Navigate into the Project Directory**:
    ```bash
    cd 03-BitmapMessage
    ```

3. **Run the Project**
    ```bash
    python main.py
    ```

## Running with Docker
To run the Bitmap Message Project using Docker, ensure Docker is installed, then use the following commands:
```bash
    docker build -t bitmap-message
    docker run -it bitmap-message
```

## Using the Development Container
If you're using Visual Studio Code with the Remote - Containers extension, you can open this project in a Dev Container for a consistent development environment. Simply open the project folder and select the option to reopen in a container.


## Usage
Run the program and enter a message when prompted. The message will display in a pixelated style according to the bitmap pattern, with spaces left blank and other characters replaced by your input.


## Contributing
Contributions to this repository are welcome! Here are some general ways you can contribute:

- **Bug Reports**: If you find any bugs or issues, please report them in the Issues section.
- **Feature Requests**: Suggestions for new features or improvements are appreciated.

## License
This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.