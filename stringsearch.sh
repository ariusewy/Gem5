build/RISCV/gem5.opt --stats-file=${APP}_${BNUM}.txt \
--dump-config=${APP}_${BNUM}.ini configs/example/se.py \
-c /home/ywang/Benchmark/mibench_choosed/${APP}/search_large \
--caches --l1i_size=${L1ISIZE} --l1i_assoc=${L1IASSOC} --l1d_size=${L1DSIZE} \
--l1d_assoc=${L1DASSOC} --cacheline_size=${CACHELINE} \
--l2cache --l2_size=${L2SIZE} --l2_assoc=${L2ASSOC} \
--cpu-type=boom  \
--branch_history_size=${BSIZE} 
