### 0.Environment
![](./environment/M1-ENV.png)

### 1.Versions
| version   | date          |
|:----------|:--------------|
| 3.9.17    | June 6, 2023  |
| 3.10.10   | Feb. 8, 2023  |
| 3.10.11   | April 5, 2023 |
| 3.10.9    | Dec. 6, 2022  |
| 3.11.0    | Oct. 24, 2022 |
| 3.11.1    | Dec. 6, 2022  |
| 3.11.2    | Feb. 8, 2023  |
| 3.11.3    | April 5, 2023 |

### 2.Source
|    | Task                          | 3.9.17               | 3.10.10              | 3.10.11              | 3.10.9               | 3.11.0               | 3.11.1               | 3.11.2               | 3.11.3               |
|---:|:------------------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
|  0 | 2to3                          | 247 ms +- 19 ms      | 262 ms +- 52 ms      | 243 ms +- 6 ms       | 242 ms +- 11 ms      | 184 ms +- 9 ms       | 179 ms +- 4 ms       | 257 ms +- 106 ms     | 184 ms +- 5 ms       |
|  1 | async_generators              | 279 ms +- 9 ms       | 315 ms +- 70 ms      | 281 ms +- 6 ms       | 292 ms +- 54 ms      | 219 ms +- 5 ms       | 225 ms +- 12 ms      | 242 ms +- 31 ms      | 220 ms +- 5 ms       |
|  2 | async_tree_none               | 589 ms +- 72 ms      | 608 ms +- 192 ms     | 559 ms +- 30 ms      | 563 ms +- 36 ms      | 402 ms +- 19 ms      | 394 ms +- 9 ms       | 604 ms +- 155 ms     | 388 ms +- 8 ms       |
|  3 | async_tree_cpu_io_mixed       | 979 ms +- 301 ms     | 814 ms +- 51 ms      | 810 ms +- 31 ms      | 819 ms +- 42 ms      | 621 ms +- 44 ms      | 640 ms +- 50 ms      | 862 ms +- 257 ms     | 628 ms +- 44 ms      |
|  4 | async_tree_eager              | 577 ms +- 50 ms      | /                    | /                    | 561 ms +- 44 ms      | /                    | /                    | /                    | /                    |
|  5 | async_tree_eager_cpu_io_mixed | 867 ms +- 108 ms     | /                    | /                    | 813 ms +- 39 ms      | /                    | /                    | /                    | /                    |
|  6 | async_tree_eager_io           | 1.59 sec +- 0.15 sec | /                    | /                    | 1.48 sec +- 0.13 sec | /                    | /                    | /                    | /                    |
|  7 | async_tree_eager_memoization  | 935 ms +- 526 ms     | /                    | /                    | 721 ms +- 403 ms     | /                    | /                    | /                    | /                    |
|  8 | async_tree_io                 | 1.58 sec +- 0.14 sec | 1.58 sec +- 0.16 sec | 1.43 sec +- 0.05 sec | 1.70 sec +- 0.53 sec | 873 ms +- 30 ms      | 875 ms +- 23 ms      | 1.35 sec +- 0.50 sec | 898 ms +- 31 ms      |
|  9 | async_tree_memoization        | 669 ms +- 33 ms      | 662 ms +- 39 ms      | 655 ms +- 30 ms      | 641 ms +- 32 ms      | 456 ms +- 33 ms      | 451 ms +- 29 ms      | 661 ms +- 217 ms     | 467 ms +- 47 ms      |
| 10 | asyncio_tcp                   | 932 ms +- 579 ms     | /                    | /                    | 836 ms +- 86 ms      | /                    | /                    | /                    | /                    |
| 11 | asyncio_tcp_ssl               | 2.76 sec +- 0.51 sec | /                    | /                    | 2.60 sec +- 0.82 sec | /                    | /                    | /                    | /                    |
| 12 | chameleon                     | 7.57 ms +- 0.35 ms   | 6.66 ms +- 0.15 ms   | 6.89 ms +- 0.36 ms   | 6.49 ms +- 0.40 ms   | 4.77 ms +- 0.07 ms   | 4.85 ms +- 0.07 ms   | 5.27 ms +- 0.76 ms   | 4.74 ms +- 0.10 ms   |
| 13 | chaos                         | 83.4 ms +- 8.6 ms    | 78.2 ms +- 2.9 ms    | 79.2 ms +- 2.8 ms    | 85.6 ms +- 33.7 ms   | 51.1 ms +- 0.7 ms    | 51.1 ms +- 0.7 ms    | 58.4 ms +- 8.6 ms    | 52.5 ms +- 1.0 ms    |
| 14 | comprehensions                | 20.1 us +- 0.5 us    | /                    | /                    | 21.5 us +- 4.1 us    | /                    | /                    | /                    | /                    |
| 15 | bench_mp_pool                 | 8.85 ms +- 1.27 ms   | 8.49 ms +- 0.74 ms   | 8.63 ms +- 0.98 ms   | 9.37 ms +- 1.69 ms   | 5.98 ms +- 0.37 ms   | 6.00 ms +- 0.35 ms   | 10.6 ms +- 6.5 ms    | 7.35 ms +- 1.37 ms   |
| 16 | bench_thread_pool             | 1.11 ms +- 0.06 ms   | 1.10 ms +- 0.03 ms   | 1.16 ms +- 0.06 ms   | 1.29 ms +- 0.34 ms   | 1.07 ms +- 0.03 ms   | 1.08 ms +- 0.04 ms   | 1.39 ms +- 0.74 ms   | 1.09 ms +- 0.06 ms   |
| 17 | coroutines                    | 33.7 ms +- 12.7 ms   | 22.9 ms +- 0.3 ms    | 24.0 ms +- 0.9 ms    | 22.9 ms +- 0.4 ms    | 18.4 ms +- 0.2 ms    | 18.5 ms +- 0.3 ms    | 21.3 ms +- 3.0 ms    | 19.6 ms +- 2.1 ms    |
| 18 | coverage                      | 35.2 ms +- 1.0 ms    | 45.3 ms +- 0.6 ms    | 45.4 ms +- 0.9 ms    | 44.9 ms +- 1.9 ms    | 66.3 ms +- 18.7 ms   | 62.2 ms +- 1.6 ms    | 75.5 ms +- 12.2 ms   | 65.5 ms +- 2.6 ms    |
| 19 | crypto_pyaes                  | 90.8 ms +- 5.4 ms    | 90.7 ms +- 1.8 ms    | 92.1 ms +- 3.2 ms    | 90.9 ms +- 3.4 ms    | 55.1 ms +- 0.8 ms    | 56.2 ms +- 1.6 ms    | 64.6 ms +- 13.7 ms   | 58.1 ms +- 2.2 ms    |
| 20 | dask                          | 520 ms +- 91 ms      | /                    | /                    | 554 ms +- 359 ms     | /                    | /                    | /                    | /                    |
| 21 | deepcopy                      | 320 us +- 6 us       | 316 us +- 5 us       | 315 us +- 12 us      | 363 us +- 123 us     | 235 us +- 5 us       | 237 us +- 4 us       | 275 us +- 40 us      | 255 us +- 13 us      |
| 22 | deepcopy_reduce               | 2.85 us +- 0.20 us   | 2.71 us +- 0.06 us   | 2.74 us +- 0.09 us   | 2.78 us +- 0.36 us   | 2.08 us +- 0.03 us   | 2.09 us +- 0.03 us   | 2.40 us +- 0.41 us   | 2.19 us +- 0.15 us   |
| 23 | deepcopy_memo                 | 38.9 us +- 3.1 us    | 37.2 us +- 0.8 us    | 37.7 us +- 1.3 us    | 36.3 us +- 0.7 us    | 25.0 us +- 0.3 us    | 25.2 us +- 0.5 us    | 28.4 us +- 4.1 us    | 25.7 us +- 0.6 us    |
| 24 | deltablue                     | 7.36 ms +- 4.88 ms   | 5.62 ms +- 0.74 ms   | 5.59 ms +- 0.15 ms   | 5.41 ms +- 0.13 ms   | 2.62 ms +- 0.05 ms   | 2.66 ms +- 0.04 ms   | 3.13 ms +- 0.58 ms   | 2.78 ms +- 0.09 ms   |
| 25 | django_template               | 36.3 ms +- 2.5 ms    | 32.5 ms +- 0.9 ms    | 32.8 ms +- 1.0 ms    | 33.8 ms +- 3.9 ms    | 23.1 ms +- 0.4 ms    | 22.9 ms +- 0.4 ms    | 26.9 ms +- 4.9 ms    | 24.3 ms +- 0.6 ms    |
| 26 | docutils                      | 2.21 sec +- 0.12 sec | 2.21 sec +- 0.04 sec | 2.20 sec +- 0.10 sec | 2.26 sec +- 0.12 sec | 1.72 sec +- 0.03 sec | 1.73 sec +- 0.06 sec | 3.06 sec +- 1.04 sec | 1.86 sec +- 0.05 sec |
| 27 | dulwich_log                   | 52.6 ms +- 5.6 ms    | 49.9 ms +- 1.1 ms    | 49.6 ms +- 0.7 ms    | 50.5 ms +- 1.7 ms    | 40.2 ms +- 0.7 ms    | 40.3 ms +- 0.7 ms    | 86.8 ms +- 54.7 ms   | 42.5 ms +- 1.7 ms    |
| 28 | fannkuch                      | 338 ms +- 10 ms      | 357 ms +- 7 ms       | 358 ms +- 8 ms       | 338 ms +- 7 ms       | 277 ms +- 3 ms       | 281 ms +- 4 ms       | 338 ms +- 47 ms      | 287 ms +- 5 ms       |
| 29 | float                         | 105 ms +- 2 ms       | 94.2 ms +- 1.8 ms    | 93.9 ms +- 1.2 ms    | 94.3 ms +- 2.5 ms    | 64.3 ms +- 2.2 ms    | 64.1 ms +- 1.3 ms    | 88.4 ms +- 32.3 ms   | 67.1 ms +- 18.9 ms   |
| 30 | create_gc_cycles              | 969 us +- 24 us      | /                    | /                    | 1.02 ms +- 0.04 ms   | /                    | /                    | /                    | /                    |
| 31 | gc_traversal                  | 2.94 ms +- 0.14 ms   | /                    | /                    | 2.98 ms +- 0.13 ms   | /                    | /                    | /                    | /                    |
| 32 | generators                    | 33.8 ms +- 2.2 ms    | 32.2 ms +- 0.9 ms    | 32.7 ms +- 1.1 ms    | 32.7 ms +- 2.5 ms    | 27.3 ms +- 0.6 ms    | 27.2 ms +- 0.4 ms    | 31.0 ms +- 4.1 ms    | 28.4 ms +- 0.9 ms    |
| 33 | genshi_text                   | 21.9 ms +- 1.5 ms    | 19.5 ms +- 0.2 ms    | 20.0 ms +- 0.5 ms    | 19.7 ms +- 0.7 ms    | 15.1 ms +- 0.2 ms    | 16.4 ms +- 4.2 ms    | 17.4 ms +- 3.0 ms    | 15.7 ms +- 0.4 ms    |
| 34 | genshi_xml                    | 43.0 ms +- 2.9 ms    | 40.3 ms +- 0.5 ms    | 40.0 ms +- 0.8 ms    | 41.0 ms +- 4.6 ms    | 33.4 ms +- 0.7 ms    | 36.8 ms +- 9.5 ms    | 41.6 ms +- 9.8 ms    | 35.8 ms +- 0.9 ms    |
| 35 | go                            | 192 ms +- 4 ms       | 175 ms +- 5 ms       | 176 ms +- 6 ms       | 175 ms +- 6 ms       | 98.9 ms +- 2.1 ms    | 99.4 ms +- 2.2 ms    | 125 ms +- 39 ms      | 102 ms +- 1 ms       |
| 36 | hexiom                        | 6.96 ms +- 0.13 ms   | 6.84 ms +- 0.11 ms   | 6.94 ms +- 0.20 ms   | 6.97 ms +- 0.24 ms   | 4.45 ms +- 0.06 ms   | 4.46 ms +- 0.08 ms   | 5.13 ms +- 0.77 ms   | 4.65 ms +- 0.08 ms   |
| 37 | html5lib                      | 57.8 ms +- 5.6 ms    | 51.9 ms +- 3.4 ms    | 49.8 ms +- 2.3 ms    | 58.7 ms +- 33.3 ms   | 35.0 ms +- 2.0 ms    | 35.5 ms +- 2.0 ms    | 51.3 ms +- 22.7 ms   | 36.4 ms +- 2.2 ms    |
| 38 | json_dumps                    | 12.1 ms +- 0.2 ms    | 12.0 ms +- 0.2 ms    | 12.0 ms +- 0.2 ms    | 11.9 ms +- 0.4 ms    | 11.1 ms +- 0.2 ms    | 11.3 ms +- 0.1 ms    | 13.9 ms +- 3.6 ms    | 11.6 ms +- 0.2 ms    |
| 39 | json_loads                    | 27.0 us +- 0.6 us    | 27.4 us +- 0.4 us    | 27.3 us +- 0.4 us    | 26.8 us +- 1.4 us    | 25.9 us +- 0.5 us    | 25.9 us +- 0.2 us    | 29.2 us +- 3.6 us    | 26.6 us +- 0.4 us    |
| 40 | logging_format                | 6.50 us +- 0.13 us   | 6.71 us +- 0.10 us   | 6.71 us +- 0.10 us   | 6.59 us +- 0.14 us   | 4.83 us +- 0.09 us   | 4.75 us +- 0.09 us   | 5.68 us +- 1.20 us   | 4.85 us +- 0.06 us   |
| 41 | logging_silent                | 153 ns +- 19 ns      | 143 ns +- 7 ns       | 141 ns +- 4 ns       | 138 ns +- 4 ns       | 70.6 ns +- 1.0 ns    | 70.8 ns +- 1.9 ns    | 80.3 ns +- 12.8 ns   | 74.2 ns +- 2.1 ns    |
| 42 | logging_simple                | 6.07 us +- 0.20 us   | 6.20 us +- 0.13 us   | 6.28 us +- 0.36 us   | 6.07 us +- 0.11 us   | 4.45 us +- 0.07 us   | 4.40 us +- 0.06 us   | 7.52 us +- 2.70 us   | 4.48 us +- 0.07 us   |
| 43 | mako                          | 13.2 ms +- 1.2 ms    | 11.8 ms +- 0.8 ms    | 11.9 ms +- 0.2 ms    | 12.0 ms +- 0.5 ms    | 7.92 ms +- 0.25 ms   | 7.88 ms +- 0.23 ms   | 15.1 ms +- 4.4 ms    | 8.05 ms +- 0.16 ms   |
| 44 | mdp                           | 2.89 sec +- 0.56 sec | 2.77 sec +- 0.03 sec | 2.76 sec +- 0.02 sec | 2.95 sec +- 0.43 sec | 2.49 sec +- 0.03 sec | 2.52 sec +- 0.02 sec | 3.13 sec +- 0.64 sec | 2.58 sec +- 0.03 sec |
| 45 | meteor_contest                | 89.5 ms +- 8.1 ms    | 85.2 ms +- 1.8 ms    | 85.2 ms +- 0.6 ms    | 84.5 ms +- 1.9 ms    | 78.2 ms +- 0.9 ms    | 77.9 ms +- 0.9 ms    | 80.1 ms +- 1.2 ms    | 80.4 ms +- 0.6 ms    |
| 46 | nbody                         | 97.2 ms +- 7.0 ms    | 95.2 ms +- 1.0 ms    | 96.8 ms +- 2.4 ms    | 94.3 ms +- 1.0 ms    | 64.7 ms +- 0.6 ms    | 63.4 ms +- 1.2 ms    | 63.8 ms +- 0.7 ms    | 64.8 ms +- 1.7 ms    |
| 47 | nqueens                       | 72.6 ms +- 1.9 ms    | 73.5 ms +- 1.0 ms    | 73.4 ms +- 1.6 ms    | 73.9 ms +- 3.6 ms    | 62.0 ms +- 1.1 ms    | 63.1 ms +- 0.8 ms    | 64.6 ms +- 1.1 ms    | 64.4 ms +- 1.0 ms    |
| 48 | pathlib                       | 26.2 ms +- 20.6 ms   | 18.7 ms +- 0.9 ms    | 18.3 ms +- 0.3 ms    | 19.2 ms +- 1.2 ms    | 16.8 ms +- 0.6 ms    | 17.4 ms +- 1.6 ms    | 17.8 ms +- 0.5 ms    | 17.2 ms +- 0.4 ms    |
| 49 | pickle                        | 11.7 us +- 4.0 us    | 9.12 us +- 0.11 us   | 9.21 us +- 0.12 us   | 9.62 us +- 3.36 us   | 8.38 us +- 0.12 us   | 8.25 us +- 0.14 us   | 8.41 us +- 0.23 us   | 8.43 us +- 0.10 us   |
| 50 | pickle_dict                   | 31.4 us +- 13.1 us   | 25.1 us +- 0.3 us    | 25.2 us +- 0.3 us    | 24.9 us +- 0.6 us    | 20.4 us +- 0.2 us    | 19.4 us +- 0.5 us    | 19.4 us +- 0.1 us    | 19.8 us +- 0.4 us    |
| 51 | pickle_list                   | 4.66 us +- 1.26 us   | 3.87 us +- 0.04 us   | 3.86 us +- 0.06 us   | 3.96 us +- 0.53 us   | 3.06 us +- 0.09 us   | 3.02 us +- 0.05 us   | 3.04 us +- 0.05 us   | 3.11 us +- 0.05 us   |
| 52 | pickle_pure_python            | 427 us +- 131 us     | 339 us +- 9 us       | 340 us +- 8 us       | 411 us +- 194 us     | 216 us +- 3 us       | 216 us +- 6 us       | 223 us +- 8 us       | 220 us +- 3 us       |
| 53 | pidigits                      | 250 ms +- 121 ms     | 220 ms +- 1 ms       | 220 ms +- 2 ms       | 224 ms +- 24 ms      | 213 ms +- 11 ms      | 212 ms +- 2 ms       | 215 ms +- 1 ms       | 218 ms +- 1 ms       |
| 54 | pprint_pformat                | 1.21 sec +- 0.12 sec | 1.50 sec +- 0.03 sec | 1.48 sec +- 0.02 sec | 1.72 sec +- 0.52 sec | 1.03 sec +- 0.01 sec | 1.05 sec +- 0.02 sec | 1.04 sec +- 0.02 sec | 1.07 sec +- 0.05 sec |
| 55 | pyflate                       | 528 ms +- 25 ms      | 494 ms +- 22 ms      | 488 ms +- 6 ms       | 497 ms +- 14 ms      | 316 ms +- 25 ms      | 303 ms +- 6 ms       | 309 ms +- 14 ms      | 310 ms +- 10 ms      |
| 56 | python_startup                | 16.6 ms +- 2.6 ms    | 13.5 ms +- 0.3 ms    | 14.0 ms +- 0.9 ms    | 14.4 ms +- 1.4 ms    | 13.6 ms +- 0.7 ms    | 13.5 ms +- 0.3 ms    | 13.6 ms +- 0.7 ms    | 13.4 ms +- 0.3 ms    |
| 57 | python_startup_no_site        | 9.55 ms +- 1.69 ms   | 7.58 ms +- 0.29 ms   | 7.77 ms +- 0.26 ms   | 7.75 ms +- 0.55 ms   | 8.52 ms +- 0.47 ms   | 8.49 ms +- 0.45 ms   | 8.41 ms +- 0.22 ms   | 8.44 ms +- 0.25 ms   |
| 58 | raytrace                      | 464 ms +- 266 ms     | 374 ms +- 6 ms       | 373 ms +- 15 ms      | 391 ms +- 55 ms      | 212 ms +- 3 ms       | 211 ms +- 2 ms       | 211 ms +- 3 ms       | 213 ms +- 3 ms       |
| 59 | regex_compile                 | 140 ms +- 95 ms      | 110 ms +- 1 ms       | 108 ms +- 2 ms       | 109 ms +- 2 ms       | 81.4 ms +- 1.1 ms    | 81.3 ms +- 0.9 ms    | 82.1 ms +- 1.6 ms    | 81.7 ms +- 0.9 ms    |
| 60 | regex_dna                     | 176 ms +- 2 ms       | 170 ms +- 2 ms       | 176 ms +- 56 ms      | 171 ms +- 8 ms       | 128 ms +- 5 ms       | 130 ms +- 13 ms      | 128 ms +- 1 ms       | 127 ms +- 1 ms       |
| 61 | regex_effbot                  | 2.54 ms +- 0.10 ms   | 2.53 ms +- 0.06 ms   | 2.47 ms +- 0.03 ms   | 2.43 ms +- 0.17 ms   | 1.96 ms +- 0.02 ms   | 1.96 ms +- 0.02 ms   | 1.98 ms +- 0.05 ms   | 1.97 ms +- 0.02 ms   |
| 62 | regex_v8                      | 21.6 ms +- 0.4 ms    | 21.3 ms +- 0.7 ms    | 21.3 ms +- 0.7 ms    | 21.5 ms +- 0.7 ms    | 15.2 ms +- 0.3 ms    | 15.5 ms +- 1.0 ms    | 15.3 ms +- 0.2 ms    | 16.0 ms +- 2.2 ms    |
| 63 | richards                      | 56.3 ms +- 1.2 ms    | 57.3 ms +- 0.9 ms    | 57.6 ms +- 1.3 ms    | 60.3 ms +- 7.6 ms    | 33.0 ms +- 1.3 ms    | 32.3 ms +- 0.9 ms    | 32.4 ms +- 0.7 ms    | 32.3 ms +- 0.7 ms    |
| 64 | richards_super                | 65.3 ms +- 1.4 ms    | /                    | /                    | 75.0 ms +- 13.4 ms   | /                    | /                    | /                    | /                    |
| 65 | scimark_fft                   | 423 ms +- 11 ms      | 452 ms +- 7 ms       | 447 ms +- 5 ms       | 460 ms +- 46 ms      | 387 ms +- 8 ms       | 392 ms +- 16 ms      | 396 ms +- 6 ms       | 395 ms +- 6 ms       |
| 66 | scimark_lu                    | 177 ms +- 5 ms       | 159 ms +- 5 ms       | 156 ms +- 1 ms       | 161 ms +- 5 ms       | 126 ms +- 7 ms       | 124 ms +- 3 ms       | 122 ms +- 2 ms       | 124 ms +- 1 ms       |
| 67 | scimark_monte_carlo           | 101 ms +- 2 ms       | 96.2 ms +- 2.0 ms    | 95.4 ms +- 1.8 ms    | 101 ms +- 17 ms      | 68.5 ms +- 3.8 ms    | 69.0 ms +- 2.8 ms    | 69.6 ms +- 2.8 ms    | 67.5 ms +- 1.9 ms    |
| 68 | scimark_sor                   | 180 ms +- 5 ms       | 162 ms +- 3 ms       | 160 ms +- 1 ms       | 162 ms +- 4 ms       | 104 ms +- 2 ms       | 106 ms +- 6 ms       | 104 ms +- 1 ms       | 104 ms +- 1 ms       |
| 69 | scimark_sparse_mat_mult       | 8.95 ms +- 1.82 ms   | 8.87 ms +- 0.20 ms   | 8.80 ms +- 0.05 ms   | 8.94 ms +- 0.97 ms   | 8.20 ms +- 0.76 ms   | 8.02 ms +- 0.06 ms   | 8.05 ms +- 0.11 ms   | 8.17 ms +- 0.05 ms   |
| 70 | spectral_norm                 | 108 ms +- 4 ms       | 105 ms +- 2 ms       | 106 ms +- 21 ms      | 106 ms +- 7 ms       | 75.0 ms +- 4.3 ms    | 73.5 ms +- 0.8 ms    | 74.7 ms +- 0.7 ms    | 74.4 ms +- 0.9 ms    |
| 71 | sqlalchemy_declarative        | 106 ms +- 11 ms      | 94.3 ms +- 1.9 ms    | 93.5 ms +- 1.4 ms    | 98.7 ms +- 3.7 ms    | 77.0 ms +- 2.6 ms    | 76.8 ms +- 1.5 ms    | 78.0 ms +- 2.4 ms    | 77.5 ms +- 0.9 ms    |
| 72 | sqlalchemy_imperative         | 15.9 ms +- 15.5 ms   | 11.8 ms +- 0.1 ms    | 11.7 ms +- 0.2 ms    | 12.8 ms +- 2.0 ms    | 8.99 ms +- 0.23 ms   | 8.99 ms +- 0.17 ms   | 9.11 ms +- 0.17 ms   | 9.15 ms +- 0.13 ms   |
| 73 | sqlglot_parse                 | 2.40 ms +- 1.58 ms   | 1.50 ms +- 0.08 ms   | 1.46 ms +- 0.01 ms   | 1.52 ms +- 0.09 ms   | 953 us +- 47 us      | 940 us +- 17 us      | 944 us +- 22 us      | 953 us +- 13 us      |
| 74 | sqlglot_transpile             | 2.16 ms +- 0.41 ms   | 1.72 ms +- 0.05 ms   | 1.70 ms +- 0.03 ms   | 1.79 ms +- 0.12 ms   | 1.11 ms +- 0.02 ms   | 1.12 ms +- 0.02 ms   | 1.13 ms +- 0.01 ms   | 1.14 ms +- 0.02 ms   |
| 75 | sqlglot_optimize              | 50.0 ms +- 4.5 ms    | 45.6 ms +- 0.5 ms    | 45.1 ms +- 0.7 ms    | 46.3 ms +- 1.1 ms    | 35.9 ms +- 0.6 ms    | 35.7 ms +- 0.5 ms    | 36.2 ms +- 0.8 ms    | 36.3 ms +- 0.6 ms    |
| 76 | sqlglot_normalize             | 242 ms +- 13 ms      | 237 ms +- 3 ms       | 236 ms +- 2 ms       | 245 ms +- 8 ms       | 199 ms +- 3 ms       | 199 ms +- 5 ms       | 199 ms +- 3 ms       | 200 ms +- 2 ms       |
| 77 | sqlite_synth                  | 3.72 us +- 0.61 us   | 3.09 us +- 0.06 us   | 3.08 us +- 0.05 us   | 3.44 us +- 0.79 us   | 2.71 us +- 0.07 us   | 2.71 us +- 0.11 us   | 2.77 us +- 0.13 us   | 2.72 us +- 0.06 us   |
| 78 | sympy_expand                  | 372 ms +- 71 ms      | 329 ms +- 8 ms       | 326 ms +- 5 ms       | 338 ms +- 10 ms      | 280 ms +- 6 ms       | 282 ms +- 12 ms      | 290 ms +- 10 ms      | 310 ms +- 105 ms     |
| 79 | sympy_integrate               | 20.9 ms +- 12.9 ms   | 15.8 ms +- 0.3 ms    | 15.7 ms +- 0.2 ms    | 16.7 ms +- 1.3 ms    | 13.2 ms +- 0.3 ms    | 13.3 ms +- 0.3 ms    | 13.6 ms +- 0.3 ms    | 13.9 ms +- 0.3 ms    |
| 80 | sympy_sum                     | 114 ms +- 4 ms       | 116 ms +- 4 ms       | 114 ms +- 2 ms       | 128 ms +- 9 ms       | 99.9 ms +- 2.2 ms    | 100 ms +- 2 ms       | 103 ms +- 5 ms       | 105 ms +- 3 ms       |
| 81 | sympy_str                     | 205 ms +- 13 ms      | 202 ms +- 8 ms       | 199 ms +- 4 ms       | 206 ms +- 6 ms       | 174 ms +- 4 ms       | 174 ms +- 3 ms       | 177 ms +- 4 ms       | 182 ms +- 3 ms       |
| 82 | telco                         | 8.86 ms +- 2.58 ms   | 7.55 ms +- 0.28 ms   | 7.54 ms +- 0.29 ms   | 7.34 ms +- 0.29 ms   | 6.95 ms +- 0.20 ms   | 7.08 ms +- 0.21 ms   | 7.03 ms +- 0.21 ms   | 7.37 ms +- 0.39 ms   |
| 83 | tomli_loads                   | 2.15 sec +- 0.30 sec | /                    | /                    | 2.03 sec +- 0.12 sec | /                    | /                    | /                    | /                    |
| 84 | tornado_http                  | 105 ms +- 22 ms      | 96.6 ms +- 5.2 ms    | 97.5 ms +- 6.4 ms    | 105 ms +- 7 ms       | 76.1 ms +- 2.1 ms    | 78.1 ms +- 4.9 ms    | 77.4 ms +- 4.0 ms    | 81.6 ms +- 2.8 ms    |
| 85 | typing_runtime_protocols      | 385 us +- 28 us      | /                    | /                    | 388 us +- 7 us       | /                    | /                    | /                    | /                    |
| 86 | unpack_sequence               | 42.8 ns +- 25.4 ns   | 37.3 ns +- 0.6 ns    | 37.3 ns +- 0.3 ns    | 38.0 ns +- 0.6 ns    | 31.7 ns +- 0.4 ns    | 32.5 ns +- 2.4 ns    | 32.5 ns +- 0.2 ns    | 33.2 ns +- 0.5 ns    |
| 87 | unpickle                      | 12.7 us +- 2.0 us    | 11.9 us +- 0.1 us    | 12.0 us +- 0.1 us    | 12.0 us +- 0.3 us    | 11.5 us +- 0.1 us    | 11.6 us +- 0.2 us    | 11.6 us +- 0.4 us    | 11.9 us +- 0.3 us    |
| 88 | unpickle_list                 | 5.10 us +- 0.09 us   | 5.15 us +- 0.05 us   | 5.21 us +- 0.12 us   | 5.23 us +- 0.15 us   | 5.10 us +- 0.05 us   | 5.35 us +- 0.84 us   | 5.11 us +- 0.08 us   | 5.25 us +- 0.11 us   |
| 89 | unpickle_pure_python          | 243 us +- 4 us       | 227 us +- 4 us       | 227 us +- 4 us       | 236 us +- 5 us       | 174 us +- 3 us       | 175 us +- 4 us       | 173 us +- 2 us       | 176 us +- 9 us       |
| 90 | xml_etree_parse               | 171 ms +- 2 ms       | 176 ms +- 5 ms       | 177 ms +- 3 ms       | 178 ms +- 6 ms       | 172 ms +- 3 ms       | 174 ms +- 4 ms       | 176 ms +- 6 ms       | 184 ms +- 28 ms      |
| 91 | xml_etree_iterparse           | 97.9 ms +- 1.9 ms    | 104 ms +- 2 ms       | 106 ms +- 3 ms       | 107 ms +- 4 ms       | 96.7 ms +- 1.8 ms    | 96.8 ms +- 2.2 ms    | 102 ms +- 2 ms       | 96.9 ms +- 1.7 ms    |
| 92 | xml_etree_generate            | 81.5 ms +- 1.7 ms    | 83.3 ms +- 1.3 ms    | 83.8 ms +- 3.0 ms    | 88.4 ms +- 11.9 ms   | 74.7 ms +- 1.2 ms    | 74.5 ms +- 1.6 ms    | 77.4 ms +- 1.5 ms    | 76.9 ms +- 1.3 ms    |
| 93 | xml_etree_process             | 66.8 ms +- 8.6 ms    | 64.3 ms +- 0.8 ms    | 65.2 ms +- 1.9 ms    | 66.3 ms +- 2.4 ms    | 48.9 ms +- 0.8 ms    | 49.6 ms +- 3.7 ms    | 49.9 ms +- 1.1 ms    | 51.6 ms +- 3.0 ms    |
| 94 | pprint_safe_repr              | /                    | 734 ms +- 26 ms      | 722 ms +- 9 ms       | 755 ms +- 77 ms      | 503 ms +- 7 ms       | 512 ms +- 8 ms       | 512 ms +- 40 ms      | 522 ms +- 8 ms       |

