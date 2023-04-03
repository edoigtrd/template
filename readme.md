# Template

Template is a CLI template manager.

With template you can easily manage templates.

---
# Usage

## Update template manager :
```bash
template manager-update
```
this will check for updates and update it if a new version is available.<br>
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
this will open a prompt asking you for template configuration, once you have done, the template will be created.


## Load template :

Go to the directory you want to load the template to and run:
```bash
template load <template name>
```
this will load the template to the current directory. <br>
Note: that template name is specified in the template configuration file while creating the template.

## Get template info :
To get info about a template run:
```bash
template info <template name>
```
this will show you the template configuration and ressources tree.<br>

## Remove template :
    
To delete a template run:
```bash
template remove <template name>
```
this will delete the template from the template directory.<br>
Note: that template name is specified in the template configuration file while creating the template.

## Update template files :
To update the template files run:
```bash
template update <template name>
```
this will change the template files to files in the current directory.

---

# Installation

## Manual

1. clone the repo <br>
    `git clone https://github.com/edoigtrd/template.git`

2. cd into the repo<br>
    `cd template`

3. make sure bin/template is executable <br>
    `chmod +x bin/template`

4. add template bin to /usr/bin <br>
    `sudo ln -s "$(pwd)/bin/template" /usr/bin -f`

5. Add execution perimssion to the symlink <br>
    `sudo chmod +x /usr/bin/template`

## Automatic

Simply run the following command in your terminal:
```bash
curl -s https://raw.githubusercontent.com/edoigtrd/template/master/install.sh | bash
```
