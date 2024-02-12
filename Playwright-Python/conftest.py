import playwright
import pytest
from pom.common import passed
from pom.common.testsetup import TestSetup


@pytest.fixture(scope='function') # session - Keeps test running on the same window
def set_up(playwright):
    # --Start Test-------------------
    browser = playwright.chromium.launch(headless=True)  # slow_mo=500 if you need to slowdown
    record_video_dir = "../results/videos/nintendo/"
    # screenshot_dir = "../results/screenshots/nintendo/"
    video_folder_path = TestSetup.create_video_folder(record_video_dir)
    # screenshot_folder_path = TestSetup.create_screenshot_folder(screenshot_dir)

    # Set the directory for video recording
    context = browser.new_context(
        record_video_dir=video_folder_path)

    page = context.new_page()
    page.goto("https://www.nintendo.com/us/")

    yield page
    browser.close()

    # --End Test-------------------
    passed.Passed_Test.print_nintendo_logo()
