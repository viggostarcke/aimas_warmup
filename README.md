# aimas_warmup


| Level               | Strategy | States Generated | Time/s | Solution length |
|---------------------|----------|------------------|--------|-----------------|
| MAPF00            | BFS      |                  |        |                 |
| MAPF00            | DFS      |                  |        |                 |
| MAPF01            | BFS      |                  |        |                 |
| MAPF01            | DFS      |                  |        |                 |
| MAPF02            | BFS      |                  |        |                 |
| MAPF02            | DFS      |                  |        |                 |
| MAPF02C          | BFS      |                  |        |                 |
| MAPF02C          | DFS      |                  |        |                 |
| MAPF03            | BFS      |                  |        |                 |
| MAPF03            | DFS      |                  |        |                 |
| MAPF03C          | BFS      |                  |        |                 |
| MAPF03C          | DFS      |                  |        |                 |
| MAPFslidingpuzzle | BFS      |                  |        |                 |
| MAPFslidingpuzzle | DFS      |                  |        |                 |
| MAPFreorder2      | BFS      |                  |        |                 |
| MAPFreorder2      | DFS      |                  |        |                 |
| BFSfriendly       | BFS      |                  |        |                 |
| BFSfriendly       | DFS      |                  |        |                 |

**Table 1:** Benchmarks table for uninformed search.

### Exercise 4.2: GoalCount as h(n)

| Level            | Eval   | Heuristic  | States Generated | Time/s  | Solution length |
|------------------|--------|------------|--------------|---------|-----------------|
| MAPF00           | A*     | Goal Count |              | 0.005s  | 14              |
| MAPF00           | Greedy | Goal Count |              | 0.005s  | 14              |
| MAPF01           | A*     | Goal Count | 2,154        | 0.282s  | 14              |
| MAPF01           | Greedy | Goal Count | 2,154        | 0.278s  | 14              |
| MAPF02           | A*     | Goal Count | 110,437      | 47.28s  | 14              |
| MAPF02           | Greedy | Goal Count | 107,826      | 46.80s  | 14              |
| MAPF02C          | A*     | Goal Count | 105,780      | 45.25s  | 14              |
| MAPF02C          | Greedy | Goal Count | 67,489       | 23.08s  | 27              |
| MAPF03           | A*     | Goal Count | 284,878      | ~3m     | no solution     |
| MAPF03           | Greedy | Goal Count | 284,878      | ~3m     | no solution     |
| MAPF03C          | A*     | Goal Count | 284,878      | ~3m     | no solution     |
| MAPF03C          | Greedy | Goal Count | 280,102      | 170.27s | no solution     |
| MAPFslidingpuzzle | A*     | Goal Count | 104,674      | 5.62s   | 28              |
| MAPFslidingpuzzle | Greedy | Goal Count |              | 0.04s   | 46              |
| MAPFreorder2     | A*     | Goal Count | 365,398      | ~3m     | no solution     |
| MAPFreorder2     | Greedy | Goal Count | 417,258      | ~3m     | no solution     |
| BFSFriendly      | A*     | Goal Count | level        | does    | not exist       |
| BFSFriendly      | Greedy | Goal Count | level        | does    | not exist       |

### Exercise 4.4: Summed Manhattan distance as h(n)

| Level            | Eval   | Heuristic  | States Generated | Time/s | Solution length |
|------------------|--------|------------|------------------|--------|-----------------|
| MAPF00           | A*     | Goal Count |                  | 0.004s | 14              |
| MAPF00           | Greedy | Goal Count |                  | 0.003s | 18              |
| MAPF01           | A*     | Goal Count | 1,547            | 0.208s | 14              |
| MAPF01           | Greedy | Goal Count |                  | 0.034s | 18              |
| MAPF02           | A*     | Goal Count | 89,039           | 29.75s | 14              |
| MAPF02           | Greedy | Goal Count | 16,170           | 3.527s | 18              |
| MAPF02C          | A*     | Goal Count |                  | 0.149s | 18              |
| MAPF02C          | Greedy | Goal Count |                  | 0.031s | 21              |
| MAPF03           | A*     | Goal Count | 383,041          | ~3m    | no solution     |
| MAPF03           | Greedy | Goal Count | 298,403          | ~3m    | no solution     |
| MAPF03C          | A*     | Goal Count |                  | 0.031s | 18              |
| MAPF03C          | Greedy | Goal Count |                  | 0.032s | 18              |
| MAPFslidingpuzzle | A*     | Goal Count | 6,157            | 0.437s | 28              |
| MAPFslidingpuzzle | Greedy | Goal Count |                  | 0.011s | 36              |
| MAPFreorder2     | A*     | Goal Count | 542,364          | ~3m    | no solution     |
| MAPFreorder2     | Greedy | Goal Count | 432,344          | ~3m    | no solution     |
| BFSFriendly      | A*     | Goal Count | level            | does   | not exist       |
| BFSFriendly      | Greedy | Goal Count | level            | does   | not exist       |