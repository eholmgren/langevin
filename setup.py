from distutils.core import setup

with open('README.md') as f:
      long_description = ''.join(f.readlines())

setup(name='LangevinSim',
      version='0.01',
      description='Langevin Simulator',
      long_description=long_description,
      author='Eric Holmgren',
      author_email='eholmgr2@u.rochester.edu',
      packages=['lans'],
     )
