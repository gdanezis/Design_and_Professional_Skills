# Call these commands with:
# $ doit

import doit
import glob

Python_files = glob.glob("src/*.py")

def task_test():
    """Test all fragments"""
    return {
        'actions': [r'pytest --doctest-modules %s > testreport.txt' % (" ".join(Python_files)),],
        'file_dep': Python_files,
        'targets': ["testreport.txt"],
        'verbosity': 2,
        }


def task_build():
    """build cmd """
    return {
        'actions': ['pdflatex -shell-escape 04_Development_Practices_Slides ;pdflatex -shell-escape 04_Development_Practices_Slides ; bibtex 04_Development_Practices_Slides ; pdflatex -shell-escape 04_Development_Practices_Slides',],
        'file_dep': ["testreport.txt"] + Python_files +
                     ["04_Development_Practices_Slides.tex"],
        'targets': ["04_Development_Practices_Slides.pdf"],
        'verbosity': 2,
        }
