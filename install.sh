#!/usr/bin/env bash

set -Eeuo pipefail
IFS=$'\n\t'
trap 'echo "❌ Error on line $LINENO. Exiting."; exit 1' ERR

CURRENT_DIR="$(pwd)"
INSTALL_DIR="$HOME/.local/bin/golgi_bot_GUI_app"
DESKTOP_FILE="$INSTALL_DIR/GolgiBotGUI.desktop"
APPLICATIONS_DIR="$HOME/.local/share/applications"

command -v apt >/dev/null || { echo "apt not found. Debian-based system required."; exit 1; }
for cmd in python3 sudo sed ln cp mkdir; do
  command -v "$cmd" >/dev/null || { echo "Required command '$cmd' not found."; exit 1; }
done
[[ -d "$CURRENT_DIR" ]] || { echo "Current directory does not exist."; exit 1; }

DEPENDENCIES=(tk python3-tk python3-venv python3-pandas python3-serial python3-pil.imagetk)

echo "Installing dependencies..."
sudo apt update
sudo apt -y install --no-install-recommends "${DEPENDENCIES[@]}"
sudo apt-mark auto "${DEPENDENCIES[@]}"

python3 -m venv venv
[[ -f "venv/bin/activate" ]] || { echo "Virtual environment creation failed."; exit 1; }

source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install customtkinter

python3 - <<EOF
import customtkinter
EOF

sed -i 's/false/true/g' venv/pyvenv.cfg
echo "Dependencies installed."

echo "Copying files to $INSTALL_DIR..."
[[ -d "$INSTALL_DIR" ]] && { echo "Existing installation found. Overwriting."; rm -rf "$INSTALL_DIR"; }
mkdir -p "$HOME/.local/bin"
cp -r "$CURRENT_DIR" "$INSTALL_DIR"
[[ -d "$INSTALL_DIR" ]] || { echo "Application files were not copied correctly."; exit 1; }

echo "Generating .desktop entry..."
cp "$CURRENT_DIR/GolgiBotGUIBase.desktop" "$DESKTOP_FILE"
cat >> "$DESKTOP_FILE" <<EOF
Path=$INSTALL_DIR
Exec=$INSTALL_DIR/golgibotgui
Icon=$INSTALL_DIR/images/logo-gradient.png
EOF
[[ -f "$DESKTOP_FILE" ]] || { echo "Desktop file creation failed."; exit 1; }

mkdir -p "$APPLICATIONS_DIR"
ln -sf "$DESKTOP_FILE" "$APPLICATIONS_DIR/GolgiBotGUI.desktop"

echo "Creating Desktop shortcut..."
DESKTOP_DIR="$(source "$HOME/.config/user-dirs.dirs" && echo "$XDG_DESKTOP_DIR")"
[[ -d "$DESKTOP_DIR" ]] || { echo "Desktop directory not found."; exit 1; }
ln -sf "$DESKTOP_FILE" "$DESKTOP_DIR/GolgiBotGUI.desktop"

echo "Installation complete!"
echo "Run with: $INSTALL_DIR/golgibotgui"

