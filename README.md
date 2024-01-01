
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
| 3.8.0     | Oct. 14, 2019 | 100.5802% | >          |
| 3.8.14    | Sept. 6, 2022 | 100.0000% | >          |

### 2.Details
|    | Task                     | 3.8.0                | 3.8.14               |
|---:|:-------------------------|:---------------------|:---------------------|
|  0 | 2to3                     | 460 ms +- 3 ms       | 466 ms +- 3 ms       |
|  1 | async_generators         | 512 ms +- 4 ms       | 514 ms +- 4 ms       |
|  2 | async_tree_none          | 961 ms +- 37 ms      | 959 ms +- 45 ms      |
|  3 | async_tree_cpu_io_mixed  | 1.30 sec +- 0.03 sec | 1.33 sec +- 0.05 sec |
|  4 | async_tree_io            | 2.35 sec +- 0.02 sec | 2.36 sec +- 0.02 sec |
|  5 | async_tree_memoization   | 1.11 sec +- 0.03 sec | 1.17 sec +- 0.04 sec |
|  6 | asyncio_tcp              | 1.20 sec +- 0.01 sec | 1.21 sec +- 0.02 sec |
|  7 | asyncio_tcp_ssl          | 4.10 sec +- 0.63 sec | 4.09 sec +- 0.64 sec |
|  8 | asyncio_websockets       | 633 ms +- 2 ms       | 635 ms +- 2 ms       |
|  9 | chameleon                | 13.9 ms +- 0.2 ms    | 13.7 ms +- 0.2 ms    |
| 10 | chaos                    | 167 ms +- 1 ms       | 168 ms +- 2 ms       |
| 11 | comprehensions           | 38.2 us +- 0.3 us    | 38.2 us +- 0.2 us    |
| 12 | bench_mp_pool            | 19.3 ms +- 1.5 ms    | 19.4 ms +- 1.6 ms    |
| 13 | bench_thread_pool        | 1.62 ms +- 0.02 ms   | 1.62 ms +- 0.03 ms   |
| 14 | coroutines               | 54.8 ms +- 0.4 ms    | 54.7 ms +- 0.6 ms    |
| 15 | coverage                 | 48.3 ms +- 0.5 ms    | 48.5 ms +- 0.4 ms    |
| 16 | crypto_pyaes             | 163 ms +- 2 ms       | 159 ms +- 2 ms       |
| 17 | dask                     | 885 ms +- 12 ms      | 893 ms +- 13 ms      |
| 18 | deepcopy                 | 637 us +- 6 us       | 644 us +- 6 us       |
| 19 | deepcopy_reduce          | 5.61 us +- 0.07 us   | 5.68 us +- 0.04 us   |
| 20 | deepcopy_memo            | 71.8 us +- 0.5 us    | 72.9 us +- 0.5 us    |
| 21 | deltablue                | 11.0 ms +- 0.2 ms    | 11.1 ms +- 0.2 ms    |
| 22 | django_template          | 75.2 ms +- 1.1 ms    | 75.7 ms +- 0.7 ms    |
| 23 | docutils                 | 3.98 sec +- 0.06 sec | 4.02 sec +- 0.05 sec |
| 24 | dulwich_log              | 113 ms +- 1 ms       | 113 ms +- 1 ms       |
| 25 | fannkuch                 | 611 ms +- 4 ms       | 611 ms +- 5 ms       |
| 26 | float                    | 164 ms +- 2 ms       | 166 ms +- 3 ms       |
| 27 | create_gc_cycles         | 1.74 ms +- 0.01 ms   | 1.73 ms +- 0.01 ms   |
| 28 | gc_traversal             | 3.97 ms +- 0.01 ms   | 4.22 ms +- 0.02 ms   |
| 29 | generators               | 82.9 ms +- 0.6 ms    | 85.1 ms +- 0.6 ms    |
| 30 | genshi_text              | 42.7 ms +- 0.5 ms    | 43.8 ms +- 0.5 ms    |
| 31 | genshi_xml               | 86.3 ms +- 1.0 ms    | 89.5 ms +- 1.3 ms    |
| 32 | go                       | 380 ms +- 5 ms       | 375 ms +- 3 ms       |
| 33 | hexiom                   | 14.4 ms +- 0.2 ms    | 14.6 ms +- 0.2 ms    |
| 34 | html5lib                 | 124 ms +- 6 ms       | 122 ms +- 5 ms       |
| 35 | json_dumps               | 17.5 ms +- 0.2 ms    | 17.5 ms +- 0.2 ms    |
| 36 | json_loads               | 36.7 us +- 0.9 us    | 37.0 us +- 0.7 us    |
| 37 | logging_format           | 14.4 us +- 0.3 us    | 14.3 us +- 0.2 us    |
| 38 | logging_silent           | 285 ns +- 4 ns       | 283 ns +- 5 ns       |
| 39 | logging_simple           | 13.2 us +- 0.2 us    | 13.0 us +- 0.2 us    |
| 40 | mako                     | 23.4 ms +- 0.2 ms    | 23.7 ms +- 0.3 ms    |
| 41 | mdp                      | 4.27 sec +- 0.03 sec | 4.17 sec +- 0.02 sec |
| 42 | meteor_contest           | 184 ms +- 6 ms       | 150 ms +- 3 ms       |
| 43 | nbody                    | 176 ms +- 1 ms       | 178 ms +- 1 ms       |
| 44 | nqueens                  | 136 ms +- 1 ms       | 138 ms +- 1 ms       |
| 45 | pathlib                  | 34.4 ms +- 0.5 ms    | 32.9 ms +- 0.5 ms    |
| 46 | pickle                   | 13.0 us +- 0.2 us    | 12.7 us +- 0.2 us    |
| 47 | pickle_dict              | 32.7 us +- 0.3 us    | 31.4 us +- 0.2 us    |
| 48 | pickle_list              | 5.05 us +- 0.06 us   | 5.05 us +- 0.07 us   |
| 49 | pickle_pure_python       | 679 us +- 8 us       | 690 us +- 14 us      |
| 50 | pidigits                 | 236 ms +- 4 ms       | 236 ms +- 1 ms       |
| 51 | pprint_pformat           | 2.06 sec +- 0.01 sec | 2.11 sec +- 0.02 sec |
| 52 | pyflate                  | 967 ms +- 7 ms       | 973 ms +- 10 ms      |
| 53 | python_startup           | 12.6 ms +- 0.2 ms    | 12.8 ms +- 0.3 ms    |
| 54 | python_startup_no_site   | 8.19 ms +- 0.14 ms   | 8.42 ms +- 0.15 ms   |
| 55 | raytrace                 | 775 ms +- 5 ms       | 784 ms +- 7 ms       |
| 56 | regex_compile            | 236 ms +- 2 ms       | 240 ms +- 2 ms       |
| 57 | regex_dna                | 222 ms +- 2 ms       | 222 ms +- 2 ms       |
| 58 | regex_effbot             | 3.71 ms +- 0.10 ms   | 3.59 ms +- 0.02 ms   |
| 59 | regex_v8                 | 29.6 ms +- 0.6 ms    | 29.7 ms +- 0.4 ms    |
| 60 | richards                 | 110 ms +- 2 ms       | 110 ms +- 2 ms       |
| 61 | richards_super           | 132 ms +- 2 ms       | 131 ms +- 3 ms       |
| 62 | scimark_fft              | 480 ms +- 4 ms       | 488 ms +- 3 ms       |
| 63 | scimark_lu               | 218 ms +- 1 ms       | 221 ms +- 3 ms       |
| 64 | scimark_monte_carlo      | 147 ms +- 2 ms       | 151 ms +- 3 ms       |
| 65 | scimark_sor              | 278 ms +- 4 ms       | 289 ms +- 2 ms       |
| 66 | scimark_sparse_mat_mult  | 5.80 ms +- 0.06 ms   | 5.92 ms +- 0.17 ms   |
| 67 | spectral_norm            | 183 ms +- 1 ms       | 189 ms +- 1 ms       |
| 68 | sqlalchemy_declarative   | 225 ms +- 5 ms       | 224 ms +- 5 ms       |
| 69 | sqlalchemy_imperative    | 31.9 ms +- 1.3 ms    | 32.4 ms +- 1.3 ms    |
| 70 | sqlglot_parse            | 3.23 ms +- 0.04 ms   | 3.22 ms +- 0.03 ms   |
| 71 | sqlglot_transpile        | 3.71 ms +- 0.03 ms   | 3.69 ms +- 0.03 ms   |
| 72 | sqlglot_optimize         | 91.1 ms +- 0.7 ms    | 92.4 ms +- 0.5 ms    |
| 73 | sqlglot_normalize        | 193 ms +- 3 ms       | 193 ms +- 1 ms       |
| 74 | sqlite_synth             | 4.31 us +- 0.13 us   | 4.42 us +- 0.13 us   |
| 75 | sympy_expand             | 725 ms +- 6 ms       | 731 ms +- 5 ms       |
| 76 | sympy_integrate          | 31.8 ms +- 0.2 ms    | 32.3 ms +- 0.3 ms    |
| 77 | sympy_sum                | 252 ms +- 3 ms       | 254 ms +- 3 ms       |
| 78 | sympy_str                | 443 ms +- 3 ms       | 450 ms +- 4 ms       |
| 79 | telco                    | 9.00 ms +- 0.15 ms   | 9.03 ms +- 0.26 ms   |
| 80 | tomli_loads              | 3.68 sec +- 0.04 sec | 3.74 sec +- 0.04 sec |
| 81 | tornado_http             | 203 ms +- 6 ms       | 206 ms +- 7 ms       |
| 82 | typing_runtime_protocols | 755 us +- 6 us       | 757 us +- 7 us       |
| 83 | unpack_sequence          | 64.6 ns +- 0.8 ns    | 64.4 ns +- 0.8 ns    |
| 84 | unpickle                 | 20.1 us +- 0.2 us    | 20.3 us +- 0.2 us    |
| 85 | unpickle_list            | 6.30 us +- 0.07 us   | 6.49 us +- 0.07 us   |
| 86 | unpickle_pure_python     | 473 us +- 9 us       | 461 us +- 5 us       |
| 87 | xml_etree_parse          | 199 ms +- 3 ms       | 206 ms +- 3 ms       |
| 88 | xml_etree_iterparse      | 135 ms +- 2 ms       | 138 ms +- 2 ms       |
| 89 | xml_etree_generate       | 136 ms +- 3 ms       | 136 ms +- 3 ms       |
| 90 | xml_etree_process        | 108 ms +- 1 ms       | 109 ms +- 1 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      | 3.8.14     |
|:----|:-------------------------|:-----------|:-----------|
| 0   | 2to3                     | 460.0      | 466.0      |
| 1   | async_generators         | 512.0      | 514.0      |
| 2   | async_tree_none          | 961.0      | 959.0      |
| 3   | async_tree_cpu_io_mixed  | 1300.0     | 1330.0     |
| 4   | async_tree_io            | 2350.0     | 2360.0     |
| 5   | async_tree_memoization   | 1110.0     | 1170.0     |
| 6   | asyncio_tcp              | 1200.0     | 1210.0     |
| 7   | asyncio_tcp_ssl          | 4100.0     | 4090.0     |
| 8   | asyncio_websockets       | 633.0      | 635.0      |
| 9   | chameleon                | 13.9       | 13.7       |
| 10  | chaos                    | 167.0      | 168.0      |
| 11  | comprehensions           | 0.0382     | 0.0382     |
| 12  | bench_mp_pool            | 19.3       | 19.4       |
| 13  | bench_thread_pool        | 1.62       | 1.62       |
| 14  | coroutines               | 54.8       | 54.7       |
| 15  | coverage                 | 48.3       | 48.5       |
| 16  | crypto_pyaes             | 163.0      | 159.0      |
| 17  | dask                     | 885.0      | 893.0      |
| 18  | deepcopy                 | 0.637      | 0.644      |
| 19  | deepcopy_reduce          | 0.0056     | 0.0057     |
| 20  | deepcopy_memo            | 0.0718     | 0.0729     |
| 21  | deltablue                | 11.0       | 11.1       |
| 22  | django_template          | 75.2       | 75.7       |
| 23  | docutils                 | 3980.0     | 4020.0     |
| 24  | dulwich_log              | 113.0      | 113.0      |
| 25  | fannkuch                 | 611.0      | 611.0      |
| 26  | float                    | 164.0      | 166.0      |
| 27  | create_gc_cycles         | 1.74       | 1.73       |
| 28  | gc_traversal             | 3.97       | 4.22       |
| 29  | generators               | 82.9       | 85.1       |
| 30  | genshi_text              | 42.7       | 43.8       |
| 31  | genshi_xml               | 86.3       | 89.5       |
| 32  | go                       | 380.0      | 375.0      |
| 33  | hexiom                   | 14.4       | 14.6       |
| 34  | html5lib                 | 124.0      | 122.0      |
| 35  | json_dumps               | 17.5       | 17.5       |
| 36  | json_loads               | 0.0367     | 0.037      |
| 37  | logging_format           | 0.0144     | 0.0143     |
| 38  | logging_silent           | 0.0003     | 0.0003     |
| 39  | logging_simple           | 0.0132     | 0.013      |
| 40  | mako                     | 23.4       | 23.7       |
| 41  | mdp                      | 4270.0     | 4170.0     |
| 42  | meteor_contest           | 184.0      | 150.0      |
| 43  | nbody                    | 176.0      | 178.0      |
| 44  | nqueens                  | 136.0      | 138.0      |
| 45  | pathlib                  | 34.4       | 32.9       |
| 46  | pickle                   | 0.013      | 0.0127     |
| 47  | pickle_dict              | 0.0327     | 0.0314     |
| 48  | pickle_list              | 0.005      | 0.005      |
| 49  | pickle_pure_python       | 0.679      | 0.69       |
| 50  | pidigits                 | 236.0      | 236.0      |
| 51  | pprint_pformat           | 2060.0     | 2110.0     |
| 52  | pyflate                  | 967.0      | 973.0      |
| 53  | python_startup           | 12.6       | 12.8       |
| 54  | python_startup_no_site   | 8.19       | 8.42       |
| 55  | raytrace                 | 775.0      | 784.0      |
| 56  | regex_compile            | 236.0      | 240.0      |
| 57  | regex_dna                | 222.0      | 222.0      |
| 58  | regex_effbot             | 3.71       | 3.59       |
| 59  | regex_v8                 | 29.6       | 29.7       |
| 60  | richards                 | 110.0      | 110.0      |
| 61  | richards_super           | 132.0      | 131.0      |
| 62  | scimark_fft              | 480.0      | 488.0      |
| 63  | scimark_lu               | 218.0      | 221.0      |
| 64  | scimark_monte_carlo      | 147.0      | 151.0      |
| 65  | scimark_sor              | 278.0      | 289.0      |
| 66  | scimark_sparse_mat_mult  | 5.8        | 5.92       |
| 67  | spectral_norm            | 183.0      | 189.0      |
| 68  | sqlalchemy_declarative   | 225.0      | 224.0      |
| 69  | sqlalchemy_imperative    | 31.9       | 32.4       |
| 70  | sqlglot_parse            | 3.23       | 3.22       |
| 71  | sqlglot_transpile        | 3.71       | 3.69       |
| 72  | sqlglot_optimize         | 91.1       | 92.4       |
| 73  | sqlglot_normalize        | 193.0      | 193.0      |
| 74  | sqlite_synth             | 0.0043     | 0.0044     |
| 75  | sympy_expand             | 725.0      | 731.0      |
| 76  | sympy_integrate          | 31.8       | 32.3       |
| 77  | sympy_sum                | 252.0      | 254.0      |
| 78  | sympy_str                | 443.0      | 450.0      |
| 79  | telco                    | 9.0        | 9.03       |
| 80  | tomli_loads              | 3680.0     | 3740.0     |
| 81  | tornado_http             | 203.0      | 206.0      |
| 82  | typing_runtime_protocols | 0.755      | 0.757      |
| 83  | unpack_sequence          | 0.0001     | 0.0001     |
| 84  | unpickle                 | 0.0201     | 0.0203     |
| 85  | unpickle_list            | 0.0063     | 0.0065     |
| 86  | unpickle_pure_python     | 0.473      | 0.461      |
| 87  | xml_etree_parse          | 199.0      | 206.0      |
| 88  | xml_etree_iterparse      | 135.0      | 138.0      |
| 89  | xml_etree_generate       | 136.0      | 136.0      |
| 90  | xml_etree_process        | 108.0      | 109.0      |
| SUM |                          | 37086.8757 | 37302.0538 |
| AVG |                          | 407.5481   | 409.9127   |
| UP% |                          | 100.5802%  | 100.0000%  |

