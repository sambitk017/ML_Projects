"""
is reponsible for running the application as a package 
you can also use it and can be deployed in pipi.

"""
dot = "-e ."
from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str)->list[str]:
    """give th elist of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        
        if dot in requirements:
            requirements.remove(dot)
    return requirements

setup(
name="mlproject",
version='0.0.1',
author="Sambit",
author_email="sambitk017@gmail.com",
packages= find_packages(),
install_requires=get_requirements('requirements.txt')
)