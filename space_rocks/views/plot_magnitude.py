"""Function to create a bokeh scatter plot.

    It takes in the absolute magnitude, relative velocity and N.E.O's name and returns
    a scatter plot charting them.
"""

import os
from bokeh.plotting import figure, output_file, save, ColumnDataSource
from bokeh.models import HoverTool
from space_rocks.CustomExceptions.custom_exceptions import UnknownAxisException


def graph_abs_magnitude(abs_mag=None, velocity=None, neo_names=None):
    """Create Bokeh Scatter Plot."""
    
    """Redundant checks in case API provides incomplete info."""
    try:
        if len(abs_mag) > 0 and len(velocity) > 0 and len(neo_names) > 0:
            here = os.path.abspath(__file__)
            graph_file_path = os.path.join(os.path.dirname(os.path.dirname(here)),"static/graphs/abs_magnitude.html")

            output_file(graph_file_path)

            p = figure(
                title="Brightness and Velocity", tools="tap",
                x_axis_label='Absolute Magnitude', y_axis_label='Velocity km/s'
            )

            source = ColumnDataSource(data=dict(
                x=abs_mag,
                y=velocity,
                names=neo_names,
                fonts=[
                    '<i>italics</i>',
                    '<pre>pre</pre>',
                    '<b>bold</b>',
                    '<small>small</small>',
                    '<del>del</del>'
                ]
            ))

            hover = HoverTool(tooltips="""
                <div>
                    <div>
                    </div>
                    <div>
                        <span style="font-size: 17px; font-weight: lighter;">Name of NEO: </span>
                        <span style="font-size: 17px; font-weight: bold;">@names</span>
                        <span style="font-size: 15px; color: #966;">[$index]</span>
                    </div>
                    <div>
                        <span style="font-size: 17px; font-weight: lighter;">Absolute Magnitude: </span>
                        <span style="font-size: 17px; font-weight: bold;">@x</span>
                    </div>
                    <div>
                        <span style="font-size: 17px; font-weight: lighter;">Relative Velocity: </span>
                        <span style="font-size: 17px; font-weight: bold;">@y</span>
                    </div>
                </div>
                """)

            p = figure(plot_width=850,
                       plot_height=850,
                       tools=[hover],
                       title="Brightness and Velocity",
                       x_axis_label='Absolute Magnitude',
                       y_axis_label='Velocity km/s',
                       background_fill_color='black',
                       background_fill_alpha=0.8,
                       border_fill_color='black',
                       border_fill_alpha=0.8,
                       toolbar_location=None,
                       sizing_mode='scale_width'
                       )

            p.circle('x', 'y', size=10, source=source)
            p.ygrid.grid_line_color = "#333333"
            p.xgrid.grid_line_color = "#333333"

            save(p)
        else:
            raise UnknownAxisException
    except TypeError:
        raise UnknownAxisException
