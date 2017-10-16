Introduction to Validation
============================

Somewhere on the way to the decision of using a biomechanical model you
have probably asked yourself the question: Will I be able to trust the
results I get?

This is a very relevant question indeed. Computer models are just that:
a model of reality, and there will always be some amount of
approximation involved. The good news is that with careful modeling and
the 'right model for the right problem' you can get very close to
reality with the AnyBody Modeling System because it is tailor-made
for the complexity of musculoskeletal systems.

Investigation of the accuracy of the model goes under the term
'validation', and this is what we will be dealing with in this tutorial.
More precisely, you can expect to find the following in this tutorial:

1. Clever ideas for validation methods.

2. Examples of models that have been validated previously.

Several `previous
webcasts <https://www.anybodytech.com/anybody.html?fwd=webcasts>`__ have
presented validation studies and results, the most recent one was
“Seated Human Model Validation”.

What Can Go Wrong?
------------------

Well, lots, actually. But it is helpful to try to categorize the matter
into a few sources of error.

-  Errors sources in the model

-  Errors sources in the basic assumptions

-  Errors sources in the software

Errors Sources in the Model
---------------------------

An AnyScript model contains a lot of data, and they are all infested
with some degree of inaccuracy: Geometry and mass properties of
segments, assumptions about the kinematics and reactions of joints,
properties and attachment points of muscles, and much more.

It has been said about biomechanics that there is a 'right' model for
each case. For instance, there is little point in using a complex muscle
model if you have little information about the muscle properties, for
instance fiber lengths and pennation angles. Another consideration is
the level of subject-specific accuracy. Is the purpose of the model to
simulate a particular individual, or should it reflect a cross section
of the population?

Model Data Uncertainties
~~~~~~~~~~~~~~~~~~~~~~~~

In general, the models in the `*AnyScript Managed Model
Repository* <http://www.anybodytech.com/anybody.html?fwd=modelrepository>`__
are based on data reported in the literature. They often come from
studies of one or few subjects or cadavers, and the data has little or
no statistical significance. You will find the references of the data
listed in the comments in the individual AnyScript files. However, the
fact that a specific fiber length or muscle insertion point has been
found in an individual cadaver does not mean that the value is valid for
every individual or even typical.

In conclusion there is no guarantee that the values in models from any
library are valid for the case you may want to analyse, and the best
advice is to approach the matter with a critical mind. If results look
suspicious in some part of the model, consider whether this can be due
to the model input. Some typical cases are:

-  The muscle primarily responsible for carrying the load over a joint
   does not have sufficient strength. This can happen even in
   well-tested models if an unusual loading, posture or support
   condition that was never tested before is imposed.

-  The model has attained a posture in which the moment arm of a primary
   muscle erroneously becomes zero or negative. This can happen, for
   instance, if a wrapping muscle slides off its wrapping surface. The
   variation of muscle length with the joint angle reflects the moment
   arm, so if the moment arm is too small, then the muscle will have
   little length variation when the joint is articulated.

-  If the model makes use of a muscle model with stength/length
   variation and passive stiffness, then a tendon length that is poorly
   calibrated to the model can cause malfunction of its muscle. A too
   long tendon will cause its muscle to have little or no strength in
   its usual operation interval. A too short tendon will cause a muscle
   to excert passive force and likely cause muscles on the other side of
   the joint to work more than they are supposed to. Please notice that
   AnyBody has facilities for calibrating tendon lengths. :doc:`*The muscle
   modeling tutorial* </Muscle_modeling/intro>` has
   in-depth information about these issues.

Boundary Conditions
~~~~~~~~~~~~~~~~~~~

Input to inverse dynamics is movement and boundary conditions, and these
can have more influence on the result than most inexperienced modelers
would expect. In fact, they are the principal source of error in many
models. The human body is remarkable in its ability to make the best of
the available supports, and this often creates the illusion that
supports are solid while they really are not.

