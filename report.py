import pandas as pd

# Load the Excel file
df = pd.read_excel("bestPopulationData.xlsx")

# Convert DataFrame to HTML
html_table = df.to_html(index=False)

# Wrap it in a complete HTML document
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Traffic Simulation Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
        }}
        h1 {{
            color: #333;
        }}
        table {{
            border-collapse: collapse;
            width: 60%;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Traffic Simulation Report</h1>
    {html_table}
</body>
</html>
"""

# Save the HTML to a file
with open("traffic_simulation_report.html", "w") as file:
    file.write(html_content)