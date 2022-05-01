FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /dincolo-job-portal

RUN python3 -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /dincolo-job-app/
RUN pip install -r requirements.txt
COPY . /dincolo-job-app/
