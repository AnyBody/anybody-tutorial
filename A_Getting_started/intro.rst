Getting Started
===============

.. toctree::
   :hidden:

    Lesson 1 <lesson1>
    Lesson 2 <lesson2>
    Lesson 3 <lesson3>


The AnyBody Modeling System caters to a wide range of users with very
different modeling needs. Some may simply want to load and run an
existing model, some may need to modify an existing or build their own
model bottom-up. These tutorials serve as a common starting point for
all such new users.

.. rubric:: The AnyBody Managed Model Repository (AMMR)

The AnyBody software comes along with an inbuilt model repository. This
is the AMMR, a collection of human body models that are based on the
latest research studies.

**Most importantly, it comes with a set of demo models** (eg: MoCap
based walking model, cycling etc.) that can serve as a useful learning
tool, or even as the foundations for own modeling studies. As a new
user, you are likely to find yourself in one of the following scenarios.

-  Loading a model from AMMR and changing simple parameters like the
   applied load or the posture.

-  Modifying one of the existing motion capture models from the
   repository to your own lab/experimental setup.

-  Modifying a model from the repository with some similarity to what
   you want. For instance, a normal bicycle model could be changed into
   a recumbent bike.

-  Constructing a body model and its environment bottom-up, like when
   you’re modeling an animal or making a new detailed joint model. Such
   bottom-up modeling is described in the tutorial "`Getting Started:
   AnyScript
   Programming <../A_Getting_started_anyscript/intro.docx>`__".

These various levels of model building complexity are covered in
":doc:`Getting Started:
Modeling <../A_Getting_started_modeling/intro>`" in the ":doc:`Making
Things Move <../Making_things_move/intro>`" tutorial.

.. rubric:: Goal for this tutorial


We will take the top-down approach in this tutorial and use the model
repository to accomplish the following:

1. Create a new standing model using the Human Standing template model,
   load it in a given posture, and practice how to use the Model View
   functions.

2. Learn how to change the posture of the human model.

3. Run the inverse dynamics analysis of the model and review the
   analysis results. Change the posture of the human model and see how
   it will give us a different result.

This entire tutorial relies heavily on using the AMMR described above.

.. rubric:: Setup the AMMR

Before you continue you must unpack the entire repository and save it on
your hard disk. To get a copy of the AMMR press the Demo tab in the
AnyBody assistant dialog box.

|AnyBody assistent|

The Demo tab will install a copy of the AMMR in your documents folder by
default. It is good practice to create a second local copy of the AMMR
so that you do not overwrite the existing AMMR folder by accident.

.. rubric:: AMMR structure

With the repository unpacked, let us take a brief look at its structure.
Please open a file manager and navigate to the place you unpacked the
repository. You should see a folder structure that includes the
following subfolders:

“Application” includes the models that can be loaded into AnyBody and
actually simulate some biomechanical situation, such as cycling, lifting
a box or propelling a wheelchair. “Body” contains models of body parts
and collections of body parts which are used by the applications. For
instance, Body includes a lumbar spine model, which is used by all the
applications needing an upper body.

A closer inspection of the Application branch reveals that it has three
subfolders:

The “Beta” folder contains models that are unfinished, but they may
still be useful. The “Examples” folder contains many models doing
different activities of daily living, and it is very likely that you
will be able to find a model doing something similar to what you want.
The “Validation” folder contains models that have been used for
validation purposes, typically by comparison of the model predictions
with experimental measurements.

With that knowledge, you are all set to go, and you can proceed with
:doc:`*Lesson 1: Creating the standing model* <lesson1>` using
template.

.. |AnyBody assistent| image:: _static/intro/image1.png
   :width: 6.68750in
   :height: 4.62500in