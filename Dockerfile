FROM continuumio/miniconda:latest

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

ENV PATH /opt/conda/envs/meu_ambiente/bin:$PATH

COPY . .

EXPOSE 5000

CMD ["python", "main.py", "--ui", "flask"]