### 0.Environment
![](./environment/M1-ENV.png)

### 1.Versions
| version   |
|:----------|
| 3.9.17    |

### 2.Source
|    | Task                          | 3.9.17               |
|---:|:------------------------------|:---------------------|
|  0 | 2to3                          | 247 ms +- 19 ms      |
|  1 | async_generators              | 279 ms +- 9 ms       |
|  2 | async_tree_none               | 589 ms +- 72 ms      |
|  3 | async_tree_cpu_io_mixed       | 979 ms +- 301 ms     |
|  4 | async_tree_eager              | 577 ms +- 50 ms      |
|  5 | async_tree_eager_cpu_io_mixed | 867 ms +- 108 ms     |
|  6 | async_tree_eager_io           | 1.59 sec +- 0.15 sec |
|  7 | async_tree_eager_memoization  | 935 ms +- 526 ms     |
|  8 | async_tree_io                 | 1.58 sec +- 0.14 sec |
|  9 | async_tree_memoization        | 669 ms +- 33 ms      |
| 10 | asyncio_tcp                   | 932 ms +- 579 ms     |
| 11 | asyncio_tcp_ssl               | 2.76 sec +- 0.51 sec |
| 12 | chameleon                     | 7.57 ms +- 0.35 ms   |
| 13 | chaos                         | 83.4 ms +- 8.6 ms    |
| 14 | comprehensions                | 20.1 us +- 0.5 us    |
| 15 | bench_mp_pool                 | 8.85 ms +- 1.27 ms   |
| 16 | bench_thread_pool             | 1.11 ms +- 0.06 ms   |
| 17 | coroutines                    | 33.7 ms +- 12.7 ms   |
| 18 | coverage                      | 35.2 ms +- 1.0 ms    |
| 19 | crypto_pyaes                  | 90.8 ms +- 5.4 ms    |
| 20 | dask                          | 520 ms +- 91 ms      |
| 21 | deepcopy                      | 320 us +- 6 us       |
| 22 | deepcopy_reduce               | 2.85 us +- 0.20 us   |
| 23 | deepcopy_memo                 | 38.9 us +- 3.1 us    |
| 24 | deltablue                     | 7.36 ms +- 4.88 ms   |
| 25 | django_template               | 36.3 ms +- 2.5 ms    |
| 26 | docutils                      | 2.21 sec +- 0.12 sec |
| 27 | dulwich_log                   | 52.6 ms +- 5.6 ms    |
| 28 | fannkuch                      | 338 ms +- 10 ms      |
| 29 | float                         | 105 ms +- 2 ms       |
| 30 | create_gc_cycles              | 969 us +- 24 us      |
| 31 | gc_traversal                  | 2.94 ms +- 0.14 ms   |
| 32 | generators                    | 33.8 ms +- 2.2 ms    |
| 33 | genshi_text                   | 21.9 ms +- 1.5 ms    |
| 34 | genshi_xml                    | 43.0 ms +- 2.9 ms    |
| 35 | go                            | 192 ms +- 4 ms       |
| 36 | hexiom                        | 6.96 ms +- 0.13 ms   |
| 37 | html5lib                      | 57.8 ms +- 5.6 ms    |
| 38 | json_dumps                    | 12.1 ms +- 0.2 ms    |
| 39 | json_loads                    | 27.0 us +- 0.6 us    |
| 40 | logging_format                | 6.50 us +- 0.13 us   |
| 41 | logging_silent                | 153 ns +- 19 ns      |
| 42 | logging_simple                | 6.07 us +- 0.20 us   |
| 43 | mako                          | 13.2 ms +- 1.2 ms    |
| 44 | mdp                           | 2.89 sec +- 0.56 sec |
| 45 | meteor_contest                | 89.5 ms +- 8.1 ms    |
| 46 | nbody                         | 97.2 ms +- 7.0 ms    |
| 47 | nqueens                       | 72.6 ms +- 1.9 ms    |
| 48 | pathlib                       | 26.2 ms +- 20.6 ms   |
| 49 | pickle                        | 11.7 us +- 4.0 us    |
| 50 | pickle_dict                   | 31.4 us +- 13.1 us   |
| 51 | pickle_list                   | 4.66 us +- 1.26 us   |
| 52 | pickle_pure_python            | 427 us +- 131 us     |
| 53 | pidigits                      | 250 ms +- 121 ms     |
| 54 | pprint_pformat                | 1.21 sec +- 0.12 sec |
| 55 | pyflate                       | 528 ms +- 25 ms      |
| 56 | python_startup                | 16.6 ms +- 2.6 ms    |
| 57 | python_startup_no_site        | 9.55 ms +- 1.69 ms   |
| 58 | raytrace                      | 464 ms +- 266 ms     |
| 59 | regex_compile                 | 140 ms +- 95 ms      |
| 60 | regex_dna                     | 176 ms +- 2 ms       |
| 61 | regex_effbot                  | 2.54 ms +- 0.10 ms   |
| 62 | regex_v8                      | 21.6 ms +- 0.4 ms    |
| 63 | richards                      | 56.3 ms +- 1.2 ms    |
| 64 | richards_super                | 65.3 ms +- 1.4 ms    |
| 65 | scimark_fft                   | 423 ms +- 11 ms      |
| 66 | scimark_lu                    | 177 ms +- 5 ms       |
| 67 | scimark_monte_carlo           | 101 ms +- 2 ms       |
| 68 | scimark_sor                   | 180 ms +- 5 ms       |
| 69 | scimark_sparse_mat_mult       | 8.95 ms +- 1.82 ms   |
| 70 | spectral_norm                 | 108 ms +- 4 ms       |
| 71 | sqlalchemy_declarative        | 106 ms +- 11 ms      |
| 72 | sqlalchemy_imperative         | 15.9 ms +- 15.5 ms   |
| 73 | sqlglot_parse                 | 2.40 ms +- 1.58 ms   |
| 74 | sqlglot_transpile             | 2.16 ms +- 0.41 ms   |
| 75 | sqlglot_optimize              | 50.0 ms +- 4.5 ms    |
| 76 | sqlglot_normalize             | 242 ms +- 13 ms      |
| 77 | sqlite_synth                  | 3.72 us +- 0.61 us   |
| 78 | sympy_expand                  | 372 ms +- 71 ms      |
| 79 | sympy_integrate               | 20.9 ms +- 12.9 ms   |
| 80 | sympy_sum                     | 114 ms +- 4 ms       |
| 81 | sympy_str                     | 205 ms +- 13 ms      |
| 82 | telco                         | 8.86 ms +- 2.58 ms   |
| 83 | tomli_loads                   | 2.15 sec +- 0.30 sec |
| 84 | tornado_http                  | 105 ms +- 22 ms      |
| 85 | typing_runtime_protocols      | 385 us +- 28 us      |
| 86 | unpack_sequence               | 42.8 ns +- 25.4 ns   |
| 87 | unpickle                      | 12.7 us +- 2.0 us    |
| 88 | unpickle_list                 | 5.10 us +- 0.09 us   |
| 89 | unpickle_pure_python          | 243 us +- 4 us       |
| 90 | xml_etree_parse               | 171 ms +- 2 ms       |
| 91 | xml_etree_iterparse           | 97.9 ms +- 1.9 ms    |
| 92 | xml_etree_generate            | 81.5 ms +- 1.7 ms    |
| 93 | xml_etree_process             | 66.8 ms +- 8.6 ms    |

