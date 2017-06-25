#!/usr/bin/env python
# encoding: utf-8

import nbformat as nbf
import nbtransom as nbt
import sys


def create_nb ():
    """
    old-school approach, for comparison

    NB: a notebook can also be run at the command line with:
       `jupyter nbconvert --execute --inplace test.ipynb`
    """
    nb = nbf.v4.new_notebook()

    text = "# My first automagic Jupyter Notebook"

    code = """\
%pylab inline
hist(normal(size=2000), bins=50);
"""

    cell_text = nbf.v4.new_markdown_cell(text.strip())
    cell_code = nbf.v4.new_code_cell(code.strip())
    cell_data = nbt.create_data_cell("foo", { "x": [ 2.31, 12.34 ], "y": 3 })

    nb["cells"] = [ cell_text, cell_code, cell_data ]
    return nb


if __name__ == "__main__":
    # define some example data...
    foo = [1, 3, 4, 5, 9, 8, 5, 2, 7, 0, 1, 3, 4, 5, 9, 8, 5, 2, 7, 0, 1, 3, 4, 5, 9, 8, 5, 2, 7, 0, 1, 3, 4, 5, 9, 8, 5, 2, 7, 0, 1, 3, 4, 5, 9, 8, 5, 2, 7, 0, 1, 3, 4, 5, 9, 8, 5, 2, 7, 0]

    x = {
        'orm:Deep_Learning': [
            [ "9780128104095", "B9780128104088000158.xhtml", "Deep Learning for Medical Image Analysis" ],
            [ "9781491924570", "ch06.html", "Deep Learning" ],
            [ "9780128104095", "B9780128104088000110.xhtml", "Deep Learning for Medical Image Analysis" ],
            [ "9781491924570", "ch03.html", "Deep Learning" ],
            [ "9781491971444", "ch01.html", "Machine Learning for Designers" ],
        ],
        'orm:Edu_Psychology': [
            [ "9781522505136", "978-1-5225-0513-6.ch004.xhtml", "Handbook of Research on Serious Games for Educational Applications" ],
            [ "9781522505310", "978-1-5225-0531-0.ch008.xhtml", "Innovative Practices for Higher Education" ],
            [ "9781522504801", "978-1-5225-0480-1.ch011.xhtml", "Knowledge Visualization and Visual Literacy" ],
        ],
        'null': [
            [ "9780123973085", "CHP005.html", "General Aviation Aircraft Design" ],
            [ "9780132761772", "ch20.html", "Scala for the Impatient" ],
            [ "9780132885478", "ch05.html", "Basic Principles and Calculations in Chemical Engineering" ],
        ]
    }

    # create a notebook manually via `nbformat` API, then read/write
    # some of the notebook's cells
    nb = create_nb()
    nbt.set_val(nb, nbt.get_var_name(foo), foo)

    lib_cell = nbt.create_code_cell("imports", "import pandas as pd")
    nb.cells.append(lib_cell)

    nbt.put_df(nb, "my_df", [ [1, 2], [3, 4] ], ["a", "b"])
    nbt.set_val(nb, nbt.get_var_name(x), x, formatter=nbt.min_pretty)

    file_name = "test.ipynb"
    nbt.save_nb(nb, file_name)

    # re-read the whole enchilada
    nb = nbt.open_nb(file_name)
    print(nbt.min_pretty(nb.cells, level=1))

    # i can haz `5`?
    derived_foo = nbt.get_val(nb, nbt.get_var_name(foo))
    assert derived_foo[3] == foo[3]
