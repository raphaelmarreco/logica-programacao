#!/bin/bash
# Por conta de erros nas depedências do Python3 e PIP, adicionei ao script a rotina de instalação dessas depedências via APT, já que estou utilizando Debian 12
# Válido também para Ubuntu e outros Debian-based OSs.

sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
sudo apt install pipx

python3 /PATH/TO/YOUR/script_calculadora.py