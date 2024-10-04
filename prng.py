import random
import time

class RandomNumber:
    """
    Class to generate a random number if prng-service reads 'run'
    """
    def read_prng(self):
        """
        Reads prng service text file
        """
        with open("prng-service.txt", "r") as file:
            return file.read().strip()

    def clear_prng(self):
        """
        Clears the contents of prng service text file
        """
        with open("prng-service.txt", "w") as file:
            file.write('')

    def generate_random_int(self):
        """
        Generates a random number
        """
        return random.randrange(0, 1000)

    def write_num(self):
        """
        Writes a random number to prng service if 'run' is found
        """
        prng_command = self.read_prng()
        if prng_command == 'run':
            self.clear_prng()  # Clear the file before writing the number
            random_number = str(self.generate_random_int())
            with open("prng-service.txt", "w") as file:
                file.write(random_number)

            # Write the random number to image-service.txt
            with open("image-service.txt", "w") as file:
                file.write(random_number)

            time.sleep(5)
        elif prng_command == '':
            print("prng-service.txt is empty. Please add 'run' to the file.")
        else:
            self.clear_prng()  # Clear the file if no valid command
            print("prng-service.txt does not contain the string 'run'")


if __name__ == "__main__":
    random_number_service = RandomNumber()
    while True:
        random_number_service.write_num()
        time.sleep(1)  # Add a delay to prevent busy-waiting
