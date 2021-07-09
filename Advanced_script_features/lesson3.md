# Lesson 3: Mathematical Expressions

One of the definite advantages of a modeling language like AnyScript is
that mathematical expressions become a natural element in model
construction. By means of mathematical expressions in models you can
make the model parametric, enable scaling in various ways, and create
dependencies between elements.

In AnyScript you can in principle write a mathematical expression
involving variables and references to other objects and to time anywhere
in an object definition where you would otherwise use a number.
Furthermore, AnyScript handles scalar numbers, vectors, matrices, and in
fact tensors of arbitrary dimensions.

Unlike most programming languages, definition sequence does not have any
significance in an AnyScript model. This means that variables can refer
to other variables that are created further down in the model like this:

```AnyScriptDoc
AnyVar b = a;
AnyVar a = 10;
```

Instead of the sequence of **definition**, AnyScript variables depend on
the sequence of **evaluation**. Some expressions are can be evaluated
when the model is loaded, while others have to wait for certain
operations to complete. For instance, a muscle force is not known until
an InverseDynamicAnalysis operation is performed. The systems keeps
track of when everything is evaluated and will complain if you try to
use a variable prematurely.

For instance, kinematic analysis is the first step of an inverse dynamic
analysis, so you can make an external force or a muscle strength depend
on a position. This is because forces and muscles strengths are not used
until after the kinematic analysis when the positions have been
evaluated. However, you cannot make a position depend on a muscle force
because muscle forces are always computed after positions.

Much of the capability of the mathematical expressions is demonstrated
in the example
{download}`Demo.MathExpressions.any <Downloads/Demo.MathExpressions.any>`.
