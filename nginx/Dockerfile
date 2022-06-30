FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN service nginx reload
ENTRYPOINT ["nginx", "-g", "daemon off;"]
