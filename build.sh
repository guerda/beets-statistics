IMAGE_VERSION=`uv version --short`
docker build -t "guerda/beets-statistics:${IMAGE_VERSION}" . 
