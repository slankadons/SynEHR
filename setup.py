from setuptools import setup

setup(name='synehr',
      version='0.1',
      description='Package to generate synthetic identified EHR data',
      url='https://github.com/slankadons/SynEHR/tree/type_gen_pull',
      author='Shraddha Lanka, Tennyson Lee',
      author_email='slanka@dons.usfca.edu, talee@dons.usfca.edu',
      license='',
      packages=['synehr'],
      install_requires=[
          'numpy','random','pandas','fake-factory','datetime'],
      zip_safe=False)