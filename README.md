# lambdata-Lopez-John
This is a repo for Sprint 1 that will contain a bunch of package modules.

# Motivation
A learning module to learn:
* How to create Modules and Packages
* OOP code style
* PEP8 python code
* how to create and launch docker containers
* Unit Testing Framework
* read and write quality comments, Pydocs and READMEs

# Code Style
Used PEP8 code style

# Tech/framework used
Built with
* Pip
* Visual Studio Code
* Docker
* Ubuntu

# Features
Includes a Dockerfile container which install for Ubuntu and pypi for lambdata-Lopez-John Package

# Code Example

```class NewDataFrame(pd.DataFrame)```
    ```Class that inherits from pandas DataFrame```
    ```def list_2_series(self, list):```
       ``` """Method takes a list, turns it into a Series,```
        ```adds a new column and returns the NewDataFrame"""```
        ```new_series = pd.Series(list)```
        ```self['New_Column'] = new_series```
        ```return self```

# Installation
If Docker is installed
    ```docker build . -t (image name)```
    ```docker run -it myimage bash```

# Hot to use
Still figuring that out myself.

#Contribute
Feel free to add comments on how to better my code or drop in suggestions

# License 
MIT © John Lopez