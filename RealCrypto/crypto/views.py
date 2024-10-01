# crypto/views.py
from django.shortcuts import render
from bokeh.plotting import figure #, output_file, show
from bokeh.embed import components
import pandas as pd
from math import pi
import datetime
from .dataservice import get_cypto_data,convert_to_df_crypto
from bokeh.models import  HoverTool

def homepage(request):
    crypto = 'BTC'
    market = 'CAD'
    if request.method == 'POST':
        crypto = request.POST['crypto']
        market = request.POST['market']
    
    result = get_cypto_data(crypto,market, '#your APIKEY here#') #Add your own APIKEY

    source = convert_to_df_crypto(result,market)

    TOOLS = "pan, box_zoom, reset, save"

    title = f'{crypto} to {market} chart'

    p = figure(x_axis_type="datetime", tools=TOOLS, width=700, height=500, title = title)
    p.xaxis.major_label_orientation = pi / 4
    line = p.line(x='date', y='high', line_width=2,line_color="#ed0505", source=source)

    #setup tooltip
    hover_tool = HoverTool(tooltips=[
                    ('Price', '$y{0,0.00}'),
                    ('Date', '$x{%F}'),], 
                    formatters={'$x': 'datetime'},  
              
        )
    p.tools.append(hover_tool)

    script, div = components(p)

    return render(request,'crypto/base.html',{'script':script, 'div':div })