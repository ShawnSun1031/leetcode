
#include <iostream>
#include <vector>
using namespace std;

// here maxD represent the diameter of the tree
int maxD = -1, maxNode = -1;
// maxNode represents node at maximum distance

// declaring the visited node as we will be using the DFS
int vis[8];

void createEdge(int a, int b, vector<int> graph[])
{

    // creating undireted edges between the connected nodes
    graph[a].push_back(b);
    graph[b].push_back(a);
}

void DFS(vector<int> graph[], int node, int d)
{
    // marking the node as visited
    vis[node] = 1;

    // if the distance from root is greater then maximum Distance then updating the maximum value of distance
    // also storing the maxNode no. as this node is now at the farthest distance
    if (d > maxD)
    {
        maxNode = node;
        maxD = d;
    }

    // applying the standard dfs
    for (auto x : graph[node])
    {
        if (vis[x] == 0)
        {
            DFS(graph, x, d + 1);
        }
    }
}

int main()
{

    // first creating the nodes of the graph
    vector<int> graph[8];

    // now creating the edges of the tree as shown in the image of  this article
    createEdge(1, 2, graph);
    createEdge(2, 3, graph);
    createEdge(3, 7, graph);
    createEdge(2, 4, graph);
    createEdge(4, 5, graph);
    createEdge(4, 6, graph);

    // Applyting DFS from node 1
    DFS(graph, 1, 1);
    // we could have choosen any node in the graph but for simplicity we have choosen node 1

    // making every node unvisited as we will be applying DFS
    maxD = -1;
    for (int i = 1; i <= 8; i++)
    {
        vis[i] = 0;
    }

    // applying the dfs for the second time as this will give the diameter of the tree
    DFS(graph, maxNode, 1);

    // Now printing the maximum diameter of the tree
    cout << maxD << " is the diameter of the tree " << endl;

    return 0;
}
