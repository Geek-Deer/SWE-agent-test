from setuptools import setup, find_packages

setup(
    name="helloworld",  # Name of the package
    version="0.1",  # Version of the package
    packages=find_packages(),  # Automatically finds all packages in the project
    author="Your Name",  # Your name as the author
    author_email="your.email@example.com",  # Your email
    description="A simple hello world package",  # Short description
    long_description=open('README.md').read(),  # Read from README file
    long_description_content_type='text/markdown',  # Format of README
    url="https://github.com/yourname/helloworld",  # URL of the project repository (if applicable)
    classifiers=[
        "Programming Language :: Python :: 3",  # Python version compatibility
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python version required
)
