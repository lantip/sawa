#!/usr/bin/env bash

# Variable
PROJECT=sawa
COMMAND=sawa
COMMAND_JW=ꦱꦮ

# Removing existing installation
rm -rf $HOME/$PROJECT
rm -f /usr/local/bin/${COMMAND}
rm -f /usr/local/bin/${COMMAND_JW}
#if [ -f "/usr/local/bin/${COMMAND}" ];then
#    rm /usr/local/bin/${COMMAND}
#fi

#if [ -f "/usr/local/bin/${COMMAND_JW}" ];then
#    rm /usr/local/bin/${COMMAND_JW}
#fi
