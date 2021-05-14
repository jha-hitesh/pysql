"""Setup.py."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysql",
    version="0.0.1",
    author="Hitesh Jha",
    author_email="hitesh4official@gmail.com",
    description="A lighweight fully functional ORM over SQL/NoSQL databses and python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jha-hitesh/pysql",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "ujson",
        "ordered-set",
        "mysql-connector-python"
    ]
)
