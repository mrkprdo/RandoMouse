from setuptools import setup

def read(fname):
    return open(fname,'r').read()

setup(
   name='randomouse',
   version='0.0.6',
   author='Mark Prado',
   author_email='otsukaranz@gmail.com',
   packages=['randomouse'],
   url='http://pypi.python.org/pypi/randomouse/',
   license='LICENSE',
   description='A package that will run random mouse movement',
   long_description=read('README.md'),
   long_description_content_type='text/markdown',
   classifiers=[
       "Development Status :: 4 - Beta",
       "Environment :: Win32 (MS Windows)",
       "Topic :: Utilities"
   ],
   install_requires=[
       "pywin32",
   ]
)