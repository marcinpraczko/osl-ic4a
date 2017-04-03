from setuptools import setup, find_packages

setup(
    name='osl-ic4a',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    url='',
    license='',
    author='Marcin Praczko',
    author_email='',
    description='Interactive Console For Automation',
    entry_points='''
        [console_scripts]
        ic4a=ic4a.cli:main
    ''',
)
