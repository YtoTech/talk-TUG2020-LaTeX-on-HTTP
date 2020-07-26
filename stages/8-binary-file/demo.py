# -*- coding: utf-8 -*-
import requests
import codecs
import os
import jinja2
import base64

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


# Open a local binary file (here an image).

input_logo_path = os.path.join(dirname, "duck_logo.png")

with open(input_logo_path, "rb") as f:
    logo_data = f.read()
    print("Read duck_logo.png")


# Hello World LaTeX-on-HTTP request.

response = requests.post(
    "https://latex.ytotech.com/builds/sync",
    json={
        "compiler": "xelatex",
        "resources": [
            {"main": True, "content": latex_document,},
            {"path": "logo.png", "file": base64.b64encode(logo_data).decode("utf-8"),},
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
