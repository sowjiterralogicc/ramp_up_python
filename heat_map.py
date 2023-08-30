import pandas as pd   # pandas is used for data manipulation and reading the Excel file 
import plotly.graph_objects as go #and plotly.graph_objects is used for creating interactive visualizations.

# Read the Excel sheet
df = pd.read_excel("Heat_map.csv.xlsx")

# Define color mapping
color_mapping = {
    "Dark Green": "#006400",
    "One Level Below Dark Green": "#228B22",
    "Two-Level Below Dark Green": "#32CD32",
    "Two-Level Above Light Green": "#FFD700",
    "One Level Above Light Green": "#ADFF2F",
    "Light Green": "#00FF00",
    "White": "#FFFFFF",
    "Two Level Above Light Green": "#ADFF2F",
    "Two Level Below Dark Green": "#32CD32"  
}


# Create the heatmap figure #A treemap is a visualization used to display hierarchical data.
fig = go.Figure(data=go.Treemap(
    #labels=df['Area'],
    labels=df['Area'] + ' (' + df['Existing team members proficient with this area'].astype(str) + ')',
    parents=[''] * len(df['Area']),
    values=df['Existing team members proficient with this area'],
    marker=dict(
        colors=[color_mapping[level] for level in df['Average team expertise(1-5)']],
        line=dict(width=2, color='black'), 
        
    ),

))

# Update layout
fig.update_layout(
    title="Team Expertise Heatmap",
    margin=dict(t=0, l=0, r=0, b=0)  #to remove any space around the visualization.
)

# Show the figure
fig.show()


