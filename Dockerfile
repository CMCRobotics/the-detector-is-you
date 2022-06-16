FROM node:14-alpine3.13

RUN apk add --update nodejs npm

RUN mkdir /home/node/app && chown -R node:node /home/node/app

WORKDIR /home/node/app

# Cache node modules first
COPY --chown=node:node package*.json ./

USER node

RUN npm install --only=prod

COPY --chown=node:node . .

RUN npm run build

CMD ["npm","start"]