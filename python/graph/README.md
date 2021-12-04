# Graphs

Graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge

Graphs Implementation that should be represented as an adjacency list, and it should include the following methods: `add node` `add edge` `get nodes` `get neighbors` `size`

## Approach & Efficiency

1. Vertex class for Adding a node to the graph
2. Stack class and Queue class a helper class for the graph
3. Edge class for adding a new edge between two nodes in the graph
4. Graph class that contain the following methods:

-   `add node` Adding a node to the graph ==> time: O(1), space: O(1)
-   `add edge` Adding an edge to the graph ==> time : O(n), space : O(n)
-   `get nodes` Getting all nodes in the Graph ==> time: O(n), space: O(n)
-   `get neighbors` Getting the collection of edges connected to a given node ==> time: O(n), space: O(n)
-   `size` Returning the total number of nodes in the graph ==> time: O(1), space: O(1)

## API

-   [x] add node

*   Arguments: value
*   Returns: The added node
*   Add a node to the graph

-   [x] add edge

*   Arguments: 2 nodes to be connected by the edge, weight (optional)
*   Returns: nothing
*   Adds a new edge between two nodes in the graph
*   If specified, assign a weight to the edge
*   Both nodes should already be in the Graph

-   [x] get nodes

*   Arguments: none
*   Returns all of the nodes in the graph as a collection (set, list, or similar)

-   [x] get neighbors

*   Arguments: node
*   Returns a collection of edges connected to the given node
*   Include the weight of the connection in the returned collection

-   [x] size

*   Arguments: none
*   Returns the total number of nodes in the graph

Structure and Testing

-   [x] Node can be successfully added to the graph
-   [x] An edge can be successfully added to the graph
-   [x] A collection of all nodes can be properly retrieved from the graph
-   [x] All appropriate neighbors can be retrieved from the graph
-   [x] Neighbors are returned with the weight between nodes included
-   [x] The proper size is returned, representing the number of nodes in the graph
-   [x] A graph with only one node and edge can be properly returned
-   [x] An empty graph properly returns null

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/43
