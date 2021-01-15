VERSION=$1

echo "******** Building API ********"
API=tradecalls/api:v${VERSION}
docker build -t ${API} -f Dockerfile.api .

echo "******** Building Frontend ********"
FRONTEND=tradecalls/frontend:v${VERSION}
docker build -t ${FRONTEND} -f Dockerfile.front .

echo "******** Building telegram ********"
TELEGRAM=tradecalls/telegram:v${VERSION}
docker build -t ${TELEGRAM} -f Dockerfile.telegram .