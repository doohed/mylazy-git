# Make the script executable
chmod +x git_automation.py

# Move the script to a directory in your PATH
mkdir -p ~/bin
mv git_automation.py ~/bin/mylazy-git

# Ensure the directory is in your PATH
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

echo "Installation completed successfully."
echo "You can now use the MyLazy Git CLI by typing 'mylazy-git' in your terminal."
