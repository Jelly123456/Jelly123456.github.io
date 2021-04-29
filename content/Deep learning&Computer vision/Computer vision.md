title: Other things about computer vision
date: 16-Feb-2021
author: YiLi

# Command list

* Training command with multiple GPU

* `python -m torch.distributed.launch --nproc_per_node 2 train.py --batch-size 64 --data data/Allcls_one.yaml --weights weights/yolov5l.pt --cfg models/yolov5l_1cls.yaml --epochs 1 --device 0,1`
* Training command with single GPU

  `python train.py --batch-size 32 --data data/Allcls_one.yaml --weights weights/yolov5l.pt --cfg models/yolov5l_1cls.yaml --epochs 1 --device 0`

# Problems faced so far during training

* A picture with JPG is recognised as MPO?
* Data pre-prcessing
  * Missing lables
  * Corrupted images
  * Leble files are empty
* Multi GPU training problem
  *
