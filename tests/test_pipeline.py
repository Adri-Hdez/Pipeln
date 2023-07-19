import sys
sys.path.append('../')

from Pipeln.pipeline import Pipeline
from features.auxiliar_test_methods import add, sub, cap
import unittest

# ----------------------------------- Pipeln testing units -----------------------------------
class Testing(unittest.TestCase):
  def test_pipeline_initialization(self):
    obj = Pipeline(methods=[add, sub, cap], params=[(2, 4), (1, 2), ('spain',)], orders=[3, 1, 2])

    self.assertIsNotNone(obj)
  
  def test_pipeline_get_methods(self):
    obj = Pipeline(methods=[add, sub, cap], params=[(2, 4), (1, 2), ('spain',)], orders=[3, 1, 2])
    methods = obj.get_methods

    self.assertEqual(methods, ['add', 'sub', 'cap'])
  
  def test_pipeline_get_params(self):
    obj = Pipeline(methods=[add, sub, cap], params=[(2, 4), (1, 2), ('spain',)], orders=[3, 1, 2])
    params = obj.get_params

    self.assertEqual(params, [(2, 4), (1, 2), ('spain',)])
  
  def test_pipeline_get_orders(self):
    obj = Pipeline(methods=[add, sub, cap], params=[(2, 4), (1, 2), ('spain',)], orders=[3, 1, 2])
    orders = obj.get_orders

    self.assertEqual(orders, [3, 1, 2])
  
  def test_pipeline_creation(self):
    obj = Pipeline(methods=[add, sub, cap], params=[(2, 4), (1, 2), ('spain',)], orders=[3, 1, 2])
    obj.create()
    
    self.assertIsNotNone(obj) # This method doesn't returns

  def test_pipeline_execution(self):
    obj = Pipeline(methods=[add, sub, cap], params=[{'a': 2, 'b': 4}, (1, 2), ('spain',)], orders=[1, 2, 3])
    obj.create()
    obj.run()
    
    self.assertIsNotNone(obj) # This method doesn't returns

if __name__ == '__main__':
  unittest.main()