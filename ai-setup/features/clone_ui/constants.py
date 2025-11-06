SYSTEM_PROMPT_CLONE = """
Help me rebuild that exact same UI design in a single html file as website.html, below is extracted CSS. Ensure you use the exact same colors and fonts as the original website:
{}


"""

SYSTEM_PROMPT_CREATE_STYLE_MD = """
Great, now help me generate a detailed style guide

In style guide, you must include the following part:
- Overview

- Color pallette

- Typography (Pay attention to font weight, font size and how different fonts have been used
together in the project)

- Spacing System

In style guide, you must include the following part:
- Overview

- Color pallette

- Typography (Pay attention to font weight, font size and how different fonts have been used
together in the project)

- Spacing System

- Component Styles

- Shadows & Elevation

- Animations & Transitions

- Border Radius

- Opacity & Transparency

- Common Tailwind CSS Usage in Project

— Example component reference design code

- And so on...

In a word, Give detailed analysis and descriptions to the project style system, and don't miss any
important details.
"""