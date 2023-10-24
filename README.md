# Pay calculator for UNC OASIS Workstudy position
Created as a personal tool for pay management, but fellow students working for OASIS as a Workstudy can use this calculator to determine the amount of financial aid allotment they have left based on current number of hours worked. Calculator also offers a rough recommended number of hours to work per week to get the max allotment possible.

## Instructions: 
1. Install a Python compilation package like [PyInstaller](https://www.pyinstaller.org) on your computer (see [recommended instructions below](#recommended-instructions))
2. Download the source code: `pay_calc.py` if you prefer the terminal interface, or `pay_calc_GUI.py` if you prefer a GUI
3. Within the terminal or shell, navigate to the directory where the source code is located
4. Compile using your selected package
5. Run your executable!

## Recommended Instructions: 
I personally recommend using PyInstaller as the process is very simple. Do note that the compiled executable will only run on the same OS as the machine you compiled the source code on. For example, if I compile the code on MacOS/OSX, the executable will only be able to run on Unix machines, not Windows computers.

1. Install PyInstaller using the instructions [here](https://pyinstaller.org/en/stable/installation.html)
2. Download the source code: `pay_calc.py` if you prefer the terminal interface, or `pay_calc_GUI.py` if you prefer a GUI
3. Within the terminal or shell, navigate to the directory where the source code is located
4. Compile using the command `pyinstaller --onefile pay_calc.py` (or `pyinstaller --onefile pay_calc_GUI.py` if you chose the GUI version)
5. The executable will be found in the folder called `dist`. Simply click it to run!
