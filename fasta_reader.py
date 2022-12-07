import os
from tkinter.filedialog import askopenfilename
import tkinter
import ctypes


def choose_file():
    """
    Open tkinter to choose fastA
    :return: path to choosen file
    """
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except AttributeError:
        pass
    tkinter.Tk().withdraw()
    file = askopenfilename(title="Open fastA file", initialdir="/")
    if file:
        return file


def fasta(file):
    """
    Get sequences from fastA file
    :param file: path to fastA file
    :return: array of sequences from fastA file
    """
    dot_name = os.path.basename(file)[os.path.basename(file).find('.'):]
    if dot_name == '.fa' or dot_name == '.fasta':
        with open(file, 'r') as f:
            data = f.readlines()
        seq = []
        for line in range(len(data)):
            if data[line].startswith('>'):
                seq.append(data[line + 1])
        for line in range(0, len(seq)):
            while seq[line][-1] == '\n':
                seq[line] = seq[line][:-1]
        return seq
    else:
        print('Invalid format')
        exit()
