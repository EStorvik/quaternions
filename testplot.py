import plotly.graph_objects as go

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=[1],  # x-coordinate
    y=[2],  # y-coordinate
    z=[3],  # z-coordinate
    mode='markers',
    marker=dict(
        size=10,
        color='red',  # set color to red
    )
)])

# Set titles and labels
fig.update_layout(title='3D Plot of a Single Point',
                  scene=dict(
                      xaxis_title='X Axis',
                      yaxis_title='Y Axis',
                      zaxis_title='Z Axis'
                  ))


filename = 'my_3d_plot.html'
fig.write_html(filename)


# Show plot
fig.show()