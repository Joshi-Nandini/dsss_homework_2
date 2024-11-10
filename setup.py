from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Nandini Joshi",
    author_email="nandini.joshi@fau.de",
    packages=find_packages(),
    include_package_data=True,
    description="Mathematics quiz based on random numbers and operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Joshi-Nandini/dsss_homework_2",
    license="Apache License 2.0",
    install_requires=[
        "required_package1>=1.0.0",         # List your dependencies here
        "required_package2>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                # Minimum Python version required
    entry_points={
        "console_scripts": [
            "your_command=your_module:main_function",  # Command-line interface entry point
        ],
    },
)
