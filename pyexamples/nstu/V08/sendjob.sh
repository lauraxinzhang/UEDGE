#! /bin/bash

#SBATCH --job-name=ue
#SBATCH --partition=general
#SBATCH --ntasks=32
#SBATCH --time=48:00:00
#SBATCH --mail-user=xzhang@pppl.gov
#SBATCH --mail-type=ALL
#source

#cd /u/xzhang/ue_nstu
#bash --login
#conda activate uedge_dev
python runcase.py > outputV08.txt
