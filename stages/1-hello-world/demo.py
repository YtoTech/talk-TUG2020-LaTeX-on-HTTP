import requests
import os

dirname = os.path.dirname(__file__)


# Hello World LaTeX-on-HTTP request.

response = requests.post(
    "https://latex.ytotech.com/builds/sync",
    json={
        "resources": [
            {
                "content": r"""
                    \documentclass{article}
                    \begin{document}
                    Hello World
                    \end{document}
                """,
            }
        ]
    },
)


# Write the result to a file.

output_path = os.path.join(dirname, "output.pdf")
with open(output_path, "wb") as f:
    f.write(response.content)
    print("Written to output.pdf")
