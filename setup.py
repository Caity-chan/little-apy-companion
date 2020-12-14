import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="little_api_companion_caitlin_chan",
    version="0.0.1",
    author="Caitlin-chan",
    author_email="pandonautical@gmail.com",
    description="API comapnion for discord.py bot making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Caity-chan/little-apy-companion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
