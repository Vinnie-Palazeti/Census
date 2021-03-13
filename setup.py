import setuptools

setuptools.setup(
    name="Census",  # Replace with your own username
    version="0.0.1",
    author="Vinnie Palazeti",
    author_email="vinnie.palazeti@gmail.com",
    description="Grabbing Census Data",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'jupyter'
    ],
    python_requires='>=3.6',
)