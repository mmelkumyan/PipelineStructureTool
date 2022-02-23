# COPIED OVER FROM GLODON CLEANUP SCRIPT

import os
import sys
import shutil
import argparse
import re

DEFAULT_OUTPUT_DIR = 'output'
DEFAULT_DISPLAY = False
VALID_EXTENSIONS = ['png', 'json']

if __name__ == "__main__":
    description = "Clean '/output' directory of project files."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--output_dir", help=f"Output directory. Default is '{DEFAULT_OUTPUT_DIR}'", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--file_type", help="File type to delete. Either JSON or PNG. Default is to delete all types. Case insensitive. Ex: '--file_type png'",default=None)
    parser.add_argument("--projects", help="Project #s to delete. Default is to delete all projects. Ex: '--projects 5'; '--projects 1,2,3'", default=None)
    parser.add_argument("--score", help="Deletes scores above the threshold. Default is '0'. Ex: '--score 50'", default=0, type=float)
    parser.add_argument("--display", help=f"Print each file name deleted. Default is '{DEFAULT_DISPLAY}'", default=DEFAULT_DISPLAY, type=bool)
    args = parser.parse_args()

    root = os.getcwd()
    output_path = os.path.join(root, args.output_dir)
    print(f"Deleting files from '{output_path}'...")

    # Error check arguments
    # Grab specific project #s and exts from string; Deletes all by default
    specific_projects_to_del = None
    if args.projects:
        specific_projects_to_del = str(args.projects).split(',')
        for n in specific_projects_to_del:
            try:
                int(n)
            except ValueError:
                print("Error: argument --projects: Must be integers. Ex: '--projects 5'; '--projects 1,2,3'")
                sys.exit()

    specific_exts_to_del = None
    if args.file_type:
        if (not type(args.file_type) is str) or (not args.file_type.lower() in VALID_EXTENSIONS):
            print("Error: argument --file_type: Must be either 'png' or 'json'. Ex: '--file_type png'; '--file_type json'")
            sys.exit()
        specific_exts_to_del = args.file_type.lower()

    # Loop through subdirectories in output directory
    dir_del_cnt = 0
    file_del_cnt = 0
    for sub_dir in os.listdir(output_path):

        sub_dir_path = os.path.join(output_path, sub_dir)
        if os.path.isdir(sub_dir_path):

            # Loop through files in subdirectory
            for file in os.listdir(sub_dir_path):

                # Grab file info
                (file_name, ext) = os.path.splitext(file)
                file_path = os.path.join(sub_dir_path, file)
                project_num = file_name.split('_')[0]

                project_num = re.search("^(project|office)([\d]+)", project_num).group()
                project_num = project_num.replace("project", "", 1)
                project_num = project_num.replace("office", "", 1)

                ext = ext[1:].lower()

                score = file_name.split('_')[-2]
                score = float(score)

                # Check whether to delete or not
                if (not specific_projects_to_del or (project_num in specific_projects_to_del)) and \
                        (not specific_exts_to_del or (ext in specific_exts_to_del)) and \
                        (score >= args.score):

                    if args.display:
                        print(f"Deleting file '{os.path.join(sub_dir, file)}'")

                    os.remove(file_path)
                    file_del_cnt += 1

            # Delete subdirectory if empty
            if not os.listdir(sub_dir_path):
                if args.display:
                    print(f"Deleting subdirectory '{sub_dir}'")

                os.rmdir(sub_dir_path)
                dir_del_cnt += 1

    # Output number of files deleted
    if not dir_del_cnt:
        print(f"No directories deleted.")
    else:
        print(f"{dir_del_cnt} directories deleted.")

    if not file_del_cnt:
        print(f"No files found to delete in subdirectories.")
    else:
        print(f"{file_del_cnt} file(s) deleted.")
