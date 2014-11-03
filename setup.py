#!/usr/bin/env python
#setup script

from distutils.core import setup
import importlib
import sys

module = {'pymongo' : 'Python MongoDB interface',
          'smtplib' : 'Default smtplib installed with Python',
          'email'   : 'Default email module usually installed with Python'
};

def main():

  sys.stdout.write("Checking modules required modules...")
  missing_modules = False

  for key,value in module.iteritems():
    missing_modules = check_import(key,value) or missing_modules

  if missing_modules:
    sys.stdout.write("Please install missing modules\n")
    unsuccessful()

  sys.stdout.write("Complete!\n")

  sys.stdout.write("Seting up metadata...")
  setup_meta()
  sys.stdout.write("Complete!\n")



#Unsuccessful termination
def unsuccessful():
  #cleanup

  #exit
  sys.stdout.write("Setup terminated unsucessfuly\n")
  exit()

#Check if modules exist, if not try to install them
def check_import(mod,desc):
  try:  
    importlib.import_module( mod)
    return False
  except ImportError:
    print('\nError: Missing module ' + mod)
    print('Description of ' + mod + ": " + desc+"\n")
    #Try to install required module with user permission

    #if unsuccesful, return True
    return True

#setup project to allow proper organization as per Python specifications
def setup_meta():
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



if __name__ == "__main__":
  main()

