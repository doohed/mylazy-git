#!/bin/bash

# Check if a Python script file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <python_script>"
    exit 1
fi

# Assign the provided Python script file to a variable
script_file="$1"

# Check if the provided file exists
if [ ! -f "$script_file" ]; then
    echo "Error: File '$script_file' not found."
    exit 1
fi

# Add a shebang line if it doesn't exist
if ! head -n 1 "$script_file" | grep -q "^#!/"; then
    echo "#!/usr/bin/env python3" | cat - "$script_file" > temp && mv temp "$script_file"
fi

# Make the script executable
chmod +x "$script_file"

# Move the script to /usr/local/bin directory
sudo mv "$script_file" /usr/local/bin

echo "Script '$script_file' has been made executable globally."

