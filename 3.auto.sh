
apt update
apt install -y python3-venv
python3 -m venv a
source a/bin/activate

python -m pip install tqdm pandas tabulate
git config --global user.email "ivan@tangjt.cn"
git config --global user.name "ivan"

# nohup python3 3.auto.py > 3.auto.log &
# watch -n 1 -d "docker stats --no-stream && echo '---' && tail -n 15 3.auto.log && echo '---' && tail -n 30 Version/*/py*.log"
