
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
| 3.8.0     | Oct. 14, 2019 | 100.9640% | >          |
| 3.8.1     | Dec. 18, 2019 | 100.0000% | >          |
| 3.8.2     | Feb. 24, 2020 | 102.0611% | >>>        |

### 2.Details
|    | Task                     | 3.8.0                | 3.8.1                | 3.8.2                |
|---:|:-------------------------|:---------------------|:---------------------|:---------------------|
|  0 | 2to3                     | 496 ms +- 16 ms      | 498 ms +- 17 ms      | 491 ms +- 16 ms      |
|  1 | async_generators         | 563 ms +- 26 ms      | 564 ms +- 25 ms      | 557 ms +- 15 ms      |
|  2 | async_tree_cpu_io_mixed  | 1.41 sec +- 0.05 sec | 1.41 sec +- 0.05 sec | 1.39 sec +- 0.05 sec |
|  3 | async_tree_io            | 2.53 sec +- 0.05 sec | 2.54 sec +- 0.04 sec | 2.53 sec +- 0.05 sec |
|  4 | async_tree_memoization   | 1.27 sec +- 0.04 sec | 1.28 sec +- 0.04 sec | 1.24 sec +- 0.05 sec |
|  5 | async_tree_none          | 1.04 sec +- 0.05 sec | 1.05 sec +- 0.04 sec | 1.04 sec +- 0.05 sec |
|  6 | asyncio_tcp              | 1.42 sec +- 0.05 sec | 1.40 sec +- 0.05 sec | 1.41 sec +- 0.05 sec |
|  7 | asyncio_tcp_ssl          | 3.45 sec +- 0.44 sec | 3.70 sec +- 0.65 sec | 3.28 sec +- 0.06 sec |
|  8 | asyncio_websockets       | 629 ms +- 18 ms      | 624 ms +- 14 ms      | 630 ms +- 14 ms      |
|  9 | bench_mp_pool            | 11.6 ms +- 1.3 ms    | 12.0 ms +- 1.1 ms    | 11.8 ms +- 1.3 ms    |
| 10 | bench_thread_pool        | 1.83 ms +- 0.09 ms   | 1.80 ms +- 0.07 ms   | 1.81 ms +- 0.07 ms   |
| 11 | chameleon                | 15.1 ms +- 0.8 ms    | 14.9 ms +- 0.8 ms    | 15.0 ms +- 0.9 ms    |
| 12 | chaos                    | 179 ms +- 12 ms      | 181 ms +- 4 ms       | 180 ms +- 8 ms       |
| 13 | comprehensions           | 40.5 us +- 1.6 us    | 41.2 us +- 1.4 us    | 40.7 us +- 1.7 us    |
| 14 | coroutines               | 61.0 ms +- 2.1 ms    | 60.4 ms +- 4.1 ms    | 59.7 ms +- 3.7 ms    |
| 15 | coverage                 | 72.0 ms +- 2.3 ms    | 73.3 ms +- 3.6 ms    | 71.7 ms +- 2.5 ms    |
| 16 | create_gc_cycles         | 1.79 ms +- 0.05 ms   | 1.78 ms +- 0.05 ms   | 1.78 ms +- 0.06 ms   |
| 17 | crypto_pyaes             | 167 ms +- 11 ms      | 165 ms +- 10 ms      | 166 ms +- 11 ms      |
| 18 | deepcopy                 | 692 us +- 23 us      | 702 us +- 41 us      | 696 us +- 26 us      |
| 19 | deepcopy_memo            | 79.8 us +- 3.4 us    | 80.4 us +- 1.5 us    | 80.7 us +- 4.2 us    |
| 20 | deepcopy_reduce          | 6.12 us +- 0.37 us   | 6.24 us +- 0.24 us   | 6.16 us +- 0.27 us   |
| 21 | deltablue                | 11.9 ms +- 0.6 ms    | 11.7 ms +- 0.4 ms    | 11.9 ms +- 0.8 ms    |
| 22 | docutils                 | 4.27 sec +- 0.08 sec | 4.31 sec +- 0.08 sec | 4.21 sec +- 0.06 sec |
| 23 | dulwich_log              | 116 ms +- 6 ms       | 115 ms +- 3 ms       | 118 ms +- 6 ms       |
| 24 | fannkuch                 | 659 ms +- 10 ms      | 661 ms +- 25 ms      | 663 ms +- 21 ms      |
| 25 | float                    | 179 ms +- 6 ms       | 178 ms +- 10 ms      | 176 ms +- 6 ms       |
| 26 | gc_traversal             | 4.71 ms +- 0.13 ms   | 4.77 ms +- 0.16 ms   | 4.67 ms +- 0.12 ms   |
| 27 | generators               | 94.3 ms +- 5.1 ms    | 93.7 ms +- 2.0 ms    | 95.5 ms +- 5.4 ms    |
| 28 | genshi_text              | 45.6 ms +- 2.3 ms    | 45.9 ms +- 1.0 ms    | 44.6 ms +- 1.1 ms    |
| 29 | genshi_xml               | 92.3 ms +- 5.0 ms    | 89.8 ms +- 3.0 ms    | 88.5 ms +- 3.7 ms    |
| 30 | go                       | 396 ms +- 10 ms      | 399 ms +- 9 ms       | 400 ms +- 14 ms      |
| 31 | hexiom                   | 15.5 ms +- 1.1 ms    | 15.8 ms +- 1.5 ms    | 15.5 ms +- 1.4 ms    |
| 32 | html5lib                 | 126 ms +- 12 ms      | 128 ms +- 9 ms       | 128 ms +- 10 ms      |
| 33 | json_dumps               | 19.5 ms +- 1.5 ms    | 19.5 ms +- 0.8 ms    | 19.5 ms +- 1.2 ms    |
| 34 | json_loads               | 40.5 us +- 2.4 us    | 39.7 us +- 2.2 us    | 39.2 us +- 1.9 us    |
| 35 | logging_format           | 14.6 us +- 0.5 us    | 14.4 us +- 0.3 us    | 14.7 us +- 0.6 us    |
| 36 | logging_silent           | 301 ns +- 11 ns      | 304 ns +- 32 ns      | 303 ns +- 15 ns      |
| 37 | logging_simple           | 13.2 us +- 0.5 us    | 13.4 us +- 0.5 us    | 13.4 us +- 0.7 us    |
| 38 | mako                     | 27.9 ms +- 2.5 ms    | 27.1 ms +- 1.1 ms    | 26.7 ms +- 0.8 ms    |
| 39 | mdp                      | 4.41 sec +- 0.07 sec | 4.40 sec +- 0.07 sec | 4.35 sec +- 0.07 sec |
| 40 | meteor_contest           | 147 ms +- 5 ms       | 145 ms +- 2 ms       | 146 ms +- 6 ms       |
| 41 | nbody                    | 197 ms +- 4 ms       | 187 ms +- 6 ms       | 200 ms +- 14 ms      |
| 42 | nqueens                  | 145 ms +- 5 ms       | 148 ms +- 16 ms      | 146 ms +- 4 ms       |
| 43 | pathlib                  | 39.3 ms +- 3.7 ms    | 38.8 ms +- 3.4 ms    | 36.9 ms +- 1.1 ms    |
| 44 | pickle                   | 13.6 us +- 0.4 us    | 13.8 us +- 0.9 us    | 14.0 us +- 0.7 us    |
| 45 | pickle_dict              | 37.7 us +- 0.8 us    | 37.0 us +- 1.8 us    | 37.8 us +- 1.9 us    |
| 46 | pickle_list              | 5.57 us +- 0.32 us   | 5.65 us +- 0.56 us   | 5.60 us +- 0.52 us   |
| 47 | pickle_pure_python       | 743 us +- 70 us      | 744 us +- 54 us      | 737 us +- 43 us      |
| 48 | pidigits                 | 235 ms +- 4 ms       | 236 ms +- 5 ms       | 237 ms +- 10 ms      |
| 49 | pprint_pformat           | 2.26 sec +- 0.04 sec | 2.25 sec +- 0.05 sec | 2.27 sec +- 0.04 sec |
| 50 | pyflate                  | 1.05 sec +- 0.02 sec | 1.05 sec +- 0.03 sec | 1.05 sec +- 0.03 sec |
| 51 | python_startup           | 13.8 ms +- 0.8 ms    | 13.8 ms +- 0.8 ms    | 13.6 ms +- 0.8 ms    |
| 52 | python_startup_no_site   | 9.05 ms +- 0.61 ms   | 9.00 ms +- 0.62 ms   | 8.80 ms +- 0.49 ms   |
| 53 | raytrace                 | 839 ms +- 21 ms      | 831 ms +- 21 ms      | 822 ms +- 15 ms      |
| 54 | regex_compile            | 256 ms +- 7 ms       | 263 ms +- 12 ms      | 256 ms +- 8 ms       |
| 55 | regex_dna                | 237 ms +- 12 ms      | 234 ms +- 4 ms       | 232 ms +- 10 ms      |
| 56 | regex_effbot             | 3.93 ms +- 0.15 ms   | 4.01 ms +- 0.22 ms   | 3.75 ms +- 0.14 ms   |
| 57 | regex_v8                 | 32.0 ms +- 2.2 ms    | 31.2 ms +- 1.6 ms    | 31.5 ms +- 2.7 ms    |
| 58 | richards                 | 120 ms +- 10 ms      | 116 ms +- 3 ms       | 117 ms +- 5 ms       |
| 59 | richards_super           | 141 ms +- 8 ms       | 138 ms +- 5 ms       | 138 ms +- 5 ms       |
| 60 | scimark_fft              | 526 ms +- 10 ms      | 525 ms +- 13 ms      | 524 ms +- 14 ms      |
| 61 | scimark_lu               | 231 ms +- 14 ms      | 265 ms +- 10 ms      | 232 ms +- 16 ms      |
| 62 | scimark_monte_carlo      | 158 ms +- 6 ms       | 164 ms +- 7 ms       | 162 ms +- 5 ms       |
| 63 | scimark_sor              | 306 ms +- 11 ms      | 316 ms +- 14 ms      | 308 ms +- 13 ms      |
| 64 | scimark_sparse_mat_mult  | 6.29 ms +- 0.19 ms   | 6.48 ms +- 0.16 ms   | 6.51 ms +- 0.26 ms   |
| 65 | spectral_norm            | 203 ms +- 4 ms       | 203 ms +- 7 ms       | 204 ms +- 4 ms       |
| 66 | sqlalchemy_declarative   | 228 ms +- 7 ms       | 232 ms +- 12 ms      | 229 ms +- 11 ms      |
| 67 | sqlalchemy_imperative    | 32.4 ms +- 2.2 ms    | 33.0 ms +- 2.4 ms    | 32.3 ms +- 2.4 ms    |
| 68 | sqlglot_normalize        | 202 ms +- 7 ms       | 208 ms +- 10 ms      | 200 ms +- 7 ms       |
| 69 | sqlglot_optimize         | 95.2 ms +- 3.1 ms    | 99.5 ms +- 6.2 ms    | 95.0 ms +- 2.4 ms    |
| 70 | sqlglot_parse            | 3.32 ms +- 0.16 ms   | 3.44 ms +- 0.14 ms   | 3.45 ms +- 0.29 ms   |
| 71 | sqlglot_transpile        | 3.85 ms +- 0.17 ms   | 4.03 ms +- 0.29 ms   | 3.91 ms +- 0.08 ms   |
| 72 | sqlite_synth             | 4.30 us +- 0.36 us   | 4.23 us +- 0.22 us   | 4.24 us +- 0.22 us   |
| 73 | sympy_expand             | 753 ms +- 19 ms      | 757 ms +- 21 ms      | 755 ms +- 22 ms      |
| 74 | sympy_integrate          | 34.0 ms +- 0.9 ms    | 34.4 ms +- 1.4 ms    | 33.5 ms +- 1.1 ms    |
| 75 | sympy_str                | 467 ms +- 20 ms      | 466 ms +- 10 ms      | 461 ms +- 13 ms      |
| 76 | sympy_sum                | 262 ms +- 12 ms      | 264 ms +- 9 ms       | 261 ms +- 10 ms      |
| 77 | telco                    | 9.57 ms +- 0.68 ms   | 9.37 ms +- 0.63 ms   | 9.08 ms +- 0.40 ms   |
| 78 | tomli_loads              | 4.06 sec +- 0.08 sec | 4.10 sec +- 0.08 sec | 4.05 sec +- 0.07 sec |
| 79 | tornado_http             | 229 ms +- 15 ms      | 227 ms +- 11 ms      | 220 ms +- 11 ms      |
| 80 | typing_runtime_protocols | 802 us +- 37 us      | 788 us +- 13 us      | 787 us +- 27 us      |
| 81 | unpack_sequence          | 69.8 ns +- 2.3 ns    | 70.6 ns +- 5.0 ns    | 69.7 ns +- 5.2 ns    |
| 82 | unpickle                 | 21.5 us +- 2.3 us    | 20.9 us +- 0.6 us    | 20.9 us +- 1.1 us    |
| 83 | unpickle_list            | 6.03 us +- 0.21 us   | 6.05 us +- 0.43 us   | 6.02 us +- 0.51 us   |
| 84 | unpickle_pure_python     | 496 us +- 18 us      | 500 us +- 15 us      | 500 us +- 25 us      |
| 85 | xml_etree_generate       | 145 ms +- 9 ms       | 147 ms +- 10 ms      | 145 ms +- 5 ms       |
| 86 | xml_etree_iterparse      | 148 ms +- 6 ms       | 147 ms +- 7 ms       | 143 ms +- 5 ms       |
| 87 | xml_etree_parse          | 207 ms +- 11 ms      | 205 ms +- 6 ms       | 200 ms +- 6 ms       |
| 88 | xml_etree_process        | 116 ms +- 9 ms       | 115 ms +- 5 ms       | 114 ms +- 6 ms       |

