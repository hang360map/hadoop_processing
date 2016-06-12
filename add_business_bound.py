#!/bin/bash
JOB_NAME="zhuhang-xy_add_business_bound"
INPUT="/home/hdp-map/output/hbase/spider_data_poi/stream-scan-spider_data_poi-dump-poi-2016-06-07/"
#INPUT="/home/hdp-map/zhuhang/test"
BOUND="/home/hdp-map/zhuhang/business_bound.dict"
OUTPUT="/home/hdp-map/zhuhang/business_bound1"
hadoop fs -rmr ${OUTPUT}
hadoop streaming \
-D mapred.job.name="${JOB_NAME}" \
-D mapred.reduce.tasks=40 \
-input ${INPUT} \
-output ${OUTPUT} \
-file business_bound.dict \
-file mapper.py \
-file reducer.py \
-mapper "python26 mapper.py" \
-reducer "python26 reducer.py" \