### 3.Change(UNIT: ms)
|     | Task                          | 3.9.17    |
|:----|:------------------------------|:----------|
| 0   | 2to3                          | 247.0     |
| 1   | async_generators              | 279.0     |
| 2   | async_tree_none               | 589.0     |
| 3   | async_tree_cpu_io_mixed       | 979.0     |
| 4   | async_tree_eager              | 577.0     |
| 5   | async_tree_eager_cpu_io_mixed | 867.0     |
| 6   | async_tree_eager_io           | 1590.0    |
| 7   | async_tree_eager_memoization  | 935.0     |
| 8   | async_tree_io                 | 1580.0    |
| 9   | async_tree_memoization        | 669.0     |
| 10  | asyncio_tcp                   | 932.0     |
| 11  | asyncio_tcp_ssl               | 2760.0    |
| 12  | chameleon                     | 7.57      |
| 13  | chaos                         | 83.4      |
| 14  | comprehensions                | 0.0201    |
| 15  | bench_mp_pool                 | 8.85      |
| 16  | bench_thread_pool             | 1.11      |
| 17  | coroutines                    | 33.7      |
| 18  | coverage                      | 35.2      |
| 19  | crypto_pyaes                  | 90.8      |
| 20  | dask                          | 520.0     |
| 21  | deepcopy                      | 0.32      |
| 22  | deepcopy_reduce               | 0.0029    |
| 23  | deepcopy_memo                 | 0.0389    |
| 24  | deltablue                     | 7.36      |
| 25  | django_template               | 36.3      |
| 26  | docutils                      | 2210.0    |
| 27  | dulwich_log                   | 52.6      |
| 28  | fannkuch                      | 338.0     |
| 29  | float                         | 105.0     |
| 30  | create_gc_cycles              | 0.969     |
| 31  | gc_traversal                  | 2.94      |
| 32  | generators                    | 33.8      |
| 33  | genshi_text                   | 21.9      |
| 34  | genshi_xml                    | 43.0      |
| 35  | go                            | 192.0     |
| 36  | hexiom                        | 6.96      |
| 37  | html5lib                      | 57.8      |
| 38  | json_dumps                    | 12.1      |
| 39  | json_loads                    | 0.027     |
| 40  | logging_format                | 0.0065    |
| 41  | logging_silent                | 0.0002    |
| 42  | logging_simple                | 0.0061    |
| 43  | mako                          | 13.2      |
| 44  | mdp                           | 2890.0    |
| 45  | meteor_contest                | 89.5      |
| 46  | nbody                         | 97.2      |
| 47  | nqueens                       | 72.6      |
| 48  | pathlib                       | 26.2      |
| 49  | pickle                        | 0.0117    |
| 50  | pickle_dict                   | 0.0314    |
| 51  | pickle_list                   | 0.0047    |
| 52  | pickle_pure_python            | 0.427     |
| 53  | pidigits                      | 250.0     |
| 54  | pprint_pformat                | 1210.0    |
| 55  | pyflate                       | 528.0     |
| 56  | python_startup                | 16.6      |
| 57  | python_startup_no_site        | 9.55      |
| 58  | raytrace                      | 464.0     |
| 59  | regex_compile                 | 140.0     |
| 60  | regex_dna                     | 176.0     |
| 61  | regex_effbot                  | 2.54      |
| 62  | regex_v8                      | 21.6      |
| 63  | richards                      | 56.3      |
| 64  | richards_super                | 65.3      |
| 65  | scimark_fft                   | 423.0     |
| 66  | scimark_lu                    | 177.0     |
| 67  | scimark_monte_carlo           | 101.0     |
| 68  | scimark_sor                   | 180.0     |
| 69  | scimark_sparse_mat_mult       | 8.95      |
| 70  | spectral_norm                 | 108.0     |
| 71  | sqlalchemy_declarative        | 106.0     |
| 72  | sqlalchemy_imperative         | 15.9      |
| 73  | sqlglot_parse                 | 2.4       |
| 74  | sqlglot_transpile             | 2.16      |
| 75  | sqlglot_optimize              | 50.0      |
| 76  | sqlglot_normalize             | 242.0     |
| 77  | sqlite_synth                  | 0.0037    |
| 78  | sympy_expand                  | 372.0     |
| 79  | sympy_integrate               | 20.9      |
| 80  | sympy_sum                     | 114.0     |
| 81  | sympy_str                     | 205.0     |
| 82  | telco                         | 8.86      |
| 83  | tomli_loads                   | 2150.0    |
| 84  | tornado_http                  | 105.0     |
| 85  | typing_runtime_protocols      | 0.385     |
| 86  | unpack_sequence               | 0.0       |
| 87  | unpickle                      | 0.0127    |
| 88  | unpickle_list                 | 0.0051    |
| 89  | unpickle_pure_python          | 0.243     |
| 90  | xml_etree_parse               | 171.0     |
| 91  | xml_etree_iterparse           | 97.9      |
| 92  | xml_etree_generate            | 81.5      |
| 93  | xml_etree_process             | 66.8      |
| SUM |                               | 26844.865 |
| AVG |                               | 285.5837  |
| UP% |                               | 100.0000% |

