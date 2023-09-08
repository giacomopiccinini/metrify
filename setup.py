import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metrify",                         
    version="0.0.1",                       
    author="Giacomo Piccinini",           
    author_email='giacomo@gemmo.ai',   
    license='MIT',      
    description="Metrics for Machine Learning evaluation",
    url='https://github.com/giacomopiccinini/metrify',
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["quicksample"],             # Name of the python package
    package_dir={'':'quicksample/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)


    name='chronopy',
    version='0.1.3',    
    description='A simple Python package to measure execution time',
    url='https://github.com/giacomopiccinini/Clock',
    author='Giacomo Piccinini',
    author_email='giacomo@gemmo.ai',
    license='MIT',
    packages=['chronopy'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.9',
    ],
