from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of required libraries
    '''

    requiremnets = []

    with open(file_path) as file_obj:
        requiremnets = file_obj.readlines()
        requiremnets= [req.replace("\n", " ") for req in requiremnets]

        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
    return requiremnets

setup(

    name = 'ML-Project',
    version= '0.01',
    author='Haziq',
    author_email= 'syed.haziq40@gmail.com',
    package = find_packages(),
    install_requires = get_requirements('requirment.txt')
)