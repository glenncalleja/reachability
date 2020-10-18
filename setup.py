import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reachability",
    version="0.1.2",
    author="Glenn Calleja Frendo",
    author_email="glenncal@gmail.com",
    description="Monitor and observe Online Reachability, and react to status changes as necessary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glenncalleja/reachability",
    packages=setuptools.find_packages(),
    keywords="online reachability status check connectivity",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
