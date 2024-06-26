#!/usr/bin/env python3
import subprocess
import os

def git_init():
    subprocess.run(["git", "init"])

def git_add():
    subprocess.run(["git", "add", "."])

def git_commit(message):
    subprocess.run(["git", "commit", "-m", message])

def git_branch():
    subprocess.run(["git", "branch", "-M", "main"])

def git_remote_add(remote_url):
    subprocess.run(["git", "remote", "add", "origin", remote_url])

def git_push():
    subprocess.run(["git", "push", "-u", "origin", "main"])

def main():
    print("Welcome to Git Automation CLI")

    # Check if directory is initialized with Git
    if not os.path.exists('.git'):
        print("Initializing Git repository...")
        git_init()

    message = input("Enter commit message: ")
    git_add()
    git_commit(message)

    if not os.path.exists('.git'):
        git_branch()
        remote_url = input("Enter remote URL: ")
        git_remote_add(remote_url) 
    git_push()


if __name__ == "__main__":
   main()

