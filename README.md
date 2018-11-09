Monitoring data is recorded by the manufacturing equipment itself using an embedded PC and a set of sensors. The data is recorded with 100Hz frequency. However, it is possible that the time between two consecutive data points differs significantly from 10ms. The data is available as a flat CSV file, with each line representing a single event (data point). 




# RUN KAFKA CLUSTER

docker-compose up -d

# RUN DEBS 2012 Kafka Generator

 docker run --network ksql-workshop_default --rm -v `pwd`/streaming-data.avro:/streaming-data.avro  \
    confluentinc/ksql-examples:5.0.0 \
    ksql-datagen \
        bootstrap-server=kafka:29092 \
        schemaRegistryUrl=ksql-schema-registry:8081 \
        schema=/streaming-data.avro \
        format=json \
        key=date \
        topic=debs12 \
        maxInterval=500 

NB: schema streaming-data.avro only generates data for the used part of the debs 2012 schema.

# RUN KSQL

docker run --network ksql-workshop_default --tty --interactive --rm confluentinc/cp-ksql-cli:5.0.0 http://ksql-server:8088

 SET 'auto.offset.reset'='earliest';
 CREATE STREAM CDATAS ( timestamp VARCHAR, index BIGINT, mf01 INT, mf02 INT, mf03 INT, pc13 INT, pc14 INT, pc15 INT,pc25 INT, pc26 INT, pc27 INT, res INT, bm05  INT, bm06  INT, bm07  INT, bm08  INT, bm09  INT, bm10  INT,pp01  INT, pp02  INT, pp03  INT, pp04  INT, pp05  INT, pp06  INT, pp07  INT, pp08  INT, pp09  INT, pp10  INT, pp11  INT, pp12  INT, pp13  INT, pp14  INT, pp15  INT, pp16  INT, pp17  INT, pp18  INT, pp19  INT, pp20  INT, pp21  INT, pp22  INT, pp23  INT, pp24  INT, pp25  INT, pp26  INT, pp27  INT, pp28  INT, pp29  INT, pp30  INT, pp31  INT, pp32  INT, pp33  INT, pp34  INT, pp35  INT, pp36  INT, pc01  INT, pc02  INT) WITH (KAFKA_TOPIC='cdata', VALUE_FORMAT='DELIMITED', TIMESAMP = 'timestamp');


