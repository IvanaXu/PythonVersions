
### 0.Readme
#### (1) Python Versions
> https://www.python.org/downloads/
#### (2) Running Environment
* Docker gcc library/gcc
> ecs.u1-c1m2.large/aliyun Intel(R) Xeon(R) Platinum 2核(vCPU) 4 GiB Ubuntu 22.04 64位

#### (3) Test Software
* [Pyperformance](https://github.com/python/pyperformance)

### 1.Versions
| version   | date          | UP%       | Progress   |
|:----------|:--------------|:----------|:-----------|
| 3.8.0     | Oct. 14, 2019 | 101.1048% | >>         |
| 3.8.14    | Sept. 6, 2022 | 100.5216% | >          |
| 3.8.15    | Oct. 11, 2022 | 100.2706% | >          |
| 3.8.16    | Dec. 6, 2022  | 100.3557% | >          |
| 3.8.17    | June 6, 2023  | 100.9726% | >          |
| 3.8.18    | Aug 24, 2023  | 100.8543% | >          |
| 3.9.0     | Oct. 5, 2020  | 100.0000% | >          |

### 2.Details
|    | Task                     | 3.8.0                | 3.8.14               | 3.8.15               | 3.8.16               | 3.8.17               | 3.8.18               | 3.9.0                |
|---:|:-------------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
|  0 | 2to3                     | 460 ms +- 3 ms       | 466 ms +- 3 ms       | 465 ms +- 3 ms       | 464 ms +- 3 ms       | 464 ms +- 2 ms       | 464 ms +- 4 ms       | 469 ms +- 4 ms       |
|  1 | async_generators         | 512 ms +- 4 ms       | 514 ms +- 4 ms       | 513 ms +- 5 ms       | 513 ms +- 4 ms       | 514 ms +- 5 ms       | 513 ms +- 5 ms       | 531 ms +- 5 ms       |
|  2 | async_tree_none          | 961 ms +- 37 ms      | 959 ms +- 45 ms      | 968 ms +- 49 ms      | 957 ms +- 46 ms      | 960 ms +- 48 ms      | 963 ms +- 47 ms      | 999 ms +- 44 ms      |
|  3 | async_tree_cpu_io_mixed  | 1.30 sec +- 0.03 sec | 1.33 sec +- 0.05 sec | 1.34 sec +- 0.05 sec | 1.33 sec +- 0.05 sec | 1.33 sec +- 0.05 sec | 1.33 sec +- 0.05 sec | 1.37 sec +- 0.05 sec |
|  4 | async_tree_io            | 2.35 sec +- 0.02 sec | 2.36 sec +- 0.02 sec | 2.37 sec +- 0.02 sec | 2.36 sec +- 0.02 sec | 2.36 sec +- 0.02 sec | 2.37 sec +- 0.02 sec | 2.41 sec +- 0.03 sec |
|  5 | async_tree_memoization   | 1.11 sec +- 0.03 sec | 1.17 sec +- 0.04 sec | 1.17 sec +- 0.04 sec | 1.17 sec +- 0.03 sec | 1.17 sec +- 0.03 sec | 1.17 sec +- 0.03 sec | 1.19 sec +- 0.02 sec |
|  6 | asyncio_tcp              | 1.20 sec +- 0.01 sec | 1.21 sec +- 0.02 sec | 1.21 sec +- 0.01 sec | 1.21 sec +- 0.02 sec | 1.21 sec +- 0.02 sec | 1.21 sec +- 0.02 sec | 1.21 sec +- 0.01 sec |
|  7 | asyncio_tcp_ssl          | 4.10 sec +- 0.63 sec | 4.09 sec +- 0.64 sec | 4.16 sec +- 0.59 sec | 4.15 sec +- 0.61 sec | 3.98 sec +- 0.66 sec | 3.97 sec +- 0.63 sec | 4.03 sec +- 0.63 sec |
|  8 | asyncio_websockets       | 633 ms +- 2 ms       | 635 ms +- 2 ms       | 634 ms +- 2 ms       | 634 ms +- 2 ms       | 634 ms +- 2 ms       | 634 ms +- 2 ms       | 634 ms +- 2 ms       |
|  9 | chameleon                | 13.9 ms +- 0.2 ms    | 13.7 ms +- 0.2 ms    | 14.0 ms +- 0.3 ms    | 13.7 ms +- 0.2 ms    | 13.5 ms +- 0.2 ms    | 13.5 ms +- 0.2 ms    | 13.8 ms +- 0.3 ms    |
| 10 | chaos                    | 167 ms +- 1 ms       | 168 ms +- 2 ms       | 168 ms +- 2 ms       | 167 ms +- 1 ms       | 168 ms +- 1 ms       | 167 ms +- 1 ms       | 164 ms +- 2 ms       |
| 11 | comprehensions           | 38.2 us +- 0.3 us    | 38.2 us +- 0.2 us    | 38.2 us +- 0.3 us    | 38.3 us +- 0.2 us    | 38.4 us +- 0.3 us    | 38.3 us +- 0.2 us    | 38.6 us +- 0.4 us    |
| 12 | bench_mp_pool            | 19.3 ms +- 1.5 ms    | 19.4 ms +- 1.6 ms    | 18.8 ms +- 1.5 ms    | 18.9 ms +- 1.7 ms    | 19.0 ms +- 1.5 ms    | 19.0 ms +- 1.6 ms    | 18.9 ms +- 1.3 ms    |
| 13 | bench_thread_pool        | 1.62 ms +- 0.02 ms   | 1.62 ms +- 0.03 ms   | 1.63 ms +- 0.02 ms   | 1.63 ms +- 0.02 ms   | 1.62 ms +- 0.02 ms   | 1.62 ms +- 0.02 ms   | 1.65 ms +- 0.02 ms   |
| 14 | coroutines               | 54.8 ms +- 0.4 ms    | 54.7 ms +- 0.6 ms    | 54.5 ms +- 0.4 ms    | 54.7 ms +- 0.4 ms    | 54.6 ms +- 0.4 ms    | 54.8 ms +- 0.5 ms    | 57.0 ms +- 0.5 ms    |
| 15 | coverage                 | 48.3 ms +- 0.5 ms    | 48.5 ms +- 0.4 ms    | 48.4 ms +- 0.5 ms    | 48.5 ms +- 0.3 ms    | 48.6 ms +- 0.4 ms    | 48.5 ms +- 0.3 ms    | 51.9 ms +- 0.8 ms    |
| 16 | crypto_pyaes             | 163 ms +- 2 ms       | 159 ms +- 2 ms       | 159 ms +- 2 ms       | 159 ms +- 2 ms       | 159 ms +- 1 ms       | 159 ms +- 2 ms       | 160 ms +- 1 ms       |
| 17 | dask                     | 885 ms +- 12 ms      | 893 ms +- 13 ms      | 894 ms +- 14 ms      | 896 ms +- 13 ms      | 891 ms +- 13 ms      | 893 ms +- 13 ms      | 895 ms +- 11 ms      |
| 18 | deepcopy                 | 637 us +- 6 us       | 644 us +- 6 us       | 647 us +- 5 us       | 645 us +- 5 us       | 642 us +- 5 us       | 643 us +- 5 us       | 648 us +- 5 us       |
| 19 | deepcopy_reduce          | 5.61 us +- 0.07 us   | 5.68 us +- 0.04 us   | 5.74 us +- 0.04 us   | 5.70 us +- 0.07 us   | 5.67 us +- 0.05 us   | 5.69 us +- 0.06 us   | 5.65 us +- 0.06 us   |
| 20 | deepcopy_memo            | 71.8 us +- 0.5 us    | 72.9 us +- 0.5 us    | 72.7 us +- 0.6 us    | 73.4 us +- 0.6 us    | 73.4 us +- 0.7 us    | 73.4 us +- 0.6 us    | 72.8 us +- 0.7 us    |
| 21 | deltablue                | 11.0 ms +- 0.2 ms    | 11.1 ms +- 0.2 ms    | 11.1 ms +- 0.2 ms    | 11.2 ms +- 0.2 ms    | 11.1 ms +- 0.2 ms    | 11.2 ms +- 0.3 ms    | 11.2 ms +- 0.2 ms    |
| 22 | django_template          | 75.2 ms +- 1.1 ms    | 75.7 ms +- 0.7 ms    | 75.8 ms +- 0.8 ms    | 75.8 ms +- 0.8 ms    | 75.1 ms +- 0.9 ms    | 75.4 ms +- 0.9 ms    | 76.7 ms +- 1.3 ms    |
| 23 | docutils                 | 3.98 sec +- 0.06 sec | 4.02 sec +- 0.05 sec | 4.02 sec +- 0.04 sec | 4.03 sec +- 0.05 sec | 4.01 sec +- 0.04 sec | 4.02 sec +- 0.05 sec | 4.06 sec +- 0.02 sec |
| 24 | dulwich_log              | 113 ms +- 1 ms       | 113 ms +- 1 ms       | 114 ms +- 1 ms       | 113 ms +- 1 ms       | 113 ms +- 2 ms       | 113 ms +- 1 ms       | 114 ms +- 1 ms       |
| 25 | fannkuch                 | 611 ms +- 4 ms       | 611 ms +- 5 ms       | 612 ms +- 4 ms       | 612 ms +- 4 ms       | 611 ms +- 4 ms       | 611 ms +- 5 ms       | 622 ms +- 3 ms       |
| 26 | float                    | 164 ms +- 2 ms       | 166 ms +- 3 ms       | 166 ms +- 2 ms       | 167 ms +- 3 ms       | 165 ms +- 1 ms       | 167 ms +- 3 ms       | 171 ms +- 3 ms       |
| 27 | create_gc_cycles         | 1.74 ms +- 0.01 ms   | 1.73 ms +- 0.01 ms   | 1.72 ms +- 0.01 ms   | 1.72 ms +- 0.01 ms   | 1.72 ms +- 0.01 ms   | 1.72 ms +- 0.01 ms   | 1.80 ms +- 0.01 ms   |
| 28 | gc_traversal             | 3.97 ms +- 0.01 ms   | 4.22 ms +- 0.02 ms   | 4.18 ms +- 0.02 ms   | 4.22 ms +- 0.02 ms   | 4.21 ms +- 0.02 ms   | 4.21 ms +- 0.03 ms   | 3.95 ms +- 0.04 ms   |
| 29 | generators               | 82.9 ms +- 0.6 ms    | 85.1 ms +- 0.6 ms    | 85.3 ms +- 0.7 ms    | 85.0 ms +- 0.6 ms    | 84.9 ms +- 0.5 ms    | 85.3 ms +- 0.6 ms    | 84.1 ms +- 0.6 ms    |
| 30 | genshi_text              | 42.7 ms +- 0.5 ms    | 43.8 ms +- 0.5 ms    | 43.6 ms +- 0.5 ms    | 43.7 ms +- 0.5 ms    | 43.3 ms +- 0.5 ms    | 43.4 ms +- 0.5 ms    | 44.2 ms +- 0.4 ms    |
| 31 | genshi_xml               | 86.3 ms +- 1.0 ms    | 89.5 ms +- 1.3 ms    | 89.2 ms +- 1.3 ms    | 88.9 ms +- 1.6 ms    | 88.6 ms +- 1.0 ms    | 88.7 ms +- 1.4 ms    | 89.0 ms +- 1.6 ms    |
| 32 | go                       | 380 ms +- 5 ms       | 375 ms +- 3 ms       | 372 ms +- 3 ms       | 373 ms +- 3 ms       | 372 ms +- 4 ms       | 372 ms +- 4 ms       | 369 ms +- 3 ms       |
| 33 | hexiom                   | 14.4 ms +- 0.2 ms    | 14.6 ms +- 0.2 ms    | 14.5 ms +- 0.1 ms    | 14.6 ms +- 0.1 ms    | 14.5 ms +- 0.1 ms    | 14.5 ms +- 0.1 ms    | 14.3 ms +- 0.1 ms    |
| 34 | html5lib                 | 124 ms +- 6 ms       | 122 ms +- 5 ms       | 122 ms +- 5 ms       | 122 ms +- 5 ms       | 122 ms +- 6 ms       | 122 ms +- 6 ms       | 122 ms +- 7 ms       |
| 35 | json_dumps               | 17.5 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    | 17.6 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    |
| 36 | json_loads               | 36.7 us +- 0.9 us    | 37.0 us +- 0.7 us    | 36.8 us +- 0.6 us    | 36.9 us +- 0.7 us    | 36.7 us +- 0.4 us    | 37.0 us +- 0.9 us    | 33.2 us +- 0.5 us    |
| 37 | logging_format           | 14.4 us +- 0.3 us    | 14.3 us +- 0.2 us    | 14.4 us +- 0.2 us    | 14.3 us +- 0.2 us    | 14.3 us +- 0.2 us    | 14.3 us +- 0.2 us    | 14.5 us +- 0.2 us    |
| 38 | logging_silent           | 285 ns +- 4 ns       | 283 ns +- 5 ns       | 285 ns +- 8 ns       | 282 ns +- 4 ns       | 284 ns +- 6 ns       | 282 ns +- 5 ns       | 289 ns +- 5 ns       |
| 39 | logging_simple           | 13.2 us +- 0.2 us    | 13.0 us +- 0.2 us    | 13.1 us +- 0.2 us    | 13.0 us +- 0.1 us    | 13.1 us +- 0.2 us    | 13.0 us +- 0.2 us    | 13.2 us +- 0.2 us    |
| 40 | mako                     | 23.4 ms +- 0.2 ms    | 23.7 ms +- 0.3 ms    | 23.7 ms +- 0.2 ms    | 23.6 ms +- 0.2 ms    | 23.7 ms +- 0.3 ms    | 23.6 ms +- 0.3 ms    | 23.4 ms +- 0.2 ms    |
| 41 | mdp                      | 4.27 sec +- 0.03 sec | 4.17 sec +- 0.02 sec | 4.18 sec +- 0.02 sec | 4.18 sec +- 0.02 sec | 4.17 sec +- 0.02 sec | 4.18 sec +- 0.02 sec | 4.09 sec +- 0.03 sec |
| 42 | meteor_contest           | 184 ms +- 6 ms       | 150 ms +- 3 ms       | 148 ms +- 2 ms       | 150 ms +- 2 ms       | 142 ms +- 1 ms       | 142 ms +- 1 ms       | 139 ms +- 1 ms       |
| 43 | nbody                    | 176 ms +- 1 ms       | 178 ms +- 1 ms       | 176 ms +- 1 ms       | 179 ms +- 2 ms       | 179 ms +- 1 ms       | 179 ms +- 2 ms       | 187 ms +- 1 ms       |
| 44 | nqueens                  | 136 ms +- 1 ms       | 138 ms +- 1 ms       | 137 ms +- 1 ms       | 138 ms +- 1 ms       | 138 ms +- 1 ms       | 138 ms +- 1 ms       | 136 ms +- 1 ms       |
| 45 | pathlib                  | 34.4 ms +- 0.5 ms    | 32.9 ms +- 0.5 ms    | 32.9 ms +- 0.5 ms    | 32.8 ms +- 0.4 ms    | 32.8 ms +- 0.4 ms    | 32.9 ms +- 0.4 ms    | 32.8 ms +- 0.4 ms    |
| 46 | pickle                   | 13.0 us +- 0.2 us    | 12.7 us +- 0.2 us    | 12.7 us +- 0.2 us    | 12.7 us +- 0.2 us    | 12.7 us +- 0.5 us    | 12.7 us +- 0.1 us    | 14.2 us +- 0.2 us    |
| 47 | pickle_dict              | 32.7 us +- 0.3 us    | 31.4 us +- 0.2 us    | 31.3 us +- 0.2 us    | 31.4 us +- 0.3 us    | 32.0 us +- 1.8 us    | 31.4 us +- 0.4 us    | 32.8 us +- 0.3 us    |
| 48 | pickle_list              | 5.05 us +- 0.06 us   | 5.05 us +- 0.07 us   | 5.02 us +- 0.07 us   | 5.01 us +- 0.07 us   | 5.00 us +- 0.08 us   | 5.13 us +- 0.58 us   | 5.25 us +- 0.09 us   |
| 49 | pickle_pure_python       | 679 us +- 8 us       | 690 us +- 14 us      | 687 us +- 8 us       | 686 us +- 8 us       | 685 us +- 6 us       | 687 us +- 10 us      | 688 us +- 10 us      |
| 50 | pidigits                 | 236 ms +- 4 ms       | 236 ms +- 1 ms       | 236 ms +- 1 ms       | 236 ms +- 1 ms       | 236 ms +- 1 ms       | 236 ms +- 1 ms       | 242 ms +- 1 ms       |
| 51 | pprint_pformat           | 2.06 sec +- 0.01 sec | 2.11 sec +- 0.02 sec | 2.10 sec +- 0.01 sec | 2.10 sec +- 0.02 sec | 2.09 sec +- 0.02 sec | 2.09 sec +- 0.02 sec | 2.16 sec +- 0.02 sec |
| 52 | pyflate                  | 967 ms +- 7 ms       | 973 ms +- 10 ms      | 979 ms +- 11 ms      | 977 ms +- 12 ms      | 972 ms +- 10 ms      | 974 ms +- 9 ms       | 968 ms +- 9 ms       |
| 53 | python_startup           | 12.6 ms +- 0.2 ms    | 12.8 ms +- 0.3 ms    | 12.8 ms +- 0.3 ms    | 12.8 ms +- 0.3 ms    | 12.7 ms +- 0.2 ms    | 12.8 ms +- 0.2 ms    | 12.4 ms +- 0.2 ms    |
| 54 | python_startup_no_site   | 8.19 ms +- 0.14 ms   | 8.42 ms +- 0.15 ms   | 8.41 ms +- 0.16 ms   | 8.41 ms +- 0.13 ms   | 8.32 ms +- 0.13 ms   | 8.37 ms +- 0.14 ms   | 8.00 ms +- 0.16 ms   |
| 55 | raytrace                 | 775 ms +- 5 ms       | 784 ms +- 7 ms       | 784 ms +- 8 ms       | 781 ms +- 9 ms       | 780 ms +- 7 ms       | 782 ms +- 10 ms      | 782 ms +- 6 ms       |
| 56 | regex_compile            | 236 ms +- 2 ms       | 240 ms +- 2 ms       | 239 ms +- 1 ms       | 239 ms +- 2 ms       | 238 ms +- 2 ms       | 239 ms +- 2 ms       | 242 ms +- 2 ms       |
| 57 | regex_dna                | 222 ms +- 2 ms       | 222 ms +- 2 ms       | 217 ms +- 2 ms       | 222 ms +- 2 ms       | 222 ms +- 1 ms       | 222 ms +- 1 ms       | 224 ms +- 2 ms       |
| 58 | regex_effbot             | 3.71 ms +- 0.10 ms   | 3.59 ms +- 0.02 ms   | 3.58 ms +- 0.08 ms   | 3.59 ms +- 0.03 ms   | 3.57 ms +- 0.06 ms   | 3.58 ms +- 0.05 ms   | 3.52 ms +- 0.08 ms   |
| 59 | regex_v8                 | 29.6 ms +- 0.6 ms    | 29.7 ms +- 0.4 ms    | 29.8 ms +- 0.4 ms    | 29.6 ms +- 0.3 ms    | 29.3 ms +- 0.3 ms    | 29.4 ms +- 0.3 ms    | 29.5 ms +- 0.3 ms    |
| 60 | richards                 | 110 ms +- 2 ms       | 110 ms +- 2 ms       | 110 ms +- 2 ms       | 110 ms +- 1 ms       | 109 ms +- 2 ms       | 110 ms +- 2 ms       | 111 ms +- 2 ms       |
| 61 | richards_super           | 132 ms +- 2 ms       | 131 ms +- 3 ms       | 130 ms +- 3 ms       | 130 ms +- 1 ms       | 131 ms +- 3 ms       | 131 ms +- 2 ms       | 133 ms +- 2 ms       |
| 62 | scimark_fft              | 480 ms +- 4 ms       | 488 ms +- 3 ms       | 491 ms +- 4 ms       | 488 ms +- 3 ms       | 487 ms +- 4 ms       | 488 ms +- 3 ms       | 511 ms +- 3 ms       |
| 63 | scimark_lu               | 218 ms +- 1 ms       | 221 ms +- 3 ms       | 221 ms +- 3 ms       | 220 ms +- 2 ms       | 221 ms +- 2 ms       | 221 ms +- 2 ms       | 221 ms +- 3 ms       |
| 64 | scimark_monte_carlo      | 147 ms +- 2 ms       | 151 ms +- 3 ms       | 148 ms +- 3 ms       | 150 ms +- 4 ms       | 150 ms +- 3 ms       | 151 ms +- 3 ms       | 152 ms +- 3 ms       |
| 65 | scimark_sor              | 278 ms +- 4 ms       | 289 ms +- 2 ms       | 288 ms +- 3 ms       | 286 ms +- 5 ms       | 286 ms +- 4 ms       | 285 ms +- 5 ms       | 285 ms +- 5 ms       |
| 66 | scimark_sparse_mat_mult  | 5.80 ms +- 0.06 ms   | 5.92 ms +- 0.17 ms   | 5.90 ms +- 0.06 ms   | 5.87 ms +- 0.07 ms   | 5.87 ms +- 0.06 ms   | 5.92 ms +- 0.13 ms   | 6.59 ms +- 0.10 ms   |
| 67 | spectral_norm            | 183 ms +- 1 ms       | 189 ms +- 1 ms       | 190 ms +- 1 ms       | 189 ms +- 1 ms       | 189 ms +- 1 ms       | 189 ms +- 1 ms       | 194 ms +- 1 ms       |
| 68 | sqlalchemy_declarative   | 225 ms +- 5 ms       | 224 ms +- 5 ms       | 224 ms +- 5 ms       | 224 ms +- 5 ms       | 225 ms +- 5 ms       | 224 ms +- 5 ms       | 223 ms +- 5 ms       |
| 69 | sqlalchemy_imperative    | 31.9 ms +- 1.3 ms    | 32.4 ms +- 1.3 ms    | 32.5 ms +- 1.3 ms    | 32.5 ms +- 1.2 ms    | 32.5 ms +- 1.2 ms    | 32.6 ms +- 1.2 ms    | 31.6 ms +- 1.2 ms    |
| 70 | sqlglot_parse            | 3.23 ms +- 0.04 ms   | 3.22 ms +- 0.03 ms   | 3.20 ms +- 0.02 ms   | 3.21 ms +- 0.03 ms   | 3.21 ms +- 0.03 ms   | 3.21 ms +- 0.04 ms   | 3.26 ms +- 0.04 ms   |
| 71 | sqlglot_transpile        | 3.71 ms +- 0.03 ms   | 3.69 ms +- 0.03 ms   | 3.67 ms +- 0.03 ms   | 3.69 ms +- 0.03 ms   | 3.69 ms +- 0.03 ms   | 3.70 ms +- 0.04 ms   | 3.76 ms +- 0.03 ms   |
| 72 | sqlglot_optimize         | 91.1 ms +- 0.7 ms    | 92.4 ms +- 0.5 ms    | 92.4 ms +- 0.6 ms    | 92.4 ms +- 0.6 ms    | 92.3 ms +- 0.7 ms    | 92.5 ms +- 0.7 ms    | 93.4 ms +- 0.7 ms    |
| 73 | sqlglot_normalize        | 193 ms +- 3 ms       | 193 ms +- 1 ms       | 193 ms +- 2 ms       | 193 ms +- 1 ms       | 193 ms +- 1 ms       | 193 ms +- 1 ms       | 198 ms +- 2 ms       |
| 74 | sqlite_synth             | 4.31 us +- 0.13 us   | 4.42 us +- 0.13 us   | 4.42 us +- 0.11 us   | 4.45 us +- 0.12 us   | 4.48 us +- 0.13 us   | 4.46 us +- 0.13 us   | 4.36 us +- 0.08 us   |
| 75 | sympy_expand             | 725 ms +- 6 ms       | 731 ms +- 5 ms       | 734 ms +- 5 ms       | 733 ms +- 5 ms       | 736 ms +- 21 ms      | 735 ms +- 19 ms      | 756 ms +- 5 ms       |
| 76 | sympy_integrate          | 31.8 ms +- 0.2 ms    | 32.3 ms +- 0.3 ms    | 32.4 ms +- 0.3 ms    | 32.4 ms +- 0.3 ms    | 32.4 ms +- 0.3 ms    | 32.2 ms +- 0.2 ms    | 32.5 ms +- 0.2 ms    |
| 77 | sympy_sum                | 252 ms +- 3 ms       | 254 ms +- 3 ms       | 255 ms +- 3 ms       | 253 ms +- 2 ms       | 255 ms +- 3 ms       | 256 ms +- 3 ms       | 254 ms +- 3 ms       |
| 78 | sympy_str                | 443 ms +- 3 ms       | 450 ms +- 4 ms       | 451 ms +- 4 ms       | 450 ms +- 4 ms       | 451 ms +- 4 ms       | 450 ms +- 4 ms       | 455 ms +- 3 ms       |
| 79 | telco                    | 9.00 ms +- 0.15 ms   | 9.03 ms +- 0.26 ms   | 9.01 ms +- 0.35 ms   | 8.95 ms +- 0.38 ms   | 9.00 ms +- 0.25 ms   | 9.03 ms +- 0.16 ms   | 9.07 ms +- 0.35 ms   |
| 80 | tomli_loads              | 3.68 sec +- 0.04 sec | 3.74 sec +- 0.04 sec | 3.74 sec +- 0.06 sec | 3.74 sec +- 0.03 sec | 3.74 sec +- 0.03 sec | 3.75 sec +- 0.03 sec | 3.77 sec +- 0.04 sec |
| 81 | tornado_http             | 203 ms +- 6 ms       | 206 ms +- 7 ms       | 207 ms +- 6 ms       | 207 ms +- 6 ms       | 206 ms +- 5 ms       | 206 ms +- 6 ms       | 207 ms +- 7 ms       |
| 82 | typing_runtime_protocols | 755 us +- 6 us       | 757 us +- 7 us       | 760 us +- 6 us       | 756 us +- 6 us       | 760 us +- 9 us       | 758 us +- 7 us       | 742 us +- 7 us       |
| 83 | unpack_sequence          | 64.6 ns +- 0.8 ns    | 64.4 ns +- 0.8 ns    | 65.8 ns +- 6.5 ns    | 64.5 ns +- 1.2 ns    | 64.9 ns +- 1.3 ns    | 64.7 ns +- 1.1 ns    | 67.1 ns +- 1.1 ns    |
| 84 | unpickle                 | 20.1 us +- 0.2 us    | 20.3 us +- 0.2 us    | 20.3 us +- 0.2 us    | 20.3 us +- 0.2 us    | 20.3 us +- 0.2 us    | 20.3 us +- 0.3 us    | 18.7 us +- 0.3 us    |
| 85 | unpickle_list            | 6.30 us +- 0.07 us   | 6.49 us +- 0.07 us   | 6.50 us +- 0.06 us   | 6.51 us +- 0.10 us   | 6.44 us +- 0.08 us   | 6.47 us +- 0.16 us   | 6.32 us +- 0.08 us   |
| 86 | unpickle_pure_python     | 473 us +- 9 us       | 461 us +- 5 us       | 458 us +- 5 us       | 460 us +- 7 us       | 459 us +- 5 us       | 460 us +- 6 us       | 468 us +- 5 us       |
| 87 | xml_etree_parse          | 199 ms +- 3 ms       | 206 ms +- 3 ms       | 204 ms +- 2 ms       | 205 ms +- 2 ms       | 203 ms +- 2 ms       | 204 ms +- 3 ms       | 192 ms +- 2 ms       |
| 88 | xml_etree_iterparse      | 135 ms +- 2 ms       | 138 ms +- 2 ms       | 138 ms +- 2 ms       | 138 ms +- 2 ms       | 138 ms +- 2 ms       | 139 ms +- 3 ms       | 135 ms +- 2 ms       |
| 89 | xml_etree_generate       | 136 ms +- 3 ms       | 136 ms +- 3 ms       | 136 ms +- 3 ms       | 137 ms +- 2 ms       | 137 ms +- 2 ms       | 136 ms +- 2 ms       | 128 ms +- 2 ms       |
| 90 | xml_etree_process        | 108 ms +- 1 ms       | 109 ms +- 1 ms       | 109 ms +- 2 ms       | 109 ms +- 1 ms       | 108 ms +- 1 ms       | 109 ms +- 1 ms       | 103 ms +- 1 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      | 3.8.14     | 3.8.15     | 3.8.16     | 3.8.17     | 3.8.18     | 3.9.0      |
|:----|:-------------------------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|:-----------|
| 0   | 2to3                     | 460.0      | 466.0      | 465.0      | 464.0      | 464.0      | 464.0      | 469.0      |
| 1   | async_generators         | 512.0      | 514.0      | 513.0      | 513.0      | 514.0      | 513.0      | 531.0      |
| 2   | async_tree_none          | 961.0      | 959.0      | 968.0      | 957.0      | 960.0      | 963.0      | 999.0      |
| 3   | async_tree_cpu_io_mixed  | 1300.0     | 1330.0     | 1340.0     | 1330.0     | 1330.0     | 1330.0     | 1370.0     |
| 4   | async_tree_io            | 2350.0     | 2360.0     | 2370.0     | 2360.0     | 2360.0     | 2370.0     | 2410.0     |
| 5   | async_tree_memoization   | 1110.0     | 1170.0     | 1170.0     | 1170.0     | 1170.0     | 1170.0     | 1190.0     |
| 6   | asyncio_tcp              | 1200.0     | 1210.0     | 1210.0     | 1210.0     | 1210.0     | 1210.0     | 1210.0     |
| 7   | asyncio_tcp_ssl          | 4100.0     | 4090.0     | 4160.0     | 4150.0     | 3980.0     | 3970.0     | 4030.0     |
| 8   | asyncio_websockets       | 633.0      | 635.0      | 634.0      | 634.0      | 634.0      | 634.0      | 634.0      |
| 9   | chameleon                | 13.9       | 13.7       | 14.0       | 13.7       | 13.5       | 13.5       | 13.8       |
| 10  | chaos                    | 167.0      | 168.0      | 168.0      | 167.0      | 168.0      | 167.0      | 164.0      |
| 11  | comprehensions           | 0.0382     | 0.0382     | 0.0382     | 0.0383     | 0.0384     | 0.0383     | 0.0386     |
| 12  | bench_mp_pool            | 19.3       | 19.4       | 18.8       | 18.9       | 19.0       | 19.0       | 18.9       |
| 13  | bench_thread_pool        | 1.62       | 1.62       | 1.63       | 1.63       | 1.62       | 1.62       | 1.65       |
| 14  | coroutines               | 54.8       | 54.7       | 54.5       | 54.7       | 54.6       | 54.8       | 57.0       |
| 15  | coverage                 | 48.3       | 48.5       | 48.4       | 48.5       | 48.6       | 48.5       | 51.9       |
| 16  | crypto_pyaes             | 163.0      | 159.0      | 159.0      | 159.0      | 159.0      | 159.0      | 160.0      |
| 17  | dask                     | 885.0      | 893.0      | 894.0      | 896.0      | 891.0      | 893.0      | 895.0      |
| 18  | deepcopy                 | 0.637      | 0.644      | 0.647      | 0.645      | 0.642      | 0.643      | 0.648      |
| 19  | deepcopy_reduce          | 0.0056     | 0.0057     | 0.0057     | 0.0057     | 0.0057     | 0.0057     | 0.0057     |
| 20  | deepcopy_memo            | 0.0718     | 0.0729     | 0.0727     | 0.0734     | 0.0734     | 0.0734     | 0.0728     |
| 21  | deltablue                | 11.0       | 11.1       | 11.1       | 11.2       | 11.1       | 11.2       | 11.2       |
| 22  | django_template          | 75.2       | 75.7       | 75.8       | 75.8       | 75.1       | 75.4       | 76.7       |
| 23  | docutils                 | 3980.0     | 4020.0     | 4020.0     | 4030.0     | 4010.0     | 4020.0     | 4060.0     |
| 24  | dulwich_log              | 113.0      | 113.0      | 114.0      | 113.0      | 113.0      | 113.0      | 114.0      |
| 25  | fannkuch                 | 611.0      | 611.0      | 612.0      | 612.0      | 611.0      | 611.0      | 622.0      |
| 26  | float                    | 164.0      | 166.0      | 166.0      | 167.0      | 165.0      | 167.0      | 171.0      |
| 27  | create_gc_cycles         | 1.74       | 1.73       | 1.72       | 1.72       | 1.72       | 1.72       | 1.8        |
| 28  | gc_traversal             | 3.97       | 4.22       | 4.18       | 4.22       | 4.21       | 4.21       | 3.95       |
| 29  | generators               | 82.9       | 85.1       | 85.3       | 85.0       | 84.9       | 85.3       | 84.1       |
| 30  | genshi_text              | 42.7       | 43.8       | 43.6       | 43.7       | 43.3       | 43.4       | 44.2       |
| 31  | genshi_xml               | 86.3       | 89.5       | 89.2       | 88.9       | 88.6       | 88.7       | 89.0       |
| 32  | go                       | 380.0      | 375.0      | 372.0      | 373.0      | 372.0      | 372.0      | 369.0      |
| 33  | hexiom                   | 14.4       | 14.6       | 14.5       | 14.6       | 14.5       | 14.5       | 14.3       |
| 34  | html5lib                 | 124.0      | 122.0      | 122.0      | 122.0      | 122.0      | 122.0      | 122.0      |
| 35  | json_dumps               | 17.5       | 17.5       | 17.6       | 17.5       | 17.5       | 17.5       | 17.5       |
| 36  | json_loads               | 0.0367     | 0.037      | 0.0368     | 0.0369     | 0.0367     | 0.037      | 0.0332     |
| 37  | logging_format           | 0.0144     | 0.0143     | 0.0144     | 0.0143     | 0.0143     | 0.0143     | 0.0145     |
| 38  | logging_silent           | 0.0003     | 0.0003     | 0.0003     | 0.0003     | 0.0003     | 0.0003     | 0.0003     |
| 39  | logging_simple           | 0.0132     | 0.013      | 0.0131     | 0.013      | 0.0131     | 0.013      | 0.0132     |
| 40  | mako                     | 23.4       | 23.7       | 23.7       | 23.6       | 23.7       | 23.6       | 23.4       |
| 41  | mdp                      | 4270.0     | 4170.0     | 4180.0     | 4180.0     | 4170.0     | 4180.0     | 4090.0     |
| 42  | meteor_contest           | 184.0      | 150.0      | 148.0      | 150.0      | 142.0      | 142.0      | 139.0      |
| 43  | nbody                    | 176.0      | 178.0      | 176.0      | 179.0      | 179.0      | 179.0      | 187.0      |
| 44  | nqueens                  | 136.0      | 138.0      | 137.0      | 138.0      | 138.0      | 138.0      | 136.0      |
| 45  | pathlib                  | 34.4       | 32.9       | 32.9       | 32.8       | 32.8       | 32.9       | 32.8       |
| 46  | pickle                   | 0.013      | 0.0127     | 0.0127     | 0.0127     | 0.0127     | 0.0127     | 0.0142     |
| 47  | pickle_dict              | 0.0327     | 0.0314     | 0.0313     | 0.0314     | 0.032      | 0.0314     | 0.0328     |
| 48  | pickle_list              | 0.005      | 0.005      | 0.005      | 0.005      | 0.005      | 0.0051     | 0.0053     |
| 49  | pickle_pure_python       | 0.679      | 0.69       | 0.687      | 0.686      | 0.685      | 0.687      | 0.688      |
| 50  | pidigits                 | 236.0      | 236.0      | 236.0      | 236.0      | 236.0      | 236.0      | 242.0      |
| 51  | pprint_pformat           | 2060.0     | 2110.0     | 2100.0     | 2100.0     | 2090.0     | 2090.0     | 2160.0     |
| 52  | pyflate                  | 967.0      | 973.0      | 979.0      | 977.0      | 972.0      | 974.0      | 968.0      |
| 53  | python_startup           | 12.6       | 12.8       | 12.8       | 12.8       | 12.7       | 12.8       | 12.4       |
| 54  | python_startup_no_site   | 8.19       | 8.42       | 8.41       | 8.41       | 8.32       | 8.37       | 8.0        |
| 55  | raytrace                 | 775.0      | 784.0      | 784.0      | 781.0      | 780.0      | 782.0      | 782.0      |
| 56  | regex_compile            | 236.0      | 240.0      | 239.0      | 239.0      | 238.0      | 239.0      | 242.0      |
| 57  | regex_dna                | 222.0      | 222.0      | 217.0      | 222.0      | 222.0      | 222.0      | 224.0      |
| 58  | regex_effbot             | 3.71       | 3.59       | 3.58       | 3.59       | 3.57       | 3.58       | 3.52       |
| 59  | regex_v8                 | 29.6       | 29.7       | 29.8       | 29.6       | 29.3       | 29.4       | 29.5       |
| 60  | richards                 | 110.0      | 110.0      | 110.0      | 110.0      | 109.0      | 110.0      | 111.0      |
| 61  | richards_super           | 132.0      | 131.0      | 130.0      | 130.0      | 131.0      | 131.0      | 133.0      |
| 62  | scimark_fft              | 480.0      | 488.0      | 491.0      | 488.0      | 487.0      | 488.0      | 511.0      |
| 63  | scimark_lu               | 218.0      | 221.0      | 221.0      | 220.0      | 221.0      | 221.0      | 221.0      |
| 64  | scimark_monte_carlo      | 147.0      | 151.0      | 148.0      | 150.0      | 150.0      | 151.0      | 152.0      |
| 65  | scimark_sor              | 278.0      | 289.0      | 288.0      | 286.0      | 286.0      | 285.0      | 285.0      |
| 66  | scimark_sparse_mat_mult  | 5.8        | 5.92       | 5.9        | 5.87       | 5.87       | 5.92       | 6.59       |
| 67  | spectral_norm            | 183.0      | 189.0      | 190.0      | 189.0      | 189.0      | 189.0      | 194.0      |
| 68  | sqlalchemy_declarative   | 225.0      | 224.0      | 224.0      | 224.0      | 225.0      | 224.0      | 223.0      |
| 69  | sqlalchemy_imperative    | 31.9       | 32.4       | 32.5       | 32.5       | 32.5       | 32.6       | 31.6       |
| 70  | sqlglot_parse            | 3.23       | 3.22       | 3.2        | 3.21       | 3.21       | 3.21       | 3.26       |
| 71  | sqlglot_transpile        | 3.71       | 3.69       | 3.67       | 3.69       | 3.69       | 3.7        | 3.76       |
| 72  | sqlglot_optimize         | 91.1       | 92.4       | 92.4       | 92.4       | 92.3       | 92.5       | 93.4       |
| 73  | sqlglot_normalize        | 193.0      | 193.0      | 193.0      | 193.0      | 193.0      | 193.0      | 198.0      |
| 74  | sqlite_synth             | 0.0043     | 0.0044     | 0.0044     | 0.0044     | 0.0045     | 0.0045     | 0.0044     |
| 75  | sympy_expand             | 725.0      | 731.0      | 734.0      | 733.0      | 736.0      | 735.0      | 756.0      |
| 76  | sympy_integrate          | 31.8       | 32.3       | 32.4       | 32.4       | 32.4       | 32.2       | 32.5       |
| 77  | sympy_sum                | 252.0      | 254.0      | 255.0      | 253.0      | 255.0      | 256.0      | 254.0      |
| 78  | sympy_str                | 443.0      | 450.0      | 451.0      | 450.0      | 451.0      | 450.0      | 455.0      |
| 79  | telco                    | 9.0        | 9.03       | 9.01       | 8.95       | 9.0        | 9.03       | 9.07       |
| 80  | tomli_loads              | 3680.0     | 3740.0     | 3740.0     | 3740.0     | 3740.0     | 3750.0     | 3770.0     |
| 81  | tornado_http             | 203.0      | 206.0      | 207.0      | 207.0      | 206.0      | 206.0      | 207.0      |
| 82  | typing_runtime_protocols | 0.755      | 0.757      | 0.76       | 0.756      | 0.76       | 0.758      | 0.742      |
| 83  | unpack_sequence          | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     | 0.0001     |
| 84  | unpickle                 | 0.0201     | 0.0203     | 0.0203     | 0.0203     | 0.0203     | 0.0203     | 0.0187     |
| 85  | unpickle_list            | 0.0063     | 0.0065     | 0.0065     | 0.0065     | 0.0064     | 0.0065     | 0.0063     |
| 86  | unpickle_pure_python     | 0.473      | 0.461      | 0.458      | 0.46       | 0.459      | 0.46       | 0.468      |
| 87  | xml_etree_parse          | 199.0      | 206.0      | 204.0      | 205.0      | 203.0      | 204.0      | 192.0      |
| 88  | xml_etree_iterparse      | 135.0      | 138.0      | 138.0      | 138.0      | 138.0      | 139.0      | 135.0      |
| 89  | xml_etree_generate       | 136.0      | 136.0      | 136.0      | 137.0      | 137.0      | 136.0      | 128.0      |
| 90  | xml_etree_process        | 108.0      | 109.0      | 109.0      | 109.0      | 108.0      | 109.0      | 103.0      |
| SUM |                          | 37086.8757 | 37302.0538 | 37395.4135 | 37363.6993 | 37135.4189 | 37178.9706 | 37496.6061 |
| AVG |                          | 407.5481   | 409.9127   | 410.9386   | 410.5901   | 408.0815   | 408.5601   | 412.0506   |
| UP% |                          | 101.1048%  | 100.5216%  | 100.2706%  | 100.3557%  | 100.9726%  | 100.8543%  | 100.0000%  |

