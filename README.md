# aimas_warmup


| Level             | Strategy | States Generated | Time/s | Solution length |
|-------------------|----------|------------------|--------|-----------------|
| MAPF00            | BFS      | <10,000          | 0.006  | 14              |
| MAPF00            | DFS      | <10,000          | 0.003  | 16              |
| MAPF01            | BFS      | <10,000          | 0.239  | 14              |
| MAPF01            | DFS      | <10,000          | 0.020  | 78              |
| MAPF02            | BFS      | 105,273          | 33.03  | 14              |
| MAPF02            | DFS      | <10,000          | 0.186  | 331             |
| MAPF02C           | BFS      | 110,481          | 31.81  | 14              |
| MAPF02C           | DFS      | <10,000          | 1.131  | 2,531           |
| MAPF03            | BFS      | 332,415          | ~180   | no solution     |
| MAPF03            | DFS      | <10,000          | 0.168  | 74              |
| MAPF03C           | BFS      | 320,884          | ~180   | no solution     |
| MAPF03C           | DFS      | 1,054,394        | 16.71  | no solution     |
| MAPFslidingpuzzle | BFS      | 181,156          | 19.13  | 28              |
| MAPFslidingpuzzle | DFS      | 160,954          | 13.63  | 59,058          |
| MAPFreorder2      | BFS      | 516,354          | ~180   | no solution     |
| MAPFreorder2      | DFS      | 1,209,058        | 22.56  | no solution     |
| BFSfriendly       | BFS      | level            | does   | not exist       |
| BFSfriendly       | DFS      | level            | does   | not exist       |

**Table 1:** Benchmarks table for uninformed search.

### Exercise 4.2: GoalCount as h(n)

| Level             | Eval   | Heuristic  | States Generated | Time/s | Solution length |
|-------------------|--------|------------|------------------|--------|-----------------|
| MAPF00            | A*     | Goal Count |                  | 0.005  | 14              |
| MAPF00            | Greedy | Goal Count |                  | 0.005  | 14              |
| MAPF01            | A*     | Goal Count | 2,154            | 0.282  | 14              |
| MAPF01            | Greedy | Goal Count | 2,154            | 0.278  | 14              |
| MAPF02            | A*     | Goal Count | 110,437          | 47.28  | 14              |
| MAPF02            | Greedy | Goal Count | 107,826          | 46.80  | 14              |
| MAPF02C           | A*     | Goal Count | 105,780          | 45.25  | 14              |
| MAPF02C           | Greedy | Goal Count | 67,489           | 23.08  | 27              |
| MAPF03            | A*     | Goal Count | 284,878          | ~180   | no solution     |
| MAPF03            | Greedy | Goal Count | 284,878          | ~180   | no solution     |
| MAPF03C           | A*     | Goal Count | 284,878          | ~180   | no solution     |
| MAPF03C           | Greedy | Goal Count | 280,102          | 170.3  | no solution     |
| MAPFslidingpuzzle | A*     | Goal Count | 104,674          | 5.623  | 28              |
| MAPFslidingpuzzle | Greedy | Goal Count |                  | 0.042  | 46              |
| MAPFreorder2      | A*     | Goal Count | 365,398          | ~180   | no solution     |
| MAPFreorder2      | Greedy | Goal Count | 417,258          | ~180   | no solution     |
| BFSFriendly       | A*     | Goal Count | level            | does   | not exist       |
| BFSFriendly       | Greedy | Goal Count | level            | does   | not exist       |

### Exercise 4.4: Summed Manhattan distance as h(n)

