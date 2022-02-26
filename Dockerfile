FROM python:3.8

ADD . /workdir
WORKDIR /workdir

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements/common.txt -r requirements/deployment.txt
RUN python3 manage.py collectstatic

EXPOSE 8000
CMD ["gunicorn", "-b", ":8000", "meals.wsgi"]
