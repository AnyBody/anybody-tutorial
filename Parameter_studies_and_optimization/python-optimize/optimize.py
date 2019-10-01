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


constraints = {"type": "ineq", "fun": seat_distance_constraint}
bounds = [(0.61, 0.69), (-0.22, -0.05)]
initial_guess = (0.68, -0.15)

solution = scipy.optimize.minimize(
    objfun, initial_guess, constraints=constraints, bounds=bounds, method="SLSQP"
)

print(solution)
