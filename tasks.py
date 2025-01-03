from invoke import task
from invoke.context import Context
import shutil
from pathlib import Path

import datetime as dt

@task
def generate(c: Context, n: int):
    """
    Create a new Python file from template.py with the given number.
    Usage: invoke create --number=1
    """
    template_path = Path("template.py")
    new_file_path = Path(f"{n}.py")
    
    # Check if target file already exists
    if new_file_path.exists():
        print(f"Error: {new_file_path} already exists")
        return
        
    # Copy the template to new file
    shutil.copy2(template_path, new_file_path)
    print(f"Created {new_file_path} from {template_path}")



@task
def pb(c: Context):
    """Adds all, commits and pushes"""
    current_branch = c.run("git branch --show-current").stdout.strip()
    print(f"{current_branch=}")

@task
def acp(c: Context, m: str):
    """Adds all, commits and pushes"""

    current_branch = c.run("git branch --show-current").stdout.strip()

    remote_branches = [b.strip().split("/")[1] for b in c.run("git branch -r").stdout.strip().split("\n")]

    if current_branch in remote_branches:
        print(f"HERE")
        c.run(f'git add --all && git commit -m "{m}" && git push')
    else:
        print(f"OVER HERE")
        c.run(f'git add --all && git commit -m "{m}" && git push --set-upstream origin {current_branch}')

    # print(current_branch)
    # print(type(current_branch))

    # print(type(remote_branches))
    # print(len(remote_branches))
    # print(remote_branches)
    # try:
    # except Exception as e:
    #     print(f"ERROR: ")
