VERSION=$1

echo "******** Building API ********"
API=marcosfelipp/trade-calls-api:v${VERSION}
docker build -t ${API} -f Dockerfile.api .
docker push ${API}

echo "******** Building Frontend ********"
FRONTEND=tradecalls/frontend:v${VERSION}
docker build -t ${FRONTEND} -f Dockerfile.front .

echo "******** Building telegram ********"
TELEGRAM=tradecalls/telegram:v${VERSION}
docker build -t ${TELEGRAM} -f Dockerfile.telegram .