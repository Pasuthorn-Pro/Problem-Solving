import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# สร้างกราฟ
network = nx.Graph()

# เพิ่มเส้นเชื่อมของรูปดาว
edges = [(4, 1), (1, 3), (3, 5), (5, 2), (2, 4)]
network.add_edges_from(edges)

# สร้างตำแหน่งของโหนดให้เป็นรูปดาว
angles = np.linspace(0, 2 * np.pi, 6)[:-1]  # มุมสำหรับ 5 จุด
star_positions = {i+1: (np.cos(angles[i]), np.sin(angles[i])) for i in range(5)}

# กำหนดสีของโหนด
color_list = ["gold"]

plt.figure(figsize=(6, 6))

# วาดกราฟโดยใช้ตำแหน่งที่กำหนดเอง
nx.draw(network, pos=star_positions, with_labels=True, node_color=color_list, 
        node_size=800, edge_color="black", linewidths=1.5, font_size=12)

plt.show()
