from .features.clone_ui import clone_ui
from .tools import load_settings
from .ui import show_title, show_info
from .onboarding import onboard
show_title()

try:
  load_settings()
except FileNotFoundError:
  show_info("Looks like it's your first time here. Welcome!", "info")
  onboard()
  show_title()
clone_ui()