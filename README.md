# Image Service Microservice Project

## Overview

This project demonstrates a simple microservice architecture using Python, where different services communicate through text files. The main components of the project include a random number generator service (`prng.py`), an image service (`imgsrv.py`), and a user interface (`ui.py`). The services work together to generate a random number, select an image based on that number, and display the image.

## Project Structure
/your_project_directory/
├── imgsrv.py # Image service that selects and displays images
├── prng.py # Pseudo-random number generator service
├── ui.py # User interface for interacting with the services
├── dog-images/ # Directory containing image files
│ ├── 0.jpg
│ ├── 1.jpg
│ ├── 2.jpg
│ └── ... # Other images
├── image-service.txt # File used by the image service to read the selected index
└── prng-service.txt # File used by the random number generator service


## Components

### 1. Random Number Generator (`prng.py`)

- **Functionality:** Generates a random number between 0 and 999 when the command "run" is written to `prng-service.txt`.
- **Communication:** Writes the generated number to `image-service.txt`, which is used by the image service.

### 2. Image Service (`imgsrv.py`)

- **Functionality:** Reads the random number from `image-service.txt`, selects an image from the `dog-images` directory based on that number, and opens the image in the default viewer.
- **Full-Screen Display:** On macOS, it uses AppleScript to open the image in Preview and enter full-screen mode.

### 3. User Interface (`ui.py`)

- **Functionality:** Provides a command-line interface for the user to generate a new image or exit the application.
- **User Interaction:** Prompts the user to enter '1' to generate a new image or '2' to exit.

## Usage

1. **Setup:**
   - Ensure you have Python installed on your machine.
   - Create a directory named `dog-images` and place your image files (e.g., `.jpg`, `.jpeg`, `.png`) inside it.

2. **Run the Services:**
   - Open a terminal and run the random number generator service:
     ```bash
     python prng.py
     ```
   - In another terminal, run the image service:
     ```bash
     python imgsrv.py
     ```
   - In a third terminal, run the user interface:
     ```bash
     python ui.py
     ```

3. **Interacting with the Application:**
   - When prompted in the user interface, enter `1` to generate a new image. The application will generate a random number, select an image based on that number, and display it.
   - Enter `2` to exit the application.

## Notes

- The project uses text files for communication between services, which is a simple way to demonstrate microservice architecture.
- Ensure that the `prng-service.txt` file contains the string "run" to generate a new random number.
- The image service will only display a new image if the generated number is different from the last one displayed.

## Conclusion

This project serves as a basic example of how microservices can communicate through text files in Python. It can be extended further by adding more features, such as error handling, logging, or a web interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.