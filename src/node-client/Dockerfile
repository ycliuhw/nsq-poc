FROM node:8.6.0

MAINTAINER ycliuhw@gmail.com

WORKDIR /opt/app/
ADD package.json /opt/app/package.json
ADD index.js /opt/app/index.js

# Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm i --production && npm cache clear --force

CMD ["node", "/opt/app/index.js"]
