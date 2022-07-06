cd ../
./build/RISCV/gem5.opt \
--debug-flags=Branch --debug-file=branch.out \
-d path/out/visiualization configs/example/se.py \
--caches --l2cache --cpu-type=boom \
-c /home/ywang/Benchmark/mibench_choosed/fft/fft \
-o "4 32 " \
--l1d_size='16kB' --l1i_size='16kB' \
--l2_size='128kB' --l1d_assoc=8 \
--l1i_assoc=8 --l2_assoc=8 \
# --num-cpus=1 --sys-clock='2.2GHz' \