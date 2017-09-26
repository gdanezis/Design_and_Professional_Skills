# Call these commands with:
# $ doit

import doit

def task_build():
    """build cmd """
    return {
        'actions': ['python -m markdown syllabus.md > syllabus.html',],
        'file_dep': ["syllabus.md"],
        'targets': ["syllabus.html"],
        'verbosity': 2,
        }

