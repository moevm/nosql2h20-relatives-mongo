FROM python:3

RUN mkdir backend && cd backend/ && mkdir src/
ADD src/collection_manager.py ./backend/src
ADD src/database.py ./backend/src
ADD src/dynasty.py ./backend/src
ADD src/network.py ./backend/src
ADD src/person.py ./backend/src
ADD src/routing.py ./backend/src

RUN pip3 install pymongo
RUN pip3 install bottle

CMD python3 /backend/src/routing.py

