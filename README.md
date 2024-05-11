# Git Automation CLI

This command-line tool automates common Git commands to simplify your workflow.

## Features

- Initializes Git repository if not already initialized.
- Automatically adds files, commits changes, sets up the main branch, adds remote origin, and pushes changes.
- Asks for a commit message to provide context for the changes.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/git-automation-cli.git
   ```

2. Navigate to the project directory:

   ```bash
   cd git-automation-cli
   ```

3. Make the script executable:

   ```bash
   chmod +x git_automation.py
   ```

4. Move the script to a directory in your PATH (e.g., ~/bin or ~/.local/bin):

   ```bash
   mv git_automation.py ~/bin/git_automation
   ```

5. Ensure the directory is in your PATH by adding the following line to your `~/.bashrc` or `~/.bash_profile`:
   ```bash
   export PATH="$HOME/bin:$PATH"
   ```

## Usage

To use the Git Automation CLI, simply run the `git_automation` command in your terminal:

```bash
git_automation
```

Follow the prompts to provide a commit message and, if required, the remote URL.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/yourusername/git-automation-cli/issues) or [create a pull request](https://github.com/yourusername/git-automation-cli/pulls).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the content to better fit your project and add any additional sections or information you think would be helpful.