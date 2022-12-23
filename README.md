# Python Project Template

This template python project was built to carry series of best practices when creating a new python product.

## Features:
- Deploying your application as a package using setup.py
- Testing inside of the application
- notebooks for ipython or scripts
- docs for design documentations related to the repo
- Design.rst for architecture design decisions
- Basic python architecture design for data driven application:
    - Context Manager: tracks the importnat clients and varibles inside of a context for more efficient usage (ex. carry spark client).
    - Config management: This module is the config source for the application. This can read environmental and global variables as well as handling secrets.
    - Utils: this module defines/configures basic tools used by majority of applications such as logging 

## Get started:

- Clone the repository:
```bash
git clone https://github.com/erfankashani/python_project_template.git
cd python_project_template
```

- Optional: create a new virtual environment for this project
```bash
conda create --name python_project_env python=3.8
```

- Install the dependencies
```bash
pip install -r requirements.txt
```

- run test cases
```bash
pytest
```

- Run the notebook
```bash
cd notebooks
python notebook_template.py
```

## Issue Tracking:
If you feel like there are more parts to be added to this project please refer to [issue_tracker](https://github.com/erfankashani/python_project_template/issues).



__Note:__ This repository has been inspired by great work of [Mahmoud Hashemi](https://github.com/mahmoud/espymetrics). Make sure to view his course and materials :)   