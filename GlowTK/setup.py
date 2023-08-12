from setuptools import setup, find_packages

setup(
    name='GlowTK',
    version='1.0.0',
    author='Brennan',
    author_email='brennanmarxrennie@hotmail.com',
    description='TKinter enhancer ',
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'BASH = GlowTK.module_name:main_function',
        ],
    },
)
