from gettext import install
from setuptools import setup,find_packages

NAME = 'python_project_template'
AUTHOR = 'Erfan K'
VERSION = '1.0'
CONTACT = 'https://www.linkedin.com/in/erfankashani/'
URL = 'https://github.com/erfankashani'
LICENCE = 'BSD'

setup(
    name=NAME,
    version=VERSION,
    long_description=__doc__,
    author=AUTHOR,
    author_email=CONTACT,
    url=URL,
    packages=find_packages(),
    install_requirements=['pytest'],
    include_package_data=True,
    classifiers=['Intended Audience :: Developers', 'License',
                 'Programming Language :: Python :: 3.8'
    ]
)