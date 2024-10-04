import os
import subprocess
import platform
import time

class ImageService:
    """
    Service to handle image selection based on an index.
    """
    
    def __init__(self):
        self.last_image_path = None  # Store the last selected image path

    def read_image_service(self):
        """
        Reads the image service text file.
        """
        with open("image-service.txt", "r") as file:
            return file.read().strip()

    def clear_image_service(self):
        """
        Clears the contents of the image service text file.
        """
        with open("image-service.txt", "w") as file:
            file.write('')

    def find_total_images(self):
        """
        Find the total number of images in the directory.
        """
        return len(self.image_list())

    def find_index(self):
        """
        Use modulus to avoid index out of bounds and find the appropriate index.
        """
        service_value = self.read_image_service()
        
        if not service_value:
            raise ValueError("Image service file is empty.")
        
        if not service_value.isdigit():
            raise ValueError(f"Invalid value in image service file: {service_value}")

        # Calculate the index
        index = int(service_value) % self.find_total_images()
        return index

    def image_list(self):
        """
        Generate a list of image paths.
        """
        path = "dog-images"
        # Define valid image extensions
        valid_extensions = ('.jpg', '.jpeg', '.png')
        images = [f for f in os.listdir(path) if f.lower().endswith(valid_extensions)]
        return images

    def image_path(self):
        """
        Define the selected image path and return it along with the file object.
        """
        try:
            index = self.find_index()
            image = self.image_list()[index]
            image_path = f"dog-images/{image}"
            if os.path.exists(image_path):
                print(f"Selected image path: {image_path}")
                if self.last_image_path != image_path:
                    self.last_image_path = image_path  # Update the last image path
                    # Open the image in the default viewer
                    if platform.system() == "Windows":
                        os.startfile(image_path)
                    elif platform.system() == "Darwin":  # macOS
                        # Use AppleScript to open the image in Preview and enter full-screen mode
                        # script = f'''
                        # tell application "Preview"
                        #     activate
                        #     open "{image_path}"
                        #     delay 0.5
                        #     tell application "System Events"
                        #         keystroke "f" using {{control down, command down}}  -- Enter full screen
                        #     end tell
                        # end tell
                        # '''
                        # subprocess.run(['osascript', '-e', script])
                        subprocess.run(['open', image_path])
                    else:  # Linux
                        subprocess.call(["xdg-open", image_path])
                else:
                    print("The same image is already opened.")
                return image_path, open(image_path, 'rb')  # Return the path and file object
            else:
                raise FileNotFoundError(f"Image {image} not found in path {image_path}.")
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    image_service = ImageService()
    while True:  # Keep running to simulate microservice behavior
        path, file_obj = image_service.image_path()
        file_obj.close()
        time.sleep(1)  # Delay to prevent busy-waiting