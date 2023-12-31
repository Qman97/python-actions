on: [push]

jobs:
  safety:
    runs-on: ubuntu-latest
    name: "safety"
    steps:
      - uses: davidslusser/actions_python_safety@v1.0.0
on: [push]

jobs:
  safety:
    runs-on: ubuntu-latest
    name: "safety"
    steps:
      - uses: davidslusser/actions_python_safety@v1.0.0
        with:
          options: "--debug"
          pip_install_command: "pip install -e .[dev]"
          python_version: "3.9"