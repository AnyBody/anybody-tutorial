# Personalizing Your Model

Musculoskeletal models must be adaptable to sizes and anatomy of various individuals
to be useful for product design and to be used for applications, where high geometric
accuracy is required, e.g. surface articulations and patient-specific pre-operative
planning. A general method for scaling musculoskeletal models has been implemented
in the AMMR. It allows the usage of built-in, user-defined anthropometric scaling
laws as well as individual segment morphing.

:::{seealso}
The AMMR documentation for instructions how to configure the model to
use built-in scaling laws and provide general anthropometric information.
:::

This tutorial introduces an advanced procedure of model personalization by means of
nonlinear morphing for both, bone surface and relevant soft tissue attachment sites,
to take a subject-specific shape. In this example, bone geometries segmented from medical
images will be used to demonstrate how geometrically accurate subject-specific models can
be constructed.

```{rubric} Tutorial content
```

```{toctree}
:maxdepth: 1

Lesson 1: Scaling based on medical images <lesson3>
Lesson 2: Including a custom scaling function into your model <lesson4>
```
