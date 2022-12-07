#!/usr/bin/env python
import os
import sys
import json

# convert name to directory name
def name_to_dir(name) :
    name = name.lower()
    r = ""
    for c in name :
        # check if character is a letter or a number
        if c.isalpha() or c.isdigit() :
            r += c
        # if it's not, replace it with a underscore
        else :
            r += "_"
    return r


if __name__ == "__main__":
    argv = sys.argv
    argv.pop(0)
    script_path = os.path.dirname(os.path.realpath(__file__))
    wd = os.getcwd()
    # check if templates.json exists
    if not os.path.exists(script_path+"/templates.json"):
        # if it doesn't, create it
        open(script_path+"/templates.json", "w").write("[]")

    # if no arguments are passed, show help
    if len(argv) == 0:
        argv.append("help")

    if argv[0] == "list":
        # load templates.json
        templates = json.loads(open(script_path+"/templates.json").read())
        for template in templates:
            # for each template, print name and description
            print(template["name"])
            print(f"\t{template['description']}")
            print()
    elif argv[0] == "help":
        # load help.txt and print it
        print(open(script_path+"/help.txt").read())

    elif argv[0] == "load":
        # load templates.json
        templates = json.loads(open(script_path+"/templates.json").read())
        template = None
        # search for template with name argv[1]
        for t in templates:
            if t["name"] == argv[1]:
                template = t
                break
        # if template is not found, print error and exit
        if template == None:
            print(f"Template {argv[1]} not found")
            exit(1)
        else:
            # if template is found, copy template directory to current directory
            os.system(
                f"cp -r \"{script_path}/templates/{template['dir']}/.\" .")
            # if after command is not empty, run it
            if t["after"] != None or t["after"] != "":
                os.system(t["after"])

    elif argv[0] == "create":
        # load templates.json
        d = json.loads(open(script_path+"/templates.json").read())
        # ask user for template name, description, directory and after command
        p_name = input("Template name: ")
        p_desc = input("Template description: ")
        p_dir = input(f"Template directory (leave blank for default ({name_to_dir(p_name)})): ")
        p_after = input("After command (leave blank for none): ")
        # if directory is empty, use name as directory
        if p_dir == "":
            p_dir = name_to_dir(p_name)
        # check if template with same name already exists
        for t in d:
            if t["name"] == p_name:
                # if it does, ask user if he wants to overwrite it
                print("Template with same name already exists")
                if input("Overwrite? [y/N] ").lower() == "y":
                    d.remove(t)
                else:
                    exit(0)
        # check if template with same directory already exists
        for t in d:
            if t["dir"] == p_dir:
                # if it does, ask user if he wants to overwrite it
                print("Template with same directory already exists, arborting")
                print(f"Please choose another directory or remove template {t['name']}")
                exit(1)
        # add template to templates.json
        d.append({
            "name": p_name,
            "description": p_desc,
            "dir": p_dir,
            "after": p_after
        })
        open(script_path+"/templates.json", "w").write(json.dumps(d, indent=4))
        # create template directory
        os.system(f"mkdir \"{script_path}/templates/{p_dir}\"")
        # copy current directory to template directory
        os.system(f"cp -r \"{wd}/.\" \"{script_path}/templates/{p_dir}\"")
        print(f"Template {p_name} created")

    elif argv[0] == "remove":
        if len(argv) == 1:
            # if no template name is passed, print error and exit
            print("Missing argument: template name")
            exit(1)
        # load templates.json
        d = json.loads(open(script_path+"/templates.json").read())
        # search for template with name argv[1]
        for t in d:
            if t["name"] == argv[1]:
                # if it is found, ask user if he wants to delete it
                print(f"Template {argv[1]} found")
                if input("Delete? [y/N] ").lower() == "y":
                    # if he wants to delete it, delete it
                    d.remove(t)
                    open(script_path+"/templates.json", "w").write(
                        json.dumps(d, indent=4))
                    # delete template directory
                    os.system(
                        f"rm -rf \"{script_path}/templates/{t['dir']}\"")
                    print(f"Template {argv[1]} deleted")
                    exit(0)
                else:
                    exit(0)
        # if template is not found, print error and exit
        print(f"Template {argv[1]} not found")
        exit(1)

    elif argv[0] == "edit":
        if len(argv) == 1:
            # if no template name is passed, print error and exit
            print("Missing argument: template name")
            exit(1)
        # load templates.json
        d = json.loads(open(script_path+"/templates.json").read())
        # search for template with name argv[1]
        for t in d:
            if t["name"] == argv[1]:
                # if it is found, ask user for new template name, description, directory and after command
                # get actual values as default
                default = {
                    "name": t["name"],
                    "description": t["description"],
                    "dir": t["dir"],
                    "after": t["after"]
                }
                print(f"Template {argv[1]} found")
                print(f"Leave blank to keep actual values")
                p_name = input(f"Template name ({default['name']}): ") or default["name"]
                p_desc = input(f"Template description: ({default['description']})") or default["description"]
                p_dir = input(f"Template directory: ({default['dir']})") or default["dir"]
                p_after = input(f"After command: ({default['after']})") or default["after"]
                # asks user if he wants to save changes
                print("New values:")
                print(f"\tName: {p_name}")
                print(f"\tDescription: {p_desc}")
                print(f"\tDirectory: {p_dir}")
                print(f"\tAfter command: {p_after}")
                # check if template with same name already exists
                for c in d:
                    if c["name"] == p_name and c != t:
                        print("Template with same name already exists, aborting")
                        print(f"If you want to change the name, delete the template {p_name} first")
                        exit(1)
                if input("Save? [y/N] ").lower() == "y":
                    # if he wants to save changes, save them
                    t["name"] = p_name
                    t["description"] = p_desc
                    t["dir"] = p_dir
                    t["after"] = p_after
                    open(script_path+"/templates.json", "w").write(
                        json.dumps(d, indent=4))
                    # rename template directory
                    # check if template name changed
                    if default["dir"] != p_dir:
                        os.system(
                            f"mv \"{script_path}/templates/{default['dir']}\" \"{script_path}/templates/{p_dir}\"")
                    print(f"Template {argv[1]} edited")
                    exit(0)
        print(f"Template {argv[1]} not found, cannot edit")
        exit(1)
    elif argv[0] == "path":
        # print path to templates directory
        print(script_path+"/templates")
    else:
        print("Unknown command")
        print("use `template help` for help")
        exit(1)
