from os import system


def _uiFormImportIconsPathChange(path):
    new_file = None
 
    with open(path, "r") as f:
        new_file = f.readlines()
        f.close()

    with open(path, "w") as f:  
        for index, line in enumerate(new_file):
            if line == "import icons_rc\n":
                new_file[index] = "import client.Window.UI.icons_rc\n"

        f.writelines(new_file)
        f.close()


def UIToPyConverter(path, output):
    system(f"pyside6-uic {path} -o {output}")

    _uiFormImportIconsPathChange(output)

    