#!/bin/sh

mvn clean compile assembly:single

mv target/twitter-dataset-collector-0.1-SNAPSHOT-jar-with-dependencies.jar target/dependencies.jar

javac -classpath "target/dependencies.jar" run.java

