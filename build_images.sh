VERSION=$1

echo "******** Building API ********"
API=marcosfelipp/trade-calls-api:v${VERSION}
docker build -t ${API} -f Dockerfile.api .
docker push ${API}

echo "******** Building Frontend ********"
FRONTEND=marcosfelipp/trade-calls-frontend:v${VERSION}
docker build -t ${FRONTEND} -f Dockerfile.front .
docker push ${FRONTEND}

echo "******** Building telegram ********"
TELEGRAM=marcosfelipp/trade-calls-telegram-notifications:v${VERSION}
docker build -t ${TELEGRAM} -f Dockerfile.telegram .
docker push ${TELEGRAM}