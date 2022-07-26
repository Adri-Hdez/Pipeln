from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

    setup(
        long_description=LONG_DESC,
        long_description_content_type='text/markdown',
        name='pipeln',
        packages=find_packages(include=['Pipeln']),
        version='0.0.1',
        description='A package to create a custom pipeline',
        author='Adrián H.S',
        author_email='adrihs.dev@gmail.com',
        license='MIT',
        install_requires=['pandas', 'numpy'],
        setup_requires=['pytest-runner'],
        url='https://github.com/Adri-Hdez/Pipeln',
        tests_require=['pytest'],
        test_suite='tests',
        include_package_data=True,
)