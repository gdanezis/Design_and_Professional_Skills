# Call these commands with:
# $ doit

import doit

def task_build():
    """build cmd """
    return {
        'actions': ['python -m markdown sylabus.md > sylabus.html',],
        'file_dep': ["sylabus.md"],
        'targets': ["sylabus.html"],
        'verbosity': 2,
        }

