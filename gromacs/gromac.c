#! /bin/bash
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks=1
#SBATCH --time=0-0:30
#SBATCH --constraint="type_c"
module load CUDA/11.4
module load GROMACS/2019.6
module load gnu9/9.3

srun gmx_mpi mdrun -v -ntomp 1 -s /opt/software/gromacs/examples/benchmark/1400k-atoms/benchmark.tpr
