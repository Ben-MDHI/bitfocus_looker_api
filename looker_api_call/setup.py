from setuptools import setup

setup(name='looker_api_call',
      version='0.1',
      description='Functions for pulling queries from the Bitfocus Looker api and converting to dataframes using pandas',
      url="https://github.com/Ben-MDHI/bitfocus_looker_api.git",
      author='Benjamin Lordi',
      license="MIT",
      packages=['looker_api_call'],
      install_requires=['pandas', 'requests'],
      zip_safe=False)