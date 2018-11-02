# -*- coding: utf-8 -*-
from functools import lru_cache
from math import sqrt

import numpy as np
import scipy
from anypytools import AnyPyProcess
from anypytools.macro_commands import Load, OperationRun, Dump, SetValue
from datetime import datetime


def run_model(saddle_height, saddle_pos, silent=False):
    """Run the AnyBody model and return the metabolism results"""
    macro = [
        Load("BikeModel2D/BikeModel2D.main.any"),
        SetValue("Main.BikeParameters.SaddleHeight", saddle_height),
        SetValue("Main.BikeParameters.SaddlePos", saddle_pos),
        OperationRun("Main.Study.InverseDynamics"),
        Dump("Main.Study.Output.Pmet"),
        Dump("Main.Study.Output.Abscissa.t"),
    ]
    app = AnyPyProcess(silent=silent)
    results = app.start_macro(macro)
    return results[0]


def objfun(x):
    saddle_height = x[0]
    saddle_pos = x[1]
    result = run_model(saddle_height, saddle_pos, silent=True)

    if "ERROR" in result:
        raise ValueError("Failed to run model")

    # Integrate Pmet
    pmet = np.trapz(result["Pmet"], result["Abscissa.t"])
    
    return float(pmet)


# =============================================================================
# Extract the objective function value after each iteration
objfun_history = []
designvar_history = []


def callbackf(x):
    print(x,objfun(x))
    objfun_history.append(objfun(x))
    designvar_history.append(x)


initial_guess = (0.7, -0.15)


# For more settings see:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html


def seat_distance_constraint(x):
    """ Compute contraint value which must be larger than zero"""
    return (sqrt(x[0] ** 2 + x[1] ** 2) - 0.66)

constaints = {"type": "ineq", "fun": seat_distance_constraint}
bounds = [(0.65, 0.73), (-0.22, -0.05)]

solution = scipy.optimize.minimize(
    objfun, initial_guess, constraints=constaints, bounds=bounds, method="SLSQP", callback=callbackf
)


print(solution)
