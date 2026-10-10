
apt update
apt install -y python3-venv
python3 -m venv a
source a/bin/activate

python -m pip install tqdm pandas tabulate
git config --global user.email "ivan@tangjt.cn"
git config --global user.name "ivan"

# version=3.8.0
# watch -n 1 -d "docker stats --no-stream && echo '' && tail -n 30 PythonVersions/Version/$version/py$version.log"
