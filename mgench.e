#! /bin/bash
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks=1
#SBATCH --time=0-0:20
#SBATCH --constraint="type_e"
module load CUDA/11.4
module load openmpi/4.1.2
module load gnu9/9.3

cd mgbench
./run.sh

tar -cvf type_b.result l*
