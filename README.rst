Active Learning with Jupyter Notebooks
======================================

This is a Python 3 library to read/write cells programmatically in
`Jupyter notebooks <https://jupyter.org/>`_ which anticipates upcoming
`collaborative <https://groups.google.com/forum/#!topic/jupyter/r7QSObF5YSg>`_
features in Jupyter.

We use this at `O'Reilly Media <https://www.oreilly.com/>`_ for
notebooks used to manage machine learning pipelines.
That is to say, *machines and people collaborate on documents*, 
implementing a "human-in-the-loop" design pattern:

-  people adjust hyperparameters for the ML pipelines
-  machines write structured "logs" during ML modeling/evaluation
-  people run ``jupyter notebook`` via SSH tunnel for remote access

For more info about use cases for this library and *active learning* 
in general, see the `JupyterCon 2017 <https://jupytercon.com/>`_ talk
`Humans in the loop <https://conferences.oreilly.com/jupyter/jup-ny/public/schedule/detail/60058>`_


Example Usage
-------------

The following script generates a Jupyter notebook in the ``test.ipynb``
file, then runs it:

::

    python test.py
    jupyter notebook

Then launch the ``test.ipynb`` notebook and from the ``Cells`` menu
select ``Run All`` to view results.

NB: whenever you use the ``put_df()`` function to store data as a 
`Pandas dataframe <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_
be sure to include ``import pandas as pd`` at some earlier point in
the notebook.


Dependencies and Installation
-----------------------------

This code has dependencies on:

-  `nbformat <https://github.com/jupyter/nbformat>`_
-  `pandas <https://pandas.pydata.org/>`_

To install from `PyPi <https://pypi.python.org/pypi/nbtransom>`_:

::

    pip install nbtransom


To install from this Git repo:

::

    git clone https://github.com/ceteri/nbtransom.git
    cd nbtransom
    pip install -r requirements.txt


Kudos
-----

`@htmartin <https://github.com/htmartin>`_
`@esztiorm <https://github.com/esztiorm>`_
`@fperez <https://github.com/fperez>`_
`@odewahn <https://github.com/odewahn>`_
