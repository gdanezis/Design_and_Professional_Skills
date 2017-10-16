# Call these commands with:
# $ doit

import doit
import glob

Python_files = glob.glob("src/*.py")

def task_test():
    """Test all fragments"""
    return {
        'actions': [r'echo "done" > testreport.txt'],
        'file_dep': Python_files,
        'targets': ["testreport.txt"],
        'verbosity': 2,
        }


def task_build():
    """build cmd """
    return {
        'actions': ['pdflatex -shell-escape 99_CS_Visualization_Topic ;pdflatex -shell-escape 99_CS_Visualization_Topic ; bibtex 99_CS_Visualization_Topic ; pdflatex -shell-escape 99_CS_Visualization_Topic',],
        'file_dep': ["testreport.txt"] + Python_files +
                     ["99_CS_Visualization_Topic.tex"],
        'targets': ["99_CS_Visualization_Topic.pdf"],
        'verbosity': 2,
        }
