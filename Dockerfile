FROM amazoncorretto:21

WORKDIR /JAVA_SELF_TRAINING

#COPY ./Main.java ./Main.java

#RUN javac ./Main.java


ENTRYPOINT [ "javac" ]