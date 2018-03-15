Lesson 2: Adjusting the Human Model
===================================

The next step is to configure the anatomy of your human model. The body model is divided into individual
body parts: legs, arms, and trunk.

.. todo:: Add a intersphinx link to AMMMR documentation on BM statments

**Body model configuration refers to the selection of limb segments to include, muscle model types,
scaling algorithms etc. These are done by setting switches known as Body model (BM) parameters. 
The configuration process is described in greater detail in this** `document <https://anyscript.org/ammr-doc/bm_config/index>`__




Body model configuration
-------------------------

For this pedal model, you will configure the human model as follows:

-  No muscles in the trunk segment.

-  Both the left and the right arms will be excluded.

-  The left leg segments will be excluded.

-  There will be no muscles in the right leg.

This is implemented by declaring the corresponding BM statements just before
the inclusion of the “HumanModel.any” file.

.. code-block:: AnyScriptDoc

    Main = {
      //#path BM_DRAWSETTINGS_FILE "Model\DrawSettings.any"
      
      #path BM_MANNEQUIN_FILE "Model\Mannequin.any"
      
      //-->BM statements
      // Excluding the muscles in the trunk segments
      §#define BM_TRUNK_MUSCLES _MUSCLES_NONE_§
      // Excluding the left arm segments
      §#define BM_ARM_LEFT OFF§
      // Excluding the right arm segments
      §#define BM_ARM_RIGHT OFF§
      // Excluding the left leg segments
      §#define BM_LEG_LEFT OFF§
      // Using the right leg as 'TLEM' model
      §#define BM_LEG_RIGHT _LEG_MODEL_TLEM1_§
      // Excluding the muscles in the right leg segments
      §#define BM_LEG_MUSCLES_RIGHT _MUSCLES_NONE_§  
      //<--
      
      // Include default human model
      #include "<ANYBODY_PATH_BODY>\HumanModel.any"
    

Loading the model (F7 key) should produce the following message:

.. code-block:: none

    Model Warning: Study 'Main.Study' contains too few kinematic constraints to be kinematically determinate.
    Evaluating model...
    Loaded successfully.
    Elapsed Time : 0.511000

The model view should show you the following picture:

|ModelView_Human_Adjusted|

The message warns about the model containing too few kinematic
constraints, which means that AnyBody lacks the full information needed to perform movement. 

This is because we are yet to specify how the human and environment are connected in this model.
This will be the topic of the next lesson.


.. rst-class:: without-title
.. seealso::
    **Next lesson:** Next up is :doc:`Lesson 3: Making Ends Meet <lesson3>`.



.. |ModelView_Human_Adjusted| image:: _static/lesson2/image1.png
   