#!/bin/bash

python compress_graph.py

python split_seeds.py

CUDA_VISIBLE_DEVICES=0,1 python train_rgnn_multi_gpu.py --model='rgat' --layout='CSC' --use_fp16