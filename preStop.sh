#!/bin/bash

echo "################"  >  /proc/1/fd/1
echo `date`" preStop: Activating sleep 20s" >  /proc/1/fd/1
export START=$(date +%s)
for i in {1..20}; do export STOP=$(date +%s); DIFF=$(expr $STOP - $START); echo "Sleeping $DIFF sec"  > /proc/1/fd/1; sleep 1; done
STOP=$(date +%s)
DIFF=$(expr $STOP - $START)
echo "Total $DIFF sec"  > /proc/1/fd/1

echo "################"  >  /proc/1/fd/1
