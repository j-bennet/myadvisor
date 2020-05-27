import setuptools

setuptools.setup(
    name="myadvisor",
    version="0.0.1",
    author="Irina Truong",
    author_email="i.chernyavska@gmail.com",
    description="Gives useful advice.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/j-bennet/myadvisor",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["myadvisor=myadvisor.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
