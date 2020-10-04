from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='aws-deployment-utilities',
    version='0.0.6',
    author='Aaron Mamparo',
    author_email='aaronmamparo@gmail.com',
    description='Helper functions and classes for common AWS operations during deployment',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amamparo/python-aws-deployment-utilities',
    package_dir={
        '': 'src'
    },
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'build_lambda = aws_deployment_utilities_scripts.build_lambda_deployment_package:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>= 3.7'
)
