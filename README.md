# Network Routing Simulator

An interactive browser-based simulator for visualizing how routing decisions move data through a weighted network graph. This Semester 7 project combines a practical demonstration with research material about routing optimization and computer networks.

## Overview

The Network Routing Simulator turns a small network topology into an explorable learning environment. Users can inspect routers and link costs, calculate the shortest path from Router A to Router D, simulate a router failure, and view the resulting routing table.

The project is intentionally self-contained. The main demonstration is a single HTML file with inline CSS and JavaScript, so it can be opened directly in a browser without a package manager, web server, or external runtime. The research paper and presentation provide the academic context for the implementation.

## Features

- Interactive network topology and routing visualization
- Weighted links with visible costs between routers A, B, C, and D
- Shortest-path calculation from Router A to Router D
- Router failure simulation for Router B and Router C
- Routing table generated from Router A after each route calculation
- Expandable Python graph example for connecting the visual demo to the underlying data model
- Explanations of RIP, OSPF, and BGP routing concepts
- Browser-based demo with no build step or dependency installation
- Python routing engine for reusable shortest-path calculations
- Supporting research paper and presentation for background and project context

## How It Works

The sample topology contains four routers and four links:

| Link | Cost |
| --- | ---: |
| A-B | 2 |
| A-C | 4 |
| B-D | 3 |
| C-D | 1 |

With all routers available, the simulator can compare the path A-B-D with A-C-D and select the lower total cost. When Router B or Router C is marked as failed, the unavailable route is excluded from the calculation and the interface reports whether a path remains available.

The interface presents the result as a path, total cost, and status indicator. It also updates the routing table from Router A so that the next hop and cost for each reachable destination can be inspected.

## Learning Objectives

- Represent a network as a weighted graph.
- Understand how link costs influence route selection.
- Observe how failures affect network reachability.
- Relate shortest-path calculations to routing-table construction.
- Distinguish the high-level purposes of RIP, OSPF, and BGP.

## Project Structure

```
.
├── network_routing_simulator.html  # Interactive routing simulator demo
├── src/
│   └── routing_simulator.py        # Python routing engine and CLI
├── assets/                         # Images and other static assets
├── docs/
│   ├── Network_Routing_Simulator_Research_Paper.pdf
│   └── Network_Routing_Simulator_Presentation.pptx
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

```bash
git clone https://github.com/mayankswaraj18cr-cmd/Semester--7-Project-.git
cd Semester--7-Project-
```

Open `network_routing_simulator.html` in a modern browser to run the simulator. No server or package installation is required.

For a local static server, run one of the following commands from the repository root:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000/network_routing_simulator.html`.

### Run the Python Routing Engine

The Python implementation uses only the standard library. Run it from the repository root:

```bash
python3 src/routing_simulator.py
python3 src/routing_simulator.py --failed B
```

The first command calculates the optimal route from A to D. The second removes Router B and demonstrates failover through the remaining topology. You can also provide custom endpoints with `--source` and `--target`.

## Using the Demo

1. Review the network topology and the cost shown on each link.
2. Choose `No failure`, `Router B fails`, or `Router C fails` from the failure selector.
3. Select `Find Shortest Path (A -> D)` to calculate the route.
4. Read the highlighted path, total cost, and availability status.
5. Inspect the routing table generated from Router A.
6. Expand the Python Source Code section to view the graph representation.

The layout is designed for a narrow, mobile-friendly viewport and can also be opened in a desktop browser.

## Technical Notes

- **Presentation:** HTML and inline CSS provide the interface, topology drawing, tables, controls, and responsive styling.
- **Visualization:** The network diagram uses inline SVG elements for routers, links, labels, and route highlighting.
- **Interaction:** JavaScript handles failure selection, route calculation, result rendering, routing-table updates, and the source-code toggle.
- **Data model:** The topology is represented as an adjacency structure with numeric link costs in both the browser demo and `src/routing_simulator.py`.
- **Python implementation:** The routing engine uses Dijkstra's algorithm with a priority queue, returns immutable route results, and exposes routing-table data for reuse in tests or other interfaces.
- **Documentation:** The `docs/` directory contains the supporting research paper and project presentation.

There is currently no build pipeline, dependency lockfile, or third-party Python dependency. The browser demo remains self-contained, while the Python module provides a testable foundation for future services or command-line workflows.

## Documentation

- [Research Paper](docs/Network_Routing_Simulator_Research_Paper.pdf) - research and problem framing
- [Presentation](docs/Network_Routing_Simulator_Presentation.pptx) - project overview and findings

## Roadmap

- [ ] Extract the simulator into maintainable modules under `src/`
- [ ] Add automated tests for routing behavior
- [ ] Support editable nodes and link costs
- [ ] Add additional routing algorithms for comparison
- [ ] Add packet animation and step-by-step route inspection
- [ ] Add accessibility checks and broader responsive layouts

## Development Workflow

Changes should be kept small and documented in the README when they alter the user workflow or project structure. Before opening a pull request:

```bash
git diff --check
git status --short
```

For changes to the simulator, open the HTML file in a browser and verify the normal route, each failure mode, the routing table, and the source-code toggle.

## Branches

The repository uses `main` for the published project, `develop` for integration work, and `docs/updates` for documentation changes. Additional topic branches may be used for focused feature work.

## License

MIT - see [LICENSE](LICENSE)

## Contact

Mayank Swaraj - [mayankswaraj18cr@gmail.com](mailto:mayankswaraj18cr@gmail.com)