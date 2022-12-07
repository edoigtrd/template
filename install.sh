#!/bin/bash
git clone https://github.com/edoigtrd/template.git
cd template
chmod +x bin/template
export PATH=$PATH:$(pwd)/bin

if [ -n "$BASH_VERSION" ]; then
    echo "export PATH=$PATH:$(pwd)/bin" >> ~/.bashrc
elif [ -n "$ZSH_VERSION" ]; then
    echo "export PATH=$PATH:$(pwd)/bin" >> ~/.zshrc
fi
