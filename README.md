# PyDict - English to Portuguese dictionary CLI written in Python

## 1 - What is it?

This is a simple command-line based python script that works as a English to Portuguese dictionary. You type in an English word and
if it matches any of the dictionary entries, you'll get the Portuguese translation for it. Currently supports around 15k words.

## 2 - How to run it?

Clone this repository. From its root folder, run `pip install -r requirements.txt`. Then, from the `pydict` internal folder, run
`python pydict.py`. This will start the CLI. To quit, you can simply type `GETOUT` in all caps or force-quit with `ctrl+c`.

## 3 - What else comes with it?

Within the `pydict` subfolder, you'll find a `data` and an `utils` folder. Inside utils, there are two Python scripts: `parsers.py`
and `helpers.py`. The first contains a couple of functions used to parse the raw dictionary files and convert them to a `.csv` file
and then read that `.csv` file again into a Python dictionary. Since the parsing functions are very inneficient and not well written
I recommend you just ignore them, since the repo already acompanies the converted `.csv`

The latter contains a lame (and as of now still broken) attempt at a Levenshtein distance function. Don't use it. Instead, PyDict
uses the [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) package to do fuzzy matching.

The `data` folder comes with another folder, `eng-por`, which contains the raw dictionary files, which are generously provided by 
[FreeDict](https://freedict.org/) and are already manipulated to facilitate the parsing process, and a `dict.csv` file which is
the already-parsed-and-converted English-Portuguese dictionary.
