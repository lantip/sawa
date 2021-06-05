![SAWA](icons/sawa_logo.png "Sawa")
# ꦱꦮ


**_sawa (ꦱꦮ)_** is an open source programming language, an interpreter to be precise, where you can write python code using javanese character.

_sawa_ iku arane program iki sing ndadekake awakmu iso koding python nganggo aksara jawa.


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
You may import python package an rename it as javanese name. For example:
```python
ꦗꦸꦥꦸꦏ꧀ pandas ꦢꦢꦶ ꦥꦢ
ꦗꦸꦥꦸꦏ꧀ numpy ꦢꦢꦶ ꦤꦥ

ꦢꦉ = ꦥꦢ.read_csv('/location/of/csv/file.csv')

ꦢꦉ.head()

```


## Prerequisites
- Mac OS or Linux
- Python 3


## Getting Started
### Installation

**PLEASE NOTE: You need root access for Linux operating system.**
- Clone this repo:
```bash
git clone https://github.com/lantip/sawa.git
cd ya
```
- Run install.sh:
```bash
./install.sh
```

- Or run Makefile:
```bash
make install
```

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
This interpreter is build heavily based on [YaLang](https://github.com/yalang) skeleton. Thankyou!