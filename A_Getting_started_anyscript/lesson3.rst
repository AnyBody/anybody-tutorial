Lesson 3: Connecting Segments by Joints
=======================================

.. note:: Here's an AnyScript file to start on if you have not completed the
    previous lesson: :download:`demo.lesson3.any <Downloads/demo.lesson3.any>`.

Some quick theory
-----------------

You can think of joints in different ways. We tend to perceive them as
providers of freedom, which is correct compared to a rigid structure.
However, in dynamics, it is often practical to perceive joints to be
constraining movement rather than releasing it. A system of two
completely independent segments will have 2 x 6 = 12 degrees of freedom
in total. When you join them, you take some of these degrees of freedom
away. The different joint types distinguish themselves by the degrees of
freedom that are relinquished by the rigid body system.

The global reference frame
--------------------------

Not knowing where stuff is in space can be very impractical, and so the
first thing to do is usually to ground the mechanism somewhere. Perhaps
you remember these lines somewhere at the top of the AnyScript code:

.. code-block:: AnyScriptDoc

    
      AnyFixedRefFrame GlobalRef = {
    
         // Todo: Add points for grounding
         // of the model here
    
      }; // Global reference frame
    


This is actually the definition of a global reference frame for our
model. It is similar to a segment in the sense that we can add point
nodes to it for attaching joints and muscles. Let’s do just that. Again
you can insert the objects with the object inserter or save time by
simply cutting and pasting the following lines into your model:

.. code-block:: AnyScriptDoc

         AnyFixedRefFrame GlobalRef = {
          §AnyDrawRefFrame DrwGlobalRef = {};
           AnyRefNode Shoulder = {
             sRel = {0,0,0};
           };
           AnyRefNode DeltodeusA = {
             sRel = {0.05,0,0};
           };
           AnyRefNode DeltodeusB = {
             sRel = {-0.05,0,0};
           };
           AnyRefNode BicepsLong = {
             sRel = {0.1,0,0};
           };
           AnyRefNode TricepsLong = {
             sRel = {-0.1,0,0};
           };§
        }; // Global reference frame


The first line, "AnyDrawRefFrame ..." merely displays the global
reference system in the graphics window. Let us cut down on the display
size and change its color to distinguish it from the yellow segments:

.. code-block:: AnyScriptDoc

          AnyDrawRefFrame DrwGlobalRef = {
            §ScaleXYZ = {0.1, 0.1, 0.1};
            RGB = {0,1,0};§
          };


The remaining lines define point nodes attached to the global reference
system.

Creating a revolute joint
-------------------------

With all the necessary point nodes available, we can now connect the
upper arm to the global reference frame through a "shoulder" joint.
While a real shoulder is a very complex mechanism with several joints,
this is a planar 2-D model, where we will define it as a simple hinge.
We create a new folder to contain the joints and define the shoulder:

.. code-block:: AnyScriptDoc

           }; // LowerArm
         }; // Segs folder
    
       §AnyFolder Jnts = {
    
           //---------------------------------
           AnyRevoluteJoint Shoulder = {
            
             AnyRefNode &GroundNode = ..GlobalRef.Shoulder;
             AnyRefNode &UpperArmNode = ..Segs.UpperArm.ShoulderNode;
    
             Axis = z;
    
           }; // Shoulder joint
    
       }; // Jnts folder§


Why use ‘.’ and ‘..’ in AnyScript? - Relative folder paths
----------------------------------------------------------

A hinge is also called a revolute joint, and this is what the type
definition "AnyRevoluteJoint" means. The joint connects two segments,
and it needs to know which points on each segment to connect. For this
purpose, we have the lines

.. code-block:: AnyScriptDoc

           AnyRefNode &GroundNode = ..GlobalRef.Shoulder;
           AnyRefNode &UpperArmNode = ..Segs.UpperArm.ShoulderNode;


They define the two connected nodes on the GlobalRef and UpperArm
segments . Notice the two dots in front of the names. They signify that
the GlobalRef and Segs folders are defined two levels outside the folder
where we are in the Model Tree. If you neglected the two dots, then
AnyBody would search for the two objects in the Shoulder folder and fail
to find them. This "dot" system is quite similar to the system you may
know from directory structures in Dos, Windows, Unix, or just about any
other computer operating system.

Reference objects and the ‘&’ symbol
------------------------------------

But there is more to it than that. You can see that the Shoulder point
on GlobalRef has been given the local name of "GroundNode". This means
that, within the context of this joint object, we can hereafter refer to
the point as "GroundNode" instead of the longer external reference.