Consider a hand gripping a handle firmly. Apparently, the hand is
rigidly connected to the handle, and you might be inclined to define a
model connection between the two elements reflecting this notion.
However, hands have limited strength to hold on with, and handle
surfaces have limited friction to offer. If the model contrary to
reality offers an effortless connection between the hand and the handle,
then the model is likely to exploit this as we shall see later.

Movement Data
~~~~~~~~~~~~~

Recorded movement input such as motion capture data is usually in the
form of positions over time. But inertia forces in the model are derived
from accelerations, and to obtain accelerations, the positional data
must be differentiated twice thus increasing noise and inaccuracies by
two orders of magnitude. This is the topic of the first lesson of this
tutorial, starting at the bottom of this page.

Errors Sources in the Basic Assumptions
---------------------------------------

As mentioned a couple of times already, the AnyBody Modeling System is
based on inverse dynamics. This means that - for a given point in time -
the system solves the equilibrium equations and resolves the interior
muscle and joint forces. Since these time steps are solved independently
of each other, the state can in principle shift abruptly from one step
to the next, whereas, in reality, a change of muscle tone requires a bit
of time. Force development in a muscle is the result of an electric
signal from the central nervous system, which starts a chemical process
in the muscle and eventually leads to contraction. All this is done
within a few milliseconds, and inverse dynamics disregards this small
time delay. It means that if the movement is very quick and the system
predicts very rapid changes of muscle activation, then the result may
not be realistic.

Another possible source of error is the distribution of force between
the muscles. The body has more muscles than strictly necessary to carry
most loads, so is infinitely many different combinations of muscle
forces will balance the external loads. The way AnyBody picks the right
one is by an optimality criterion. The system presumes that the body
wants to make the best of its resources. The user has some amount of
control over this criterion, but in its basic form it is a minimum
fatigue criterion that distributes the loads as evenly as possible
between the muscles taking their individual strengths into account.
Please refer to :doc:`*A Study of
Studies* </A_study_of_studies/intro>` for more detailed
information.

So the system basically presumes that the body has the knowledge and the
desire to activate muscles optimally. This is supported by a lot of
research, but the precise criterion employed by the body is a matter of
continuous discussion. Furthermore, the ability to instantly choose the
optimal muscle recruitment most likely requires that the movement is
skilled and that the required changes of muscle activation are not
faster than the electro-chemical process of muscle contraction can
accommodate.

Errors in the Software
----------------------

All software has bugs, and very probably this is also the case for the
AnyBody Modeling System. However, in terms of muscle recruitment, the
validity of the software was validated independently in 2004 in a Ph.D.
thesis by Erik Forster from the University of Ulm, Germany. The thesis
is available from the list of `publications in the AnyScript
Forum <https://www.anybodytech.com/anybody.html?fwd=publications>`__.
The basic idea was to program an independent special-purpose application
for gait simulation and then compare it to an identical gait model in
AnyBody. If the results were identical, it would prove the correctness
of the algorithms of both systems. The result was that the output data
of the two systems were identical on all but a tiny fraction of the
data. Closer investigation of this tiny fraction revealed that different
algorithms - although mathematically similar - can produce slightly
deviating results due to round-off errors.

When compared to the modeling errors and approximations due to the
recruitment assumptions, errors in the software are much less likely to
disturb the result of the computation significantly.

Methods of Validation
---------------------

The expression 'garbage in - garbage out' is very much valid for
biomechanical simulation. The quality of the output can never be better
than the input. This means that the first step of any validation is to
check the quality of the input. Input comes in the form of movements and
applied forces, where the former is the more difficult. A rough check of
the specified movements can be obtained by running a kinematic analysis
and charting the positions, velocities and above all accelerations of
characteristic points and segments in the model as illustrated for the
rowing model above. Notice that proximal body parts tend to be heavier
than distal body parts, so larger accelerations are plausible in the
distal parts.

Gravity = 9.81 m/s^2 is a good measure to compare your values to. If the
accelerations oscillate or attain unrealistic values, then the input
positional information definitely needs careful reviewing and probably
smoothing with a low-pass filter.


.. rst-class:: without-title
.. seealso::
    **Next lesson:** :doc:`Kinematic input validation <Kinematic_input>`. 
