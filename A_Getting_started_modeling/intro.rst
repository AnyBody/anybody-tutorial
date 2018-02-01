Introduction: Getting Started with Modeling
============================================

The objective of this tutorial is to give an understanding of more
complex models using a full body model. A model will be created using a
template and will be adapted to explain the reaction of the human body
to an environment.

Developing accurate models of the human body is an enormous task, and it
is not something each user can do from scratch. We often have to rely on
models other people have made, and if we keep improving and exchanging
them, we shall end up with an excellent supply of models that fit most
purposes. `*The AnyBody Managed Model
Repository* <https://www.anybodytech.com/software/model-repository-ammr/>`__
that has been described in a previous chapter is an attempt to provide
such a library. Additionally, there are templates available that allow
an easy start into a new model application.

These are some of the tasks you will want to accomplish with predefined
models:

-  To change the model pieces to fit your own purposes - preferably
   without tampering with the interior workings of the parts you are
   using.

-  To be able to combine existing body parts to larger models.

-  To be able to attach the parts you can find to model bits you
   construct yourself.

All this can be done very elegantly in the AnyScript language provided
you keep it in mind when you construct your models. The AnyBody Model
Repository applications and templates are built that way, and they
contain numerous examples of the technique. In short, it uses the
following elements of the language to make it happen:

1. Include files

2. Parameters

3. Equipping parts with their own interfaces

While there are many different ways models could be constructed to
obtain the modularity we are looking for, the AnyScript Model Repository
represents one very well-structured solution, and AnyBody Technology
strongly recommends following the structure of this library when new
models are developed.

When an existing application is similar enough to what you want to do to
form the basis of the new application, then you can just copy that
application and modify it as you want. But sometimes it will be clearer
to users to build their own models from the bottom-up. We will consider
the second situation and try to create a new model using templates.

This tutorial is based on version |AMMR_VERSION_SHORT| of the AnyBody Managed Model
Repository. Please notice that the repository models are subject to
frequent updates. The newest version of the AMMR will be packaged with
the latest version of the AnyBody Modeling System. Also, the demo models
provided in the AnyBody Modeling System may be updated compared to the
version used here.

With the AnyBody Modeling System, you already have a repository of
models available, for details, please see the AnyBody Assistant
available from the menu. 


.. rst-class:: without-title
.. seealso::
    **Next lesson:** With that done, please proceed to Lesson 1: :doc:`Starting with a new Model <lesson1>` using a template.

