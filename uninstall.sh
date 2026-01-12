#!/usr/bin/env bash

set -Eeuo pipefail
IFS=$'\n\t'
trap 'echo "Error on line $LINENO. Exiting."; exit 1' ERR

INSTALL_DIR="$HOME/.local/bin/golgi_bot_GUI_app"
DESKTOP_FILE="$HOME/.local/share/applications/GolgiBotGUI.desktop"

command -v apt >/dev/null || { echo "apt not found. Debian-based system required."; exit 1; }
for cmd in sudo rm source; do
  command -v "$cmd" >/dev/null || { echo "Required command '$cmd' not found."; exit 1; }
done

DEPENDENCIES=(tk python3-tk python3-venv python3-pandas python3-serial)

echo "Removing installed files..."
[[ -d "$INSTALL_DIR" ]] && { rm -rf "$INSTALL_DIR"; echo "Installed files removed."; } || echo "Install directory not found. Skipping."

echo "Removing .desktop entry..."
[[ -f "$DESKTOP_FILE" ]] && { rm -f "$DESKTOP_FILE"; echo "Application entry removed."; } || echo "Application entry not found. Skipping."

echo "Removing Desktop shortcut..."
DESKTOP_DIR="$(source "$HOME/.config/user-dirs.dirs" && echo "$XDG_DESKTOP_DIR")"
[[ -d "$DESKTOP_DIR" ]] && { rm -f "$DESKTOP_DIR/GolgiBotGUI.desktop"; echo "Desktop shortcut removed."; } || echo "Desktop directory not found. Skipping."

echo "Removing unused dependencies..."
sudo apt -y autoremove

echo "Uninstallation complete."

