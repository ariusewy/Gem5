#!/usr/bin/env bash
APPDIR=/home/ywang/Benchmark/mibench_choosed/
SRCDIRS="bitcount
         qsort  
         stringsearch
         rijndael 
         sha
         fft"
export CONFIG = --caches --l1i_size=16kB --l1i_assoc=4 --l1d_size=32kB --l1d_assoc=2 --cacheline_size=64 --l2cache --l2_size=512kB --l2_assoc=8 --cpu-type=boom 
CURRDIR=$(pwd)
for d in ${SRCDIRS}
do
    echo ${d}
    ./${d}.sh
    cd ${CURRDIR}
done