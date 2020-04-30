import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tradecalldatabase",
    version="1.0.0",
    author="Marcos",
    author_email="mfelipe11@yahoo.com.br",
    description="Database shared by trade-calls modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=['pymongo'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)