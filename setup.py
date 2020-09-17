import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="try_parse",
    version="0.0.9",
    author="Gorinenko Anton",
    author_email="anton.gorinenko@gmail.com",
    description="Easily and safety cast objects to the desired data type",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python, parse, cast',
    url="https://github.com/agorinenko/try-parse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.7',
)
