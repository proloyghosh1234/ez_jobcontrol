from distutils.core import setup
setup(
  name = 'ez_jobcontrol',         # How you named your package folder (MyLib)
  packages = ['ez_jobcontrol'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This module once is a handy tiny job control to perform all job control functionalities including job dependency, job start and end, auto increment of load date etc',   # Give a short description about your library
  author = 'Proloy Ghosh',                   # Type in your name
  author_email = 'proloy.ghosh1234@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/proloyghosh1234/ez_jobcontrol/archive/0.1.tar.gz',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['aws', 'jobcontrol', 'dynamodb'],   # Keywords that define your package best
  install_requires=['botocore','boto3'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)