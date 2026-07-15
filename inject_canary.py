#!/usr/bin/env python3
"""
inject_canary.py — overwrite a single file's content inside a Cowrie
fs.pickle, without needing Cowrie's own codebase installed.

Usage: python3 inject_canary.py <fs.pickle path> <virtual path> <new content file>
Example: python3 inject_canary.py data/fs.pickle /root/.aws/credentials real_creds.txt
"""

import pickle
import sys

A_NAME = 0
A_TYPE = 1
A_CONTENTS = 7
T_FILE = 2


def find_node(tree, virtual_path):
    parts = [p for p in virtual_path.split("/") if p]
    node = tree
    for part in parts:
        children = node[A_CONTENTS]
        if not isinstance(children, list):
            return None
        match = next((c for c in children if c[A_NAME] == part), None)
        if match is None:
            return None
        node = match
    return node


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <fs.pickle> <virtual path> <new content file>")
        sys.exit(1)

    pickle_path, virtual_path, content_path = sys.argv[1:4]

    with open(pickle_path, "rb") as f:
        tree = pickle.load(f)

    node = find_node(tree, virtual_path)
    if node is None:
        print(f"Path not found in pickle: {virtual_path}")
        sys.exit(1)
    if node[A_TYPE] != T_FILE:
        print(f"Path exists but is not a file: {virtual_path}")
        sys.exit(1)

    with open(content_path, "rb") as f:
        new_bytes = f.read()

    node[A_CONTENTS] = new_bytes

    with open(pickle_path, "wb") as f:
        pickle.dump(tree, f)

    print(f"Updated {virtual_path} in {pickle_path} ({len(new_bytes)} bytes)")


if __name__ == "__main__":
    main()
