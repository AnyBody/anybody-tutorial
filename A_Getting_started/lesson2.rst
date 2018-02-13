Lesson 2: Controlling the Posture
=================================

The Standing Model has been set up to have its posture defined by the
specification of anatomical angles in the joints. 

These specifications have been collected in one of the model files, **Mannequin.any**. Scroll
down your model file until you come to the point where the Mannequin.any
file is included. Here is a step by step description:

Mannequin file structure
------------------------

.. code-block:: AnyScriptDoc

    ...

    // Using your own Mannequin.any file in the Model folder of your model
    #path BM_MANNEQUIN_FILE "Model\Mannequin.any"

    ...


**This line means that your model will use this Mannequin.any file located in the Model folder, 
relative to the location of the main file that you're viewing.**

**Double-clicking the file name in the editor window after loading
your model opens the mannequin file opens up in a new tab.** Then you see the
following structure. (In the interest of legibility we have removed many
of the lines):

.. code-block:: AnyScriptDoc

     AnyFolder Mannequin = {
       AnyFolder Posture = {
         AnyFolder Right = {     
         };
         AnyFolder Left = {
         };
       };
      
     AnyFolder PostureVel= { 
        AnyFolder Right = {     
         };
         AnyFolder Left = {
         };
       };
     };


**The section between each pair of braces is said to be a Folder**, with all variables defined therein forming the folder contents.

**Once loading is complete, you can scan this folder structure in the Model tree** on the left of your screen.

All contents of this file are contained within the Mannequin folder. There are sub-folders for 
postural join angles (in degrees), angular velocities (in degrees/second), and right and left-hand sides of the body.

Changing any of the joint angles and reloading the model, will change the model's posture at load time. To start with, ensure that the contents of the Right
and Left sub-folders are as follows.

.. code-block:: AnyScriptDoc
    
    ...
    AnyFolder Right = {
    
        //Arm
        AnyVar SternoClavicularProtraction=-23; //This value is not used for initial position
        AnyVar SternoClavicularElevation=11.5; //This value is not used for initial position
        AnyVar SternoClavicularAxialRotation=-20; //This value is not used for initial position
        AnyVar GlenohumeralFlexion =-0;
        AnyVar GlenohumeralAbduction = 10;
        AnyVar GlenohumeralExternalRotation = 0;
        AnyVar ElbowFlexion = 0.01;
        AnyVar ElbowPronation = -20.0;
        AnyVar WristFlexion =0;
        AnyVar WristAbduction =0;
        
        //Leg
        AnyVar HipFlexion = 0.0;
        AnyVar HipAbduction = 5.0;
        AnyVar HipExternalRotation = 0.0;
        AnyVar KneeFlexion = 0.0;
        AnyVar AnklePlantarFlexion =0.0;
        AnyVar SubTalarEversion =0.0;
        
    ...


If you scroll down, you'll see that the contents of left-hand side folder are set to be equal
to those from the Right folder, in order to create a symmetric posture. 

**This is an important feature of the AnyScript language: Instead of numbers, you can create references to other variables and mathematical expressions wherever necessary.**

To create a non-symmetric posture, simply replace some of the variable references in the Left folder with numbers of your choice.

Scrolling further below, you will find the PosturVel folder. This is organized exactly like Posture, but the numbers here specify
joint angular velocities in degrees per second. For now, please leave all the values in this folder as zero.

Now it is time to perform an analysis.

Running an analysis
-------------------

On the left-hand side of the screen, you find a tall, narrow window with
tabs on its left edge. Please select the Operations tab and find the
following:

|RunApplication|

What you see are different operations, i.e. simulations which the system
can perform on the model. Select the “RunApplication” and click the
“Run” button on the toolbar (image below):

|Run toolbar|

You will see the model move slightly into position and you are finally
awarded the following message:

1.0) Inverse dynamic analysis...

1.10) ...Inverse dynamic analysis completed

You have just completed your first analysis with an AnyBody model. In the
next lesson, we will examine the effects of posture on the results
: :doc:`Lesson 3: Reviewing analysis
results <lesson3>`.

.. |RunApplication| image:: _static/lesson2/image1.png
   
.. |Run toolbar| image:: _static/lesson2/image2.png
   