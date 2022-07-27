import logging

class Pipeline:
  '''
  Class for the creation of a custom pipeline, 
  which will sequentially execute the methods passed to the constructor. 
  In addition, it contains a boolean handler to alter the pipeline in the tests.
  
  :param methods: It is a list of tuples of maximum size 3, which contains the methods for pipeline creation.
  :type methods: list
  
  :param debug: Pipeline methods info.
  :type debug: bool
  '''
  
  def __init__(self, methods=None, debug=False):
    self.__methods = methods
    self.__debug = debug
  
  def build(self, returnable=False):
    '''
    Main method of the class, which builds and executes the user-generated pipeline.
    '''
    
    # -------------------- Variables needed & firsts conditions --------------------
    if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(levelname)8s | %(message)s')
    
    # ----------------------------- Main functionality -----------------------------
    if self.__methods == None: self.info()
    else:
      for methods in self.__methods:
        try:
          run, method, arguments = methods
        except ValueError:
          run, method = methods
          
        try:
          if run:
            try:
              method(*arguments)
            except UnboundLocalError:
              method()
            except:
              method(arguments)
          else:
            logging.debug('The' + str(method) + 'station will not run this time.')
        except TypeError:
          logging.error('Be careful with the order of the parameters! The correct order is as follows: (Handler, Method, Parameter/s) or (Handler, Method). Thank you and sorry for the inconvenience!')
          return
    
    if returnable: print('Sorry! This part is currently under development.')
  
  def info(self, lang='en'):
    if lang == 'en':
      logging.info('Welcome to the Pipeln package, here is some information on how it works.')
      print('At the moment Pipeline has 1 main methods, the build method.\n',
            'Within the build method you will be able to run a sequence of methods and change its execution through the handler.\n')
      print('Thank you very much for using Pipeln in your projects, any feedback is helpful!')
      logging.info('If you want to read this in another language you can change it from the parameters -> lang="en".')