Another specialty is the '&' in front of the local name. If you have
some experience with C++, you will realize that GroundNode is merely a
reference (a pointer) to GlobalRef.Shoulder rather than a copy of it. So
if GlobalRef.Shoulder moves around, Shoulder.GroundNode will keep up
with those changes in position. Hit F7 to load the model again to make
sure that the definition is correct.

Customizing the revolute joint
------------------------------

We then have:

.. code-block:: AnyScriptDoc

           Axis = z;


While each rigid body segment has a reference frame which moves along
with it, nodes on a segment can have their own reference frames. These
frames would also move along with the segment, but their orientations
can be made to differ from the segmental frame. The relative orientation
between the two frames can be user-defined and is held fixed thereon.

The AnyBody system is always three-dimensional, even when our model is
two dimensional. The property Axis = z simply specifies that both
segments connected by that joint will rotate about the z axis of the
node at the joint. Does that sound complicated?

In other words, the z-axes of the nodes on either connected segment will
always be parallel, and so the mechanism will rotate in the plane
perpendicular to these axes. The out-of-plane relative orientation of
the two segments can be adjusted by rotating the reference frames of the
nodes being connected. This is relevant if you want one of the segments
to rotate about some skewed axis.

.. caution:: The first of the two
    nodes declared in the joint (in this case ``GroundNode``) becomes the
    default reference frame for the joint. When directly accessing the
    post-simulation values of constraint reaction forces etc., you must
    remember to interpret them in the joint’s default reference frame.

Creating a revolute elbow joint
-------------------------------

We need an elbow joint before we are finished: the elbow. The definition
is completely parallel to what you have just seen, but we shall use one
of the handy tools to define the references. The skeleton of the elbow
joint is as follows:

.. code-block:: AnyScriptDoc

    AnyFolder Jnts = {
           //---------------------------------
        AnyRevoluteJoint Shoulder = {
            Axis = z;
            AnyRefNode &GroundNode = ..GlobalRef.Shoulder;
            AnyRefNode &UpperArmNode = ..Segs.UpperArm.ShoulderNode;
        }; // Shoulder joint

        §AnyRevoluteJoint Elbow = {
            Axis = z;
            AnyRefNode &UpperArmNode = ;
            AnyRefNode &ForeArmNode = ;
        }; // Elbow joint§
    }; // Jnts folder


As you can clearly see, the nodes in the Elbow joint are not pointing at
anything yet. In this simple model it is easy to find the relative path
of the pertinent nodes on the upper arm and the forearm, but in a
complex model, it can be difficult to sort these references out. So the
system offers a tool to help you.

Absolute folder path (and some useful tips)
-------------------------------------------

If you click the model tab in the tree view on the left-hand side of the
editor window, then the tree of objects in the loaded model appears. All
model components can be found in this tree including the two nodes we
are going to connect in the elbow. Click to place the cursor just before
the semicolon in the &UpperArmNode definition in the Elbow joint. Then
expand the tree as shown below.

|Model tree ElbowNode|

When you right-click the ElbowNode, you can select **"Insert object
name"** from the context menu. This writes the full path of the node
into the Elbow joint definition where you placed the cursor. Notice that
this method inserts the absolute and not the relative path. Repeat the
process to expand the ForeArm segment and insert its ElbowNode in the
line below to obtain this:

.. code-block:: AnyScriptDoc

           AnyRevoluteJoint Elbow = {
             Axis = z;
             AnyRefNode &UpperArmNode = §Main.ArmModel.Segs.UpperArm.ElbowNode§;
             AnyRefNode &ForeArmNode =  §Main.ArmModel.Segs.ForeArm.ElbowNode§;
           }; // Elbow joint


It seems like everything is connected now. So why do we still get the
annoying error message when we reload the model?::

    Model Warning: Study 'Main.ArmStudy' contains too few kinematic
    constraints to be kinematically determinate.

The explanation is that we have connected the model, but we have not
specified its position yet. Each of the two joints can still take any
angular position, so there are two degrees of freedom whose kinematic
states need to specified before AnyBody can determine the mechanism's
position. This is taken care of by kinematic drivers.



.. rst-class:: without-title
.. seealso::
    **Next lesson:** They are one of the subjects of :doc:`Lesson 4: Imparting Movement with Drivers <lesson4>`.


.. |Model tree ElbowNode| image:: _static/lesson3/image1.png
   :scale: 70%
   