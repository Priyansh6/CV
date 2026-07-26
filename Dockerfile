FROM alpine:3.21

RUN apk add --no-cache \
    tectonic poppler-utils font-dejavu

WORKDIR /data
VOLUME ["/data"]
