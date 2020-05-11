#! /bin/bash
#
#PBS -A "yu_group"
#PBS -l walltime=flag1
#PBS -l nodes=flag2:ppn=flag3
#PBS -W group_list="newriver"
#PBS -q flag4
#PBS -j oe
#PBS -N flag5
#PBS -M knightkp@vt.edu
#PBS -m bea
#
cd flag6
#
module purge
module load ls-dyna-smp/11.0.0
#
# Define environment variables for license server.
#
export LSTC_LICENSE=network
export LSTC_LICENSE_SERVER="128.173.241.107:31010"
#
$LSDYNA_SMP_BIN/ls-dyna_smp_d_R11_1_0_x64_redhat65_ifort160_sse2 i = flag7 > flag8
if [ $? -ne 0 ]; then
  echo "LS-DYNA_NEWRIVER: Run error!"
  exit 1
fi
#
echo "LS-DYNA_NEWRIVER: Normal end of execution."
exit 0
