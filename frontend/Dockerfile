FROM node:22.12-alpine

WORKDIR /project

COPY ./source/package*.json ./source/

WORKDIR /project/source

RUN npm install

COPY ./source .

RUN npm run build

CMD ["npm", "start"]