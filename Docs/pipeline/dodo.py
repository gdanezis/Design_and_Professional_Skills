# Call these commands with:
# $ doit

import doit

def task_test():
    """Test all fragments"""
    return {
        'actions': ['pytest -vs --doctest-modules > testreport.txt',],
        'file_dep': ["hello_world.py", 
                     "test_hello_world.py",
                     "hello_world_doc.py", ],
        'targets': ["testreport.txt"],
        'verbosity': 2,
        }


def task_build():
    """build cmd """
    return {
        'actions': ['pdflatex -shell-escape slide_hello_world',],
        'file_dep': ["testreport.txt", "hello_world.py", 
                     "test_hello_world.py",
                     "hello_world_doc.py", 
                     "slide_hello_world.tex"],
        'targets': ["slide_hello_world.pdf"],
        'verbosity': 2,
        }

def task_cleanup():
    """cleanup cmd"""
    return {
        'actions': ['rm *.aux *.log *.nav *.out *.snm *.toc',],
        'file_dep': ["slide_hello_world.pdf"],
        'verbosity': 2,
        }

