# NuclearFuelRodThermalPlayground
A User Friendly, 2D Thermal Solver Intended to Help Students Visualize the Time-Domain Heat Equation

## Setting up a Python Environment
### Windows
To set up a python environment for this project, run the following command in a terminal.

    python -m venv .venv

This environment can be activated with the following command.

    .\.venv\Scripts\Activate.ps1
    
Dependencies can now be installed with the following command.

    pip install -r requirements.txt

Please note the `PyQt5` package may not install on Windows.
Please ignore this issue as this package is purely needed for Linux systems.

### Linux
To set up a python environment for this project, run the following command in the terminal.
    python3 -m venv .venv

This environment can be activated with the following command.

    source ./.venv/bin/activate
    
Dependencies can now be installed with the following command.

    pip3 install -r requirements.txt

## Running the Model
### Windows
In the same terminal window as earlier run the following command

    python main.py

Follow along with the on-screen prompts.

### Linux
In the same terminal window as earlier run the following command

    python3 main.py

Follow along with the on-screen prompts.