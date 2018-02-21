# Utilities to manipulate csv files from EnergyPlus

EnergyPlus output file are messy and slow to manipulate in a spreadsheet, so some methods are
developed to visualize, filter, etc the csv file.

A jupyter notebook is provided with typical output file.
## Getting Started  

Download the notebook using-Eplus.ipynb, an example of each method is used.
The file Eplus.py must be saved in the folder "modulos" and the data csv files go to folder data.


### Prerequisites



```
Pandas
Bokeh
```

### Using

from modulos import Eplus as ep
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook
# from bokeh.models import Range1d, HoverTool
output_notebook()


nombres = ['t','Ein','Eout', 'Nin','Nout', 'Oin','Oout', 'Sin','Sout', 'Pin','Pout','Tein','Teout']
caso1 = ep.readEP('datos/cubo.csv',nombres)

caso1.datos.columns

p = figure(plot_width=900, plot_height=500,x_axis_type='datetime',
           toolbar_location="above")
formato de inicio y fin   YYYY-MM-DD
inicio = '2017-04-06'
fin    = '2017-04-07'

q = caso1.datos[inicio:fin]

p.line(q.index,q.Ein,color='blue',legend='Ei')
p.line(q.index,q.Eout,color='red',legend='Eout')
p.line(q.index,q.Pin,color='black',legend='Pi')
p.line(q.index,q.Pout,color='brown',legend='Pout')
show(p)


## Authors

* **Guillermo Barrios** - *Initial work* - [GEE-UNAM](https://github.com/Altamar)
* **Maximiliano Valdes ** - *Espiritual leadership* - [GEE-UNAM](https://github.com/Altamar)

## License

This project is licensed under ...

## Acknowledgments

* Requests are welcomed
