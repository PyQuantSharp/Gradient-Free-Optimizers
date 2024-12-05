# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from typing import List, Dict

from ..search import Search
from ..optimizers import GeneticAlgorithmOptimizer as _GeneticAlgorithmOptimizer


class GeneticAlgorithmOptimizer(_GeneticAlgorithmOptimizer, Search):
    """
    A class implementing the **genetic algorithm** for the public API.
    Inheriting from the `Search`-class to get the `search`-method and from
    the `GeneticAlgorithmOptimizer`-backend to get the underlying algorithm.

    Parameters
    ----------
    search_space : dict[str, list]
        The search space to explore. A dictionary with parameter
        names as keys and a numpy array as values.
    initialize : dict[str, int]
        The method to generate initial positions. A dictionary with
        the following key literals and the corresponding value type:
        {"grid": int, "vertices": int, "random": int, "warm_start": list[dict]}
    constraints : list[callable]
        A list of constraints, where each constraint is a callable.
        The callable returns `True` or `False` dependend on the input parameters.
    random_state : None, int
        If None, create a new random state. If int, create a new random state
        seeded with the value.
    rand_rest_p : float
        The probability of a random iteration during the the search process.
    population : int
        The number of individuals in the population.
    offspring : int
        The number of offspring to generate in each generation.
    crossover : str
        The crossover operator to use.
    n_parents : int
        The number of parents to select for crossover.
    mutation_rate : float
        The mutation rate.
    crossover_rate : float
        The crossover rate.
    """

    def __init__(
        self,
        search_space: Dict[str, list],
        initialize: Dict[str, int] = {"grid": 4, "random": 2, "vertices": 4},
        constraints: List[Dict[str, callable]] = [],
        random_state: int = None,
        rand_rest_p: float = 0,
        nth_process: int = None,
        population=10,
        offspring=10,
        crossover="discrete-recombination",
        n_parents=2,
        mutation_rate=0.5,
        crossover_rate=0.5,
    ):
        super().__init__(
            search_space=search_space,
            initialize=initialize,
            constraints=constraints,
            random_state=random_state,
            rand_rest_p=rand_rest_p,
            nth_process=nth_process,
            population=population,
            offspring=offspring,
            crossover=crossover,
            n_parents=n_parents,
            mutation_rate=mutation_rate,
            crossover_rate=crossover_rate,
        )
