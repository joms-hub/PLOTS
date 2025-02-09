import pandas as pd
import plotly.express as px
import plotly.io as pio

# Ensure necessary libraries are installed:
# pip install pandas plotly

print("Starting script...")

# Check if necessary libraries are installed
try:
    import pandas as pd
    import plotly.express as px
    import plotly.io as pio
    print("Libraries imported successfully.")
except ImportError as e:
    print(f"Error importing libraries: {e}")
    raise

# Load the dataset
try:
    df = pd.read_csv("bar_assignment.csv")
    print("CSV file loaded successfully.")
except FileNotFoundError:
    raise FileNotFoundError("The file 'bar_assignment.csv' was not found in the current directory.")
except pd.errors.EmptyDataError:
    raise ValueError("The file 'bar_assignment.csv' is empty.")
except pd.errors.ParserError:
    raise ValueError("Error parsing 'bar_assignment.csv'. Please check the file format.")

print(df.head())  # Print the first few rows of the dataframe to verify its content

# Convert 1 -> "Yes" and 0 -> "No"
df.replace({1: "Yes", 0: "No"}, inplace=True)
print("Data replacement done.")

# Count occurrences for stacking
category_counts = df.groupby(['LABEL', 'COUNT']).size().unstack(fill_value=0).reset_index()
category_counts.columns.name = None
category_counts.columns = ['LABEL', 'No', 'Yes']
print("Category counts calculated.")

# Sort the labels alphabetically
category_counts.sort_values('LABEL', inplace=True)
print("Labels sorted alphabetically.")

# Create a horizontal stacked bar chart using Plotly with custom colors
fig = px.bar(
    category_counts,
    x=['No', 'Yes'],
    y='LABEL',
    orientation="h",
    barmode="stack",
    title="Horizontal Stacked Bar Chart",
    labels={"value": "Count", "LABEL": "Categories"},
    text_auto=True,
    color_discrete_map={"Yes": "blue", "No": "red"}
)
print("Bar chart created.")

# Update layout: move the legend to the top of the chart
fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    font=dict(size=12)
)
print("Layout updated: legend moved to the top.")

# Save the graph as an HTML file
try:
    fig.write_html("bar_chart.html")  # Saves the file in the current directory
    print("HTML file saved as 'bar_chart.html'.")
except ValueError as e:
    print(f"Error saving HTML file: {e}.")
    raise

# Set default renderer to browser
try:
    pio.renderers.default = "browser"
    print("Renderer set to browser.")
except Exception as e:
    print(f"Error setting renderer: {e}")
    raise

# Show the interactive chart
try:
    fig.show()
    print("Chart displayed.")
except Exception as e:
    print(f"Error displaying chart: {e}")
    raise

print("Script completed successfully.")