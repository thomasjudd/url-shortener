FROM python:3.7
RUN python -m pip install autopep8==1.5.7
RUN python -m pip install click==8.0.1
RUN python -m pip install Flask==2.0.1
RUN python -m pip install Flask-WTF==0.15.1
RUN python -m pip install importlib-metadata==4.6.4
RUN python -m pip install itsdangerous==2.0.1
RUN python -m pip install Jinja2==3.0.1
RUN python -m pip install MarkupSafe==2.0.1
RUN python -m pip install pycodestyle==2.7.0
RUN python -m pip install toml==0.10.2
RUN python -m pip install typing-extensions==3.10.0.0
RUN python -m pip install Werkzeug==2.0.1
RUN python -m pip install WTForms==2.3.3
RUN python -m pip install zipp==3.5.0

COPY ./*  /app/

EXPOSE 80

WORKDIR /app/

ENTRYPOINT [ "python", "app.py" ]
