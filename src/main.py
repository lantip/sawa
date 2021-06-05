from src.process import Process
from src.enum.file_error import FileError
import os
import sys
script_dir = os.path.dirname(__file__)

num_dict = {
    "꧐": "0",
    "꧑": "1",
    "꧒": "2",
    "꧓": "3",
    "꧔": "4",
    "꧕": "5",
    "꧖": "6",
    "꧗": "7",
    "꧘": "8",
    "꧙": "9",
}

keyword_dict = {
    "ꦧꦼꦤꦼꦂ": "True", # bener
    "ꦱꦭꦃ": "False", # salah
    "ꦱꦸꦮꦸꦁ": "None", # suwung 
    "ꦢꦢꦶ": "as", # dadi
    "ꦱꦶꦢ": "assert", # sida
    "ꦲꦺꦴꦫꦩꦡꦸꦏ꧀": "async", # oramathuk
    "ꦭꦤ꧀": "and", #lan
    "ꦤꦸꦁꦒꦸ": "await", #nunggu
    "ꦭꦺꦫꦺꦤ꧀": "break", #leren
    "ꦏꦼꦭꦱ꧀": "class", #kelas
    "ꦠꦼꦫꦸꦱ꧀ꦱꦏꦺ": "continue", #terusake
    "ꦥ꦳ꦸꦁꦱꦶ": "def", #fungsi
    "ꦧꦸꦱꦏ꧀": "del", #busak
    "ꦲꦸꦠꦮꦭꦶꦪꦤꦺ": "elif", #utawaliyane
    "ꦭꦶꦪꦤꦺ": "else", #liyane
    "ꦏꦼꦗꦧ": "except", #kejaba
    "ꦫꦩ꧀ꦥꦸꦁꦔꦤ꧀": "finally", #rampungane
    "ꦏꦁꦒꦺꦴ": "for", #kanggo
    "ꦱꦏ": "from", #saka
    "ꦗꦒꦢ꧀": "global", #jagad
    "ꦪꦺꦤ꧀": "if", #yen
    "ꦗꦸꦥꦸꦏ꧀": "import", #jupuk
    "ꦤꦁ": "in", #nang
    "ꦪꦲꦶꦏꦸ": "is", #yaiku
    "ꦧꦶꦪꦤ꧀ꦠꦸ": "lambda", #biyantu
    "ꦢꦸꦢꦸ": "not", #dudu
    "ꦲꦺꦴꦫꦭꦺꦴꦏꦭ꧀": "nonlocal", #oralokal
    "ꦲꦸꦠꦮ": "or", #utawa
    "ꦭꦺꦮꦠ꧀ꦠꦶ": "pass", #lewati
    "ꦲꦁꦏꦠ꧀": "raise", #angkat
    "ꦧꦭꦶꦏ꧀": "return", #balik
    "ꦕꦺꦴꦧ": "try", #coba
    "ꦱꦮꦼꦠꦮꦶꦱ꧀": "while", #sawetawis
    "ꦏꦫꦺꦴ": "with", #karo
    "ꦏꦱꦶꦭ꧀": "yield", #kasil
    "ꦭꦺꦴꦒꦶꦱ꧀": "bool", #logis
    "ꦲꦁꦏ": "int", #angka
    "ꦣꦺꦱꦶꦩꦭ꧀": "float", #dhesimal
    "ꦲꦸꦏꦫ": "string", #ukara
    "__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__": "__dict__", # __objek__
}

