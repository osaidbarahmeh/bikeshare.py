# Bikeshare Project 

This project is a command-line Python application that analyzes bikeshare data for three major US cities: Chicago, New York City, and Washington. Users can filter the data by city, month, and day to view various statistics about bikeshare usage.

refactoring
## datasets
=======
##datasets
 main

- `Python 3.x`
- `Pandas`
- `NumPy`

These datasets are required to run the project and should be placed in the same directory as the python file. 
## rrequirements 

-python 3.x
-pandas 
-numpy 

You can install the required libraries using: 
```bash 
pip install pandas numpy
```
## How to Run 

To execute the program, run the following command in your terminal:

```bash 
python bikeshare.py
```
You will be prompted to choose:

- A city (`chicago`,`new york city`,`washington`)
- A month (January to June or `all`)
- A day of the week or `all`

The program will then display: 

- The most frequent times of travel 
- The most popular stations and trips 
- Trip duration statistics 
- User demographics


## Know Issues

- Program currently only supports CSV files with specific column names
- Limited to data from January to June
- Input balidation accept only lowercase city names



## Author

**Osaid barahmeh**
An-Najah National University
Department of Management Information system 

## acknowledgments

Special thanks to:

- Udacity for the project idea and daraset structure 
- Stack overflow and python documentation 
- Everyone who contributed expamles and tutorials on bikeshare analysis 

## License
© 2025 Osayd Barahmeh. All rights reserved.

