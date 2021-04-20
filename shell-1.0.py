import os
import shutil
import sys

name = "shell"
version = "1.0"
command = ["clear", "pwd", "cd", "mkdir", "ls", "rm", "touch", "cat", "cp", "mv", "echo", "license", "ver", "help"]

license = """
MIT License

Copyright (c) 2021 miniprime1 [Kyumin]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
"""

class shell:
    def ver():
        try:
            print("{version}")
        except Exception as err:
            print("Error:", str(err))
    
    def help():
        try:
            for i in command:
                print(i)
        except Exception as err:
            print("Error:", str(err))

    def clear():
        try:
            print('\x1bc')
        except Exception as err:
            print("Error:", str(err))

    def license():
        try:
            print(license)
        except Exception as err:
            print("Error:", str(err))

    def pwd():
        try:
            print(os.getcwd())
        except Exception as err:
            print("Error:", str(err))
    
    def exit():
        try:
            sys.exit()
        except Exception as err:
            print("Error:", str(err))

    def cd(path): 
        try:
            os.chdir(path)
        except Exception as err:
            print("Error:", str(err))

    def mkdir(path):
        try: 
            os.mkdir(path)
        except Exception as err:
            print("Error:", str(err))
        
    def ls(): 
        try:
            tmp = os.listdir()
            for i in tmp: print(i)
        except Exception as err:
            print("Error:", str(err))

    def rm(path):
        try:
            os.remove(path)
        except Exception as err:
            print("Error:", str(err))

    def touch(path):
        try:
            f = open(path, "ab")
            f.close()
        except Exception as err:
            print("Error:", str(err))
    
    def cat(path):
        try:
            f = open(path, 'r')
            print(f.read())
            f.close()
        except Exception as err:
            print("Error:", str(err))
    
    def cp(path1, path2):
        try:
            shutil.copy2(path1, path2)
        except Exception as err:
            print("Error:", str(err))
    
    def mv(path1, path2):
        try:
            shutil.move(path1, path2)
        except Exception as err:
            print("Error:", str(err))

    def echo(*text):
        try:
            txt = ""
            for i in text: 
                txt += i
                txt += " "
            print(txt)
        except Exception as err:
            print("Error:", str(err))

def execute(cmd):
    p = cmd.split(" ")
    l = len(p)
    if l==0:
        pass
    elif l==1: 
        exec(f'shell.{p[0]}()')
    elif l==2: 
        exec(f'shell.{p[0]}("{p[1]}")')
    elif l==3:
        exec(f'shell.{p[0]}("{p[1]}", "{p[2]}")')
    else:
        tc = f"shell.{p[0]}("
        for i in range(1, l+1):
            if i==l:
                tp = f'"{p[i]}"'
                tc += tp
            else:
                tp = f'"{p[i]}", '
                tc += tp
        tc += ")"
        exec(tc)

while True:
    try:
        cmd = input(f"{name}-{version}$ ")
        execute(cmd)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as err:
        print("Error:", str(err))
