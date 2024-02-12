import os
from datetime import datetime

class TestSetup:
    @staticmethod
    def create_video_folder(record_video_dir):
        # Get current date
        current_date = datetime.now().strftime("%m-%d-%Y")

        # Create folder with current date
        folder_path = os.path.join(record_video_dir, current_date)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{current_date}' created successfully at '{folder_path}'")
        else:
            print(f"Folder '{current_date}' already exists at '{folder_path}'")
        return folder_path

    @staticmethod
    def create_screenshot_folder(screenshot_dir):
        # Get current date
        current_date = datetime.now().strftime("%m-%d-%Y")

        # Create folder with current date
        folder_path = os.path.join(screenshot_dir, current_date)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{current_date}' created successfully at '{folder_path}'")
        else:
            print(f"Folder '{current_date}' already exists at '{folder_path}'")
        return folder_path

    @staticmethod
    def format_video_filename(test_name):
        # Get current date and time
        current_time = datetime.now().strftime("%H:%M::%S")

        # Replace spaces in test name with underscores
        test_name = test_name.replace(" ", "_")

        # Format the filename
        filename = f"{current_time}-{test_name}.webm"
        return filename
    #
    # @staticmethod
    # def is_object_visible(image_path):
    #     position = pyautogui.locateOnScreen(image_path)
    #
    #     # If object is found (visible), return True
    #     if position:
    #         return True
    #     else:
    #         return False