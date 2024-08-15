FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-devel
ENV DEBIAN_FRONTEND=noninteractive

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

RUN mkdir -p /work
RUN chown -R user:user /work # /yolo

# Allow password-less 'root' login with 'su'
RUN passwd -d root
RUN sed -i 's/nullok_secure/nullok/' /etc/pam.d/common-auth

USER user

RUN pip install -U transformers==4.36.2 gradio
RUN pip install -U scikit-learn pandas clip-by-openai

WORKDIR /work

RUN ln -s /work/.python_history /home/user/.python_history
RUN ln -s /work/.bash_history /home/user/.bash_history

CMD /bin/bash
