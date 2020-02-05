from setuptools import setup

setup(
    name='cds-wrap',
    version='0.1.0',
    description='Wraps arbitrary files/folders into a package for transfer across a CDS',
    url='https://github.com/gregorydulin/cds-wrap',
    author='Gregory M. Dulin',
    author_email='gregory.dulin@gmail.com',
    license='MIT',
    packages=[],
    setup_requires=[
        'wheel',
    ],
    install_requires=[
        'logzero',
    ],
    scripts=[
        'cds-wrap',
    ],
    zip_safe=True
)
