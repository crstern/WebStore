# syntax=docker/dockerfile:1
FROM node:18-alpine
# set working directory
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN apk add bash
RUN apk add curl

RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent

# start app
CMD ["npm", "start"]