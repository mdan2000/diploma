#! /bin/bash
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks=1
#SBATCH --time=0-4:00
#SBATCH --constraint="type_b"
module load CUDA/11.4
module load openmpi/4.1.2
module load gnu9/9.3
module load INTEL/parallel_studio_xe_2020_u4_ce

cd graph500/src
TMPFILE=my_graph.txt REUSEFILE=1 ./graph500_reference_bfs 200
