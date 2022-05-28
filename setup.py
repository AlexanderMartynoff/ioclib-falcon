from setuptools import setup, find_namespace_packages


__version__ = '1.4'


setup(
    name='ioclib-falcon',
    version=__version__,
    packages=find_namespace_packages(include=['ioclib.*']),
    install_requires=[
        'ioclib-injector>=1.4',
        'falcon==3.0.1',
    ],
)
