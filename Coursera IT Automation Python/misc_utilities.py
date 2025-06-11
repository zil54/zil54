import subprocess
import sys
import re
import os
import operator
print(os.path.dirname(sys.executable))  # Example: C:\Python39
# Running a command and capturing the output
result = subprocess.run(["cmd", "/c", "echo Hello, Windows!"], capture_output=True, text=True)
subprocess.run(["notepad.exe"])

print(result.stdout)  # Output: Hello, Windows!
fruit = {"oranges": 3, "apples": 5, "bananas": 7, "peaches": 2}

print(sorted(fruit.items(), key=operator.itemgetter(1)))

# !/usr/bin/env python3

import os
import shutil
import multiprocessing


def copy_file(file_pair):
    """Copy a single file from source to destination."""
    src_file, dest_file = file_pair
    try:
        shutil.copy2(src_file, dest_file)
        # Uncomment the line below if you want to see each copy action.
        # print(f"Copied {src_file} to {dest_file}")
    except Exception as e:
        print(f"Error copying {src_file} to {dest_file}: {e}")

def create_directory_structure():
    """
    Walks through the source directory and creates all the directories
    in the destination that mirror the source structure.
    """
    for dirpath, _, _ in os.walk(src):
        # Compute the relative path from the source directory.
        relative_path = os.path.relpath(dirpath, src)
        # Construct the corresponding destination directory.
        dest_dir = os.path.join(dest, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

def build_file_list():
    """
    Constructs a list of (source_file, destination_file) tuples for all files
    in the source directory.
    """
    file_list = []
    for dirpath, _, filenames in os.walk(src):
        relative_path = os.path.relpath(dirpath, src)
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(dest, relative_path, filename)
            file_list.append((src_file, dest_file))
    return file_list

if __name__ == '__main__':
    # Step 1: Ensure the destination directory structure exists.
    create_directory_structure()

    # Step 2: Build the list of file copy tasks.
    files_to_copy = build_file_list()
    print(f"Starting copy of {len(files_to_copy)} files from {src} to {dest}...")

    # Step 3: Copy files concurrently using a multiprocessing Pool.
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool.map(copy_file, files_to_copy)
    pool.close()
    pool.join()

    print("File copy completed!")
def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()

per_user = {}  # Splitting between INFO and ERROR
errors = {}

# * Read file and create dictionaries
with open('syslog.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        # * Sample Line of log file
        # "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        # Populates error dict with ERROR messages from log file
        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] += 1
        # Populates per_user dict with users and default values
        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
        # Populates per_user dict with users logs entry
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]["INFO"] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['ERROR'] += 1


# Sorted by VALUE (Most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

# Sorted by USERNAME
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()
# Insert at the beginning of the list
errors_list.insert(0, ('Error', 'Count'))

# * Create CSV file user_statistics
with open('user_statistics.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# * Create CSV error_message
with open('error_message.csv', 'w', newline='') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ' ' + str(value))

#if __name__ == "__main__":
  #  log_file = sys.argv[1]
  #  returned_errors = error_search(log_file)
  #  file_output(returned_errors)

  #  sys.exit(0)