Lesson 2: Adding FDK Features
=============================

What we have now is a standard inverse dynamics AnyBody model capable of
computing forces in a knee joint that is presumed to be a simple hinge.
Real knees are unfortunately not as simple as that. Mechanically
speaking, the difference between an idealized revolute knee and a real
knee lies in the source of the forces which hold the joint together.

An idealized knee joint does not allow any deviations from its hinge
motion, like if the tibia and femur were to start sliding on one
another. This is accomplished by joint reaction forces which will
enforce the zero sliding constraint, regardless of how large the
required forces may be.

The real knee does not work like that. The cartilage cushioning the
contact between the femoral condyles and the tibial plateau is elastic,
and so are the ligaments and menisci stabilizing the knee against free
sliding. Since the forces in these passive structures depend on their
deformation, zero deformation implies the absence of any stabilizing
force. In other words, the knee MUST deform a little to invoke these
stabilizing forces and retain its integrity.

Let us begin the steps that will allow AnyBody to compute this
deformation. We zoom in on the definition of the knee joint and change
the definition of its reaction forces:

.. code-block:: AnyScriptDoc

    AnyRevoluteJoint KneeJoint = {
      AnyRefFrame &Shank = .Shank.KneeCenter;
      AnyRefFrame &Thigh = .Thigh.KneeCenter;
      §
      // Prepare the joint for FDK: Define the reaction types in x and y
      // directions to be FDK-dependent. These reaction forces must then
      // be switched off and provided by some elastic element that we
      // define explicitly below.
      Constraints = {
        CType = {ForceDep, ForceDep, Hard, Hard, Hard};
        Reaction.Type={Off,Off,On,On,On};
      }§;
    };


Here we redefine one of the default properties of the joint: the
definition of constraints. As mentioned in “Getting Started: AnyScript
Programming, Lesson 3: Connecting segments by joints", connecting two
completely independent rigid segments with a joint arrests some or all
of the six degrees of relative motion freedom that existed between the
two.

In this manner, a revolute joint imposes five constraints of which the
first three are translational constraints (preventing relative sliding)
whose violation is resisted by the joint reaction forces and the latter
two are rotational constraints (preventing relative, out of plane
rotation) enforced by reaction moments.

The shank’s KneeCenter node - which is the joint’s default coordinate
system - has the *y* axis pointing proximally along the shank’s length
axis and the x axis pointing forward. These are the two directions in
which we’d like to introduce elastic stabilization of tibio-femoral
translation, so the first two components of the CType vector are changed
to the value ForceDep, which means that rather than being ‘Hard’
constraints, the forces are now defined by some elastic element, which
we shall introduce later. We are thus switching off the usual reaction
forces in those directions by setting the Reaction.Type vector.

Now let us add the necessary elasticity to the joint. This can be done
anywhere in the model, but we might as well place it just below the
joint:

.. code-block:: AnyScriptDoc

    // Knee joint. Notice that this is only going to be the nominal joint.
    // The actual position of the knee joint center will depend on the forces
    // acting upon it. Notice that we list the shank before the thigh. This
    // defines the knee joint in the shank coordinate system and we can
    // relate the reaction forces to the direction of the tibial plateau.
    AnyRevoluteJoint KneeJoint = {
      AnyRefFrame &Shank = .Shank.KneeCenter;
      AnyRefFrame &Thigh = .Thigh.KneeCenter;
      // Prepare the joint for FDK: Define the reaction types in x and y
      // directions to be FDK-dependent. These reaction forces must then
      // be switched off and provided by some elastic element that we
      // define explicitly below.
      Constraints = {
        CType = {ForceDep, ForceDep, Hard, Hard, Hard};
        Reaction.Type={Off,Off,On,On,On};
      };
    };
    §// Define springs in the knee, simulating the effect of cartilage
    // and ligaments.
    AnyForce KneeStiffness = {
      AnyKinLinear &lin = Main.MyModel.KneeJoint.Linear;
      F = {-1000*lin.Pos[0], -5000*lin.Pos[1], 0};
    };§


