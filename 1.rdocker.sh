
basep=/home/WUYING_ivan_139307772273599/Desktop/PythonVersions/
regurl=python
ver=$1

cd $basep/Version
rm -rf $1
mkdir $1
cd ../docker/
ls -l

#
echo ----------------------------------------------
echo build
docker images
docker rm t$ver -f
docker rmi $regurl:$ver -f
docker build -t $regurl:$ver .
docker images

#
echo ----------------------------------------------
echo test images
docker run --name t$ver -v $basep/Version/$1:/$1 $regurl:$ver sh run.sh $1
docker ps -a
docker rm t$ver -f
docker ps -a

docker system prune --volumes -f
rm -rf $basep/Version/$1/venv
rm -rf $basep/Version/$1/dask-worker-space
touch $basep/Version/$1/py$1.log
