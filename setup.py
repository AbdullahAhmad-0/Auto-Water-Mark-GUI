import cx_Freeze
import sys

base = None
base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Auto WM",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\\Auto WM.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="Auto WM.py", icon='ico.ico', base=base,
                                    copyright='AbdullahAhmad@AhmadSoft')]

cx_Freeze.setup(
    version="1.0",
    description="AbdullahAhmad@AhmadSoft",
    author="ABDULLAH AHMAD",
    name="Auto WM",
    options={"build_exe": {"packages": ["tkinter", "PIL", "os"],
                           "include_files": ['Autocomplete_Combo.py', 'ico.ico']},
             "bdist_msi": bdist_msi_options,
             },
    executables=executables

)