| Level             | Eval   | Heuristic | States Generated | Time/s | Solution length |
|-------------------|--------|-----------|------------------|--------|-----------------|
| MAPF00            | A*     | SumManDis |                  | 0.004s | 14              |
| MAPF00            | Greedy | SumManDis |                  | 0.003s | 18              |
| MAPF01            | A*     | SumManDis | 1,547            | 0.208s | 14              |
| MAPF01            | Greedy | SumManDis |                  | 0.034s | 18              |
| MAPF02            | A*     | SumManDis | 89,039           | 29.75s | 14              |
| MAPF02            | Greedy | SumManDis | 16,170           | 3.527s | 18              |
| MAPF02C           | A*     | SumManDis |                  | 0.149s | 18              |
| MAPF02C           | Greedy | SumManDis |                  | 0.031s | 21              |
| MAPF03            | A*     | SumManDis | 383,041          | ~3m    | no solution     |
| MAPF03            | Greedy | SumManDis | 298,403          | ~3m    | no solution     |
| MAPF03C           | A*     | SumManDis |                  | 0.031s | 18              |
| MAPF03C           | Greedy | SumManDis |                  | 0.032s | 18              |
| MAPFslidingpuzzle | A*     | SumManDis | 6,157            | 0.437s | 28              |
| MAPFslidingpuzzle | Greedy | SumManDis |                  | 0.011s | 36              |
| MAPFreorder2      | A*     | SumManDis | 542,364          | ~3m    | no solution     |
| MAPFreorder2      | Greedy | SumManDis | 432,344          | ~3m    | no solution     |
| BFSFriendly       | A*     | SumManDis | level            | does   | not exist       |
| BFSFriendly       | Greedy | SumManDis | level            | does   | not exist       |

### Exercise 4.4: max(DistMap) as h(n)
| Level              | Eval   | Heuristic    | States Generated | Time/s  | Solution length |
|--------------------|--------|--------------|------------------|---------|-----------------|
| MAPF00             | A*     | MaxDistMap   |                  | 0.003s  | 14              |
| MAPF00             | Greedy | MaxDistMap   |                  | 0.002s  | 14              |
| MAPF01             | A*     | MaxDistMap   |                  | 0.125s  | 14              |
| MAPF01             | Greedy | MaxDistMap   |                  | 0.006s  | 14              |
| MAPF02             | A*     | MaxDistMap   | 60,900           | 14.77s  | 14              |
| MAPF02             | Greedy | MaxDistMap   |                  | 0.012s  | 14              |
| MAPF02C            | A*     | MaxDistMap   | 34,844           | 6.368s  | 14              |
| MAPF02C            | Greedy | MaxDistMap   |                  | 0.014s  | 14              |
| MAPF03             | A*     | MaxDistMap   | 402,030          | ~3m     | no solution     |
| MAPF03             | Greedy | MaxDistMap   |                  | 0.043s  | 14              |
| MAPF03C            | A*     | MaxDistMap   | 527,484          | 125,44s | 14              |
| MAPF03C            | Greedy | MaxDistMap   |                  | 0.515s  | 16              |
| MAPFslidingpuzzle  | A*     | MaxDistMap   | 172,707          | 10.72s  | 28              |
| MAPFslidingpuzzle  | Greedy | MaxDistMap   | 1,609            | 0.101s  | 36              |
| MAPFreorder2       | A*     | MaxDistMap   | 439,813          | ~3m     | no solution     |
| MAPFreorder2       | Greedy | MaxDistMap   | 121,521          | 45.53s  | 62              |
| BFSFriendly        | A*     | MaxDistMap   | level            | does    | not exist       |
| BFSFriendly        | Greedy | MaxDistMap   | level            | does    | not exist       |

### Exercise 6.1: GoalCount as h(n)
| Level      | Eval   | Heuristic | States Generated | Time/s | Solution length |
|------------|--------|-----------|------------------|--------|-----------------|
| SAFirefly  | Greedy | GoalCount | 7,954,213        | 347.3s | no solution     |
| SAFirefly  | BFS    |           | 2,448,236        | 70.84s | no solution     |
| SAFirefly  | DFS    |           | 7,316,782        | ~360s  | no solution     |
| SACrunch   | Greedy | GoalCount | <10,000          | ~0.00s | no solution     |
| SACrunch   | BFS    |           | <10,000          | ~0.00s | no solution     |
| SACrunch   | DFS    |           | <10,000          | ~0.00s | no solution     |

### Exercise 6.2
goalcount boxes:
SAsoko_128: states generated ~82k

distmap boxes:
SAsoko_128: states generated <10k