We are using the AnyForce class for this purpose. AnyForce in an
abstract force that works on any kinematic measure we define inside it.
In this case, we simply refer to the linear measure which tracks the
distance between the two joint nodes on each segment. In an idealized
joint, this measure will always be zero as long as AnyBody can
successfully enforce all the translational constraints, however since
the first two components of CType are set to ‘ForceDep’, they can now
vary and become non-zero.

The *x* corresponds to sliding of the condyle along the tibial plateau.
In this direction, we can perceive the elasticity as primarily being
provided by the rim of the meniscus and the cruciate ligaments.

The *y* direction is along the shank’s long axis and in this direction,
the elasticity is provided by the layer of cartilage between the tibial
plateau and the femoral condyles. The *z* axis points laterally but
since we are building a planar model of the knee, we leave it to be a
conventional hard constraint.

It is therefore likely that the stiffness in the *y* direction is
somewhat larger than in the *x* direction. We are going to define it
that way and also choose values that are much smaller than in the real
knee to get some nice, large deformations that are visually perceivable.
So, the definition of the actual force inside the AnyForce object looks
like this:

.. code-block:: AnyScriptDoc

    F = {-1000 * lin.Pos[0], -5000 * lin.Pos[1], 0};


As you can see, we simply specify the forces in the different directions
as mathematical functions of the Pos property of the lin measure. Pos
contains the actual linear displacements, and when we multiply those
with -1000 and -5000 respectively, we are generating spring forces that
are proportional and opposite to the translational deformation of the
joint. As discussed earlier, we have made the y direction stiffness five
times larger than the value for the *x* direction.

One of the beauties of the AnyScript language is that these expressions
can be as complicated as you want. So if you happen to know more
complex, realistic stiffness properties of the knee from a cadaver study
or from a detailed finite element model, then you could just as well
input those.

Let’s get the final part of the definition finalized. All that is
remaining is to tell the solver in AnyBody that it should apply
force-dependent kinematics to solve the problem. This is of course done
in the study section:

.. code-block:: AnyScriptDoc

    AnyBodyStudy Study = {
      AnyFolder &Model = .MyModel;
      Gravity = {0.0, -9.81, 0.0};
      tStart = 1;
      tEnd = 10;
      nStep = 100;
      §InverseDynamics.ForceDepKinOnOff=On;§
    };


That is all there is to it. The usual InverseDynamics operation will now
compute elastic deformations in the knee joint resulting from the
deformation of soft tissues in response to internal and external forces.
Go ahead and try it out. If something does not work, you can download a
functional model :download:`here <Downloads/DemoSimpleKnee2.any>`.

**TROUBLESHOOTING HELP**: Inverse dynamics arrives at values of the
force dependent degrees of freedom (corresponding to the flexible joint
constraints) where the resulting passive stabilizing forces and computed
muscle forces, place those degrees of freedom in static equilibrium.
This is achieved by a gradient sensing optimizer which iteratively tries
out different combinations of joint deformation and muscle force
magnitudes which fulfil the equilibrium and optimization criteria.

It may therefore be necessary to adjust optimization settings of the
AnyBodyStudy class such as “InverseDynamics.ForceDepKin.MaxNewtonStep”
and “InverseDynamics.ForceDepKin.Perturbation”. For example, a large
perturbation size implies a large finite-difference step for the knee
translation values when the optimizer computes gradients numerically. If
the knee stiffness was extremely non-linear, this gradient might not
reflect the local behaviour of the functions which the optimizer is
working with.

When using more anatomically realistic body models containing passive
spring-like ligaments, it is good to ensure that the ligaments are
calibrated to ensure that their resting length isn’t too short or long.
You can read more on calibration in “Muscle Modeling, Lesson 7:
Ligaments” and “Inverse Dynamics of Muscle Systems, Lesson 7:
Calibration”.

In the next lesson we investigate the results in more detail.


.. rst-class:: without-title
.. seealso::
    **Next lesson:** :doc:`lesson3`.