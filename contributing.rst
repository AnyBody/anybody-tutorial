.. highlight:: rest

##########
Contribute
##########

How to contribute
*****************

Every contribution is most welcome. See the `repository source files hosted 
on Github <https://github.com/AnyBody/anybody-tutorial>`_ 


The tutorials are build using ``sphinx``, which is a tool to create software
documentation. Sphinx converts reStructuredText files into html, pdf or other
formats. reStructuredText are simple text files with extra markup to define headers
and formating. Having the tutorials as reStructuredText makes it easy to control
changes to the documents and ensure consistent style.


Restructured text reference guide
*********************************

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

AnyScript highlighting is started using the :rst:dir:`code-block` 
directive and specifing ``AnyScriptDoc`` as the highlighting language

.. rst:directive:: ..code-block:: AnyScriptDoc

    Use it like this::

    .. code-block:: AnyScriptDoc

        AnyBodyStudy Study = {
            AnyFolder &Model = .Model;
            Gravity = {0.0, -9.81, 0.0};
        }; // End of study

Which gives the following:

.. code-block:: AnyScriptDoc

    AnyBodyStudy Study = {
        AnyFolder &Model = .Model;
        Gravity = {0.0, -9.81, 0.0};
    }; // End of study

.. role:: red
.. raw:: html

    <style> .red {color:red} </style>

Valid values for the highlighting language are:

* ``none``: no highlighting
* ``AnyScript``: AnyScript (Syntax must be valid)
* ``AnyBodyDoc`` AnyScript (Allows invalid syntax, code fenched with **§** are § :red:`marked red` §)
* ``python/c++/ruby`` Different known programming languages
* ``rest`` reStructuredText
* ... and any other `lexer alias that Pygments supports
  <http://pygments.org/docs/lexers/>`_.


.. code:: rest

    .. code:: AnyScriptDoc

        AnyFolder Model={
            AnyFolder &HumanModel=§.HumanModel.BodyModel§;


.. code:: AnyScriptDoc

    AnyFolder Model={
        AnyFolder &HumanModel=§.HumanModel.BodyModel§;



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

Building the tutorials locally
-----------------------------

It is also nice to be able to build the tutorials locally to view the layout 
before pushing to the server. It is often not necesssary when making small fixes 
to existing tutorials. But when writing major new sections it nice to view how 
things look. 

The easiest way to install the packages, is to have the Anaconda python distribution. 

Then run the following commands to install the necesssary packages. 

.. code-block:: conosle

    conda install sphinx pandoc cloud_sptheme pygments_anyscript
    pip install sphinxcontrib-fulltoc

Once the packages are install run this command s to build. 

.. code-block:: conosle

    C:\User\mel\anybody-tutorials> make html

Once complete open the file: ``build/html/index.html`` in a browser to view 
the result.
