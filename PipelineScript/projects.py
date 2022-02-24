import os
import json


# class ProjectManager():
#     projects = {}
#
#     def __init__(self):
#         return

def saveProject(name, row_model_map, ui):
    project = {
        "name": name,
        "models": {},
        "structure": {}
    }

    for row_name, model_name in row_model_map.items():
        project["models"][model_name] = {}
        project["models"][model_name]["numLabel"] = getattr(ui, row_name + "NumberLabel").text()
        project["models"][model_name]["modelFile"] = getattr(ui, row_name + "LocationText").text()
        project["models"][model_name]["rootDir"] = getattr(ui, row_name + "RootText").text()

    json_object = json.dumps(project, indent=4)
    root = os.path.join(os.getcwd(), "Projects")
    suffix = "_PipelineProject"
    file_name = name.replace(" ", "") + suffix + ".json"
    file_path = os.path.join(root, file_name)

    with open(file_path, "w") as out:
        out.write(json_object)
