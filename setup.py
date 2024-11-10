from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="Mathematics quiz based on random numbers and operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nandini Joshi",
    author_email="nandini.joshi@fau.de",
    url="https://github.com/Joshi-Nandini/dsss_homework_2",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
