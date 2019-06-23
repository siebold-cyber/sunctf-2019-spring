FROM node:lts-alpine

COPY /src /app/src
COPY .env /app
COPY package.json /app

WORKDIR /app

RUN npm install

CMD [ "npm","start" ]
