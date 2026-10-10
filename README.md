
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
| 3.8.0     | Oct. 14, 2019 | 100.0000% | >          |

### 2.Details
|    | Task                     | 3.8.0                |
|---:|:-------------------------|:---------------------|
|  0 | 2to3                     | 496 ms +- 16 ms      |
|  1 | async_generators         | 563 ms +- 26 ms      |
|  2 | async_tree_none          | 1.04 sec +- 0.05 sec |
|  3 | async_tree_cpu_io_mixed  | 1.41 sec +- 0.05 sec |
|  4 | async_tree_io            | 2.53 sec +- 0.05 sec |
|  5 | async_tree_memoization   | 1.27 sec +- 0.04 sec |
|  6 | asyncio_tcp              | 1.42 sec +- 0.05 sec |
|  7 | asyncio_tcp_ssl          | 3.45 sec +- 0.44 sec |
|  8 | asyncio_websockets       | 629 ms +- 18 ms      |
|  9 | chameleon                | 15.1 ms +- 0.8 ms    |
| 10 | chaos                    | 179 ms +- 12 ms      |
| 11 | comprehensions           | 40.5 us +- 1.6 us    |
| 12 | bench_mp_pool            | 11.6 ms +- 1.3 ms    |
| 13 | bench_thread_pool        | 1.83 ms +- 0.09 ms   |
| 14 | coroutines               | 61.0 ms +- 2.1 ms    |
| 15 | coverage                 | 72.0 ms +- 2.3 ms    |
| 16 | crypto_pyaes             | 167 ms +- 11 ms      |
| 17 | deepcopy                 | 692 us +- 23 us      |
| 18 | deepcopy_reduce          | 6.12 us +- 0.37 us   |
| 19 | deepcopy_memo            | 79.8 us +- 3.4 us    |
| 20 | deltablue                | 11.9 ms +- 0.6 ms    |
| 21 | docutils                 | 4.27 sec +- 0.08 sec |
| 22 | dulwich_log              | 116 ms +- 6 ms       |
| 23 | fannkuch                 | 659 ms +- 10 ms      |
| 24 | float                    | 179 ms +- 6 ms       |
| 25 | create_gc_cycles         | 1.79 ms +- 0.05 ms   |
| 26 | gc_traversal             | 4.71 ms +- 0.13 ms   |
| 27 | generators               | 94.3 ms +- 5.1 ms    |
| 28 | genshi_text              | 45.6 ms +- 2.3 ms    |
| 29 | genshi_xml               | 92.3 ms +- 5.0 ms    |
| 30 | go                       | 396 ms +- 10 ms      |
| 31 | hexiom                   | 15.5 ms +- 1.1 ms    |
| 32 | html5lib                 | 126 ms +- 12 ms      |
| 33 | json_dumps               | 19.5 ms +- 1.5 ms    |
| 34 | json_loads               | 40.5 us +- 2.4 us    |
| 35 | logging_format           | 14.6 us +- 0.5 us    |
| 36 | logging_silent           | 301 ns +- 11 ns      |
| 37 | logging_simple           | 13.2 us +- 0.5 us    |
| 38 | mako                     | 27.9 ms +- 2.5 ms    |
| 39 | mdp                      | 4.41 sec +- 0.07 sec |
| 40 | meteor_contest           | 147 ms +- 5 ms       |
| 41 | nbody                    | 197 ms +- 4 ms       |
| 42 | nqueens                  | 145 ms +- 5 ms       |
| 43 | pathlib                  | 39.3 ms +- 3.7 ms    |
| 44 | pickle                   | 13.6 us +- 0.4 us    |
| 45 | pickle_dict              | 37.7 us +- 0.8 us    |
| 46 | pickle_list              | 5.57 us +- 0.32 us   |
| 47 | pickle_pure_python       | 743 us +- 70 us      |
| 48 | pidigits                 | 235 ms +- 4 ms       |
| 49 | pprint_pformat           | 2.26 sec +- 0.04 sec |
| 50 | pyflate                  | 1.05 sec +- 0.02 sec |
| 51 | python_startup           | 13.8 ms +- 0.8 ms    |
| 52 | python_startup_no_site   | 9.05 ms +- 0.61 ms   |
| 53 | raytrace                 | 839 ms +- 21 ms      |
| 54 | regex_compile            | 256 ms +- 7 ms       |
| 55 | regex_dna                | 237 ms +- 12 ms      |
| 56 | regex_effbot             | 3.93 ms +- 0.15 ms   |
| 57 | regex_v8                 | 32.0 ms +- 2.2 ms    |
| 58 | richards                 | 120 ms +- 10 ms      |
| 59 | richards_super           | 141 ms +- 8 ms       |
| 60 | scimark_fft              | 526 ms +- 10 ms      |
| 61 | scimark_lu               | 231 ms +- 14 ms      |
| 62 | scimark_monte_carlo      | 158 ms +- 6 ms       |
| 63 | scimark_sor              | 306 ms +- 11 ms      |
| 64 | scimark_sparse_mat_mult  | 6.29 ms +- 0.19 ms   |
| 65 | spectral_norm            | 203 ms +- 4 ms       |
| 66 | sqlalchemy_declarative   | 228 ms +- 7 ms       |
| 67 | sqlalchemy_imperative    | 32.4 ms +- 2.2 ms    |
| 68 | sqlglot_normalize        | 202 ms +- 7 ms       |
| 69 | sqlglot_optimize         | 95.2 ms +- 3.1 ms    |
| 70 | sqlglot_parse            | 3.32 ms +- 0.16 ms   |
| 71 | sqlglot_transpile        | 3.85 ms +- 0.17 ms   |
| 72 | sqlite_synth             | 4.30 us +- 0.36 us   |
| 73 | sympy_expand             | 753 ms +- 19 ms      |
| 74 | sympy_integrate          | 34.0 ms +- 0.9 ms    |
| 75 | sympy_sum                | 262 ms +- 12 ms      |
| 76 | sympy_str                | 467 ms +- 20 ms      |
| 77 | telco                    | 9.57 ms +- 0.68 ms   |
| 78 | tomli_loads              | 4.06 sec +- 0.08 sec |
| 79 | tornado_http             | 229 ms +- 15 ms      |
| 80 | typing_runtime_protocols | 802 us +- 37 us      |
| 81 | unpack_sequence          | 69.8 ns +- 2.3 ns    |
| 82 | unpickle                 | 21.5 us +- 2.3 us    |
| 83 | unpickle_list            | 6.03 us +- 0.21 us   |
| 84 | unpickle_pure_python     | 496 us +- 18 us      |
| 85 | xml_etree_parse          | 207 ms +- 11 ms      |
| 86 | xml_etree_iterparse      | 148 ms +- 6 ms       |
| 87 | xml_etree_generate       | 145 ms +- 9 ms       |
| 88 | xml_etree_process        | 116 ms +- 9 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      |
|:----|:-------------------------|:-----------|
| 0   | 2to3                     | 496.0      |
| 1   | async_generators         | 563.0      |
| 2   | async_tree_none          | 1040.0     |
| 3   | async_tree_cpu_io_mixed  | 1410.0     |
| 4   | async_tree_io            | 2530.0     |
| 5   | async_tree_memoization   | 1270.0     |
| 6   | asyncio_tcp              | 1420.0     |
| 7   | asyncio_tcp_ssl          | 3450.0     |
| 8   | asyncio_websockets       | 629.0      |
| 9   | chameleon                | 15.1       |
| 10  | chaos                    | 179.0      |
| 11  | comprehensions           | 0.0405     |
| 12  | bench_mp_pool            | 11.6       |
| 13  | bench_thread_pool        | 1.83       |
| 14  | coroutines               | 61.0       |
| 15  | coverage                 | 72.0       |
| 16  | crypto_pyaes             | 167.0      |
| 17  | deepcopy                 | 0.692      |
| 18  | deepcopy_reduce          | 0.0061     |
| 19  | deepcopy_memo            | 0.0798     |
| 20  | deltablue                | 11.9       |
| 21  | docutils                 | 4270.0     |
| 22  | dulwich_log              | 116.0      |
| 23  | fannkuch                 | 659.0      |
| 24  | float                    | 179.0      |
| 25  | create_gc_cycles         | 1.79       |
| 26  | gc_traversal             | 4.71       |
| 27  | generators               | 94.3       |
| 28  | genshi_text              | 45.6       |
| 29  | genshi_xml               | 92.3       |
| 30  | go                       | 396.0      |
| 31  | hexiom                   | 15.5       |
| 32  | html5lib                 | 126.0      |
| 33  | json_dumps               | 19.5       |
| 34  | json_loads               | 0.0405     |
| 35  | logging_format           | 0.0146     |
| 36  | logging_silent           | 0.0003     |
| 37  | logging_simple           | 0.0132     |
| 38  | mako                     | 27.9       |
| 39  | mdp                      | 4410.0     |
| 40  | meteor_contest           | 147.0      |
| 41  | nbody                    | 197.0      |
| 42  | nqueens                  | 145.0      |
| 43  | pathlib                  | 39.3       |
| 44  | pickle                   | 0.0136     |
| 45  | pickle_dict              | 0.0377     |
| 46  | pickle_list              | 0.0056     |
| 47  | pickle_pure_python       | 0.743      |
| 48  | pidigits                 | 235.0      |
| 49  | pprint_pformat           | 2260.0     |
| 50  | pyflate                  | 1050.0     |
| 51  | python_startup           | 13.8       |
| 52  | python_startup_no_site   | 9.05       |
| 53  | raytrace                 | 839.0      |
| 54  | regex_compile            | 256.0      |
| 55  | regex_dna                | 237.0      |
| 56  | regex_effbot             | 3.93       |
| 57  | regex_v8                 | 32.0       |
| 58  | richards                 | 120.0      |
| 59  | richards_super           | 141.0      |
| 60  | scimark_fft              | 526.0      |
| 61  | scimark_lu               | 231.0      |
| 62  | scimark_monte_carlo      | 158.0      |
| 63  | scimark_sor              | 306.0      |
| 64  | scimark_sparse_mat_mult  | 6.29       |
| 65  | spectral_norm            | 203.0      |
| 66  | sqlalchemy_declarative   | 228.0      |
| 67  | sqlalchemy_imperative    | 32.4       |
| 68  | sqlglot_normalize        | 202.0      |
| 69  | sqlglot_optimize         | 95.2       |
| 70  | sqlglot_parse            | 3.32       |
| 71  | sqlglot_transpile        | 3.85       |
| 72  | sqlite_synth             | 0.0043     |
| 73  | sympy_expand             | 753.0      |
| 74  | sympy_integrate          | 34.0       |
| 75  | sympy_sum                | 262.0      |
| 76  | sympy_str                | 467.0      |
| 77  | telco                    | 9.57       |
| 78  | tomli_loads              | 4060.0     |
| 79  | tornado_http             | 229.0      |
| 80  | typing_runtime_protocols | 0.802      |
| 81  | unpack_sequence          | 0.0001     |
| 82  | unpickle                 | 0.0215     |
| 83  | unpickle_list            | 0.006      |
| 84  | unpickle_pure_python     | 0.496      |
| 85  | xml_etree_parse          | 207.0      |
| 86  | xml_etree_iterparse      | 148.0      |
| 87  | xml_etree_generate       | 145.0      |
| 88  | xml_etree_process        | 116.0      |
| SUM |                          | 37938.7568 |
| AVG |                          | 426.2782   |
| UP% |                          | 100.0000%  |


<div align=center>

[![IvanaXu/PythonVersions](https://gitee.com/IvanaXu/PythonVersions/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/IvanaXu/PythonVersions)

https://github.com/IvanaXu/PythonVersions

</div>
