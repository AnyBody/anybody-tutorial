Lesson 1: Using References
==========================

AnyScript is really a programming language, and just like any other
programming language you can define variables and assign values to them.
For instance, you may write

.. code-block:: AnyScriptDoc

     AnyVar a = 10.0;
     AnyVar b = a;
    


Folders are also variables, and a folder definition can go like this:

.. code-block:: AnyScriptDoc

     AnyFolder MyFolder = {
        // A whole lot of stuff inside
     };
    


However, folders cannot be assigned like a and b above, so the following
is illegal:

.. code-block:: AnyScriptDoc

    AnyFolder MyFolderCopy = MyFolder;
    


In general, you can only do direct assignment of value variables, i.e.
variables containing numbers or collection of numbers. This assignment
is allowed:

.. code-block:: AnyScriptDoc

     AnyVector aa = {1,2,3};
     AnyVector bb = aa;
    


But folder assignments are not allowed. So how can you refer to large
portions of the model in just one assignment operation? The answer is
that you can refer by reference, and just about any assignment between
variables of compatible type will work:

.. code-block:: AnyScriptDoc

    AnyFolder &MyFolderCopy = MyFolder;
    


The ampersand, ``&``, in front of the variable name specifies that this is
a reference. What it means that MyFolderCopy will just point to
MyFolder, so whatever you do to MyFolderCopy will happen to MyFolder. It
is as simple as that. A pointer variable takes up very little space in
the computer because it does not copy the data it is pointing to.

This demo example illustrates some of the important uses of pointer
variables:
:download:`demo.creatingandreferringtoobjects.any <Downloads/demo.creatingandreferringtoobjects.any>`

Now, let's continue to :doc:`Lesson 2: Using Include Files <lesson2>`.