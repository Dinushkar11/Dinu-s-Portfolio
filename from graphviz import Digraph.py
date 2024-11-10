from graphviz import Digraph

# Create a directed graph for the activity diagram
dot = Digraph(comment='Irrigation Management and Water Control')

# Define nodes for the activity diagram
dot.node('A', 'Farmer: Start')
dot.node('B', 'Farmer: Log In')
dot.node('C', 'System: Analyze Data')
dot.node('D', 'System: Display Water Usage Information')
dot.node('E', 'System: Check for Excess or Insufficient Water')
dot.node('F', 'System: Maintain Current Settings')
dot.node('G', 'System: Adjust Water Flow')
dot.node('H', 'Farmer: Review Adjustments')
dot.node('I', 'Farmer: Log Out')

# Exception conditions
dot.node('J', 'Exception: Water Supply Shortage')
dot.node('K', 'Exception: Equipment Malfunction')
dot.node('L', 'Exception: Clogged or Leaking Irrigation Lines')

# Define the edges between the nodes
dot.edges(['AB', 'BC', 'CD', 'DE'])
dot.edge('E', 'F', label='Optimal Conditions')
dot.edge('E', 'G', label='Excess/Insufficient Water')
dot.edge('G', 'H')
dot.edge('F', 'H')
dot.edge('H', 'I')

# Exception handling
dot.edge('C', 'J', label='Water Supply Shortage')
dot.edge('C', 'K', label='Equipment Malfunction')
dot.edge('C', 'L', label='Clogged/Leaking Irrigation Lines')

# Render the diagram
dot.render('/mnt/data/Irrigation_Management_Activity_Diagram', format='png', cleanup=True)

# Return the file path
'/mnt/data/Irrigation_Management_Activity_Diagram.png'
