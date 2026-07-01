# TBCards
A free and open-source python library that provides tools for creating text-based card games.

# Installation

Installation instructions for users are coming soon!

## Development
All commands assume a Linux-like command line.

1. Obtain the repo from github
```
git clone https://github.com/epsilonemae/TBCards
```

2. Create a Python virtual environment
```
cd TBCards
python3 -m venv .venv
```

3. Activate the virtual environment
```
source .venv/bin/activate
```

4. Install the development dependencies
```
pip install ".[dev]"
```

5. Editable install the repo
```
pip install -e .
```

You can then test the repo by running
```
pytest
```