function_dict = {
    "ꦩꦸꦠ꧀ꦭꦏ꧀": "abs", #mutlak
    "ꦲꦥꦸꦱ꧀ꦲꦠꦿꦶꦧꦸꦠ꧀": "delattr", #apusatribut
    "ꦕꦩ꧀ꦥꦸꦂ": "hash", #campur
    "ꦱꦏ꧀ꦭꦺꦧꦠ꧀": "memoryview", #saklebat
    "ꦲꦺꦴꦩ꧀ꦧꦾꦺꦴꦏ꧀": "set", #ombrok
    "ꦏꦧꦺꦃ": "all", #kabeh
    "ꦏꦩꦸꦱ꧀": "dict", #kamus
    "ꦠꦸꦭꦸꦁ": "help", #tulung
    "ꦩꦶꦤꦶꦩꦭ꧀": "min", # minimal
    "ꦱꦺꦠꦂ": "setattr", # setar 
    "ꦏꦁ": "any", # kang
    "ꦣꦶꦂ": "dir", # dhir
    "ꦲꦺꦏ꦳꧀": "hex", #heks
    "ꦧꦕꦸꦠ꧀": "next", #bacut
    "ꦲꦶꦫꦶꦱ꧀ꦱꦤ꧀": "slice", # irisan
    "ꦲꦱ꧀ꦏꦶ": "ascii", # aski
    "ꦢꦶꦥ꦳꧀ꦩꦺꦴꦢ꧀": "divmod", # difmod
    "ꦲꦶꦣꦶ": "id", # idhi
    "ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀": "object", # objek
    "ꦲꦸꦫꦸꦠ꧀": "sorted", # urut
    "ꦧꦶꦤ꧀": "bin", # bin
    "ꦲꦺꦤꦸꦩꦼꦂꦫꦺꦠ꧀": "enumerate", # enumeret
    "ꦠꦸꦭꦶꦱ꧀": "input", #tulis
    "ꦲꦺꦴꦏ꧀ꦠ": "oct", # okta
    "ꦱꦶꦒꦼꦒ꧀": "staticmethod", #sigeg
    "ꦭꦺꦴꦒꦶꦱ꧀": "bool", # logis
    "ꦲꦺꦥ꦳ꦭ꧀": "eval", # efal
    "ꦲꦁꦏ": "int", # angka
    "ꦧꦸꦏ": "open", # buka
    "ꦱꦼꦫꦠ꧀": "str", # serat
    "ꦊꦏꦱ꧀ꦩꦤꦺꦃ": "breakpoint", #lekasmaneh
    "ꦲꦗꦂ": "exec", # ajar
    "ꦧꦭꦤꦺ": "isinstance", #balane
    "ꦲꦺꦴꦫꦼꦢ꧀": "ord", #ored
    "ꦗꦸꦩ꧀ꦭꦃ": "sum", #jumlah
    "ꦧꦶꦠꦼꦫꦺ": "bytearray", #bitere
    "ꦥ꦳ꦶꦭ꧀ꦠꦼꦂ": "filter", #filter
    "ꦲꦤ꧀ꦣꦃꦲꦤ꧀": "issubclass", #andhahan
    "ꦏ꧀ꦮꦱ": "pow", #kwasa
    "ꦲꦸꦠꦩ": "super", #utama
    "ꦧꦪ꧀ꦠ": "bytes", #bayta
    "ꦣꦺꦱꦶꦩꦭ꧀": "float", #desimal
    "ꦥꦫ": "iter", # para
    "ꦠꦸꦥꦼꦭ꧀": "tuple", # tupel
    "ꦔꦸꦚ꧀ꦢꦁ": "callable", # ngundang
    "ꦮꦸꦗꦸꦢ꧀": "format", # wujud
    "ꦢꦮ": "len", # dawa
    "ꦏꦒꦸꦁꦔꦤꦺ": "property", # kagungane
    "ꦩꦺꦴꦣꦺꦭ꧀": "type", # modhel
    "ꦕꦂ": "chr", #car
    "ꦧꦼꦏꦸꦮꦤ꧀": "frozenset", #bekuwan
    "ꦣꦥ꦳꧀ꦠꦂ": "list", #daftar
    "ꦲꦤ꧀ꦠꦫ": "range", # antara
    "ꦥ꦳ꦉꦱ꧀": "vars", # fares
    "ꦩꦺꦠꦺꦴꦢ꧀ꦏꦼꦭꦱ꧀": "classmethod", #metodkelas
    "ꦗꦸꦥꦸꦏ꧀ꦲꦠꦼꦂ": "getattr", #jupuk ater
    "ꦥꦿꦶꦧꦸꦩꦶ": "locals", #pribumi
    "ꦫꦺꦥꦼꦂ": "repr", #reper
    "ꦗꦶꦥ꧀": "zip", #jip
    "ꦏꦺꦴꦩ꧀ꦥꦺꦭ꧀": "compile", #kompel
    "ꦱꦗꦒꦢ꧀": "globals", #sajagad
    "ꦥꦼꦠ": "map", #peta
    "ꦮꦭꦶꦏ꧀ꦲꦤꦺ": "reversed", #walikane
    "__ꦗꦸꦥꦸꦏ꧀__": "__import__", # __jupuk__
    "__ꦊꦏꦱ꧀__": "__init__", # __lekas__
    "__ꦲꦺꦴꦧ꧀ꦗꦺꦏ꧀__": "__dict__", # __objek__
    "ꦩꦤꦺꦏ": "complex", #maneka
    "ꦒꦣꦃ": "hasattr", #gadhah
    "ꦥꦺꦴꦭ꧀": "max", #pol
    "ꦮꦸꦠꦸꦃ": "round", #wutuh
    "ꦣꦺꦮꦺ": "self", #dhewe
}

def compile(file_name):
    py_content = ''
    # Appending print function code to the file
    with open(os.path.join(script_dir, 'include.py'), 'r') as file:
        py_content += file.read()

    # Reading file to process the text
    with open(file_name, 'r') as file:
        # Process all content of the file
        py_content += Process(file, num_dict, keyword_dict, function_dict).process()

    # Splitting file name to remove existing extension in order to add python extension
    file_split = file_name.split(".")
    # Name of the python file to be created
    py_file = file_split[0] + ".py"
    # Creating the python file
    f = open(py_file, "w")
    # And then writing content to the python file
    f.write(py_content)

def main(file_name):
    if os.path.isdir(file_name):
        # If the file name is directory then it will search all the file with *.ꦱꦮ and process all file
        for flnm in os.listdir(file_name):
            if flnm.endswith('.ꦱꦮ'):
                compile(flnm)
                print(' \r\n ')
    elif os.path.isfile(file_name):
        compile(file_name)
    else:
        sys.exit("'" + file_name + "'" + " " + FileError.INVALID_FILE.value)