
apt update
apt install -y python3-venv
python3 -m venv a
source a/bin/activate

python -m pip install tqdm pandas tabulate
git config --global user.email "ivan@tangjt.cn"
git config --global user.name "ivan"

# watch -n 2 -d "docker stats --no-stream && tail -n 20 py3.12.3.log"