### 3.Change(UNIT: ms)
|     | Task                          | 3.9.17    | 3.10.10    | 3.10.11    | 3.10.9     | 3.11.0     | 3.11.1     | 3.11.2     | 3.11.3     |
|:----|:------------------------------|:----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| 0   | 2to3                          | 247.0     | 262.0      | 243.0      | 242.0      | 184.0      | 179.0      | 257.0      | 184.0      |
| 1   | async_generators              | 279.0     | 315.0      | 281.0      | 292.0      | 219.0      | 225.0      | 242.0      | 220.0      |
| 2   | async_tree_none               | 589.0     | 608.0      | 559.0      | 563.0      | 402.0      | 394.0      | 604.0      | 388.0      |
| 3   | async_tree_cpu_io_mixed       | 979.0     | 814.0      | 810.0      | 819.0      | 621.0      | 640.0      | 862.0      | 628.0      |
| 4   | async_tree_eager              | 577.0     | /          | /          | 561.0      | /          | /          | /          | /          |
| 5   | async_tree_eager_cpu_io_mixed | 867.0     | /          | /          | 813.0      | /          | /          | /          | /          |
| 6   | async_tree_eager_io           | 1590.0    | /          | /          | 1480.0     | /          | /          | /          | /          |
| 7   | async_tree_eager_memoization  | 935.0     | /          | /          | 721.0      | /          | /          | /          | /          |
| 8   | async_tree_io                 | 1580.0    | 1580.0     | 1430.0     | 1700.0     | 873.0      | 875.0      | 1350.0     | 898.0      |
| 9   | async_tree_memoization        | 669.0     | 662.0      | 655.0      | 641.0      | 456.0      | 451.0      | 661.0      | 467.0      |
| 10  | asyncio_tcp                   | 932.0     | /          | /          | 836.0      | /          | /          | /          | /          |
| 11  | asyncio_tcp_ssl               | 2760.0    | /          | /          | 2600.0     | /          | /          | /          | /          |
| 12  | chameleon                     | 7.57      | 6.66       | 6.89       | 6.49       | 4.77       | 4.85       | 5.27       | 4.74       |
| 13  | chaos                         | 83.4      | 78.2       | 79.2       | 85.6       | 51.1       | 51.1       | 58.4       | 52.5       |
| 14  | comprehensions                | 0.0201    | /          | /          | 0.0215     | /          | /          | /          | /          |
| 15  | bench_mp_pool                 | 8.85      | 8.49       | 8.63       | 9.37       | 5.98       | 6.0        | 10.6       | 7.35       |
| 16  | bench_thread_pool             | 1.11      | 1.1        | 1.16       | 1.29       | 1.07       | 1.08       | 1.39       | 1.09       |
| 17  | coroutines                    | 33.7      | 22.9       | 24.0       | 22.9       | 18.4       | 18.5       | 21.3       | 19.6       |
| 18  | coverage                      | 35.2      | 45.3       | 45.4       | 44.9       | 66.3       | 62.2       | 75.5       | 65.5       |
| 19  | crypto_pyaes                  | 90.8      | 90.7       | 92.1       | 90.9       | 55.1       | 56.2       | 64.6       | 58.1       |
| 20  | dask                          | 520.0     | /          | /          | 554.0      | /          | /          | /          | /          |
| 21  | deepcopy                      | 0.32      | 0.316      | 0.315      | 0.363      | 0.235      | 0.237      | 0.275      | 0.255      |
| 22  | deepcopy_reduce               | 0.0029    | 0.0027     | 0.0027     | 0.0028     | 0.0021     | 0.0021     | 0.0024     | 0.0022     |
| 23  | deepcopy_memo                 | 0.0389    | 0.0372     | 0.0377     | 0.0363     | 0.025      | 0.0252     | 0.0284     | 0.0257     |
| 24  | deltablue                     | 7.36      | 5.62       | 5.59       | 5.41       | 2.62       | 2.66       | 3.13       | 2.78       |
| 25  | django_template               | 36.3      | 32.5       | 32.8       | 33.8       | 23.1       | 22.9       | 26.9       | 24.3       |
| 26  | docutils                      | 2210.0    | 2210.0     | 2200.0     | 2260.0     | 1720.0     | 1730.0     | 3060.0     | 1860.0     |
| 27  | dulwich_log                   | 52.6      | 49.9       | 49.6       | 50.5       | 40.2       | 40.3       | 86.8       | 42.5       |
| 28  | fannkuch                      | 338.0     | 357.0      | 358.0      | 338.0      | 277.0      | 281.0      | 338.0      | 287.0      |
| 29  | float                         | 105.0     | 94.2       | 93.9       | 94.3       | 64.3       | 64.1       | 88.4       | 67.1       |
| 30  | create_gc_cycles              | 0.969     | /          | /          | 1.02       | /          | /          | /          | /          |
| 31  | gc_traversal                  | 2.94      | /          | /          | 2.98       | /          | /          | /          | /          |
| 32  | generators                    | 33.8      | 32.2       | 32.7       | 32.7       | 27.3       | 27.2       | 31.0       | 28.4       |
| 33  | genshi_text                   | 21.9      | 19.5       | 20.0       | 19.7       | 15.1       | 16.4       | 17.4       | 15.7       |
| 34  | genshi_xml                    | 43.0      | 40.3       | 40.0       | 41.0       | 33.4       | 36.8       | 41.6       | 35.8       |
| 35  | go                            | 192.0     | 175.0      | 176.0      | 175.0      | 98.9       | 99.4       | 125.0      | 102.0      |
| 36  | hexiom                        | 6.96      | 6.84       | 6.94       | 6.97       | 4.45       | 4.46       | 5.13       | 4.65       |
| 37  | html5lib                      | 57.8      | 51.9       | 49.8       | 58.7       | 35.0       | 35.5       | 51.3       | 36.4       |
| 38  | json_dumps                    | 12.1      | 12.0       | 12.0       | 11.9       | 11.1       | 11.3       | 13.9       | 11.6       |
| 39  | json_loads                    | 0.027     | 0.0274     | 0.0273     | 0.0268     | 0.0259     | 0.0259     | 0.0292     | 0.0266     |
| 40  | logging_format                | 0.0065    | 0.0067     | 0.0067     | 0.0066     | 0.0048     | 0.0047     | 0.0057     | 0.0048     |
| 41  | logging_silent                | 0.0002    | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     |
| 42  | logging_simple                | 0.0061    | 0.0062     | 0.0063     | 0.0061     | 0.0044     | 0.0044     | 0.0075     | 0.0045     |
| 43  | mako                          | 13.2      | 11.8       | 11.9       | 12.0       | 7.92       | 7.88       | 15.1       | 8.05       |
| 44  | mdp                           | 2890.0    | 2770.0     | 2760.0     | 2950.0     | 2490.0     | 2520.0     | 3130.0     | 2580.0     |
| 45  | meteor_contest                | 89.5      | 85.2       | 85.2       | 84.5       | 78.2       | 77.9       | 80.1       | 80.4       |
| 46  | nbody                         | 97.2      | 95.2       | 96.8       | 94.3       | 64.7       | 63.4       | 63.8       | 64.8       |
| 47  | nqueens                       | 72.6      | 73.5       | 73.4       | 73.9       | 62.0       | 63.1       | 64.6       | 64.4       |
| 48  | pathlib                       | 26.2      | 18.7       | 18.3       | 19.2       | 16.8       | 17.4       | 17.8       | 17.2       |
| 49  | pickle                        | 0.0117    | 0.0091     | 0.0092     | 0.0096     | 0.0084     | 0.0083     | 0.0084     | 0.0084     |
| 50  | pickle_dict                   | 0.0314    | 0.0251     | 0.0252     | 0.0249     | 0.0204     | 0.0194     | 0.0194     | 0.0198     |
| 51  | pickle_list                   | 0.0047    | 0.0039     | 0.0039     | 0.004      | 0.0031     | 0.003      | 0.003      | 0.0031     |
| 52  | pickle_pure_python            | 0.427     | 0.339      | 0.34       | 0.411      | 0.216      | 0.216      | 0.223      | 0.22       |
| 53  | pidigits                      | 250.0     | 220.0      | 220.0      | 224.0      | 213.0      | 212.0      | 215.0      | 218.0      |
| 54  | pprint_pformat                | 1210.0    | 1500.0     | 1480.0     | 1720.0     | 1030.0     | 1050.0     | 1040.0     | 1070.0     |
| 55  | pyflate                       | 528.0     | 494.0      | 488.0      | 497.0      | 316.0      | 303.0      | 309.0      | 310.0      |
| 56  | python_startup                | 16.6      | 13.5       | 14.0       | 14.4       | 13.6       | 13.5       | 13.6       | 13.4       |
| 57  | python_startup_no_site        | 9.55      | 7.58       | 7.77       | 7.75       | 8.52       | 8.49       | 8.41       | 8.44       |
| 58  | raytrace                      | 464.0     | 374.0      | 373.0      | 391.0      | 212.0      | 211.0      | 211.0      | 213.0      |
| 59  | regex_compile                 | 140.0     | 110.0      | 108.0      | 109.0      | 81.4       | 81.3       | 82.1       | 81.7       |
| 60  | regex_dna                     | 176.0     | 170.0      | 176.0      | 171.0      | 128.0      | 130.0      | 128.0      | 127.0      |
| 61  | regex_effbot                  | 2.54      | 2.53       | 2.47       | 2.43       | 1.96       | 1.96       | 1.98       | 1.97       |
| 62  | regex_v8                      | 21.6      | 21.3       | 21.3       | 21.5       | 15.2       | 15.5       | 15.3       | 16.0       |
| 63  | richards                      | 56.3      | 57.3       | 57.6       | 60.3       | 33.0       | 32.3       | 32.4       | 32.3       |
| 64  | richards_super                | 65.3      | /          | /          | 75.0       | /          | /          | /          | /          |
| 65  | scimark_fft                   | 423.0     | 452.0      | 447.0      | 460.0      | 387.0      | 392.0      | 396.0      | 395.0      |
| 66  | scimark_lu                    | 177.0     | 159.0      | 156.0      | 161.0      | 126.0      | 124.0      | 122.0      | 124.0      |
| 67  | scimark_monte_carlo           | 101.0     | 96.2       | 95.4       | 101.0      | 68.5       | 69.0       | 69.6       | 67.5       |
| 68  | scimark_sor                   | 180.0     | 162.0      | 160.0      | 162.0      | 104.0      | 106.0      | 104.0      | 104.0      |
| 69  | scimark_sparse_mat_mult       | 8.95      | 8.87       | 8.8        | 8.94       | 8.2        | 8.02       | 8.05       | 8.17       |
| 70  | spectral_norm                 | 108.0     | 105.0      | 106.0      | 106.0      | 75.0       | 73.5       | 74.7       | 74.4       |
| 71  | sqlalchemy_declarative        | 106.0     | 94.3       | 93.5       | 98.7       | 77.0       | 76.8       | 78.0       | 77.5       |
| 72  | sqlalchemy_imperative         | 15.9      | 11.8       | 11.7       | 12.8       | 8.99       | 8.99       | 9.11       | 9.15       |
| 73  | sqlglot_parse                 | 2.4       | 1.5        | 1.46       | 1.52       | 0.953      | 0.94       | 0.944      | 0.953      |
| 74  | sqlglot_transpile             | 2.16      | 1.72       | 1.7        | 1.79       | 1.11       | 1.12       | 1.13       | 1.14       |
| 75  | sqlglot_optimize              | 50.0      | 45.6       | 45.1       | 46.3       | 35.9       | 35.7       | 36.2       | 36.3       |
| 76  | sqlglot_normalize             | 242.0     | 237.0      | 236.0      | 245.0      | 199.0      | 199.0      | 199.0      | 200.0      |
| 77  | sqlite_synth                  | 0.0037    | 0.0031     | 0.0031     | 0.0034     | 0.0027     | 0.0027     | 0.0028     | 0.0027     |
| 78  | sympy_expand                  | 372.0     | 329.0      | 326.0      | 338.0      | 280.0      | 282.0      | 290.0      | 310.0      |
| 79  | sympy_integrate               | 20.9      | 15.8       | 15.7       | 16.7       | 13.2       | 13.3       | 13.6       | 13.9       |
| 80  | sympy_sum                     | 114.0     | 116.0      | 114.0      | 128.0      | 99.9       | 100.0      | 103.0      | 105.0      |
| 81  | sympy_str                     | 205.0     | 202.0      | 199.0      | 206.0      | 174.0      | 174.0      | 177.0      | 182.0      |
| 82  | telco                         | 8.86      | 7.55       | 7.54       | 7.34       | 6.95       | 7.08       | 7.03       | 7.37       |
| 83  | tomli_loads                   | 2150.0    | /          | /          | 2030.0     | /          | /          | /          | /          |
| 84  | tornado_http                  | 105.0     | 96.6       | 97.5       | 105.0      | 76.1       | 78.1       | 77.4       | 81.6       |
| 85  | typing_runtime_protocols      | 0.385     | /          | /          | 0.388      | /          | /          | /          | /          |
| 86  | unpack_sequence               | 0.0       | 0.0        | 0.0        | 0.0        | 0.0        | 0.0        | 0.0        | 0.0        |
| 87  | unpickle                      | 0.0127    | 0.0119     | 0.012      | 0.012      | 0.0115     | 0.0116     | 0.0116     | 0.0119     |
| 88  | unpickle_list                 | 0.0051    | 0.0052     | 0.0052     | 0.0052     | 0.0051     | 0.0053     | 0.0051     | 0.0053     |
| 89  | unpickle_pure_python          | 0.243     | 0.227      | 0.227      | 0.236      | 0.174      | 0.175      | 0.173      | 0.176      |
| 90  | xml_etree_parse               | 171.0     | 176.0      | 177.0      | 178.0      | 172.0      | 174.0      | 176.0      | 184.0      |
| 91  | xml_etree_iterparse           | 97.9      | 104.0      | 106.0      | 107.0      | 96.7       | 96.8       | 102.0      | 96.9       |
| 92  | xml_etree_generate            | 81.5      | 83.3       | 83.8       | 88.4       | 74.7       | 74.5       | 77.4       | 76.9       |
| 93  | xml_etree_process             | 66.8      | 64.3       | 65.2       | 66.3       | 48.9       | 49.6       | 49.9       | 51.6       |
| SUM |                               | 26844.865 | 16176.4806 | 15861.8714 | 26420.0573 | 12217.3315 | 12289.8707 | 15702.6686 | 12626.9191 |
| AVG |                               | 285.5837  | 199.7096   | 195.8256   | 281.0644   | 150.8313   | 151.7268   | 193.8601   | 155.8879   |
| UP% |                               | 100.0000% | 165.9500%  | 169.2415%  | 101.6079%  | 219.7277%  | 218.4308%  | 170.9573%  | 212.6003%  |

