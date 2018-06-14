import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Weather_Station",
    version="0.2.0",
    author="Alexander Ross",
    author_email="asr3bj@virginia.edu",
    description="weather setup for raspberry pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github/Atech1/Weather_Station",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)