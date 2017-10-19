Lesson 1: Basic Concepts
========================

.. note:: To follow this tutorial it is recommended first to watch the
    introductory video found in Help -> AnyBody Assistant, which visually
    demonstrates several important GUI features.

|AnyBody Assistent|

Let us begin by creating a new AnyScript model from scratch. On the menu
click File -> New from template… this will bring up a new window in
which you choose “Basic Main” and provide a “Target Name” (e.g.,
*NewModel*) and click OK.

|Editor NewModel.main.any|

The new file that opens up in the text editor contains a basic skeleton
for your model, based on a built-in template.

What are “Classes”?
-------------------

Let's have a look at what the system has generated for you. If we forget
about most of the text and comments, the overall structure of the model
looks like this:

.. code-block:: AnyScriptDoc
    
    Main = {
    
       AnyFolder MyModel = {
       }; // MyModel
    
       AnyBodyStudy MyStudy = {
       };
    
    }; // Main
    


What you see is a hierarchy of braces - just like in a C, C++, or Java
computer program. The outermost pair of braces is named "Main".
Everything else in the model goes between these braces. The name
assigned to a pair of braces in the script will show up as a
folder/directory in the Model Tree.

Right now, there are two other sections inside the Main braces: The
"AnyFolder MyModel" and the "AnyBodyStudy MyStudy". These are usually
the two core components of most AnyBody models.

The code creates two objects - MyModel & MyStudy - which perform very
specific actions. The software developers have already pre-built these
actions into templates that you can use to create these objects. **These
inbuilt object templates are also known as CLASSES - eg., AnyFolder,
AnyBodyStudy**.

The object named "MyModel" (and of type AnyFolder) is simply an
organizational folder for containing the entire model you are going to
build. Let us change the folder name “MyModel” to “ArmModel”.

The object named "MyStudy" (and of type AnyBodyStudy) is a collection of
simulation tasks that you want to perform with your model. The :doc:`*Study
of Studies* <../A_study_of_studies/intro>` tutorial
contains much more information about these subjects. For now, let's just
rename "MyStudy" to "ArmModelStudy".

**In the forthcoming AnyScript text we'll highlight each change by red.
Just make the changes in the file, and *don't forget to also change
other occurrences of “MyModel” to “ArmModel”* later in the file.**

What does this file contain so far?
-----------------------------------

Let's look a little closer at the contents of what is now the ArmModel
folder:

.. code-block:: AnyScriptDoc

    
       // The actual body model goes in this folder
        AnyFolder §ArmModel§ = {
    
       // Global Reference Frame
        AnyFixedRefFrame GlobalRef = {
    
         // Todo: Add points for grounding
         // of the model here
    
      }; // Global reference frame
    
         // Todo. Add the model elements such as
         // segments, joints, and muscles here.
    
      }; // §ArmModel§
    


The only actual model element in the ArmModel is the declaration of the
"AnyFixedRefFrame GlobalRef". All models need a reference frame - a
coordinate system - to work in, so the system has created one for you.

An AnyFixedRefFrame is a predefined data type you can use when you need
it. What you have here is the definition of an object of that type. The
object gets the name "GlobalRef", and we can subsequently refer to it
anywhere in the ArmModel by that name.

You will notice that there is a "to do" comment inside the braces of
this reference frame suggesting that you add points for grounding the
model. Don't do it just yet. We will return to this task later.

But here's an important notice: Everything you define in this tutorial
from now on is part of the ArmModel folder and should go between its
pair of braces. If you define something outside these braces that should
have been inside, then the necessary references between the elements of
the model will not work.

Loading an AnyBody model
------------------------

You should be ready to load the model now by pressing the |Loadbutton
image| icon in the toolbar or the F7 key.

This action will load whatever file is chosen in the text editor. If a
file is already loaded, the above action will simply reload the file
until you give another file loading priority by right-clicking its tab
and select “Load Model”.

|Load model right click menu|

You may get a similar message in the Output Window.

.. code-block:: none

    Loading Main : "C:\\...\\NewModel.main.any"
    Scanning...
    Parsing...
    Constructing model tree...
    Linking identifiers...
    Evaluating constants...
    Configuring model...
    Evaluating model...
    Loaded successfully.
    Elapsed Time : 0.063000

 

Basic troubleshooting
---------------------

If you mistype something, you will get an error message. A common
mistake is to forget a semicolon somewhere. Try removing the last
semicolon in the AnyScript file, and load again. You get a message
saying something like: 

.. code-block:: none

    ERROR(SCR.PRS11) : C:\\...\\NewModel.main.any(26) : 'EOF' unexpected Model loading skipped

First, there is a message ID, then a file location and finally the body
of the message. The former two are written in blue and underlined to
show the underlying active links. The file location is the line where
the bug was found by the system. If you click this link, the text cursor
will jump to the file and exact line where the error was found. Remember
that an error can sometimes be caused by something you mistyped earlier
in the file so that you actually have to change something elsewhere in
your model. Try clicking the error number ERROR(SCR.PRS11). This will
give you a little pop-up window with a complete explanation:

|Error popup dialog|

We now assume that you have removed the errors and have loaded the model
successfully.


.. rst-class:: without-title
.. seealso::
    **Next lesson:** If you are up to it, let's continue onward to :doc:`Lesson 2: Segments <lesson2>`.


.. |AnyBody Assistent| image:: _static/lesson1/image1.png
   :scale: 40%
.. |Editor NewModel.main.any| image:: _static/lesson1/image2.png
   :scale: 60%
.. |Loadbutton image| image:: _static/lesson1/image3.png
   :scale: 80%
.. |Load model right click menu| image:: _static/lesson1/image4.png
   :scale: 70%
.. |Error popup dialog| image:: _static/lesson1/image5.png
   :scale: 70%