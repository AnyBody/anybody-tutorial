# Lesson2: Initial Conditions

Before we look at the InitialConditions operation, let us just notice
that when the model is loaded, the segments of the model are positioned
in space according to their definition in terms of the r0 and Axes0
properties in each segment's definition. These are called the load-time
positions.

In the figure below, the user has tried to position the forearm and the
upper arm approximately at the right positions and angles at load time.
This is always a good idea, but it is almost impossible to get them
completely in place, and it is not necessary. Indeed, in more
complicated models, you can often find the segments and muscles in a big
mess at load time. Typically, you will want to see what the model looks
like when it has been assembled correctly for time step 1. This is what
the InitialConditions operation is for.

:::{figure} _static/lesson2/image1.png
:alt: Load time positions
:scale: 100 %

The load-time positions of segments in a simple arm model. Notice that
the forearm and upper arm do not meet correctly at the elbow joint.\*
:::

When you run the InitialConditions operation, it will attempt to put the
model in the position is has at time = tStart. This may or may not be
possible, and in the development stages of a model, when the joints and
drivers are not yet fully defined, it is definitely not possible, and
this is the reason why the system does not do it automatically when you
load the model. Running the InitialConditions operation produces a
correctly assembled arm:

:::{figure} _static/lesson2/image2.png
:alt: After initial conditions
:scale: 100 %

The arm correctly assembled at the elbow by SetInitialConditions.
:::

Here's a more detailed explanation: The system must perform a
kinematical analysis to connect the model correctly at the joints. This
requires that the model is kinematically determinate. Another way of
expressing that is that there must be the correct number of - and
relationship between joints and drivers in the model. It usually takes
some iterations in the model development to get it right. During these
iterations it is useful to be able to load the model and see a picture
of it, and this is why the loading simply positions the segments where
the user placed them.

Instead of simply running the InitialConditions operation, you can also
single-step through it to see what it does. This is done by clicking the
"Step" button instead of the "Run" button.

:::{figure} _static/lesson2/image3.png
:alt: After initial conditions
:scale: 100 %

Picking the step button.
:::

The first step re-establishes the load-time conditions. This means that
it positions the model as it was when you loaded it. This is useful for
identification of kinematic problems. The second step positions the
segments honoring the joints. The third does not seem to do much, but it
is used for positioning muscles wrapping over surfaces. It is just not
visible in this simple model.

The InitialConditions study can be thought of as the first step of a
kinematic analysis, which will be the subject of {doc}`the next
lesson. <lesson3>`

:::{rst-class} without-title
:::

:::{seealso}
**Next lesson:** {doc}`lesson3`.
:::
