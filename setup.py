from setuptools import setup

VERSION = '0.0.1a0'

setup(name='hnpy',
      author='jarhill0',
      author_email='',
      description='Yet another object-based Hacker News API wrapper for Python.',
      install_requires=['requests >= 2.18.4'],
      keywords='hacker news api wrapper python3',
      license='MIT',
      long_description='Click here for README: https://github.com/jarhill0/hnpy#hnpy',
      packages=['hnpy'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest',
                     'betamax >= 0.8.0',
                     'betamax_serializers >= 0.2.0'],
      test_suite='tests',
      url='https://github.com/jarhill0/hnpy',
      version=VERSION)
