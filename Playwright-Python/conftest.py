import playwright
import pytest
from pom.common.testsetup import TestSetup


@pytest.fixture(scope="function")
def set_up(browser):
    # --Start Test-------------------
    # browser = playwright.chromium.launch(headless=False)  # slow_mo=500 if you need to slowdown
    record_video_dir = "../results/videos/nintendo/"
    folder_path = TestSetup.create_date_folder(record_video_dir)

    # Set the directory for video recording
    context = browser.new_context(record_video_dir=folder_path)

    page = context.new_page()
    page.goto("https://www.nintendo.com/us/")

    yield page
    page.close()