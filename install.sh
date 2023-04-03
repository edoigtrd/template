#!/bin/bash
git clone https://github.com/edoigtrd/template.git
cd template
chmod +x bin/template
sudo ln -s "$(pwd)/bin/template" /usr/bin -f
chmod +x /usr/bin/template
