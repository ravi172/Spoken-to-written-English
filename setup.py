import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))
setup(
	  name = 'spoken2written',
      packages = ['spoken2written'],
      version='0.1',
      description='Convert Spoken English given as text to Written English ',
      author='Ravi Kumar Verma',
      author_email='verma.ravi172@gmail.com',
      url='https://github.com/ravi172/Spoken-to-written-English',
      packages=['distutils', 'distutils.command'],
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
