# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app

COPY ./vue-project/package*.json .
RUN npm install

COPY ./vue-project .
# RUN npm run build

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]