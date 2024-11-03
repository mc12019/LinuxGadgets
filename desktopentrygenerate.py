#!/usr/bin/python
# Date: Nov. 3, 2024
# This script is a part of personal python gadgets
import os

class Localization:
    info = "Desktop entry generate, version 1.0. Belongs to personal python gadgets"
    prompt: str
    argsPrompts = ["Entry Name: ",
                    "Exec Path: ",
                    "Icon Path: ",
                    "Categories: ",
                    "Comments: "
                    ]
    
    @staticmethod 
    def init():
        Localization.prompt = "Please input some arguments in order, empty to enter directly.\n"
        Localization.prompt += "Please be advised that Categories need seperating by semicolons."

        

class EntryGenerator:
    _applicationsPath: str = "~/.local/share/applications/"
    _desktopPath: str = "~/Desktop/"
    _buffer = []
    _args: list[str]
    _fixedArgs = ["[Desktop Entry]", "Type=Application", "Terminal=false", "StartupNotify=true"]
    _keys = ["Name", "Exec", "Icon", "Categories", "Comment"]

    def __init__(self, args) -> None:
        self._args = args

    def _getFileName(self) -> str:
        strStream = []
        for c in self._args[0]:
            if (c.isalnum()):
                strStream.append(c)
            elif (c == "_"):
                strStream.append(c)
            else:
                strStream.append("-")
        return ''.join(strStream)

    def _write(self, key: str, s: str):
        if (s == ""):
            return
        self._buffer.append(f"{key}={s}")
    
    def generate(self):
        for arg in self._fixedArgs:
            self._buffer.append(arg)
        i = 0
        while (i < self._fixedArgs.__len__()):
            self._write(self._keys[i], self._args[i])
            i += 1
        content = "\n".join(self._buffer)
        print("Generated file content:\n" + content)
        c = input("Apply?[Y/n]: ").lower()
        if (c == "n"):
            exit()
        elif (c == "y" or c == ""):
            fileName = self._getFileName()
            os.system(f"echo -n -e \"{content}\" > {self._applicationsPath}/{fileName}.desktop")
            os.system(f"echo -n -e \"{content}\" > {self._desktopPath}/{fileName}.desktop")

if __name__ == "__main__":
    Localization.init()
    print(Localization.info)
    print(Localization.prompt)
    args = []
    for p in Localization.argsPrompts:
        args.append(input(p))
    generator = EntryGenerator(args)
    generator.generate()