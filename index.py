python
import pandas as pd
import plotly.express as px

# Load Community Health Services Accessibility dataset
health_data = pd.read_csv('Community_Health_Services_Accessibility.csv')

# Load Public Transport Ridership and Accessibility dataset
transport_data = pd.read_csv('Public_Transport_Ridership_Accessibility.csv')

# Merge datasets based on geographical location
merged_data = pd.merge(health_data, transport_data, on='Geographical_Location', how='inner')

# Example: Calculate average accessibility score for each location
merged_data['Average_Accessibility_Score'] = merged_data[['Health_Accessibility_Score', 'Transport_Accessibility_Score']].mean(axis=1)

# Create an interactive map using Plotly
fig = px.scatter_mapbox(merged_data,
                        lat='Latitude',
                        lon='Longitude',
                        size='Average_Accessibility_Score',
                        color='Average_Accessibility_Score',
                        hover_name='Geographical_Location',
                        mapbox_style='carto-positron',
                        title='Community Health and Transport Accessibility Map')

fig.update_layout(mapbox_zoom=10, mapbox_center={"lat": 24.4539, "lon": 54.3773})
fig.show()
