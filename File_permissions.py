#!/usr/bin/env python3
import os
import stat
import pwd
import grp
import sys
import argparse

def octal_to_symbolic(perm):
    symbolic = ""

    # Check read permission
    symbolic += "r" if perm & 4 else "-"

    # Check write permission
    symbolic += "w" if perm & 2 else "-"

    # Check execute permission
    symbolic += "x" if perm & 1 else "-"

    return symbolic

def check_file_permissions(file):
    try:
        if not os.path.exists(file):
            return f"File '{file}' does not exist."

        # Get file permissions
        file_stat = os.stat(file)
        permissions = file_stat.st_mode

        # Get owner and group
        owner = pwd.getpwuid(file_stat.st_uid).pw_name
        group = grp.getgrgid(file_stat.st_gid).gr_name

        # Convert permissions to octal
        octal_permissions = oct(permissions)[-3:]

        # Create permissions dictionary
        perms = {
            'owner': octal_to_symbolic(int(octal_permissions[0])),
            'group': octal_to_symbolic(int(octal_permissions[1])),
            'others': octal_to_symbolic(int(octal_permissions[2]))
        }

        # Check if others have write or execute permissions
        warnings = []
        if "w" in perms['others'] or "x" in perms['others']:
            warnings.append("File has overly permissive permissions for others.")

        return {
            'owner': owner,
            'group': group,
            'permissions': perms,
            'warnings': warnings
        }
    except Exception as e:
        return f"Error checking file permissions for '{file}': {e}"

def main(directory):
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist or cannot be accessed.")
        sys.exit(1)

    print(f"File permissions in '{directory}':")
    overly_permissive_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            result = check_file_permissions(file_path)
            if isinstance(result, str):
                print(result)
                continue

            print(f"File: {file_path}")
            print(f"  Owner: {result['owner']}, Permissions: {result['permissions']['owner']}")
            print(f"  Group: {result['group']}, Permissions: {result['permissions']['group']}")
            print(f"  Others Permissions: {result['permissions']['others']}")
            for warning in result['warnings']:
                print(f"  Warning: {warning}")
                overly_permissive_files.append(file_path)
            print()

    if overly_permissive_files:
        print("Summary of overly permissive files:")
        for file in overly_permissive_files:
            print(f"  {file}")
    else:
        print("No overly permissive files found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check file permissions in a directory.")
    parser.add_argument("directory", help="The directory to check.")
    args = parser.parse_args()

    main(args.directory)
