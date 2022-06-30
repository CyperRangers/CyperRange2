from setuptools import setup
try:
    import pypandoc
    description = pypandoc.convert('README.md','rst')
except:
    description=''

setup(
    name = "PythonPi",
    version = '1.0.2',
    author = 'CyperRangers',
    author_email = 'cyper@tutamail.com',
    description = "Get the Value of Pi upto as many decimal places as needed",
    license = "MIT",
    keywords = "pi maths",
    weird = "true",
    url = "https://github.com/CyperRangers/CyperRange2",
    py_modules = ['PythonPi'],
    entry_points = {
    'console_scripts': ['pythonpi = PythonPi:shell']
    },
    long_description=description,
    classifiers=[
     "Development Status :: 5 - Production/Stable",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
    ],

)
