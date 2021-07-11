# Budget-Valley
> python `3.8.2` 

## Create Enviroment
I have Python3, to create a new enviroment you have to use, `python3 -m venv venv`, to active the enviroment just have to type `source venv/bin/activate`.

### Dependency and Package Managment Setup
First we have to install all Packages that we need for the project, then when all be installed, 
we need to a list package installed in a file, for do that, we need to type `pip3 freeze > requirmentes.txt`, to push the list dependecies into the file.
This file help us keep any version of each Package was installed.

To install requiriments `pip3 install -r requirements.txt`


## Execute function
Drop your Excel Contable from *Banco General* to CSV file. (You can filter first before you export)

`python3 app.py`


## Screenshots

### Filter
---
![Banco General Filter Data](./screenshots/filter.png)

### Export Button
---
![Banco General Export Data](./screenshots/export.png)

