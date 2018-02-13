Lesson 4: Imparting movement with Drivers
=========================================

.. note:: Here's an AnyScript file to start on if you have not completed the
    previous lesson: :download:`*demo.lesson4.any* <Downloads/demo.lesson4.any>`.

If you have completed the three previous lessons, you should have a
model with an upper arm grounded at the shoulder joint and connected to
a forearm by the elbow. What we want to do now is to make the arm move.

|ModelView Arm2D initial load|

**Can an arm without muscles move? Well, in reality no, but AnyBody simulations use
the inverse dynamics technique, where we prescribe motion first and then deduce
the values of muscle forces which produce the motion.**

Measures & drivers
-------------------

We need to specify the motion for two degrees of freedom (DOF) of our arm mechanism, because it has hinge joints at the
shoulder and at the elbow. 

- **Measures** are AnyBody objects which literally measure the value of a specific DOF within the model.

- **Drivers** are AnyBody objects which constrain the value of a measure to a constant value or a mathematical function of time. **Drivers** essentially assemble and impart motion to your mechanisms.

In this model, we therefore need two drivers, to specify motions for the two DOF. We therefore also need two measures, 
which we will chose to be measures of the shoulder and elbow joint angle values.

.. note:: **There is no unique way to choose measures that need to be driven (i.e. constrained). What's important is that 
    the measures represent the total number of DOFs in your model.** For example in this arm model, we could have used the X and Y coordinates
    of the end-point of the ForeArm segment (the wrist), instead of the shoulder and elbow angles. 
    **Creating driver constraints for more than 2 DOFs in this case would over-constrain the model and lead to errors.**

Creating a constant velocity joint motion 
------------------------------------------

Let's create a new folder and define two drivers:

.. code-block:: AnyScriptDoc

         }; // Jnts folder
    
         §AnyFolder Drivers = {
           //---------------------------------
           AnyKinEqSimpleDriver ShoulderMotion = {
             AnyRevoluteJoint &Jnt = ..Jnts.Shoulder;
             DriverPos = {-100*pi/180};
             DriverVel = {30*pi/180};
           }; // Shoulder driver
           //---------------------------------
           AnyKinEqSimpleDriver ElbowMotion = {
             AnyRevoluteJoint &Jnt = ..Jnts.Elbow;
             DriverPos = {90*pi/180};
             DriverVel = {45*pi/180};
           }; // Elbow driver
         }; // Driver folder§


The folder contains two objects named "ShoulderMotion" and "ElbowMotion", belonging to the
"AnyKinEqSimpleDriver" class. 

**All AnyBody drivers only work on the measures that are supplied to them. The "AnyKinEqSimpleDriver" used in this case, constrains 
the measure positions to a given value at time = 0 ("DriverPos") and changes this position at constant velocity thereon ("DriverVel").**

Since the measures supplied to the above drivers are joints, the drivers produce joint rotation.
But the same driver class could be used to drive translations, for instance the cartesian
position of a point.

.. note:: Since these drivers drive angles, the units are radians and
    radians/sec.


**The following lines assign the shoulder and elbow joint angle measures to the respective drivers.
Standard AnyBody joints created using classes such as "AnyRevoluteJoint", "AnySphericalJoint" etc. automatically function as measures.
More customized measures can be created using classes such as "AnyKinLinear", "AnyKinRotational" etc. 
(see** :doc:`*this lesson* <../The_mechanical_elements/lesson4>`).:

.. code-block:: AnyScriptDoc

           AnyRevoluteJoint &Jnt = ..Jnts.Shoulder;


and

.. code-block:: AnyScriptDoc

           AnyRevoluteJoint &Jnt = ..Jnts.Elbow;


Just like in :doc:`*Lesson 3* <lesson3>`, these lines also
use the reference operator '&' to point the local variable "Jnt" towards the 
actual shoulder/elbow joint objects existing in a different folder

Since "Jnt" is a reference, it will automatically update as the joint state changes during motion.


Running simulations - making things move!
-----------------------------------------

Re-load the model by hitting F7, and you should see the message "Loaded successfully" with NO
warning messages about lacking kinematic constraints this time. You're now ready to get this model moving.

**The model tree window has a second tab labelled “Operations”.
This window shows a curated version of the model tree, by only displaying 
the "Studies" or simulation objects created in your model.**


|Operations ArmStudy|

