
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
|  0 | 2to3                     | 460 ms +- 3 ms       |
|  1 | async_generators         | 512 ms +- 4 ms       |
|  2 | async_tree_none          | 961 ms +- 37 ms      |
|  3 | async_tree_cpu_io_mixed  | 1.30 sec +- 0.03 sec |
|  4 | async_tree_io            | 2.35 sec +- 0.02 sec |
|  5 | async_tree_memoization   | 1.11 sec +- 0.03 sec |
|  6 | asyncio_tcp              | 1.20 sec +- 0.01 sec |
|  7 | asyncio_tcp_ssl          | 4.10 sec +- 0.63 sec |
|  8 | asyncio_websockets       | 633 ms +- 2 ms       |
|  9 | chameleon                | 13.9 ms +- 0.2 ms    |
| 10 | chaos                    | 167 ms +- 1 ms       |
| 11 | comprehensions           | 38.2 us +- 0.3 us    |
| 12 | bench_mp_pool            | 19.3 ms +- 1.5 ms    |
| 13 | bench_thread_pool        | 1.62 ms +- 0.02 ms   |
| 14 | coroutines               | 54.8 ms +- 0.4 ms    |
| 15 | coverage                 | 48.3 ms +- 0.5 ms    |
| 16 | crypto_pyaes             | 163 ms +- 2 ms       |
| 17 | dask                     | 885 ms +- 12 ms      |
| 18 | deepcopy                 | 637 us +- 6 us       |
| 19 | deepcopy_reduce          | 5.61 us +- 0.07 us   |
| 20 | deepcopy_memo            | 71.8 us +- 0.5 us    |
| 21 | deltablue                | 11.0 ms +- 0.2 ms    |
| 22 | django_template          | 75.2 ms +- 1.1 ms    |
| 23 | docutils                 | 3.98 sec +- 0.06 sec |
| 24 | dulwich_log              | 113 ms +- 1 ms       |
| 25 | fannkuch                 | 611 ms +- 4 ms       |
| 26 | float                    | 164 ms +- 2 ms       |
| 27 | create_gc_cycles         | 1.74 ms +- 0.01 ms   |
| 28 | gc_traversal             | 3.97 ms +- 0.01 ms   |
| 29 | generators               | 82.9 ms +- 0.6 ms    |
| 30 | genshi_text              | 42.7 ms +- 0.5 ms    |
| 31 | genshi_xml               | 86.3 ms +- 1.0 ms    |
| 32 | go                       | 380 ms +- 5 ms       |
| 33 | hexiom                   | 14.4 ms +- 0.2 ms    |
| 34 | html5lib                 | 124 ms +- 6 ms       |
| 35 | json_dumps               | 17.5 ms +- 0.2 ms    |
| 36 | json_loads               | 36.7 us +- 0.9 us    |
| 37 | logging_format           | 14.4 us +- 0.3 us    |
| 38 | logging_silent           | 285 ns +- 4 ns       |
| 39 | logging_simple           | 13.2 us +- 0.2 us    |
| 40 | mako                     | 23.4 ms +- 0.2 ms    |
| 41 | mdp                      | 4.27 sec +- 0.03 sec |
| 42 | meteor_contest           | 184 ms +- 6 ms       |
| 43 | nbody                    | 176 ms +- 1 ms       |
| 44 | nqueens                  | 136 ms +- 1 ms       |
| 45 | pathlib                  | 34.4 ms +- 0.5 ms    |
| 46 | pickle                   | 13.0 us +- 0.2 us    |
| 47 | pickle_dict              | 32.7 us +- 0.3 us    |
| 48 | pickle_list              | 5.05 us +- 0.06 us   |
| 49 | pickle_pure_python       | 679 us +- 8 us       |
| 50 | pidigits                 | 236 ms +- 4 ms       |
| 51 | pprint_pformat           | 2.06 sec +- 0.01 sec |
| 52 | pyflate                  | 967 ms +- 7 ms       |
| 53 | python_startup           | 12.6 ms +- 0.2 ms    |
| 54 | python_startup_no_site   | 8.19 ms +- 0.14 ms   |
| 55 | raytrace                 | 775 ms +- 5 ms       |
| 56 | regex_compile            | 236 ms +- 2 ms       |
| 57 | regex_dna                | 222 ms +- 2 ms       |
| 58 | regex_effbot             | 3.71 ms +- 0.10 ms   |
| 59 | regex_v8                 | 29.6 ms +- 0.6 ms    |
| 60 | richards                 | 110 ms +- 2 ms       |
| 61 | richards_super           | 132 ms +- 2 ms       |
| 62 | scimark_fft              | 480 ms +- 4 ms       |
| 63 | scimark_lu               | 218 ms +- 1 ms       |
| 64 | scimark_monte_carlo      | 147 ms +- 2 ms       |
| 65 | scimark_sor              | 278 ms +- 4 ms       |
| 66 | scimark_sparse_mat_mult  | 5.80 ms +- 0.06 ms   |
| 67 | spectral_norm            | 183 ms +- 1 ms       |
| 68 | sqlalchemy_declarative   | 225 ms +- 5 ms       |
| 69 | sqlalchemy_imperative    | 31.9 ms +- 1.3 ms    |
| 70 | sqlglot_parse            | 3.23 ms +- 0.04 ms   |
| 71 | sqlglot_transpile        | 3.71 ms +- 0.03 ms   |
| 72 | sqlglot_optimize         | 91.1 ms +- 0.7 ms    |
| 73 | sqlglot_normalize        | 193 ms +- 3 ms       |
| 74 | sqlite_synth             | 4.31 us +- 0.13 us   |
| 75 | sympy_expand             | 725 ms +- 6 ms       |
| 76 | sympy_integrate          | 31.8 ms +- 0.2 ms    |
| 77 | sympy_sum                | 252 ms +- 3 ms       |
| 78 | sympy_str                | 443 ms +- 3 ms       |
| 79 | telco                    | 9.00 ms +- 0.15 ms   |
| 80 | tomli_loads              | 3.68 sec +- 0.04 sec |
| 81 | tornado_http             | 203 ms +- 6 ms       |
| 82 | typing_runtime_protocols | 755 us +- 6 us       |
| 83 | unpack_sequence          | 64.6 ns +- 0.8 ns    |
| 84 | unpickle                 | 20.1 us +- 0.2 us    |
| 85 | unpickle_list            | 6.30 us +- 0.07 us   |
| 86 | unpickle_pure_python     | 473 us +- 9 us       |
| 87 | xml_etree_parse          | 199 ms +- 3 ms       |
| 88 | xml_etree_iterparse      | 135 ms +- 2 ms       |
| 89 | xml_etree_generate       | 136 ms +- 3 ms       |
| 90 | xml_etree_process        | 108 ms +- 1 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      |
|:----|:-------------------------|:-----------|
| 0   | 2to3                     | 460.0      |
| 1   | async_generators         | 512.0      |
| 2   | async_tree_none          | 961.0      |
| 3   | async_tree_cpu_io_mixed  | 1300.0     |
| 4   | async_tree_io            | 2350.0     |
| 5   | async_tree_memoization   | 1110.0     |
| 6   | asyncio_tcp              | 1200.0     |
| 7   | asyncio_tcp_ssl          | 4100.0     |
| 8   | asyncio_websockets       | 633.0      |
| 9   | chameleon                | 13.9       |
| 10  | chaos                    | 167.0      |
| 11  | comprehensions           | 0.0382     |
| 12  | bench_mp_pool            | 19.3       |
| 13  | bench_thread_pool        | 1.62       |
| 14  | coroutines               | 54.8       |
| 15  | coverage                 | 48.3       |
| 16  | crypto_pyaes             | 163.0      |
| 17  | dask                     | 885.0      |
| 18  | deepcopy                 | 0.637      |
| 19  | deepcopy_reduce          | 0.0056     |
| 20  | deepcopy_memo            | 0.0718     |
| 21  | deltablue                | 11.0       |
| 22  | django_template          | 75.2       |
| 23  | docutils                 | 3980.0     |
| 24  | dulwich_log              | 113.0      |
| 25  | fannkuch                 | 611.0      |
| 26  | float                    | 164.0      |
| 27  | create_gc_cycles         | 1.74       |
| 28  | gc_traversal             | 3.97       |
| 29  | generators               | 82.9       |
| 30  | genshi_text              | 42.7       |
| 31  | genshi_xml               | 86.3       |
| 32  | go                       | 380.0      |
| 33  | hexiom                   | 14.4       |
| 34  | html5lib                 | 124.0      |
| 35  | json_dumps               | 17.5       |
| 36  | json_loads               | 0.0367     |
| 37  | logging_format           | 0.0144     |
| 38  | logging_silent           | 0.0003     |
| 39  | logging_simple           | 0.0132     |
| 40  | mako                     | 23.4       |
| 41  | mdp                      | 4270.0     |
| 42  | meteor_contest           | 184.0      |
| 43  | nbody                    | 176.0      |
| 44  | nqueens                  | 136.0      |
| 45  | pathlib                  | 34.4       |
| 46  | pickle                   | 0.013      |
| 47  | pickle_dict              | 0.0327     |
| 48  | pickle_list              | 0.005      |
| 49  | pickle_pure_python       | 0.679      |
| 50  | pidigits                 | 236.0      |
| 51  | pprint_pformat           | 2060.0     |
| 52  | pyflate                  | 967.0      |
| 53  | python_startup           | 12.6       |
| 54  | python_startup_no_site   | 8.19       |
| 55  | raytrace                 | 775.0      |
| 56  | regex_compile            | 236.0      |
| 57  | regex_dna                | 222.0      |
| 58  | regex_effbot             | 3.71       |
| 59  | regex_v8                 | 29.6       |
| 60  | richards                 | 110.0      |
| 61  | richards_super           | 132.0      |
| 62  | scimark_fft              | 480.0      |
| 63  | scimark_lu               | 218.0      |
| 64  | scimark_monte_carlo      | 147.0      |
| 65  | scimark_sor              | 278.0      |
| 66  | scimark_sparse_mat_mult  | 5.8        |
| 67  | spectral_norm            | 183.0      |
| 68  | sqlalchemy_declarative   | 225.0      |
| 69  | sqlalchemy_imperative    | 31.9       |
| 70  | sqlglot_parse            | 3.23       |
| 71  | sqlglot_transpile        | 3.71       |
| 72  | sqlglot_optimize         | 91.1       |
| 73  | sqlglot_normalize        | 193.0      |
| 74  | sqlite_synth             | 0.0043     |
| 75  | sympy_expand             | 725.0      |
| 76  | sympy_integrate          | 31.8       |
| 77  | sympy_sum                | 252.0      |
| 78  | sympy_str                | 443.0      |
| 79  | telco                    | 9.0        |
| 80  | tomli_loads              | 3680.0     |
| 81  | tornado_http             | 203.0      |
| 82  | typing_runtime_protocols | 0.755      |
| 83  | unpack_sequence          | 0.0001     |
| 84  | unpickle                 | 0.0201     |
| 85  | unpickle_list            | 0.0063     |
| 86  | unpickle_pure_python     | 0.473      |
| 87  | xml_etree_parse          | 199.0      |
| 88  | xml_etree_iterparse      | 135.0      |
| 89  | xml_etree_generate       | 136.0      |
| 90  | xml_etree_process        | 108.0      |
| SUM |                          | 37086.8757 |
| AVG |                          | 407.5481   |
| UP% |                          | 100.0000%  |

