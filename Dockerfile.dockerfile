FROM  nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04

# 環境変数の設定
ENV NOTO_DIR /usr/share/fonts/opentype/notosans

# 必要なパッケージのインストール
RUN apt update \
  && apt install -y \
  wget \
  bzip2 \
  git \
  curl \
  unzip \
  file \
  xz-utils \
  sudo \
  python3 \
  python3-pip

# Noto Sans CJK JPフォントのインストール
RUN mkdir -p ${NOTO_DIR} &&\
  wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O noto.zip &&\
  unzip ./noto.zip -d ${NOTO_DIR}/ &&\
  chmod a+r ${NOTO_DIR}/NotoSans* &&\
  rm ./noto.zip

# 一時ファイルのクリーンアップ
RUN apt-get autoremove -y && apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# requirements.txtとkaggle.jsonのコピー
COPY requirements.txt /tmp/
COPY .kaggle/kaggle.json /root/.kaggle/

# Pythonパッケージのインストール
RUN pip install --no-cache-dir -U pip setuptools wheel && \
  pip install --no-cache-dir -r /tmp/requirements.txt

# Kaggle APIの認証ファイルのパーミッション設定
RUN chmod 600 /root/.kaggle/kaggle.json
