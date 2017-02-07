from setuptools import setup

setup(name='slackHandler',
      version='0.1',
      description='Handler for python logging module to send slack message',
      url='http://github.com/',
      author='koibadkid',
      author_email='koibadkid@gmail.com',
      license='PIXNET',
      packages=['slackHandler'],
      install_requires=[
          'slacker',
      ],
      zip_safe=False)
