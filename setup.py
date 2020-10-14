from setuptools import setup

setup(
    name='pycky',
    version='0.1.0',
    description='A simple unit testing framework for Python.',
    url='http://github.com/xaviripo/pycky',
    author='Xavier Ripoll',
    author_email='xaviripo97@gmail.com',
    license='MIT',
    packages=['pycky'],
    install_requires=[
        'click',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'pycky=pycky.bin.pycky:main',
        ],
    },
    zip_safe=False
)