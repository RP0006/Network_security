from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]: #this function will return list of requirements
    requirements_list: List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines= file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and comments -e.
                if requirement and requirement!='-e.':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the same directory as setup.py")
    return requirements_list

setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Rohit Pal',
    author_email='palr71646@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)