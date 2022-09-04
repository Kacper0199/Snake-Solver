<p align="center">
  <img src="https://github.com/Kacper0199/Snake-Solver/blob/main/pictures/banner.png" width="700" height="250">
</p>
<h1 align="center">Snake-Solver</h1>

<div align="center">

  <a href="">![Repo Language](https://img.shields.io/github/languages/top/Kacper0199/Snake-Solver)</a>
  <a href="">![License](https://img.shields.io/github/license/Kacper0199/Snake-Solver?color=blueviolet)</a>
  <a href="">![Repo Elements](https://img.shields.io/github/directory-file-count/Kacper0199/Snake-Solver?color=yellow)</a>
  <a href="">![Downloads](https://img.shields.io/github/downloads/Kacper0199/Snake-Solver/total?color=green)</a>

</div>

---

This snake game solver is represented by an undirected graph and the **Hamiltonian Cycle** algorithm that generates path visiting each vertex exactly once. This approach ensures that the snake will never collide and maximum score will be achieved. 

---

- [1. Program Preview](#1-program-preview)
- [2. More About the Algorithm](#2-more-about-the-algorithm)
- [3. Installation](#3-installation)
- [4. Get Started](#4-get-started)

## 1. Program Preview

<p align="center">
<img src="https://github.com/Kacper0199/Snake-Solver/blob/main/pictures/preview.gif" width="600" height="400" />
</p>

## 2. More About the Algorithm

The application is based on the fundamental algorithm in the field of a graph theory to determine the cycle in the graph.
Finding the cycle allows the solver to traverse all the vertices in the graph exactly once, hence it always gets maximum score in the game.
The graph in **_algorithm.py_** script is represented by a hash table composed of vertices keywords. Each vertex corresponds to a cell in the game grid 
and is connected to its adjacents according to a schema presented in the picture below.

<p align="center">
<img src="https://github.com/Kacper0199/Snake-Solver/blob/main/pictures/grid.png" width="600" height="350" />
</p>

The algorithm calculates only one of several available paths. It is caused by a NP-complete problem and a polynomial time complexity to find all existing paths.
In this program a recursive backtracking approach was also proposed.

## 3. Installation

Copy the repository by forking and then downloading it using:

```bash
git clone https://github.com/<YOUR-USERNAME>/Snake-Solver
```

To install requirements use:

```bash
cd Snake-Solver
pip install -r requirements.txt
```

Run App:

```bash
cd Snake-Solver
python3 main.py
```

## 4. Get Started

- Randomly place snake on the board by pressing <kbd>Space</kbd>

- To run solver press <kbd>Enter</kbd>
