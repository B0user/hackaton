import pickle
import pandas as pd

# Function to load pickle files
def load_pickle(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)

# Load the distance matrix
distance_matrix_file = "distant_matrices.pkl"  # Replace with your file path
dm = load_pickle(distance_matrix_file)

# Load the station graph
station_graph_file = "station_graph.pkl"  # Replace with your file path
station_graph = load_pickle(station_graph_file)

# Display the distance matrix in tabular form
print("\nDistance Matrix Data:")
for road, stations in dm['road71'].items():
    for station, value in stations.items():
        print(f"Road: {road}, Station: {station}, Value: {value}")

# Assuming the station graph can be processed similarly (adjust based on actual structure)
print("\nStation Graph Data:")
# Assuming station_graph is a dictionary of nodes and edges
if isinstance(station_graph, dict):
    for node, connections in station_graph.items():
        print(f"Node: {node}, Connections: {connections}")
else:
    # If it's a graph-like object (such as a NetworkX graph), customize as needed
    print("Station Graph cannot be displayed as a simple table.")

# Optional: convert to pandas DataFrame if desired
df_dm = pd.DataFrame(dm['road71']).transpose()
print("\nDistance Matrix in DataFrame format:")
print(df_dm)

# Add additional processing for station_graph if necessary
