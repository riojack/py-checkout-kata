import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-checkout-kata-pkg-riojack",
    version="0.0.1",
    author="riojack",
    author_email="riojack@github.com",
    description="Checkout kata in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riojack/py-checkout-kata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
