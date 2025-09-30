# ttrpg-copilot
A homemade copilot that would help a group of geeks navigating faster across all the rules out there.

## Jupyter test setup
Add the following into your Jupyter Command Line Arguments settings file: 
    "jupyter.runStartupCommands": [
        "import os, sys",
        "from pathlib import Path",
        "os.environ['API_KEY'] = '---'",
        "sys.path.append(str(Path().absolute().parent))",
        "%load_ext autoreload",
        "%autoreload 2"
    ]
