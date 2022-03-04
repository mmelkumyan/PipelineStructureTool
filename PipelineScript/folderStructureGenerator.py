import argparse
import os

# TODO:
# windows folders -> store as JSON template ->

# TO CREATE UI FILE: `pyuic5 -x .\pipelineToolQT.src_ui -o ui_mainWindow_BACKUP.py`

# Tutorial on how to dynamically create widgets: https://www.youtube.com/watch?v=4BZL3cF_Dww

DEBUG_ON = False

DEFAULT_ROOT_DIR = "root"
DEFAULT_TEMPLATE_FILE = "Models/sms_baseStructure_test.txt"
DEFAULT_TAB_SIZE = 4


def count_tabs(line):
    cnt = 0
    for char in line:
        if char == " ":
            cnt += 1
        else:
            break
    if cnt % 4 != 0:
        raise Exception("Irregular tab length")
    else:
        return cnt//4


def move_up_dirs(cnt):
    for i in range(0, cnt):
        os.chdir('..')
    return


def generate_dirs(root_path, template_file):
    try:
        details = "Generated directories:\n"
        cwd = os.getcwd()

        current_level = 0
        prev_level = 0
        with open(template_file, 'r') as template:
            os.chdir(root_path)
            for line in template:
                dir_name = line.lstrip().rstrip()  # Strip white space before and after
                prev_level = current_level
                current_level = count_tabs(line) + 1

                # Move up directories if needed
                if prev_level >= current_level:
                    move_up_dirs(prev_level - current_level + 1)

                if DEBUG_ON:
                    print(f"Current path: {os.getcwd()}")
                    print(f"Cur Level={current_level}, Prev Level={prev_level}, {dir_name}")

                # Create directory and enter it
                os.mkdir(dir_name)
                dir_path = os.path.join(os.getcwd(), dir_name)
                # details += f"Created directory: {dir_path}\n"
                details += current_level*"\\" + f"{dir_name}\n"
                os.chdir(dir_path)

        os.chdir(cwd)
        return 0, details
    except Exception as exception:
        return 1, str(exception)


def model_to_json(model_file):
    #... Take in text file and generate json model file.
    return

def create_project_file(project_name):
    # project_name = "Story Medicine"
    # create `Story Medicine.json`
    # Store in it info for this project, like # of episodes, where episode root is, same for seasons, etc.
    return


if __name__ == "__main__":
    description = "Create directory structure based off template file."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--root_dir", help=f"Root directory. Default is '{DEFAULT_ROOT_DIR}'", default=DEFAULT_ROOT_DIR)
    parser.add_argument("--template", help=f"Template file. Default is '{DEFAULT_TEMPLATE_FILE}'", default=DEFAULT_TEMPLATE_FILE)
    parser.add_argument("--tab_size", help=f"Tab size in spaces. Default is '{DEFAULT_TAB_SIZE}'", default=DEFAULT_TAB_SIZE)
    args = parser.parse_args()

    starting_path = os.getcwd()
    root_path = os.path.join(starting_path, args.root_dir)

    if not os.path.isdir(root_path):
        os.mkdir(root_path)

    generate_dirs(root_path, args.template, "Project Medicine")
