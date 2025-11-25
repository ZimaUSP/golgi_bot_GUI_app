#!/usr/bin/env bash

install_dir="$HOME/.local/bin/golgi_bot_GUI_app"

source "$install_dir/venv/bin/activate"
cd $install_dir
python3 $install_dir/golgi_main.py
