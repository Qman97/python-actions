on: [push]

jobs:
  safety:
    runs-on: ubuntu-latest
    name: "isort"
    steps:
      - uses: davidslusser/actions_python_isort@v1.0.0
on: [push]

jobs:
  safety:
    runs-on: ubuntu-latest
    name: "isort"
    steps:
      - uses: davidslusser/actions_python_isort@v1.0.0
        with:
          options: "--check --diff"
          pip_install_command: "pip install -e .[dev]"
          python_version: "3.9"