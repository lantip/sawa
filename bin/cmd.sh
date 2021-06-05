#!/bin/bash

PROJECT=sawa

compile_n_run() {
    # Checking if python 3 is installed
    if command -v python3 &>/dev/null; then
        # Removing previous python converted file
        if [ -f "$1.py" ];then
            rm "$1.py"
        fi
        if [ "$#" -gt 2 ]; then
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1.$2"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py" ${@:3}
                rm "$1.py"
            fi
        elif [ "$#" -gt 1 ]; then
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1.$2"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py"
                rm "$1.py"
            fi
        else
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py"
                rm "$1.py"
            fi
        fi
    else
        echo "Python3 ꦢꦸꦫꦸꦁꦢꦶꦲꦤ"
    fi
}

if [ "$#" -gt 1 ]; then
    IFS='.' read -ra names <<< "$1"
    echo "${@:2}"
    if [ "${#names[@]}" -gt 1 ]; then
        compile_n_run "${names[0]}" "${names[1]}" ${@:2}
    else
        # Checking file extensions and running code
        if [ -f "$1.ꦱꦮ" ];then
            compile_n_run "$1" "ꦱꦮ" ${@:2}
        elif [ -f "$1.sawa" ];then
            compile_n_run "$1" "sawa" ${@:2}
        else
            echo "ꦥ꦳ꦲꦶꦭ꧀ꦲꦺꦴꦫꦥꦭꦶꦢ꧀ $1" ${@:2}
        fi
    fi

elif [ "$#" -gt 0 ]; then
    IFS='.' read -ra names <<< "$1"

    if [ "${#names[@]}" -gt 1 ]; then
        compile_n_run "${names[0]}" "${names[1]}"
    else
        # Checking file extensions and running code
        if [ -f "$1.ꦱꦮ" ];then
            compile_n_run "$1" "ꦱꦮ"
        elif [ -f "$1.sawa" ];then
            compile_n_run "$1" "sawa"
        else
            echo "ꦥ꦳ꦲꦶꦭ꧀ꦲꦺꦴꦫꦥꦭꦶꦢ꧀ $1"
        fi
    fi
else
    echo "ꦏꦼꦠꦶꦏ꧀ꦗꦼꦤꦼꦁꦥ꦳ꦲꦶꦭ꧀ "
fi
