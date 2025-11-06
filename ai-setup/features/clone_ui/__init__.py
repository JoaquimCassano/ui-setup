from .constants import SYSTEM_PROMPT_CLONE, SYSTEM_PROMPT_CREATE_STYLE_MD
from .tools import get_website_css, get_website_screenshot
from ...ui import ask, prompt_string, show_info
from rich import print as pprint
from ...tools import load_settings

def clone_ui():
  settings = load_settings()
  url = prompt_string("What is the url of the website you want to clone the UI from? ")
  pprint("Good choice! Now, let us work.")
  show_info("Fetching CSS data from the website...")
  css = get_website_css(url)
  show_info("Getting a screenshot from the website...")
  path = get_website_screenshot(url)
  show_info("Done! Now, cloning it with your AI tool.", 'success')
  if settings['developer']:
    additional_instructions = prompt_string("Add here additional instructions we should give to the LLM, such as specific stack to use, best practices etc. (Optional)")
  final_prompt = SYSTEM_PROMPT_CLONE.format(css)+additional_instructions


if __name__ == "__main__":
  clone_ui()