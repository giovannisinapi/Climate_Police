import plotly.offline as py
py.init_notebook_mode()

from temp_pre_process import temp_pre_process

def temp_map(temp, year):
	
	# Pre-processes the temperature data so that it can be plotted by plotly.
	df2 = temp_pre_process(temp, year)

	#scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            #[0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

	data = [ dict(
        	type='choropleth',
        	#colorscale = scl,
        	autocolorscale = True,
        	locations = df2.index,
        	z = df2['AverageTemperature'].astype(float),
        	locationmode = 'USA-states',
        	text = df2['text'],
        	marker = dict(
            	line = dict (
                	color = 'rgb(255,255,255)',
                	width = 2
            	) ),
        	colorbar = dict(
            	title = '°C')
        	) ]

	layout = dict(
			title = year+' US Average Temperature by State<br>(Hover for details)',
        	geo = dict(
            	scope='usa',
            	projection=dict( type='albers usa' ),
            	showlakes = True,
            	lakecolor = 'rgb(255, 255, 255)'),
            	)
    
	fig = dict( data=data, layout=layout )
	py.iplot( fig, filename='us-temperature-map' )
	return fig
