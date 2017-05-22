# nbtransom

This is a Python 3 library to read/write cells programmatically in
[Jupyter notebooks](https://jupyter.org/), which anticipates upcoming
collaborative document features in Jupyter.


## Usage

To set up:
```
pip install -r requirements.txt
```

Then try running:
```
python nbtransom.py
```

Which will produce a notebook `test.ipynb`


## Background

We use this at [O'Reilly Media](https://www.oreilly.com/) for
notebooks used to manage machine learning pipelines, where machines
and people collaborate on documents.

This approach helps support examples in our work for what's being
called "human-in-the-loop" AI.

  * people adjust hyperparameters for the ML pipelines
  * machines write their “logs” during ML modeling and evaluation
  * people run `jupyter notebook` via SSH tunnel for remote access
