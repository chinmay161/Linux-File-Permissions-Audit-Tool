# Linux-File-Permissions-Audit-Tool

## Objective

The primary objective of this project is to develop a comprehensive and user-friendly tool that enables system administrators, security professionals, and IT personnel to audit, analyze, and report file permissions across Linux systems efficiently. This project aims to enhance cybersecurity posture by identifying misconfigured or overly permissive file access rights that could potentially lead to security vulnerabilities, data breaches, or compliance issues.

## Skills Learned

1. **Linux System Administration:**
   - Deepened understanding of Linux file systems, user and group management, and the intricacies of Linux permissions (read, write, execute for user, group, and others).
   - Gained proficiency in managing and navigating the Linux command line interface and utilizing system administration tools.

2. **Scripting and Automation:**
   - Developed advanced Bash scripting skills to automate the process of file permissions auditing.
   - Learned to write clean, efficient, and reusable scripts that perform complex tasks with minimal user input.

3. **Cybersecurity Fundamentals:**
   - Acquired knowledge about the importance of file permissions in cybersecurity and how improper configurations can lead to vulnerabilities.
   - Understood the principle of least privilege and its application in securing Linux environments.

4. **Vulnerability Assessment:**
   - Learned how to identify and assess security vulnerabilities related to file permissions.
   - Gained insights into common security pitfalls in Unix/Linux systems and how to avoid them.

5. **Compliance and Best Practices:**
   - Familiarized with information security standards and compliance requirements relevant to file permissions and access controls.
   - Learned how to audit systems for compliance with security best practices and regulatory standards.

### Tools Used
This project primarily utilizes Bash scripting along with standard Linux command-line tools to audit file permissions. Here are the main tools and technologies used in the project:

1. **Bash Scripting:** Bash (Bourne Again Shell) is the scripting language used to develop the Audit tool. It provides a powerful and flexible environment for automating tasks and interacting with the Linux operating system.

2. **Linux Command-Line Tools:**
   - `stat`: Used to retrieve file or file system status.
   - `find`: Utilized for searching files in a directory hierarchy.
   - `cut`: Employed for extracting fields or columns from input data.
   - `groups`: Used to display group membership of a user.

3. **Text Editors:**
   - Text editors such as Vim, Nano, or GNU Emacs are used for writing and editing the Bash script files in the Linux.

4. **Development Environment:**
   - A Linux environment (e.g., Ubuntu, CentOS, Debian) serves as the development environment for writing, testing, and executing the Bash script.

These tools, combined with Bash scripting, enable the project to effectively audit file permissions and enhance the security posture of Linux systems.
## Steps
To execute the provided Bash script, follow these steps:

### Step 1: Prepare Your Environment
Ensure that you have access to a Linux system where you intend to run the script. Make sure you have appropriate permissions to access the directories you want to audit.

### Step 2: Copy the Script
Copy the provided Bash script into a text editor or directly into a file on your Linux system. Save the file with a `.sh` extension, for example, `File_Permissions.sh`.

### Step 3: Set Execution Permissions
Make the script executable by running the following command in your terminal:

```bash
chmod +x File_Permissions.sh
```

This command grants execute permissions to the script, allowing you to run it as a standalone executable.

### Step 4: Run the Script
Execute the script by running the following command in your terminal:

```bash
./File_Permissions.sh <directory>
```
You can also execute the script using `bash` keyword

```bash
bash File_Permissions.sh <directory>
```

Replace `<directory>` with the path to the directory you want to audit for file permissions. For example:

```bash
./File_Permissions.sh /home
```

### Step 5: Review the Output
Once the script completes execution, it will display a report showing the file permissions within the specified directory for all users on the system. Review the output to identify any security risks or misconfigurations.

### Step 6: Interpret Results and Take Action
Analyze the output of the script to identify any files with overly permissive permissions or other security vulnerabilities. Take appropriate action to address any identified risks, such as adjusting permissions or applying access controls as needed.

### Step 7: Optional - Customize and Iterate
If necessary, customize the script to suit your specific requirements. You can modify the script to include additional checks, filters, or reporting options based on your unique security needs.

By following these steps, you can effectively execute the  Bash script to audit file permissions and enhance the security of your Linux system.
