FROM openjdk:17-jdk-alpine
WORKDIR /app
COPY target/myapp.jar /app/myapp.jar
EXPOSE 8082
CMD ['java' '-jar' '']