Try expanding the ArmStudy root. You will get a list of the study types
that the system can perform. "Study" is a common name for operations you
can perform on a model. Try clicking the KinematicAnalysis study. With
the buttons in the Operations window, you can now execute various types
of analysis.

The Execute toolbar above the operations tree contains three buttons
|Model tree toolbar Execute buttons|:

-  **Run operation**: Starts or pauses the chosen operation. Shortcut
   F5.

-  **Step operation**: Advances to next step of operation, typically a
   time step. Shortcut F6. 

-  **Stop operation**: Sets the operation back to its initial position.
   You must reset before you start a new analysis that was previously
   aborted. Shortcut F4 

Replaying a simulation
----------------------

All these functions are also available from the main frame toolbar
|Execute toolbar| and the menu Operation.

Now, try your luck with the **KinematicAnalysis** study and the Run
button. What should happen is that the model starts to move as the
system runs through 101 timesteps of the study.

When the analysis in finished, you can use the replay panel to replay
the model as you do in a movie player.

|Replay toolbar|

Since we have no muscles so far, kinematic analysis is really all that
makes sense. A kinematic analysis is pure motion. The model moves, and
you can subsequently investigate positions, velocities, and
accelerations. But no force, power, energy or other such things are
computed. These properties are calculated by the
**InverseDynamicAnalysis**.

Fetching simulation results
---------------------------

The analysis has 101 time steps corresponding to a division of the total
analysis time into 100 equal pieces. The total time span simulated in
the analysis is 1 sec. These are default values because we did not
specify them when we defined the ArmModelStudy in the AnyScript model.
If you want more or fewer time steps or a longer or shorter analysis
interval, all you have to do is to set the corresponding property in the
ArmModelStudy definition. When you click "Run", all the time steps are
executed in sequence, and the mechanism animates in the graphics window.

So far, the model was merely a two-bar mechanism moving at constant
joint angular velocities. However, the system has actually computed
information that might be interesting to investigate. **All the analysis
results are available in the ArmModelStudy branch of the tree view**.

Directly under the ArmModelStudy branch, you find the **Output branch**
where all computed results are stored. Notice that the Output branch
contains the same folders we defined in the AnyScript model: GlobalRef,
Segs, and so on. In the Segs folder you find ForeArm, and in that a
branch for each of the nodes we defined on the arm. Try expanding the
branch for the HandNode. It contains the field 'r' which is the position
vector of the node. We might want to know the precise position of the
HandNode at each time in the analysis, for instance, if we were doing an
ergonomic study and wanted to know if the hand had collided with
anything on its way.

If you double-click the 'r' node, the instantaneous position vector
(depending on where your replay slider is) of the hand node for each
time step is dumped in the message window at the bottom of the screen.

Plotting simulation results
---------------------------

However, we often prefer to plot our results. With the default layout,
this feature is located in the same window as Model View under the tab
called “Chart 1”. You can also open it from the pull-down menus by
choosing View -> Charts -> ...

This gives you a new window structured just like the editor window with
a tree view to the left, but with an empty field for graphing results.

The tree in this window is much like the tree in the editor window
except that some of the data has been filtered out so that you mainly
see the parts of the tree that are relevant in terms of results or
output. You can expand the tree in the chart window through ArmStudy and
Output until you come to the HandNode. When you pick the property 'r',
you get three curves corresponding to the movement of the three
Cartesian coordinates of this node during the simulated time period. Try
holding the mouse pointer over one of the curves for a moment. A small
label with the global name of the data of the curve appears. All data
computed in AnyBody can be visualized this way.

|Chart view HandNode|

So far, we have only the kinematic data to look at. Before we can start
the real biomechanics, we must add some muscles to the model.

.. rst-class:: without-title
.. seealso::
    **Next lesson:** This is the subject of :doc:`*Lesson 5: Definition of muscles and external forces* <lesson5>`.



.. |ModelView Arm2D initial load| image:: _static/lesson4/image1.png
    
.. |Operations ArmStudy| image:: _static/lesson4/image2.png
    
.. |Model tree toolbar Execute buttons| image:: _static/lesson4/image3.png
    
.. |Execute toolbar| image:: _static/lesson4/image4.png
    
.. |Replay toolbar| image:: _static/lesson4/image5.png
    
.. |Chart view HandNode| image:: _static/lesson4/image6.png
   