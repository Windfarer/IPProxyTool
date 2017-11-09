FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN pip install -i https://mirrors.aliyun.com/pypi/simple gevent gunicorn
RUN pip install -i https://mirrors.aliyun.com/pypi/simple scrapy
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
CMD python ipproxytool.py