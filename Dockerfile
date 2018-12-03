FROM continuumio/miniconda3

COPY pytorch-CycleGAN-and-pix2pix/requirements.txt .
RUN pip install -r requirements.txt

RUN conda install -c conda-forge rise

RUN pip install matplotlib imageio

EXPOSE 8888

CMD jupyter notebook --ip='0.0.0.0' --log-level 'DEBUG' --allow-root
