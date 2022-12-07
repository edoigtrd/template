# Template

Template is a CLI template manager.

With template you can create and load templates.

---
# Usage

## Update template manager :
```bash
template update
```
this will check for updates and update it if a new version is available.
Note : this command requires git to be used.

## list templates :

To list all templates run:
```bash
template list
```
this will list all templates in the template directory.


## Create template :

creating a template is easy, just go to the directory you want to create a template from and run:
```bash
template create
```
this will open a prompt asking you for template configuration, after you are done, the template will be created.


## Load template :

Go to the directory you want to load the template to and run:
```bash
template load <template name>
```
this will load the template to the current directory.
note that template name is specified in the template configuration file while creating the template.

## Remove template :
    
To delete a template run:
```bash
template remove <template name>
```
this will delete the template from the template directory.
note that template name is specified in the template configuration file while creating the template.

---

# Installation

## Manual

1. clone the repo <br>
    `git clone https://github.com/edoigtrd/template.git`

2. cd into the repo<br>
    `cd template`

3. make sure bin/template is executable <br>
    `chmod +x bin/template`

4. add /bin to your path <br>
    `export PATH=$PATH:$(pwd)/bin`

5. make path modifications permanent by adding the above line to your .bashrc or .zshrc file <br>
    `echo "export PATH=$PATH:$(pwd)/bin" >> ~/.bashrc`

## Automatic

Simply run the following command in your terminal:
```bash
curl -s https://raw.githubusercontent.com/edoigtrd/template/master/install.sh | bash
```