import requests
import os

dirname = os.path.dirname(__file__)


# Open LaTeX template file.

latex_template_path = os.path.join(dirname, "template.tex")
with open(latex_template_path) as f:
    latex_template = f.read()


# Hello World LaTeX-on-HTTP request.

response = requests.post(
    "https://latex.ytotech.com/builds/sync",
    json={"resources": [{"content": latex_template,}]},
)


# Write the result to a file.

output_path = os.path.join(dirname, "output.pdf")

with open(output_path, "wb") as f:
    f.write(response.content)
    print("Written to output.pdf")
