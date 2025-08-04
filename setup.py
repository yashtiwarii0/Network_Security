from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements.txt file and return a list of dependencies."""
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    return requirements_lst

setup(
    name='network_security',
    version='0.1',
    author='Yash',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A package for network security analysis and tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yashtiwarii0/network_security'
)