"""
Author:  Sumedh R Rao
Purpose: This script showcases a subset of escape sequenses specified by Ansii, 
         Graphical Rendition 033
Usage:   python <script.py> ; use with stand alone terminals, 
         and not ide integrated ones (at least for vs code)
OS:      Ideally any OS consoles that support ANSI encoding,
         tested on Linux (Ubuntu 20) and Windows 10
warning: print and input functions modify the output of these functions,
         as they add a newline after their execution.
"""
import time
import sys
import os

if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def text_functions(heading: str, escape_sequeunce: str):
    print("\n" + heading)
    print(escape_sequeunce + "Hello" + "\033[0m\n")

def cursor_functions(heading: str, command: str):
    print(heading)
    time.sleep(2)
    sys.stdout.write(command)

    
if __name__ == "__main__":
    
    print("Documentation on how to change text properties in a terminal while printing from any language")
    print("(c) => caution, not widely supported")
    text_functions("Foreground Color: 38;2;<r>;<g>;<b>", "\033[38;2;255;0;0m")
    text_functions("Background Color: 48;2;<r>;<g>;<b>", "\033[48;2;255;0;0m")
    text_functions("Slow Blink: 5 off: 25", "\033[5m")
    text_functions("Rapid Blink: 6 off: 26", "\033[6m")
    text_functions("Bold: 1 off; 21", "\033[1m")
    text_functions("(c)Faint: 2 off: 22", "\033[2m")
    text_functions("(c)Italic: 3 off: 23", "\033[3m")
    text_functions("(c)underlined: 4 off: 24", "\033[4m")
    text_functions("(c)Crossed Out: 9 off: 29", "\033[9m")
    print("Entering into cursor functions, will need input to proceed")
    cursor_functions("Clear Screen: 2J", "\033[2J")
    cursor_functions("Move to Line, Column: L;CH/L;Cf", "\033[4;0f")
    print("1\n2\n3\n4\n5")
    cursor_functions("Move up N lines <N>A", "\033[s\033[7A")
    cursor_functions("Move down N lines <N>B", "\033[6B")
    print("exit")
    
