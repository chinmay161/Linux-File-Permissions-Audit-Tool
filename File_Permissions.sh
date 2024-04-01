#!/bin/bash

# Check if directory argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

DIRECTORY="$1"

# Function to convert octal permissions to symbolic representation
octal_to_symbolic() {
    local perm=$1
    local symbolic=""

    # Check read permission
    [[ $((perm & 4)) != 0 ]] && symbolic+="r" || symbolic+="-"

    # Check write permission
    [[ $((perm & 2)) != 0 ]] && symbolic+="w" || symbolic+="-"

    # Check execute permission or directory flag
    if [ "$((perm & 1))" != 0 ]; then
        if [ -d "$file" ]; then
            symbolic+="x"
        else
            symbolic+="x"
        fi
    else
        symbolic+="-"
    fi

    echo "$symbolic"
}

# Function to check file permissions for a given user
check_file_permissions() {
    file=$1
    user=$2

    # Check if file exists
    if [ ! -e "$file" ]; then
        echo "File '$file' does not exist."
        return
    fi

    # Get file permissions
    permissions=$(stat -c "%a" "$file")

    # Get owner and group
    owner=$(stat -c "%U" "$file")
    group=$(stat -c "%G" "$file")

    # Check if user is the owner
    if [ "$owner" == "$user" ]; then
        owner_permissions=$(octal_to_symbolic $((permissions / 100)))
        echo "Owner: $owner, Permissions: $owner_permissions"
    fi

    # Check if user is in the file's group
    if groups "$user" | grep -q "\b$group\b"; then
        group_permissions=$(octal_to_symbolic $(((permissions / 10) % 10)))
        echo "Group: $group, Permissions: $group_permissions"
    fi

    # Check others' permissions
    others_permissions=$(octal_to_symbolic $((permissions % 10)))
    echo "Others Permissions: $others_permissions"

    # Check if others have write or execute permissions
    if [ "${others_permissions:1:1}" == "w" ] || [ "${others_permissions:2:1}" == "x" ]; then
        echo "Warning: File has overly permissive permissions."
    fi
}

# Check if directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Directory '$DIRECTORY' does not exist or cannot be accessed."
    exit 1
fi

# List file permissions for all users
echo "File permissions in '$DIRECTORY' for all users:"
for user in $(cut -d: -f1 /etc/passwd); do
    echo "User: $user"
    echo "------------------------"
    find "$DIRECTORY" -type f | while read -r file; do
        echo "File: $file"
        check_file_permissions "$file" "$user"
        echo
    done
    echo
done