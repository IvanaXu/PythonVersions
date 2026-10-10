
version=$1

apt update
apt install -y python3-venv

wget https://www.python.org/ftp/python/$version/Python-$version.tgz

tar -zxvf Python-$version.tgz
cd Python-$version
./configure
make && make install

python3 -V

python3 -m venv A
source A/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install pyperformance

rm -rf py$version.json
python3 -m pyperformance run -o py$version.json > /$version/py$version.log
