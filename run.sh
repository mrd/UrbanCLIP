#!/bin/bash

IMAGE=urbanclip

docker run --gpus 1 --net=host -it --rm \
       -e XAUTHORITY=$HOME/.Xauthority \
       -e DISPLAY="$DISPLAY" \
       -v $PWD:/work \
       -v $PWD/.cache:/home/user/.cache \
       -v $PWD/.local:/home/user/.local \
       -v "$HOME":"$HOME":ro \
       -u `id -u`:`id -g` \
       "$IMAGE" $*
