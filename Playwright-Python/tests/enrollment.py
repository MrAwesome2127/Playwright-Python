import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.skip(reason="in-progress")
def test_create_account(playwright: Playwright) -> None:
    # --Start Test-------------------
    browser = playwright.chromium.launch(headless=False)  # slow_mo=500 if you need to slowdown
    context = browser.new_context(
        record_video_dir="../results/videos/nintendo/")
    page = context.new_page()

    # --Landing Page-------------------
    page.goto("https://www.nintendo.com/us/")