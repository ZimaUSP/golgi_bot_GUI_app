#!/usr/bin/env bash

INSTALL_DIR=$HOME/.local/bin/golgi_bot_GUI_app

# There are currently no verifications whatsoever!
# Should add more verifications!

echo "Removing dependencies..."
sudo apt -y remove tk python3-tk python3-venv python3-pandas python3-serial
sudo apt -y autoremove
echo "Done removing dependencies!"

echo "Removing installed files..."
rm -rf $INSTALL_DIR
echo "Done removing installed files!"

echo "Removing .desktop entry..."
rm -rf "$HOME/.local/share/applications/GolgiBotGUI.desktop"
echo "Done removing .desktop entry!"

echo "Removing Desktop Shortcut"
DESKTOP_DIR="$(source $HOME/.config/user-dirs.dirs && echo $XDG_DESKTOP_DIR)"
rm -rf "$DESKTOP_DIR/GolgiBotGUI.desktop"
echo "Done removing Desktop Shortcut!"

echo "Done uninstalling!"
