"""Shortest-path routing utilities for the Network Routing Simulator."""

from __future__ import annotations

import argparse
import heapq
from dataclasses import dataclass
from typing import Mapping

Graph = Mapping[str, Mapping[str, int]]

BASE_GRAPH: dict[str, dict[str, int]] = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 3},
    "C": {"A": 4, "D": 1},
    "D": {"B": 3, "C": 1},
}


@dataclass(frozen=True)
class Route:
    """A reachable route and its total link cost."""

    path: tuple[str, ...]
    cost: int


def graph_with_failure(graph: Graph = BASE_GRAPH, failed_node: str | None = None) -> dict[str, dict[str, int]]:
    """Return a copy of graph with a failed router and its links removed."""
    if failed_node is None:
        return {node: dict(neighbors) for node, neighbors in graph.items()}

    return {
        node: {
            neighbor: cost
            for neighbor, cost in neighbors.items()
            if node != failed_node and neighbor != failed_node
        }
        for node, neighbors in graph.items()
        if node != failed_node
    }


def shortest_path(graph: Graph, source: str, target: str) -> Route | None:
    """Find the least-cost route between two routers using Dijkstra's algorithm."""
    if source not in graph or target not in graph:
        return None

    distances = {node: float("inf") for node in graph}
    previous: dict[str, str] = {}
    distances[source] = 0
    queue: list[tuple[int, str]] = [(0, source)]

    while queue:
        distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        if node == target:
            break

        for neighbor, cost in graph[node].items():
            candidate = distance + cost
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                previous[neighbor] = node
                heapq.heappush(queue, (candidate, neighbor))

    if distances[target] == float("inf"):
        return None

    path: list[str] = [target]
    while path[-1] != source:
        path.append(previous[path[-1]])
    path.reverse()
    return Route(tuple(path), int(distances[target]))


def routing_table(graph: Graph, source: str) -> dict[str, tuple[str | None, int | None]]:
    """Build destination -> (next hop, cost) entries from source."""
    table: dict[str, tuple[str | None, int | None]] = {}
    for destination in graph:
        if destination == source:
            continue
        route = shortest_path(graph, source, destination)
        table[destination] = (
            (route.path[1], route.cost) if route else (None, None)
        )
    return table


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate routes in the sample network.")
    parser.add_argument("--source", default="A", help="Source router (default: A)")
    parser.add_argument("--target", default="D", help="Target router (default: D)")
    parser.add_argument("--failed", help="Router to remove before calculating")
    args = parser.parse_args()

    graph = graph_with_failure(failed_node=args.failed)
    route = shortest_path(graph, args.source, args.target)
    if route is None:
        print(f"No route from {args.source} to {args.target}.")
    else:
        print(f"Route: {' -> '.join(route.path)}")
        print(f"Cost: {route.cost}")

    print("Routing table:")
    for destination, (next_hop, cost) in routing_table(graph, args.source).items():
        status = f"next hop {next_hop}, cost {cost}" if next_hop else "unreachable"
        print(f"  {destination}: {status}")


if __name__ == "__main__":
    main()