import os
from tkinter.filedialog import askopenfilename
import tkinter
import ctypes


def choose_file():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except AttributeError:
        pass
    tkinter.Tk().withdraw()
    file = askopenfilename(title="Open fastA file", initialdir="/")
    if file:
        return file


def fasta(file):
    dot_name = os.path.basename(file)[os.path.basename(file).find('.'):]
    if dot_name == '.fa' or dot_name == '.fasta':
        with open(file, 'r') as f:
            data = f.readlines()
        seq = []
        for line in range(len(data)):
            if data[line].startswith('>'):
                seq.append(data[line + 1])
        return str(seq)[2:-2]
    else:
        print('Invalid format')
        exit()
