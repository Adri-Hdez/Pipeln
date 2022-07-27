import sys
sys.path.append('../')

from Pipeln.pipeline import Pipeline
from auxiliar_test_methods import testOne, testStr, testTwo
import unittest

# ----------------------------------- Pipeln testing units -----------------------------------
class Testing(unittest.TestCase):
  def pipeline_unittests(self):
    obj = Pipeline(methods=[(True, testOne, (2,2)), (True, testTwo, 3), (True, testStr, 'epic')])
    self.assertIsNotNone(obj)

if __name__ == '__main__':
  unittest.main()