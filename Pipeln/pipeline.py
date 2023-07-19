from typing import final, Union
import logging
import time

class Pipeline:
  """
  Class for the creation of a custom pipeline, 
  which will sequentially execute the methods passed to the constructor.
  
  :param methods: Is a collection of objects that reference the names of the methods to be executed. It allows us to define the sequence of method calls in the pipeline.
  :type methods: list[object]

  :param params: Is a collection of tuples that store the parameters for each method. Each tuple corresponds to a method in the method list and contains the necessary parameters required for its execution.
  :type params: list[tuple]

  :param orders: Is a collection of integers that assign a specific execution order to the methods in the pipeline. The methods are executed based on the order specified in this list, allowing for a customized execution flow.
  :type orders: list[int]
  
  :param debug: Pipeline methods info.
  :type debug: bool
  """

  def __init__(self, methods: list[object] = None, params: list[Union[tuple, dict]] = None, orders: list[int] = None, debug: bool = False) -> None:
    self._methods = methods
    self._params = params
    self._orders = orders
    self._debug = debug

    self._stacks = [] # combination of methods and params
  
  # ###########################################################################
  # #                              CLASS GETTERS                              #
  # ###########################################################################

  @property
  def get_methods(self) -> list:
    """Method to access the pipeline methods.

    Returns:
        list: List with the names of the methods to be executed in the pipeline.
    """
    return [method.__name__ for method in self._methods]
  
  @property
  def get_params(self) -> list:
    """Method to access the pipeline params.

    Returns:
        list: List with the parameters of each of the methods to be executed in the pipeline.
    """
    return self._params
  
  @property
  def get_orders(self) -> list:
    """Method to access the pipeline orders.

    Returns:
        list: List with the execution order of the pipeline.
    """
    return self._orders
  
  # ############################################################################
  # #                               MAIN METHODS                               #
  # ############################################################################

  @final
  def create(self) -> None:
    """Method for creating and initializing the pipeline.
    """
    
    # -------------------- Variables needed & firsts conditions --------------------
    if self._debug: logging.basicConfig(level=logging.DEBUG, format='%(levelname)8s | %(message)s')
    
    # ----------------------------- Main functionality -----------------------------
    # Check if nulls & variables lenght
    if (self._methods or self._params or self._orders) is None:
      raise ValueError("Innapropiate argument value, check if there is any None object.")
    if len(self._methods) != len(self._orders) != len(self._params):
      raise ValueError("Inappropiate argument value, check parameters length. There is a missing value.")

    # Check argument values
    if not all(isinstance(value, object) for value in self._methods): 
      raise ValueError("Inappropiate methods argument value.")
    if not all(isinstance(value, (tuple, dict)) for value in self._params): 
      raise ValueError("Inappropiate params argument value.")
    if  not all(isinstance(value, int) for value in self._orders): 
      raise ValueError("Inappropiate order argument value.")

    # Create functions stack
    for func, parms in zip(self._methods, self._params):
      combination = (func, parms)
      self._stacks.append(combination)
  

  def run(self) -> None:
    """Method for sorting and executing the custom pipeline.
    """

    # -------------------- Variables needed & firsts conditions --------------------
    start_time = time.time()
    methods = self._stacks
    orders = self._orders

    # ----------------------------- Main functionality -----------------------------
    if self._debug: logging.debug('***********************************')
    if self._debug: logging.debug('        > Starting pipeline        ')
    if self._debug: logging.debug('')

    ordered_methods = [x for _, x in sorted(zip(orders, methods))]

    for func, params in ordered_methods:
      try:
        if type(params) is tuple:
          func(*params)
          if self._debug: logging.debug(f'EXEC: Method \033[94m{str(func.__name__)}\033[0m executed successfully.')
        else:
          func(**params)
          if self._debug: logging.debug(f'EXEC: Method \033[94m{str(func.__name__)}\033[0m executed successfully.')
      except TypeError:
        logging.error(f'ERROR: There is an error in \033[91m{str(func.__name__)}\033[0m method. Inappropiate argument type.')

    finish_time = time.time() - start_time
    if self._debug: logging.debug('')
    if self._debug: logging.debug(f'     Pipeline finished in {round(finish_time, 1)}s     ')
    if self._debug: logging.debug('***********************************')