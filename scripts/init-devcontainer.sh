#!/bin/bash -xe

sudo apt update

# SQLite
sudo apt install -y --no-install-recommends postgresql-client

# Completion
sudo apt install --no-install-recommends bash-completion
mkdir -p ~/.local/share/bash-completion/completions
pipx install argcomplete

# pipx
echo 'eval "$(register-python-argcomplete pipx)"' > ~/.local/share/bash-completion/completions/pipx

# Poetry
pipx install poetry
echo 'eval "$(poetry completions bash)"' > ~/.local/share/bash-completion/completions/poetry
poetry config virtualenvs.in-project true
poetry install --sync
