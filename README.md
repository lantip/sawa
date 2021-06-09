![SAWA](icons/sawa_logo.png "Sawa")
# ꦱꦮ


**_sawa (ꦱꦮ)_** is an open source programming language, an interpreter to be precise, where you can write Python code using Javanese character.

_sawa_ iku arané program iki sing ndadèkaké awakmu bisa kodhing Python nganggo aksara Jawa.



- **Hello world** 
```python
ꦥꦿꦶꦤ꧀("ꦱꦸꦒꦼꦁꦫꦮꦸꦃ")
```
Output:
```bash
ꦲꦸꦒꦼꦁꦫꦮꦸꦃ
```

- **Condition** 
```python
ꦲ = ꧗
ꦪꦺꦤ꧀ ꧗ == ꧐:
    ꦥꦿꦶꦤ꧀("ꦲ ꦏꦺꦴꦱꦺꦴꦁ")
ꦲꦸꦠꦮꦭꦶꦪꦤꦺ ꦲ%2 == ꧐:
    ꦥꦿꦶꦤ꧀("ꦲ ꦒꦤꦼꦥ꧀")
ꦭꦶꦪꦤꦺ:
    ꦥꦿꦶꦤ꧀("ꦲ ꦒꦚ꧀ꦗꦶꦭ꧀")
    
```
Output:
```bash
ꦲ ꦒꦚ꧀ꦗꦶꦭ꧀
```

- **Function** 
```python
ꦥ꦳ꦸꦁꦱꦶ ꦠꦩ꧀ꦧꦃ(ꦲ,ꦧ):
    ꦕ = ꦲ + ꦧ
    ꦧꦭꦶꦏ꧀ ꦕ

ꦥꦿꦶꦤ꧀("ꦒꦸꦁꦒꦸꦁ = ", ꦠꦩ꧀ꦧꦃ(꧓,꧖))

```
Output:
```bash
ꦒꦸꦁꦒꦸꦁ = ꧙
```

- **Importing** 
You may import Python package an rename it as Javanese name. For example:
```python
ꦗꦸꦥꦸꦏ꧀ pandas ꦢꦢꦶ ꦥꦢ
ꦗꦸꦥꦸꦏ꧀ numpy ꦢꦢꦶ ꦤꦥ

ꦢꦉ = ꦥꦢ.read_csv('/location/of/csv/file.csv')

ꦢꦉ.head()

```


## Prerequisites
- Mac OS, Linux, Windows
- Python 3

***NOTE: Windows is still _untested_. Please use `pip` version, and let me know if it's not working.***

## Getting Started
### Installation

### Build from scratch (for Mac OS and Linux)
> **PLEASE NOTE: You need root access for Linux operating system.**
- Clone this repo:
```bash
git clone https://github.com/lantip/sawa.git
cd sawa
```
- Run install.sh:
```bash
./install.sh
```

- Or run Makefile:
```bash
make install
```

### Uninstall
- Run uninstall.sh
```bash
./uninstall.sh
```
### Using `pip` (For all OS)
- Run Pip install:
```bash
pip install sawa
```

***NOTE: WINDOWS user***
Install this package on `virtualenv`.

```bash
C:>python -m venv C:\Users\<name>\venv

C:>C:\Users\<name>\venv\Scripts\activate.bat

(venv)C:>pip install sawa
```

and you're good to go.



## Running

- Create a new file with name `ꦲꦭꦮ.ꦱꦮ` and open in any editor.

- Write this in the file

```vim
ꦥꦿꦶꦤ꧀("ꦱꦸꦒꦼꦁꦱꦶꦪꦁ")
```

- Save it

- Open a terminal and go to the folder where file is saved

- Run this command

```bash
ꦱꦮ ꦲꦭꦮ.ꦱꦮ
```

- It will print 

```bash
ꦱꦸꦒꦼꦁꦱꦶꦪꦁ
```

## Contributing

You are most welcome to contribute for sawa.
For guidelines see CONTRIBUTING.md

To get started take a fork of this repository and clone it.

## Credits
This interpreter is build heavily based on [YaLang](https://github.com/yalang) skeleton. Thank you!