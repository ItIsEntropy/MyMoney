from setuptools import setup

setup(name='MyMoney',
      version='0.1',
      description='Investment Portfolio manager',
      url='https://github.com/ItIsEntropy/MyMoney',
      author='ItIsEntropy',
      author_email='paulsiame@live.co.uk',
      license='MPLv2',
      packages=['geektrust'],
      install_requires=[
          'numpy',
      ]
      zip_safe=True)