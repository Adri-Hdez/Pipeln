import os

# Use the VERSION file to get Pipeln version
version_file = os.path.join(os.path.dirname(__file__), "Pipeln", "VERSION")
with open(version_file) as fh:
    pipeln_version = fh.read().strip()

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

    setup(
        long_description=LONG_DESC,
        long_description_content_type='text/markdown',
        name='pipeln',
        packages=find_packages(include=['Pipeln']),
        version=pipeln_version,
        description='A Python package to create a custom pipeline',
        author='Adrián H.S',
        author_email='adrihs.dev@gmail.com',
        license='MIT',
        install_requires=[],
        setup_requires=['pytest-runner'],
        url='https://github.com/Adri-Hdez/Pipeln',
        tests_require=['pytest'],
        test_suite='tests',
        include_package_data=True,
    )