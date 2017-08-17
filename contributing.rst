Contributing
####################


We highly encourage contributions to Tutorials! If you find typos, missing links or anything else wrong, don't hesite to fix it. 
It is as easy as forking `the repository on GitHub <https://github.com/AnyBody/anybody-tutorial>`__ , making your changes, and issuing a pull request. 

If you have any questions about this process don’t hesitate to ask.


Building the tutorials
**********************

The tutorials are build using `sphinx <http://www.sphinx-doc.org/>`_, a tool for software
documentation. Sphinx converts reStructuredText files into html, pdf or other
formats. reStructuredText are simple text files with extra markup to define headers
and formating. Having the tutorials as reStructuredText makes it easy to control
changes to the documents and ensure consistent style.

The tutorials are build automatically as soon as changes are accepted and merged in 
the repository. The system also deploys the html files to the anyscript.org home page. 

The newest released version of the tutorials are available at: 

* https://anyscript.org/tutorials

The newest development version (current master branch) is availble at:

* https://anyscript.org/tutorials/dev


Building the tutorials locally
==============================

Eventhought the tutorials are build automatically, it is also possible to build
them locally to view the layout and see results before pushing changes to the
server. It is often not necesssary when making small fixes to existing
tutorials. But when writing major new sections it nice to view how things look. 

The easiest way to install needed packages tools, is to have the [Anaconda
python distribution](https://www.continuum.io/downloads). 

Then run the following commands to install the necesssary packages. 

.. code-block:: bat

    c:\path\to\anybody_tutorials> conda install sphinx pandoc cloud_sptheme pygments_anyscript
    c:\path\to\anybody_tutorials> pip install sphinxcontrib-fulltoc

Once the packages are install run this command s to build. 

.. code-block:: bat

    c:\path\to\anybody_tutorials> make html

Once complete open the file: ``build/html/index.html`` in a browser to view 
the result.


Short reStructuredText guide
****************************

There are plenty of guides on reStructuredText available on Google. So here is just a 
quick primer for the reST concepts which are important for the tutorials.

Paragraphs
==========

Any block of text is a paragraph. Paragraphs must be separated by one 
or more blank lines. Identation matters in reST, so lines of the same 
paragraph must be left aligned to the same indentation.

* one asterisk: ``*text*`` for emphasis (italics),
* two asterisks: ``**text**`` for strong emphasis (boldface), and
* backquotes: ````text```` for code samples.

There is also options for :subscript:`subssscript` 
:superscript:`superscript` and more. See the 


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

Here is an example::

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
* ``rest`` reStructuredText
* ... and any other `lexer alias that Pygments supports
  <http://pygments.org/docs/lexers/>`_.


Building the tutorials
**********************

The tutorials are automatically build with sphinx when commits are 
pushed to the github repository. The process is handle by
`Travis CI, here <https://travis-ci.org/AnyBody/anybody-tutorial>`_. 
If the build fails, for example because of 
wrong reST syntax etc, the Pull Request can not be merged.

Once the pull request is accepted on Github and the changes are merged to the master 
branch the tutorials becomes availble online. 

The lates version of the tutorial which has git tag in the repository is always
available here: http://anyscript.org/tutorials/ A development version (the
master branch) can be viewed at  http://anyscript.org/tutorials/dev

