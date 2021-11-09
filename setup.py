from setuptools import setup

setup(name='revcorml',
      version='0.1',
      description='tools to probe machine learning classifiers with noise, bubbles and reverse correlation',
      url='XXX',
      author='Etienne Thoret, Thomas Andrillon, Damien Léger, Daniel Pressnitzer',
      author_email='etienne.thoret@univ-amu.fr',
      license='MIT',
      packages=['revcorml'],
      install_requires=['numpy','sklearn'],
      zip_safe=False)