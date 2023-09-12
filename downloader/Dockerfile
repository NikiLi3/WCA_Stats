FROM debian

RUN apt-get update && apt-get install curl wget unzip -y jq

COPY script.sh ./

RUN chmod +x script.sh

CMD /script.sh