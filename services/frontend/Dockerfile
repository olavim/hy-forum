FROM node:10-alpine

WORKDIR /usr/src/app

COPY ./ ./

RUN yarn install
RUN yarn build
RUN yarn cache clean

EXPOSE 80

CMD ["node", "dist/index.js"]