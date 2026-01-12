#!/usr/bin/env bash

CURRENT_DIR=$(pwd)
INSTALL_DIR=$HOME/.local/bin/golgi_bot_GUI_app

# There are currently no verifications whatsoever!
# Should add more verifications!

echo "Installing dependencies..."
sudo apt -y install tk python3-tk python3-venv python3-pandas python3-serial
python3 -m venv venv
source venv/bin/activate
python3 -m pip install customtkinter
sed -i 's/false/true/g' venv/pyvenv.cfg
echo "Done installing dependencies!"

echo "Copying files to $INSTALL_DIR..."
mkdir -p $HOME/.local/bin
cp -r $CURRENT_DIR $INSTALL_DIR
cp $CURRENT_DIR/GolgiBotGUIBase.desktop $INSTALL_DIR/GolgiBotGUI.desktop
echo "Done copying!"

echo "Generating .desktop entry..."
echo "Path=$INSTALL_DIR" >> $INSTALL_DIR/GolgiBotGUI.desktop
echo "Exec=$INSTALL_DIR/golgibotgui" >> $INSTALL_DIR/GolgiBotGUI.desktop
echo "Icon=$INSTALL_DIR/images/logo-gradient.png" >> $INSTALL_DIR/GolgiBotGUI.desktop
mkdir -p $HOME/.local/share/applications/
ln -s $INSTALL_DIR/GolgiBotGUI.desktop $HOME/.local/share/applications/
echo "Done generating .desktop entry!"

echo "Creating Desktop Shortcut"
DESKTOP_DIR="$(source $HOME/.config/user-dirs.dirs && echo $XDG_DESKTOP_DIR)"
ln -s $INSTALL_DIR/GolgiBotGUI.desktop "$DESKTOP_DIR"
echo "Done creating Desktop Shortcut!"

echo "Done installing!"

