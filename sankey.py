import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv("D:\\.school\\'24\\2nd Semester\\dANAL\\sankey_assignment.csv")

# Define the labels for the Sankey diagram
labels = [
    "PS", "OMP", "CNP", "NRP", "NMCCC", "PEC", "NCDM", "RGS",
    "I", "S", "D", "F", "N",
    "Reg", "Aca", "Oth"
]

# Define a color palette for the labels
label_colors = {
    "PS": "rgba(255, 140, 0, 0.8)",
    "OMP": "rgba(123, 104, 238, 0.8)",
    "CNP": "rgba(0, 191, 255, 0.8)",
    "NRP": "rgba(34, 139, 34, 0.8)",
    "NMCCC": "rgba(255, 20, 147, 0.8)",
    "PEC": "rgba(218, 165, 32, 0.8)",
    "NCDM": "rgba(210, 105, 30, 0.8)",
    "RGS": "rgba(70, 130, 180, 0.8)",
    "S": "rgba(255, 87, 51, 0.8)",
    "F": "rgba(51, 255, 87, 0.8)",
    "D": "rgba(51, 87, 255, 0.8)",
    "N": "rgba(255, 51, 161, 0.8)",
    "I": "rgba(161, 51, 255, 0.8)",
    "Reg": "rgba(152, 251, 152, 0.8)",
    "Aca": "rgba(240, 128, 128, 0.8)",
    "Oth": "rgba(123, 104, 238, 0.8)"
}

# Initialize lists for source, target, value, and color
source = []
target = []
value = []
colors = []

# Stage 1 to Stage 2 flows
for index, row in df.iterrows():
    for col in df.columns[1:9]:  # Only consider columns from Stage 1
        stage1_index = labels.index(col)
        stage2_index = labels.index(row['LABEL'])
        count = row[col]
        if count > 0:
            source.append(stage1_index)
            target.append(stage2_index)
            value.append(count)
            colors.append(label_colors[col])

# Stage 2 to Stage 3 flows
stage2_to_stage3 = {
    "S": {"Reg": 2, "Aca": 7, "Oth": 1},
    "F": {"Reg": 2, "Aca": 2},
    "D": {"Reg": 1, "Aca": 3, "Oth": 1},
    "N": {"Reg": 2, "Aca": 2, "Oth": 1},
    "I": {"Aca": 1}
}

for src, targets in stage2_to_stage3.items():
    src_index = labels.index(src)
    for tgt, cnt in targets.items():
        tgt_index = labels.index(tgt)
        source.append(src_index)
        target.append(tgt_index)
        value.append(cnt)
        colors.append(label_colors[src])

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=[label_colors[label] for label in labels]
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=colors
    ))])

fig.update_layout(title_text="Sankey Diagram Assignment", font_size=12)

# Save the figure as an HTML file
fig.write_html("sankey_diagram_stages.html")

# Optionally, if you want to automatically open the file in a browser
import webbrowser
webbrowser.open("sankey_diagram_stages.html")