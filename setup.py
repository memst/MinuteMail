import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MinuteMail", # Replace with your own username
    version="0.1.0",
    author="memst",
    author_email="stankev.martynas@gmail.com",
    description="Package that lets you generate email addresses and read their mail through dropmail.me websocket.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memst/MinuteMail",
    packages=setuptools.find_packages(),
    install_requires=[
    	'websocket-client'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)