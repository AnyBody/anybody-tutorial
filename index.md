---
sd_hide_title: true
---
# Overview!

::::{grid}
:reverse:
:gutter: 3 4 4 4
:margin: 1 2 1 2

:::{grid-item}
:columns: 12 4 4 4

```{image} _static/AnyBodyTutorials.svg
:width: 200px
:class: sd-m-auto
```

:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-fs-5

```{rubric} Tutorials for the AnyBody Modeling System
```

The Tutorials cover a wide range of topics and are a good place to start learning how to
do musculoskeletal modeling in the AnyBody Modeling System.

```{button-ref} A_Getting_started/intro
:ref-type: doc
:color: primary
:class: sd-rounded-pill

Get Started
```

:::

::::



You can find the available tutorials in the sidebar. The tutorials are ordered in a suitable sequence for
new users who are unfamiliar with AnyBody, but this sequence may not be optimal
for you depending on your background and interests.

It is recommended to start with the four Getting Started tutorials.



```{rubric} Other resources!
```
[AnyScript forums](https://forum.anyscript.org/)
: The Forum is a place to give and get help from other users. Get help and and learn from the experts.


[Wiki](https://github.com/AnyBody/support/wiki)
: The wiki has a wealth of information, tips&tricks and FAQs for working with the AnyBody Modeling System.


[AMMR documenation](https://anyscript.org/ammr-doc)
: Browse documentation on AMMR models and learn about possible settings

[The AnyBodyTech channel](https://www.youtube.com/user/anybodytech)
: AnyBody Technology Youtube channel watch webcasts and other videos

[AnyPyTools](https://anybody-research-group.github.io/anypytools-docs/)
: AnyPyTools is a toolkit for working with the AnyBody Modeling System (AMS) from Python.

[GitHub repositories](https://github.com/anybody)
: The repositories on Github has large and small models under development. Download cutting edge models and join development.





```{rubric} Help make tutorials better!
```

We highly appreciate any contributions to Tutorials!

If you find typos, missing links or anything else wrong, don't hesitate to fix
it your self or report the problem. Just click the link header bar. 

```{image} ./_static/suggest_edits.png
:alt: Suggesting edits
:class: bg-primary
:width: 30%
:align: center
```

More details are in the {doc}`how to contribute section <contributing>`.



```{toctree}
:caption: Getting started
:includehidden: true
:maxdepth: 2
:numbered: 1
:hidden: true
:titlesonly: true

First steps <A_Getting_started/index>
A_Getting_started_anyscript/index
A_Getting_started_modeling/index
A_Getting_started_AMMR/index

```

```{toctree}
:caption: Tutorials
:includehidden: true
:maxdepth: 2
:hidden: true
:titlesonly: true

A_study_of_studies/index
Making_things_move/index
MuscleRecruitment/index
ForceDependentKinematics/index
Muscle_modeling/index
The_mechanical_elements/index
Finite_element_analysis/index
AnyExp4SOLIDWORKS/index
Scaling/index
Validation_of_models/index
Parameter_studies_and_optimization/index
Posture_and_movement/intro
```

```{toctree}
:caption: Internals of AnyBody
:includehidden: true
:maxdepth: 2
:hidden: true
:titlesonly: true

Interface_features/index
Advanced_script_features/index
Troubleshooting_anyscript/intro
```


```{toctree}
:caption: Others
:maxdepth: 1
:hidden: true


contributing
legal
```