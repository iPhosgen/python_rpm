from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        #check_call("cp etc/python_rpm.service etc/sysytemd/system".split())
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        #check_call("cp etc/python_rpm.service etc/sysytemd/system".split())
        install.run(self)


description = 'Simple RPM template project'
long_description = 'Simple template project for building RPM package from Python solution'
requires = []
with open('requirements.txt', 'r') as f:
    requires = f.readlines()

setup(name='python_rpm', version='0.1', author='Me', author_email='me@example.com', url='example.com',
      license='MIT', description=description, long_description=long_description, install_requires=requires, packages=find_packages(), cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      },)
