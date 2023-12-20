
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
pyperformance run -o py$version.json

# Try to rerun the benchmark with more runs, values and/or loops.
# Run 'python -m pyperf system tune' command to reduce the system jitter.
# Use pyperf stats, pyperf dump and pyperf hist to analyze results.
# Use --quiet option to hide these warnings.

# https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors
# sudo mkdir -p /etc/docker
# sudo tee /etc/docker/daemon.json <<-'EOF'
# {
#   "registry-mirrors": ["https://xxxxxx.mirror.aliyuncs.com"]
# }
# EOF
# sudo systemctl daemon-reload
# sudo systemctl restart docker
