#!/bin/bash
git clone https://github.com/edoigtrd/template.git
cd template
chmod +x bin/template
export PATH=$PATH:$(pwd)/bin

if [ -f ~/.bashrc ]; then
    echo "export PATH=\$PATH:$(pwd)/bin" >> ~/.bashrc
fi

if [ -f ~/.zshrc ]; then
    echo "export PATH=\$PATH:$(pwd)/bin" >> ~/.zshrc
fi