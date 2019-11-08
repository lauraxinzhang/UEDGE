#! /bin/bash

#SBATCH --job-name=ue
#SBATCH --partition=general
#SBATCH --ntasks=32
#SBATCH --time=48:00:00
#SBATCH --mail-user=xzhang@pppl.gov
#SBATCH --mail-type=END
#source

python runcase.py > outputV12.txt
