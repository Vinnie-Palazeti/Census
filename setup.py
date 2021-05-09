import setuptools

setuptools.setup(
    name="GPS",  # Replace with your own username
    version="0.0.1",
    author="Vinnie Palazeti",
    author_email="vinnie.palazeti@gmail.com",
    description="GPS point to demographic data",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'requests'
    ],
    python_requires='>=3.6',
)