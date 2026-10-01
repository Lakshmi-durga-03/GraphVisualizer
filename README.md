# GraphVisualizer - Graph Algorithm Visualization

GraphVisualizer is an interactive web application designed to help students understand and visualize **graph traversal algorithms** such as **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

Instead of only reading the algorithm or looking at code, users can visually observe how the traversal progresses through a grid, making it easier to understand concepts such as **queues, stacks, visited nodes, and traversal order**.

## 📌 Overview

GraphVisualizer provides a simple and interactive interface where users can:

- Select BFS or DFS traversal
- Generate a custom grid by entering rows and columns
- Select any starting cell
- Visualize the traversal step-by-step
- Observe visited and currently processing cells through different colors
- Understand how BFS uses a **Queue**
- Understand how DFS uses a **Stack**

The project is built using **HTML, CSS, and JavaScript**, without requiring any backend or database.

## ✨ Features

- 🔹 Interactive BFS visualization
- 🔹 Interactive DFS visualization
- 🔹 Custom grid size
- 🔹 User-selectable starting node
- 🔹 Color-based traversal states
- 🔹 Real-time traversal animation
- 🔹 Queue visualization for BFS
- 🔹 Stack visualization for DFS
- 🔹 Responsive grid handling
- 🔹 Simple and beginner-friendly interface
- 🔹 No backend or database required

## 🧠 Algorithms Implemented

### 1. Breadth-First Search (BFS)

BFS explores nodes **level by level** using a **Queue** data structure.

In this project:

1. The user selects a starting cell.
2. The selected cell is added to the queue.
3. Its neighboring cells are explored.
4. Unvisited neighbors are added to the queue.
5. The current cell is marked as visited.
6. The process continues until all reachable cells are visited.

### 2. Depth-First Search (DFS)

DFS explores as deeply as possible before backtracking and uses a **Stack** data structure.

In this project:

1. The user selects a starting cell.
2. The starting cell is added to the stack.
3. A cell is removed from the stack.
4. Its unvisited neighbors are added to the stack.
5. The current cell is marked as visited.
6. The process continues until the stack becomes empty.

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Concepts
- Breadth-First Search
- Depth-First Search
- Queue
- Stack
- Graph Traversal
- Grid Traversal
- DOM Manipulation
- Asynchronous JavaScript

## 📂 Project Structure

```text
GraphVisualizer/
│
├── index.html          # Main page for selecting an algorithm
├── bfs.html            # BFS visualization page
├── dfs.html            # DFS visualization page
│
├── bfs.js              # BFS implementation and visualization
├── dfs.js              # DFS implementation and visualization
│
├── gen.css             # Common styling
├── index.css           # Styling for the home page
│
└── README.md           # Project documentation
```

## 🚀 How to Run the Project

Since this is a frontend-only project, you don't need to install any dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Lakshmi16-03/GraphVisualizer.git
```

### Step 2: Open the Project

Navigate to the project folder:

```bash
cd GraphVisualizer
```

### Step 3: Run the Application

Open:

```text
index.html
```

in your web browser.

You can also use **VS Code with the Live Server extension** to run the project.

## 🎯 How to Use

### BFS

1. Open the application.
2. Select **BFS**.
3. Enter the number of rows and columns.
4. Click **Generate**.
5. Click any cell to select the starting point.
6. Watch the BFS traversal happen automatically.
7. Observe the cells changing their states during traversal.

### DFS

1. Open the application.
2. Select **DFS**.
3. Enter the number of rows and columns.
4. Click **Generate**.
5. Click any cell to select the starting point.
6. Watch the DFS traversal happen automatically.
7. Observe the stack-based traversal visually.

## 🎨 Visualization States

The application uses different visual states to represent the progress of the algorithms.

### BFS

- **Unvisited** → Node has not been explored
- **Visiting** → Node is currently being processed
- **In Queue** → Node has been added to the BFS queue
- **Visited** → Node has already been processed

### DFS

- **Unvisited** → Node has not been explored
- **Visiting** → Node is currently being processed
- **In Stack** → Node has been added to the DFS stack
- **Visited** → Node has already been processed

## ⏱️ Time Complexity

For a graph with `V` vertices and `E` edges:

### BFS

```text
Time Complexity: O(V + E)
Space Complexity: O(V)
```

### DFS

```text
Time Complexity: O(V + E)
Space Complexity: O(V)
```

In this implementation, the graph is represented through a grid, where each cell can have up to four neighboring cells.

## 💡 Learning Objective

The main objective of this project is to make graph traversal algorithms easier to understand through **visual learning**.

It helps students connect the theoretical concepts of:

- Graph traversal
- Queue
- Stack
- Visited nodes
- Neighbor exploration

with their actual execution.

## 🌐 Live Demo

You can try the project here:

https://lakshmi16-03.github.io/GraphVisualizer/

## 📸 Project Preview

You can add screenshots of the application here after uploading them to your GitHub repository.

For example:

```markdown
![GraphVisualizer Home](screenshots/home.png)

![BFS Visualization](screenshots/bfs.png)

![DFS Visualization](screenshots/dfs.png)
```

## 🔮 Future Enhancements

Some possible improvements for the project are:

- Add Dijkstra's Algorithm
- Add A* Pathfinding
- Add maze generation
- Add weighted graphs
- Add animation speed controls
- Add pause and resume functionality
- Add step-by-step traversal controls
- Display traversal order
- Add graph/node-based visualization
- Add mobile-friendly improvements

Live Link: https://lakshmi16-03.github.io/GraphVisualizer/
