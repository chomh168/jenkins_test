#import time

#start = time.time()
#while True:

#    term = time.time() - start
#    if term>9:
#        start = time.time()
#        print(term)

from setuptools import setup, find_packages

setup(name='test',

      version='0.4',

      url='https://github.com/chomh168/jenkins_test.git',

      license='MIT',

      author='minho cho',

      author_email='cho7627@gmail.com',

      description='Manage configuration files',

      classifiers=[

          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',

          'Topic :: Software Development :: Libraries',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3',

          'Programming Language :: Python :: 3.6.5',

      ],

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=['nose>=1.0'],

      test_suite='nose.collector')
