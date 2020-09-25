from setuptools import setup

setup(
    name="changefn",
    version="1.0",
    py_modules=['changefn'],
    install_requires=[
        'Click'
    ],
    author="keshav wadhwa",
    author_email="onwheelmeals@gmail.com",
    entry_points=''' 
    [console_scripts]
    changefn=changefn:cli
    
    '''
)