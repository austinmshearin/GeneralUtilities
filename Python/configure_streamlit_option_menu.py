"""
Configures streamlit-option-menu package so menu clicks don't move web page
"""
import os
import site
import glob

site_packages = site.getsitepackages()
for site_package in site_packages:
    option_menu_js = os.path.join(site_package, "streamlit_option_menu/frontend/dist/js/*.js")
    js_files = glob.glob(option_menu_js)
    for js_file in js_files:
        with open(js_file, "r") as filein:
            contents = filein.read()
        mod_contents = contents.replace("href:\"#\"", "href:\"#dummy\"")
        with open(js_file, "w") as fileout:
            fileout.write(mod_contents)
