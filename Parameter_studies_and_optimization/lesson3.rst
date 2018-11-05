Optimization Studies in Python
==============================

The optimization study introduces in the preceding lesson used AnyBody's builtin
facilities for optimizing. Sometimes that is not enough, either because the
objective functions depends on data that is not easily included in AnyBody, or
because a different solver is needed. 

In this tutorial we use an external optimizer together with AnyBody. The example is
based on the model from the :doc:`previous lesson <lesson2>` but uses an optimizer
in the Python programming language. But the same could be achived with other
tools like MatLab etc. 

Requirements
------------

Before we begin you need to install the Anaconda Python distribution. It is free and comes
with most of the necessary packages preinstalled.

* Download and install Anaconda Python Distribution (>3.6)

We also need one additional Python library (`AnyPyTools
<https://anybody-research-group.github.io/anypytools-docs/>`__) which will make
it easier to work with AnyBody from Python.

AnyPyTools can be easily installed from the command prompt. Open the Anaconda
command prompt and type: 

.. code-block:: bat

     conda config --add channels conda-forge
     conda install anypytools

Running a model from Python
---------------------------

If you didn't complete the model from :doc:`lesson 2 <lesson2>`, you can download the
:download:`finshed model here <Downloads/OptimBike2-lesson3.zip>`. 

For the external optimizers to work, we need a way to run AnyBody models from
Python and record the results of the simulations. There are more information on
how to do this in the `documentaion for AnyPyTools
<https://anybody-research-group.github.io/anypytools-docs/>`__. So here we will
just show how the code looks and not discuss the details.

First we create a new Python file ``optimize.py`` and place next to our main file ``BikeModel2D.main.any``.
Within the file we create a Python function to run the AnyBody simulation. 

.. code-block:: python

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
           Dump("Main.Study.Output.Pmet"),
           Dump("Main.Study.Output.Abscissa.t"),
       ]
       app = AnyPyProcess(silent=silent)
       results = app.start_macro(macro)
       return results[0]

    result = run_model(0.66, -0.16)
    print(result["Main.Study.Output.Pmet"])


The functions ``run_model()`` takes ``saddle_height`` and ``saddle_pos`` as input and return
the ``Pmet`` metabolism output. 

The two last lines are just for testing. They call the function and prints the result. 
Let us test it by running the python file: 

.. code-block:: bat

     python optimize.py
     [****************100%******************]  1 of 1 completeTotal time: 0.6 seconds
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



Defining the objective function
-------------------------------

The next step is to define the objective function. The objective function should
take an array of design values as input and return the objective function value.
In :doc:`Lesson 2 <lesson2>` the objective function was the time integral of the
metabolism variable. So we will do the same: 

So remove the last two lines and add a new function like this. 

.. code-block:: python

    
    def objfun(x):
        saddle_height = x[0]
        saddle_pos = x[1]
        result = run_model(saddle_height, saddle_pos, silent=True)
    
        if "ERROR" in result:
            raise ValueError("Failed to run model")
    
        # Integrate Pmet
        pmet = scipy.integrate.trapz(result["Pmet"], result["Abscissa.t"])
        
        return float(pmet)
    
    pmet = objfun([0.66, -0.16])
    print(pmet) 


Now let us try running the file again: 

.. code-block:: bat

     $ python optimize.py
     505.329399532772


Setting up the optimization study
---------------------------------

Finally, we wrap things up by calling the ``scipy.optimize.minimize``....

.. code-block:: python

    def seat_distance_constraint(x):
        """ Compute contraint value which must be larger than zero"""
        return (math.sqrt(x[0] ** 2 + x[1] ** 2) - 0.66)
    
    constaints = {"type": "ineq", "fun": seat_distance_constraint}
    bounds = [(0.65, 0.73), (-0.22, -0.05)]
    initial_guess = (0.7, -0.15)
    
    solution = scipy.optimize.minimize(
        objfun, initial_guess, constraints=constaints, bounds=bounds, method="SLSQP"
    )
    
    
    print(solution)
