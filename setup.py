#!/usr/bin/env python
#setup script

from distutils.core import setup
import importlib

module = {'pymongo' : 'Python MongoDB interface',
          'smtplib' : 'Default smtplib installed with Python',
          'email'   : 'Default email module usually installed with Python'
};

def check_import(mod,desc):
  try:  
    importlib.import_module( mod)
    return False
  except ImportError:
    print('\nError: Missing module ' + mod)
    print('Description of ' + mod + ": " + desc+"\n")
    return True


missing_modules = False
for key,value in module.iteritems():
  missing_modules = check_import(key,value) or missing_modules
if missing_modules:
  print("Please install missing modules\n")
  exit()






setup(
  name='Nutrition Automation',
  version = '0.05',
  description="",                             #define
  long_description="",                        #define
  author="Nicolas Primeau",
  author_email="nicolas.primeau@gmail.com",
  url="",                                     #define
  download_url="",                            #define
  packages = [""],                            #define
  py_modules = {},                            #define
  package_dir = {},                           #define
  #ext_modules = [],                          #OpenCL Support, will develop later
  classifiers = [],                           #define
  keywords = [],                              #define
  platforms = [],                             #define

)

