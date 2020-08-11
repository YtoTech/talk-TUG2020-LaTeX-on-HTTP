# TUG2020 talk on LaTeX-on-HTTP

Presentation material for the [LaTeX-on-HTTP]() talk at [TUG2020](https://tug.org/tug2020/).

## Slides

[Open Talk slides](slides.pdf)

## Demo code

### Navigate the demo

Look at the code progression from the demo [stages](stages/).

### Run the code

To run the demo code, you'll need:
* [Python](https://www.python.org/downloads/)
* [pipenv](https://pipenv.pypa.io/en/latest/) (or the [`requests`](https://requests.readthedocs.io/en/master/user/install/#install) and [`Jinja2`](https://jinja.palletsprojects.com/en/2.11.x/intro/#installation) packages installed)

With Pipenv, run the following command to install Python dependencies to run the demo:

```sh
pipenv install
```

Then you can run the demo:

```sh
pipenv run python demo.py
```

You can also run any intermediate step of the demo. For example for the _Hello world_ step:

```sh
pipenv run python stages/1-hello-world/demo.py
```

## Related resources

* LaTeX-on-HTTP: https://github.com/YtoTech/latex-on-http
* Interactive web demo: https://latex-http-demo.ytotech.com/

-------------

Yoan Tournade
