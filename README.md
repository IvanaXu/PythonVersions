
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
|  0 | 2to3                     | 502 ms +- 18 ms      |
|  1 | async_generators         | 557 ms +- 10 ms      |
|  2 | async_tree_none          | 1.04 sec +- 0.05 sec |
|  3 | async_tree_cpu_io_mixed  | 1.41 sec +- 0.05 sec |
|  4 | async_tree_io            | 2.51 sec +- 0.04 sec |
|  5 | async_tree_memoization   | 1.24 sec +- 0.04 sec |
|  6 | asyncio_tcp              | 1.40 sec +- 0.06 sec |
|  7 | asyncio_tcp_ssl          | 3.28 sec +- 0.04 sec |
|  8 | asyncio_websockets       | 626 ms +- 18 ms      |
|  9 | chameleon                | 15.0 ms +- 0.7 ms    |
| 10 | chaos                    | 177 ms +- 6 ms       |
| 11 | comprehensions           | 40.9 us +- 3.2 us    |
| 12 | bench_mp_pool            | 11.4 ms +- 1.2 ms    |
| 13 | bench_thread_pool        | 1.84 ms +- 0.08 ms   |
| 14 | coroutines               | 61.5 ms +- 4.5 ms    |
| 15 | coverage                 | 74.1 ms +- 7.0 ms    |
| 16 | crypto_pyaes             | 168 ms +- 12 ms      |
| 17 | deepcopy                 | 692 us +- 25 us      |
| 18 | deepcopy_reduce          | 6.16 us +- 0.38 us   |
| 19 | deepcopy_memo            | 78.9 us +- 1.2 us    |
| 20 | deltablue                | 11.9 ms +- 1.0 ms    |
| 21 | docutils                 | 4.28 sec +- 0.07 sec |
| 22 | dulwich_log              | 117 ms +- 9 ms       |
| 23 | fannkuch                 | 668 ms +- 26 ms      |
| 24 | float                    | 181 ms +- 10 ms      |
| 25 | create_gc_cycles         | 1.78 ms +- 0.05 ms   |
| 26 | gc_traversal             | 4.85 ms +- 0.21 ms   |
| 27 | generators               | 93.8 ms +- 2.8 ms    |
| 28 | genshi_text              | 45.4 ms +- 1.5 ms    |
| 29 | genshi_xml               | 90.5 ms +- 4.9 ms    |
| 30 | go                       | 398 ms +- 12 ms      |
| 31 | hexiom                   | 15.5 ms +- 0.8 ms    |
| 32 | html5lib                 | 126 ms +- 8 ms       |
| 33 | json_dumps               | 19.0 ms +- 0.4 ms    |
| 34 | json_loads               | 40.1 us +- 2.0 us    |
| 35 | logging_format           | 14.5 us +- 0.6 us    |
| 36 | logging_silent           | 302 ns +- 19 ns      |
| 37 | logging_simple           | 13.1 us +- 0.4 us    |
| 38 | mako                     | 28.2 ms +- 3.4 ms    |
| 39 | mdp                      | 4.40 sec +- 0.07 sec |
| 40 | meteor_contest           | 148 ms +- 8 ms       |
| 41 | nbody                    | 197 ms +- 6 ms       |
| 42 | nqueens                  | 143 ms +- 5 ms       |
| 43 | pathlib                  | 38.7 ms +- 1.8 ms    |
| 44 | pickle                   | 13.8 us +- 0.7 us    |
| 45 | pickle_dict              | 38.6 us +- 1.9 us    |
| 46 | pickle_list              | 5.65 us +- 0.33 us   |
| 47 | pickle_pure_python       | 734 us +- 58 us      |
| 48 | pidigits                 | 236 ms +- 4 ms       |
| 49 | pprint_pformat           | 2.26 sec +- 0.04 sec |
| 50 | pyflate                  | 1.05 sec +- 0.03 sec |
| 51 | python_startup           | 13.8 ms +- 0.8 ms    |
| 52 | python_startup_no_site   | 9.00 ms +- 0.40 ms   |
| 53 | raytrace                 | 836 ms +- 24 ms      |
| 54 | regex_compile            | 260 ms +- 14 ms      |
| 55 | regex_dna                | 237 ms +- 8 ms       |
| 56 | regex_effbot             | 3.91 ms +- 0.11 ms   |
| 57 | regex_v8                 | 31.3 ms +- 1.2 ms    |
| 58 | richards                 | 115 ms +- 3 ms       |
| 59 | richards_super           | 138 ms +- 4 ms       |
| 60 | scimark_fft              | 528 ms +- 15 ms      |
| 61 | scimark_lu               | 230 ms +- 10 ms      |
| 62 | scimark_monte_carlo      | 161 ms +- 11 ms      |
| 63 | scimark_sor              | 313 ms +- 18 ms      |
| 64 | scimark_sparse_mat_mult  | 6.48 ms +- 0.50 ms   |
| 65 | spectral_norm            | 205 ms +- 6 ms       |
| 66 | sqlalchemy_declarative   | 228 ms +- 7 ms       |
| 67 | sqlalchemy_imperative    | 32.6 ms +- 3.2 ms    |
| 68 | sqlglot_normalize        | 203 ms +- 8 ms       |
| 69 | sqlglot_optimize         | 95.7 ms +- 4.2 ms    |
| 70 | sqlglot_parse            | 3.33 ms +- 0.17 ms   |
| 71 | sqlglot_transpile        | 3.85 ms +- 0.12 ms   |
| 72 | sqlite_synth             | 4.32 us +- 0.26 us   |
| 73 | sympy_expand             | 756 ms +- 27 ms      |
| 74 | sympy_integrate          | 34.0 ms +- 0.8 ms    |
| 75 | sympy_sum                | 262 ms +- 12 ms      |
| 76 | sympy_str                | 462 ms +- 15 ms      |
| 77 | telco                    | 9.53 ms +- 0.56 ms   |
| 78 | tomli_loads              | 4.05 sec +- 0.07 sec |
| 79 | tornado_http             | 223 ms +- 12 ms      |
| 80 | typing_runtime_protocols | 798 us +- 63 us      |
| 81 | unpack_sequence          | 69.4 ns +- 8.3 ns    |
| 82 | unpickle                 | 20.8 us +- 0.5 us    |
| 83 | unpickle_list            | 6.08 us +- 0.57 us   |
| 84 | unpickle_pure_python     | 493 us +- 16 us      |
| 85 | xml_etree_parse          | 207 ms +- 9 ms       |
| 86 | xml_etree_iterparse      | 147 ms +- 5 ms       |
| 87 | xml_etree_generate       | 146 ms +- 10 ms      |
| 88 | xml_etree_process        | 114 ms +- 3 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      |
|:----|:-------------------------|:-----------|
| 0   | 2to3                     | 502.0      |
| 1   | async_generators         | 557.0      |
| 2   | async_tree_none          | 1040.0     |
| 3   | async_tree_cpu_io_mixed  | 1410.0     |
| 4   | async_tree_io            | 2510.0     |
| 5   | async_tree_memoization   | 1240.0     |
| 6   | asyncio_tcp              | 1400.0     |
| 7   | asyncio_tcp_ssl          | 3280.0     |
| 8   | asyncio_websockets       | 626.0      |
| 9   | chameleon                | 15.0       |
| 10  | chaos                    | 177.0      |
| 11  | comprehensions           | 0.0409     |
| 12  | bench_mp_pool            | 11.4       |
| 13  | bench_thread_pool        | 1.84       |
| 14  | coroutines               | 61.5       |
| 15  | coverage                 | 74.1       |
| 16  | crypto_pyaes             | 168.0      |
| 17  | deepcopy                 | 0.692      |
| 18  | deepcopy_reduce          | 0.0062     |
| 19  | deepcopy_memo            | 0.0789     |
| 20  | deltablue                | 11.9       |
| 21  | docutils                 | 4280.0     |
| 22  | dulwich_log              | 117.0      |
| 23  | fannkuch                 | 668.0      |
| 24  | float                    | 181.0      |
| 25  | create_gc_cycles         | 1.78       |
| 26  | gc_traversal             | 4.85       |
| 27  | generators               | 93.8       |
| 28  | genshi_text              | 45.4       |
| 29  | genshi_xml               | 90.5       |
| 30  | go                       | 398.0      |
| 31  | hexiom                   | 15.5       |
| 32  | html5lib                 | 126.0      |
| 33  | json_dumps               | 19.0       |
| 34  | json_loads               | 0.0401     |
| 35  | logging_format           | 0.0145     |
| 36  | logging_silent           | 0.0003     |
| 37  | logging_simple           | 0.0131     |
| 38  | mako                     | 28.2       |
| 39  | mdp                      | 4400.0     |
| 40  | meteor_contest           | 148.0      |
| 41  | nbody                    | 197.0      |
| 42  | nqueens                  | 143.0      |
| 43  | pathlib                  | 38.7       |
| 44  | pickle                   | 0.0138     |
| 45  | pickle_dict              | 0.0386     |
| 46  | pickle_list              | 0.0057     |
| 47  | pickle_pure_python       | 0.734      |
| 48  | pidigits                 | 236.0      |
| 49  | pprint_pformat           | 2260.0     |
| 50  | pyflate                  | 1050.0     |
| 51  | python_startup           | 13.8       |
| 52  | python_startup_no_site   | 9.0        |
| 53  | raytrace                 | 836.0      |
| 54  | regex_compile            | 260.0      |
| 55  | regex_dna                | 237.0      |
| 56  | regex_effbot             | 3.91       |
| 57  | regex_v8                 | 31.3       |
| 58  | richards                 | 115.0      |
| 59  | richards_super           | 138.0      |
| 60  | scimark_fft              | 528.0      |
| 61  | scimark_lu               | 230.0      |
| 62  | scimark_monte_carlo      | 161.0      |
| 63  | scimark_sor              | 313.0      |
| 64  | scimark_sparse_mat_mult  | 6.48       |
| 65  | spectral_norm            | 205.0      |
| 66  | sqlalchemy_declarative   | 228.0      |
| 67  | sqlalchemy_imperative    | 32.6       |
| 68  | sqlglot_normalize        | 203.0      |
| 69  | sqlglot_optimize         | 95.7       |
| 70  | sqlglot_parse            | 3.33       |
| 71  | sqlglot_transpile        | 3.85       |
| 72  | sqlite_synth             | 0.0043     |
| 73  | sympy_expand             | 756.0      |
| 74  | sympy_integrate          | 34.0       |
| 75  | sympy_sum                | 262.0      |
| 76  | sympy_str                | 462.0      |
| 77  | telco                    | 9.53       |
| 78  | tomli_loads              | 4050.0     |
| 79  | tornado_http             | 223.0      |
| 80  | typing_runtime_protocols | 0.798      |
| 81  | unpack_sequence          | 0.0001     |
| 82  | unpickle                 | 0.0208     |
| 83  | unpickle_list            | 0.0061     |
| 84  | unpickle_pure_python     | 0.493      |
| 85  | xml_etree_parse          | 207.0      |
| 86  | xml_etree_iterparse      | 147.0      |
| 87  | xml_etree_generate       | 146.0      |
| 88  | xml_etree_process        | 114.0      |
| SUM |                          | 37694.9704 |
| AVG |                          | 423.539    |
| UP% |                          | 100.0000%  |


<div align=center>

[![IvanaXu/PythonVersions](https://gitee.com/IvanaXu/PythonVersions/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/IvanaXu/PythonVersions)

https://github.com/IvanaXu/PythonVersions

</div>
