import openai
import requests, tempfile
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from ..tools import load_settings
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_website_css(url:str) -> str:
    response = requests.get(url)
    logger.debug(f"Fetching CSS from {url}")
    if response.status_code == 200:
        html = BeautifulSoup(response.content, 'html.parser')
        styles = html.find_all('link', rel='stylesheet')
        css_content = ""
        for style in styles:
            logger.debug(f"Found stylesheet: {style['href']}")
            css_url = style['href']
            if not css_url.startswith('http'):
                css_url = url + css_url
            css_response = requests.get(css_url)
            if css_response.status_code == 200:
                css_content += css_response.text + "\n"
        logger.debug("Successfully retrieved CSS content")
        logger.debug(css_content)
        return css_content
    else:
        raise Exception(f"Failed to retrieve CSS from {url}")

def get_website_screenshot(url:str) -> str:
    """
    Takes a screenshot of the given website URL.
    Arguments:
        url (str): The URL of the website to screenshot.
    Returns:
        str: The file path to the screenshot image (temporary file).
    """
    settings = load_settings()
    with sync_playwright() as p:
        logger.debug(f"Launching browser for screenshot: {url}")
        browser = p.chromium.launch(executable_path=settings.get("browser_path"), headless=True)
        page = browser.new_page()
        page.goto(url)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
            screenshot_path = tmpfile.name
            logger.debug(f"Taking screenshot and saving to: {screenshot_path}")
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()
    return screenshot_path