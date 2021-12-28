import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KeywordPlus-CaKa12",
    version="0.0.1",
    author="CaKa12",
    author_email="nickageddes09@gmail.com",
    description="A Package That Makes Keyword Management Easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MortyHub/Keywords-Python-Package",
    project_urls={
        "Bug Tracker": "https://github.com/MortyHub/Keywords-Python-Package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "Keywords/src"},
    packages=setuptools.find_packages(where="Keywords/src"),
    python_requires=">=3.6",
)