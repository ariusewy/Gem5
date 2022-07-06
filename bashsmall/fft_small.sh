cd ../
build/RISCV/gem5.opt --debug-flags=O3PipeView --debug-file=trace.out -d path/out/${APP}_${BNUM} configs/example/se.py \
-c /home/ywang/Benchmark/mibench_choosed/${APP}/${APP} \
-o "4 256 " \
--caches --l1i_size=${L1ISIZE} --l1i_assoc=${L1IASSOC} --l1d_size=${L1DSIZE} \
--l1d_assoc=${L1DASSOC} \
--l2cache --l2_size=${L2SIZE} --l2_assoc=${L2ASSOC} \
--cpu-type=boom  \
--reorder_buffer_entries=${ROBSIZE} --instruction_queue_entries=${IQSIZE} --issue_width=${ISSUEWIDTH} \
--nHistoryTables=4 --tagTableTagWidths ${TAGWIDTH} \
--logTagTableSizes ${LOGSIZE}

