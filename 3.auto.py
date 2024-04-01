import os
import time
from tqdm import tqdm

for ver in tqdm([
    # '3.8.0', 
    # '3.8.1', 
    # '3.8.2', 
    # '3.8.3', 
    # '3.8.4', 
    # '3.8.5', 
    # '3.8.6', 
    # '3.8.7', 
    # '3.8.8', 
    # '3.8.9', 
    # '3.8.10', 
    # '3.8.11', 
    # '3.8.12', 
    # '3.8.13', 
    # '3.8.14', 
    # '3.8.15', 
    # '3.8.16', 
    # '3.8.17', 
    # '3.8.18', 
    '3.8.19',

    # '3.9.0', 
    # '3.9.1', 
    # '3.9.2', 
    # '3.9.3', 
    # '3.9.4', 
    # '3.9.5', 
    # '3.9.6', 
    # '3.9.7', 
    # '3.9.8', 
    # '3.9.9', 
    # '3.9.10', 
    # '3.9.11', 
    # '3.9.12', 
    # '3.9.13', 
    # '3.9.14', 
    # '3.9.15', 
    # '3.9.16', 
    # '3.9.17', 
    # '3.9.18', 
    # '3.9.19', 

    # '3.10.0', 
    # '3.10.1', 
    # '3.10.2', 
    # '3.10.3', 
    # '3.10.4', 
    # '3.10.5', 
    # '3.10.6', 
    # '3.10.7', 
    # '3.10.8', 
    # '3.10.9', 
    # '3.10.10',
    # '3.10.11', 
    # '3.10.12', 
    # '3.10.13',
    # "3.10.14",

    # '3.11.0', 
    # '3.11.1', 
    # '3.11.2', 
    # '3.11.3', 
    # '3.11.4', 
    # '3.11.5', 
    # '3.11.6', 
    # '3.11.7', 
    
    # '3.12.0', 
    # '3.12.1',
]):
    print(f"\n\n\n\n{'-'*100}\n{ver} WAIT...")
    # time.sleep(60)
    # os.system(f"""time sh 1.rdocker.sh {ver}""")
    os.system(f"""python3 2.compare.py && git add * && git commit -m "#28 {ver}" && git push""")
