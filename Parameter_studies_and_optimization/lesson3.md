# Optimization Studies in Python

The optimization study introduced in the preceding lesson used AnyBody's builtin
facilities for optimizing. Sometimes that is not enough, either because the
objective functions depends on data that is not easily included in AnyBody, or
because a different solver is needed.

In this tutorial we use an external optimizer together with AnyBody. The example
is based on the model from the {doc}`previous lesson <lesson2>` but uses an
optimizer from the [Scipy](https://scipy.org/) python library. The same
could also have been achived with other optimization frameworks (like [NLopt](https://nlopt.readthedocs.io/en/latest/), or languages (like [MatLab](https://www.mathworks.com/products/matlab.html)).

## Requirements

Before we begin you need to install the Anaconda Python distribution.
It is free and comes with most of the necessary packages preinstalled.

- [Download and install Anaconda Python Distribution (>3.6)](https://www.anaconda.com/download/)

We also need one additional Python library (AnyPyTools) which will make it
easier to work with AnyBody from Python. [AnyPyTools](https://anybody-research-group.github.io/anypytools-docs/) can be easily
installed from the command prompt. Open the Anaconda command prompt and type:

```bat
conda config --add channels conda-forge
conda install anypytools
```

## Example Python script

First we show the full Python program used in this tutorial.
Secondly, we will go through and explain the different sections in the file.

```{code-block} python
:linenos: true

 import math
 import scipy

 from anypytools import AnyPyProcess
 from anypytools.macro_commands import Load, OperationRun, Dump, SetValue


 def run_model(saddle_height, saddle_pos, silent=False):
     """Run the AnyBody model and return the metabolism results"""
     macro = [
         Load("BikeModel2D.main.any"),
         SetValue("Main.BikeParameters.SaddleHeight", saddle_height),
         SetValue("Main.BikeParameters.SaddlePos", saddle_pos),
         OperationRun("Main.Study.InverseDynamics"),
         Dump("Main.Study.Output.Pmet_total"),
         Dump("Main.Study.Output.Abscissa.t"),
     ]
     app = AnyPyProcess(silent=silent)
     results = app.start_macro(macro)
     return results[0]


 def objfun(designvars):
     """Calculate the objective function value"""
     saddle_height = designvars[0]
     saddle_pos = designvars[1]
     result = run_model(saddle_height, saddle_pos, silent=True)

     if "ERROR" in result:
         raise ValueError("Failed to run model")

     pmet = scipy.integrate.trapz(result["Pmet_total"], result["Abscissa.t"])

     return float(pmet)


 def seat_distance_constraint(designvars):
     """Compute contraint value which must be larger than zero"""
     return math.sqrt(designvars[0] ** 2 + designvars[1] ** 2) - 0.66


 constaints = {"type": "ineq", "fun": seat_distance_constraint}
 bounds = [(0.61, 0.69), (-0.22, -0.05)]
 initial_guess = (0.68, -0.15)

 solution = scipy.optimize.minimize(
     objfun, initial_guess, constraints=constaints, bounds=bounds, method="SLSQP"
 )

 print(solution)
```

A copy of the file can be {download}`downloaded here. <python-optimize/optimize.py>`
For now you can place the `optimize.py` next to your main file `BikeModel2D.main.any`.
If you didn't complete the model from {doc}`lesson 2 <lesson2>`, you can download the
{download}`finshed model here <Downloads/OptimBike2-lesson3.zip>`.

## Importing the necessary libraries

:::{role} python(code)
:language: python
:::

The first part of the code is the {python}`import` statements. They include the
libraries which is used by the code:

```{code-block} python
:linenos: true

 import math
 import scipy

 from anypytools import AnyPyProcess
 from anypytools.macro_commands import Load, OperationRun, Dump, SetValue
```

## Running a model from Python

For the external optimizers to work, we need a way to run AnyBody models from
Python and record the results of the simulations, so we need to create a
function to do this. There are more information on how to do this in the
[documentaion for AnyPyTools](https://anybody-research-group.github.io/anypytools-docs/). So here we will
just show how the code looks and not discuss the details.

```{code-block} python
:lineno-start: 8

 def run_model(saddle_height, saddle_pos, silent=False):
    """Run the AnyBody model and return the metabolism results"""
    macro = [
        Load("BikeModel2D.main.any"),
        SetValue("Main.BikeParameters.SaddleHeight", saddle_height),
        SetValue("Main.BikeParameters.SaddlePos", saddle_pos),
        OperationRun("Main.Study.InverseDynamics"),
        Dump("Main.Study.Output.Pmet_total"),
        Dump("Main.Study.Output.Abscissa.t"),
    ]
    app = AnyPyProcess(silent=silent)
    results = app.start_macro(macro)
    return results[0]

 result = run_model(0.66, -0.16)
 print(result["Main.Study.Output.Pmet_total"])
```

The function {python}`run_model()` takes {python}`saddle_height` and {python}`saddle_pos` as input
and return the `Pmet` metabolism output from AnyBody.

If you use an interactive Python environment (like [IPython](https://ipython.org/)) you could try calling the function directly to to
test it and investigate the results:

```ipython
In [4]: result = run_model(0.66, -0.16)
[****************100%******************]  1 of 1 completeTotal time: 0.8 seconds

In [5]: print(result.keys())
odict_keys(['Main.Study.Output.Pmet_total', 'Main.Study.Output.Abscissa.t'])

In [6]: print(result["Main.Study.Output.Pmet_total"])
[  17.20903341   73.49291834  209.58490241  379.67002659  559.57715608
  736.92126247  901.88875426 1045.75303378 1162.65470516 1248.32088806
 1299.79539032 1315.38241529 1294.6947524  1238.68684947 1149.59584772
 1030.78784505  886.60667952  722.43408728  547.1840971   368.64175002
  198.07134668   53.41928909   25.84379129   30.60376508   23.17442367
   24.30809055  139.3209062   292.35610808  469.73382854  649.02576552
  821.74094457  977.02863522 1108.05435136 1209.79739513 1278.65973442
 1312.31195028 1309.70451022 1271.1212895  1198.17227557 1093.68215448
  961.51890402  806.51623776  634.74029158  458.00117565  280.40563034
  121.30841553   21.54859903   28.97200722   26.82989147   17.2090334 ]
```

As we expected the output contains the `Main.Study.Output.Pmet_total` value for each timestep in our model.

## Defining the objective function

The next step is to define the objective function. The objective function should
take a list of design values as input and return the objective function value.
In {doc}`Lesson 2 <lesson2>` the objective function was the time integral of the
metabolism variable. So we will do the same here with Scipy's
{py:func}`scipy.integrate.trapz`: function.

```{code-block} python
:lineno-start: 23

 def objfun(x):
     saddle_height = x[0]
     saddle_pos = x[1]
     result = run_model(saddle_height, saddle_pos, silent=True)

     if "ERROR" in result:
         raise ValueError("Failed to run model")
     # Integrate Pmet_total
     pmet = scipy.integrate.trapz(result["Pmet_total"], result["Abscissa.t"])

     return float(pmet)
```

:::{note}
The function also checks the results for errors reported
by AnyBody and raises a {py:exc}`ValueError` exception if that happens.
There could be ways of handle error without failing but it is important to
handle model failures, otherwise they may go unnoticed or mess with the
optimization results.
:::

Again, we can run this function interactively to test it:

```ipython
In [9]: pmet = objfun([0.66, -0.16])

In [10]: print(pmet)
505.329399532772
```

Now we get the time integral of the `Pmet_total` variable as as single value,
and we are now ready to define the optimization process.

## Setting up the optimization study

We wrap things up by creating a function, {ref}`similar to what we did in AnyBody <optimization-contraint>`,
as well as defining the bounds and initial guess
for the design variables.

```{code-block} python
:lineno-start: 37

 def seat_distance_constraint(x):
     """ Compute contraint value which must be larger than zero"""
     return (math.sqrt(x[0] ** 2 + x[1] ** 2) - 0.66)


 constaints = {"type": "ineq", "fun": seat_distance_constraint}
 bounds = [(0.61, 0.69), (-0.22, -0.05)]
 initial_guess = (0.68, -0.15)
```

The documentation {py:func}`scipy.optimize.minimize` has more information on how to define bounds, contraints, tolerances, etc.

Finally, we call the `scipy.optimize.minimize` function run the optimizer. In this case we used the
[SLSQP](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html#optimize-minimize-slsqp) algorithm.

```{code-block} python
:lineno-start: 46

 solution = scipy.optimize.minimize(
     objfun, initial_guess, constraints=constaints, bounds=bounds, method="SLSQP"
 )
```

Let us try to do this interactively and look at the results.

```ipython
In [11]: solution = scipy.optimize.minimize(
    ...:     objfun, initial_guess, constraints=constaints, bounds=bounds, method="SLSQP"
    ...: )

In [12]: print(solution)
     fun: 503.57634385063113
     jac: array([39.43954086, -6.95677948])
 message: 'Optimization terminated successfully.'
    nfev: 56
     nit: 12
    njev: 12
  status: 0
 success: True
       x: array([ 0.65010304, -0.11386853])
```

And there we have it!
We can now take advantage of the many different algorithms and settings available for {py:func}`scipy.optimize.minimize`.
We could also use a different package or customize our own algorithm, constraints etc.

The possibilities are practically endless. The full example from this tutorial can be
\:download:\` downloaded here \<Downloads/python-optimize.zip>\`.

For more information regarding the `AnyPyTools` python package follow [this link.](https://anybody-research-group.github.io/anypytools-docs/)
You can also check out this [webcast.](https://www.youtube.com/results?search_query=anybody+webcast+batch)
