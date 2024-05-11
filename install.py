
def make_script_executable(script_path):
        with open(script_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("#!/usr/bin/env python\n" + content)

    # Make the script executable
    os.chmod(script_path, 0o755)

def move_script_to_bin(script_path):
    # Create directory if it doesn't exist
    bin_dir = os.path.expanduser("~/bin")
    os.makedirs(bin_dir, exist_ok=True)

    # Move the script to the bin directory
    shutil.move(script_path, bin_dir)

def add_bin_to_path():
    # Add bin directory to PATH in bashrc/bash_profile
    bashrc_path = os.path.expanduser("~/.bashrc")
    bash_profile_path = os.path.expanduser("~/.bash_profile")
    if os.path.exists(bashrc_path):
        profile_file = bashrc_path
    elif os.path.exists(bash_profile_path):
        profile_file = bash_profile_path
    else:
        print("Could not find .bashrc or .bash_profile")
        return

    with open(profile_file, 'a') as f:
        f.write('\nexport PATH="$HOME/bin:$PATH"\n')

def main():
    script_path = input("Enter the path to your script: ")

    if not os.path.isfile(script_path):
        print("Error: Script file not found.")
        return

    make_script_executable(script_path)
    move_script_to_bin(script_path)
    add_bin_to_path()

    print("Script installed successfully. You can now use it globally.")

if __name__ == "__main__":
    main()
