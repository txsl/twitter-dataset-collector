#!/bin/sh

mvn clean compile assembly:single

javac -classpath "target/twitter-dataset-collector-0.1-SNAPSHOT-jar-with-dependencies.jar" run.java

