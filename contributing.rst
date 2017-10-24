Contributing
####################


We highly appreciate any contributions to Tutorials! 

If you find typos, missing links or anything else wrong, don't hesitate to fix it. 

It is as easy as forking `the repository on GitHub
<https://github.com/AnyBody/anybody-tutorial>`__ , making your changes, and
issuing a pull request.  If you have any questions about this process don’t
hesitate to ask.


Building the tutorials
**********************

The tutorials are created using `sphinx <http://www.sphinx-doc.org/>`_, a tool for software
documentation. Sphinx converts ReStructuredText(.rst) files into html, pdf or other
formats. ReStructuredTexts are simple text files with extra markup to define headers
and formating. Having the tutorials as ReStructuredText makes it easy to control
changes to the documents and ensure consistent style. 

The tutorials are automatically build with sphinx when commits are 
pushed to the github repository. The process is handle by
`Travis CI, here <https://travis-ci.org/AnyBody/anybody-tutorial>`_. 
If the build fails, for example because of 
wrong reST syntax etc, the Pull Request can not be merged.

Once the pull request is accepted on Github and the changes are merged to the
master branch the tutorials becomes availble online. 

The newest released version of the tutorials are available at: 

* https://anyscript.org/tutorials

The newest development version (current master branch) is availble at:

* https://anyscript.org/tutorials/dev


Building the tutorials locally
==============================

Even though the tutorials are build automatically, it is also possible to build
them locally to view the layout and see results before pushing changes to the
server. It is often not necesssary when making small fixes to existing
tutorials. But when writing major new sections it nice to view how things look. 

The easiest way to install needed packages tools, is to have the `Anaconda Python distribution <https://www.continuum.io/downloads>`_. 

Then run the following commands to install the necesssary packages. 

.. code-block:: bat

    c:\path\to\anybody_tutorials> conda install -c conda-forge sphinx pandoc cloud_sptheme pygments_anyscript
    c:\path\to\anybody_tutorials> pip install sphinxcontrib-fulltoc

Once the packages are install run this command to build the tutorial files. 

.. code-block:: bat

    c:\path\to\anybody_tutorials> make html

Once complete open the file: ``build/html/index.html`` in a browser to view 
the result.


Short ReStructuredText guide
****************************

There are plenty of guides on ReStructuredText available on Google. So here is just a 
quick run through over some of the reST concepts which are important for the tutorials.

Paragraphs
==========

Any block of text is a paragraph. Paragraphs must be separated by one 
or more blank lines. Identation matters in reST, so lines of the same 
paragraph must be left aligned to the same indentation.

* one asterisk: :literal:`*text*` for emphasis (italics),
* two asterisks: :literal:`**text**` for strong emphasis (boldface), and
* backquotes: :literal:` ``text`` ` for code samples.

There are also options for :subscript:`subscript` and :superscript:`superscript` plus more:

.. code-block:: rest

    :subscript:`subscript` and :superscript:`superscript`

Headers
=======

.. code-block:: rst

    Chapter header
    **************

    Section header
    =============

    Subsection header
    -----------------


Lists and Quote-like
====================

.. code-block:: rst

    - A bullet list item
    - Second item

      - A sub item

    # Numbered list
    # It has two items

Quotes are just paragraph indented more than the surrounding paragraphs. 

.. code-block:: rst

    This is an ordinary paragraph, introducing a block quote.

        "Don't panic"

        -- HG2G


Highlighting code
=================
Highlighting AnyScript code snippets is also supported, using the ``pygments_anyscript`` 
extension to pygments. 

AnyScript highlighting is started using the ``code-block``
directive and specifing ``AnyScriptDoc`` as the highlighting language. 

.. role:: red
.. raw:: html

    <style> .red {color:red} </style>

The ``AnyScriptDoc`` is highlighter specifically for the documentation in sphinx. 
It can highlight AnyScript code even if the syntax is not correct, and any code 
fenced with **§** is :red:`§marked in red§`.

Here is an example

.. code-block:: none

    .. code-block:: AnyScriptDoc

        AnyBodyStudy Study = {
            AnyFolder &Model = .Model;
            Gravity = {0.0, §-9.81§, 0.0};
        }; // End of study

Which gives the following:

.. code-block:: AnyScriptDoc

    AnyBodyStudy Study = {
        AnyFolder &Model = .Model;
        Gravity = {0.0, §-9.81§, 0.0};
    }; // End of study

Valid values for the highlighting languages are:

* ``none``: no highlighting
* ``AnyScript``: AnyScript (Syntax must be valid)
* ``AnyBodyDoc`` AnyScript (Allows invalid syntax)
* ``python/c++/ruby`` Different known programming languages
* ``rest`` ReStructuredText
* ... and any other `lexer alias that Pygments supports
  <http://pygments.org/docs/lexers/>`_.


