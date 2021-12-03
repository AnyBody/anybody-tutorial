# Lesson 4: Inverse Dynamics

The inverse dynamic analysis in AnyBodyStudy is at the heart of what the
AnyBody Modeling System does. An InverseDynamics operation is like the
Kinematics operation, except it is augmented with calculation of forces
in the system, i.e. kinetic or dynamic analysis.

Computing forces in a rigid body mechanical system is more difficult
than it may seem. In principle, resolving forces is a question of
setting up the equilibrium equations and solving them. But in mechanism
analysis in general and biomechanics in particular, there are several
complications. The system may very easily become statically
indeterminate, which means that there are not enough equilibrium
equations available to resolve the forces in the system. Another
complication is caused by the muscles in the system because they can
only pull. This constrains the space of possible solutions and adds a
fair bit of mathematical complexity to the problem.

In AnyBodyStudy, these complexities are handled with algorithms that
assume that the mechanical system is a musculoskeletal system. The
inverse dynamic solver basically deals with

- The statical indeterminacy of the musculoskeletal system
- Unilateral forces elements.

The class called AnyMechStudy does also contain an InverseDynamics
operation. This operations is far more simple and does not deal with
either of these problems. It simply solves the very basic inverse
dynamics problem of a general simple mechanical system, namely to solve
the dynamic equilibrium equations for a equal amount of unknown forces,
the so-called reaction forces.

To conclude this tutorial, please try InverseDynamics operations in the
arm model, {download}`arm2d.any <Downloads/arm2d.zip>`, and the slider crank
mechanism,
{download}`demo.SliderCrank3D.any <Downloads/Demo.SliderCrank3D.any>`. In both
case, you will now see forces being calculated, i.e. forces that are
non-zero in the output. But please also notice how the slider crank
study is defined with simpler AnyMechStudy whereas the arm model uses
AnyBodyStudy.

If you use AnyMechStudy in the arm model, the analysis will stop with a
failure, because it cannot balance the mechanism. This is because the
AnyMechStudy does not recognize the muscles as unknown forces. It
regards them as applied (known) forces (which will be zero because their
value is not defined anywhere) and therefore there are no forces to
balance the moments exerted about the elbow and shoulder joints by the
external load.

Much more details about inverse dynamics of musculoskeletal systems are
found {doc}`the special tutorial on the topic <../MuscleRecruitment/Inverse_dynamics>`.
