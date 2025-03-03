'''

The setup.py file is an essential part of packaging and distributiing Python projects .
It is used by setuptools ( or distutils  in older python version  ) to define the configuration 
of your project  , such as metadata , dependencies , and more . 

Metadata here means it consider the versions it has and any important package it contain .

'''

from setuptools import find_packages , setup
from typing import List


# This function will return  the list of requirements from the requirements.txt file
def get_requirements() -> List[str]:

    requirement_lst:List[str] = []

    try:
        with open('requirements.txt' , 'r') as file:
            # read lines from the file .
            lines = file.readlines()
            for line in lines:
                # return the list of requirements

                requirement = line.strip()  # cutting the sides is spaces present 
                # ignore the empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
        
    except FileNotFoundError:
        print('requirements.txt file not found')


    return requirement_lst

setup(
    name = "NetworkSecurity" ,
    version = "0.0.1" ,
    author = " Ashis Kumar Mishra " ,
    author_email = "mishralucky074@gmail.com" ,
    packages = find_packages() ,
    install_requires = get_requirements()
)