### 3.Calculation(UNIT: ms)
|     | Task                     | 3.8.0      | 3.8.1      | 3.8.2      |
|:----|:-------------------------|:-----------|:-----------|:-----------|
| 0   | 2to3                     | 496.0      | 498.0      | 491.0      |
| 1   | async_generators         | 563.0      | 564.0      | 557.0      |
| 2   | async_tree_cpu_io_mixed  | 1410.0     | 1410.0     | 1390.0     |
| 3   | async_tree_io            | 2530.0     | 2540.0     | 2530.0     |
| 4   | async_tree_memoization   | 1270.0     | 1280.0     | 1240.0     |
| 5   | async_tree_none          | 1040.0     | 1050.0     | 1040.0     |
| 6   | asyncio_tcp              | 1420.0     | 1400.0     | 1410.0     |
| 7   | asyncio_tcp_ssl          | 3450.0     | 3700.0     | 3280.0     |
| 8   | asyncio_websockets       | 629.0      | 624.0      | 630.0      |
| 9   | bench_mp_pool            | 11.6       | 12.0       | 11.8       |
| 10  | bench_thread_pool        | 1.83       | 1.8        | 1.81       |
| 11  | chameleon                | 15.1       | 14.9       | 15.0       |
| 12  | chaos                    | 179.0      | 181.0      | 180.0      |
| 13  | comprehensions           | 0.0405     | 0.0412     | 0.0407     |
| 14  | coroutines               | 61.0       | 60.4       | 59.7       |
| 15  | coverage                 | 72.0       | 73.3       | 71.7       |
| 16  | create_gc_cycles         | 1.79       | 1.78       | 1.78       |
| 17  | crypto_pyaes             | 167.0      | 165.0      | 166.0      |
| 18  | deepcopy                 | 0.692      | 0.702      | 0.696      |
| 19  | deepcopy_memo            | 0.0798     | 0.0804     | 0.0807     |
| 20  | deepcopy_reduce          | 0.0061     | 0.0062     | 0.0062     |
| 21  | deltablue                | 11.9       | 11.7       | 11.9       |
| 22  | docutils                 | 4270.0     | 4310.0     | 4210.0     |
| 23  | dulwich_log              | 116.0      | 115.0      | 118.0      |
| 24  | fannkuch                 | 659.0      | 661.0      | 663.0      |
| 25  | float                    | 179.0      | 178.0      | 176.0      |
| 26  | gc_traversal             | 4.71       | 4.77       | 4.67       |
| 27  | generators               | 94.3       | 93.7       | 95.5       |
| 28  | genshi_text              | 45.6       | 45.9       | 44.6       |
| 29  | genshi_xml               | 92.3       | 89.8       | 88.5       |
| 30  | go                       | 396.0      | 399.0      | 400.0      |
| 31  | hexiom                   | 15.5       | 15.8       | 15.5       |
| 32  | html5lib                 | 126.0      | 128.0      | 128.0      |
| 33  | json_dumps               | 19.5       | 19.5       | 19.5       |
| 34  | json_loads               | 0.0405     | 0.0397     | 0.0392     |
| 35  | logging_format           | 0.0146     | 0.0144     | 0.0147     |
| 36  | logging_silent           | 0.0003     | 0.0003     | 0.0003     |
| 37  | logging_simple           | 0.0132     | 0.0134     | 0.0134     |
| 38  | mako                     | 27.9       | 27.1       | 26.7       |
| 39  | mdp                      | 4410.0     | 4400.0     | 4350.0     |
| 40  | meteor_contest           | 147.0      | 145.0      | 146.0      |
| 41  | nbody                    | 197.0      | 187.0      | 200.0      |
| 42  | nqueens                  | 145.0      | 148.0      | 146.0      |
| 43  | pathlib                  | 39.3       | 38.8       | 36.9       |
| 44  | pickle                   | 0.0136     | 0.0138     | 0.014      |
| 45  | pickle_dict              | 0.0377     | 0.037      | 0.0378     |
| 46  | pickle_list              | 0.0056     | 0.0057     | 0.0056     |
| 47  | pickle_pure_python       | 0.743      | 0.744      | 0.737      |
| 48  | pidigits                 | 235.0      | 236.0      | 237.0      |
| 49  | pprint_pformat           | 2260.0     | 2250.0     | 2270.0     |
| 50  | pyflate                  | 1050.0     | 1050.0     | 1050.0     |
| 51  | python_startup           | 13.8       | 13.8       | 13.6       |
| 52  | python_startup_no_site   | 9.05       | 9.0        | 8.8        |
| 53  | raytrace                 | 839.0      | 831.0      | 822.0      |
| 54  | regex_compile            | 256.0      | 263.0      | 256.0      |
| 55  | regex_dna                | 237.0      | 234.0      | 232.0      |
| 56  | regex_effbot             | 3.93       | 4.01       | 3.75       |
| 57  | regex_v8                 | 32.0       | 31.2       | 31.5       |
| 58  | richards                 | 120.0      | 116.0      | 117.0      |
| 59  | richards_super           | 141.0      | 138.0      | 138.0      |
| 60  | scimark_fft              | 526.0      | 525.0      | 524.0      |
| 61  | scimark_lu               | 231.0      | 265.0      | 232.0      |
| 62  | scimark_monte_carlo      | 158.0      | 164.0      | 162.0      |
| 63  | scimark_sor              | 306.0      | 316.0      | 308.0      |
| 64  | scimark_sparse_mat_mult  | 6.29       | 6.48       | 6.51       |
| 65  | spectral_norm            | 203.0      | 203.0      | 204.0      |
| 66  | sqlalchemy_declarative   | 228.0      | 232.0      | 229.0      |
| 67  | sqlalchemy_imperative    | 32.4       | 33.0       | 32.3       |
| 68  | sqlglot_normalize        | 202.0      | 208.0      | 200.0      |
| 69  | sqlglot_optimize         | 95.2       | 99.5       | 95.0       |
| 70  | sqlglot_parse            | 3.32       | 3.44       | 3.45       |
| 71  | sqlglot_transpile        | 3.85       | 4.03       | 3.91       |
| 72  | sqlite_synth             | 0.0043     | 0.0042     | 0.0042     |
| 73  | sympy_expand             | 753.0      | 757.0      | 755.0      |
| 74  | sympy_integrate          | 34.0       | 34.4       | 33.5       |
| 75  | sympy_str                | 467.0      | 466.0      | 461.0      |
| 76  | sympy_sum                | 262.0      | 264.0      | 261.0      |
| 77  | telco                    | 9.57       | 9.37       | 9.08       |
| 78  | tomli_loads              | 4060.0     | 4100.0     | 4050.0     |
| 79  | tornado_http             | 229.0      | 227.0      | 220.0      |
| 80  | typing_runtime_protocols | 0.802      | 0.788      | 0.787      |
| 81  | unpack_sequence          | 0.0001     | 0.0001     | 0.0001     |
| 82  | unpickle                 | 0.0215     | 0.0209     | 0.0209     |
| 83  | unpickle_list            | 0.006      | 0.006      | 0.006      |
| 84  | unpickle_pure_python     | 0.496      | 0.5        | 0.5        |
| 85  | xml_etree_generate       | 145.0      | 147.0      | 145.0      |
| 86  | xml_etree_iterparse      | 148.0      | 147.0      | 143.0      |
| 87  | xml_etree_parse          | 207.0      | 205.0      | 200.0      |
| 88  | xml_etree_process        | 116.0      | 115.0      | 114.0      |
| SUM |                          | 37938.7568 | 38304.4973 | 37530.9638 |
| AVG |                          | 426.2782   | 430.3876   | 421.6962   |
| UP% |                          | 100.9640%  | 100.0000%  | 102.0611%  |


<div align=center>

[![IvanaXu/PythonVersions](https://gitee.com/IvanaXu/PythonVersions/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/IvanaXu/PythonVersions)

https://github.com/IvanaXu/PythonVersions

</div>
