import setuptools

setuptools.setup(
    name="tradecalldatabase",
    version="1.0.0",
    author="Marcos",
    author_email="mfelipe11@yahoo.com.br",
    description="Database shared by trade-calls modules",
    url="",
    install_requires=["pymongo", "marshmallow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)