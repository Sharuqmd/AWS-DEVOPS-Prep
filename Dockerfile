FROM openjdk:17-jdk-alpine
WORKDIR /app
COPY target/medicure-0.0.1-SNAPSHOT.jar /app/medicare.jar
EXPOSE 8082
CMD ['java' '-jar' 'medicare.jar']