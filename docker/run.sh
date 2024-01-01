
version=$1
wget https://www.python.org/ftp/python/$version/Python-$version.tgz

tar -zxvf Python-$version.tgz
cd Python-$version
./configure
make && make install

cd /$1
python3 -V
pip3 -V

pip3 install pyperformance -i https://pypi.tuna.tsinghua.edu.cn/simple
rm -rf py$version.json
pyperformance run -o py$version.json > /$version/py$version.log
