import plotly.graph_objects as go
import numpy as np

# Define the initial and final points
initial_point = np.array([1, 1, 1])
final_point = np.array([2, 2, 2])

# Define the plane (example plane: x + y + z = 3)
px, py = np.meshgrid(range(3), range(3))  # Plane grid
pz = 3 - px - py

# Create figure
fig = go.Figure(
    data=[
        # Initial line from the origin to the initial point
        go.Scatter3d(x=[0, initial_point[0]], y=[0, initial_point[1]], z=[0, initial_point[2]],
                     mode='lines+markers', marker=dict(size=5), name='Line to Point'),
        # Plane
        go.Surface(z=pz, x=px, y=py, colorscale='Viridis', opacity=0.5, name='Plane'),
    ],
    layout=go.Layout(
        updatemenus=[dict(type='buttons', showactive=False,
                          y=1, x=0.8, xanchor='left', yanchor='bottom',
                          pad=dict(t=45, r=10),
                          buttons=[dict(label='Move Line',
                                        method='animate',
                                        args=[None, dict(frame=dict(duration=500, redraw=True),
                                                         fromcurrent=True)])])],
        sliders=[dict(steps=[dict(method='animate')])],
    ),
    frames=[
        # Frame for the final point
        go.Frame(data=[
            go.Scatter3d(x=[0, final_point[0]], y=[0, final_point[1]], z=[0, final_point[2]],
                         mode='lines+markers', marker=dict(size=5), name='Line to Point')
        ])
    ]
)

# Show the figure
fig.show()
