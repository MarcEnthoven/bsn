import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bsn",
    version="0.0.1",
    author="Marc Enthoven",
    author_email="marc_enthoven@hotmail.com",
    description="This package can be used to test whether a number is a bsn (Burger Service Number, Dutch Social Security Number), but it can also generate the numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcenthoven/bsn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=['numpy']
	
)
