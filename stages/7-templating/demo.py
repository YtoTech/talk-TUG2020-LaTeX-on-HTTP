# -*- coding: utf-8 -*-
import requests
import codecs
import os
import jinja2

dirname = os.path.dirname(__file__)


# Open LaTeX template file.

latex_template_path = os.path.join(dirname, "template.tex")
with codecs.open(latex_template_path, "r", "utf-8") as f:
    latex_template = f.read()


# Jinja2 templating for interpolating variables.

latex_env = jinja2.Environment(
    block_start_string="\BLOCK{",
    block_end_string="}",
    variable_start_string="\VAR{",
    variable_end_string="}",
    comment_start_string="\#{",
    comment_end_string="}",
    line_statement_prefix="%%-",
    line_comment_prefix="%%#",
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath(".")),
)
jinja_template = latex_env.from_string(latex_template)
latex_document = jinja_template.render(
    {
        "author": "Yoan Tournade",
        "prestations": [
            {"title": "Create LaTeX template", "price": 320,},
            {"title": "Implement Jinja2 templating", "price": 500,},
            {"title": "LaTeX-on-HTTP integration", "price": 30,},
        ],
    }
)
print("Variables replaced in Jinja2 template")


# Hello World LaTeX-on-HTTP request.

response = requests.post(
    "https://latex.ytotech.com/builds/sync",
    json={
        "compiler": "xelatex",
        "resources": [
            {"main": True, "content": latex_document,},
            {
                "path": "logo.png",
                "url": "https://www.ytotech.com/static/images/ytotech_logo.png",
            },
        ],
    },
)


# Check the response code.

if response.status_code != 201:
    print("Error during the compilation")
    error = response.json()
    print("Error type: " + error["error"])
    print("Logs:")
    print(error["logs"])
    exit(1)

print("Compilation succeeded")


# Write the result to a file.

output_path = os.path.join(dirname, "output.pdf")

with open(output_path, "wb") as f:
    f.write(response.content)
    print("Written to output.pdf")
