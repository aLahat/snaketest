from setuptools import setup

setup(
    name='snaketest',
    version='0.0.2',    
    description='A small package to help test and prototype snakemake rules',
    url='https://github.com/aLahat/snaketest',
    author='Albert',
    author_email='lahat.albert@gmail.com',
    license='MIT License',
    packages=['snaketest'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.5',
    ],
)