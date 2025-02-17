# 0x04. AirBnB clone - Web framework

A web framework is a software framework that is designed to support the development of web applications including web services, web resources and web APIs.

In this project, I learnt how to use Flask which is a server-side web framework.

## Tasks

**0. Hello Flask!**: [0-hello_route.py](./0-hello_route.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
- You must use the option strict_slashes=False in your route definition

**1.HBNB**: [1-hbnb_route.py](./1-hbnb_route.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition

**2.C is fun!**: [2-c_route.py](./2-c_route.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option strict_slashes=False in your route definition

**3. Python is cool!**: [3-python_route.py](./3-python_route.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _symbols with a space )
  - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore_ symbols with a space )
    - The default value of text is “is cool”
- You must use the option strict_slashes=False in your route definition

**4. Is it a number?**:[4-number_route.py](./4-number_route.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _symbols with a space )
  - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore_ symbols with a space )
    - The default value of text is “is cool”
  - /number/<n>: display “n is a number” only if n is an integer
- You must use the option strict_slashes=False in your route definition

**5. Number template**: [5-number_template.py](./5-number_template.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _symbols with a space )
  - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore_ symbols with a space )
    - The default value of text is “is cool”
  - /number/<n>: display “n is a number” only if n is an integer
  - /number_template/<n>: display a HTML page only if n is an integer:
    - H1 tag: “Number: n” inside the tag BODY
- You must use the option strict_slashes=False in your route definition

**6.Odd or even?**: [6-number_odd_or_even.py](./6-number_odd_or_even.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
  - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _symbols with a space )
  - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore_ symbols with a space )
    - The default value of text is “is cool”
  - /number/<n>: display “n is a number” only if n is an integer
  - /number_template/<n>: display a HTML page only if n is an integer:
    - H1 tag: “Number: n” inside the tag BODY
  - /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    - H1 tag: “Number: n is even|odd” inside the tag BODY
- You must use the option strict_slashes=False in your route definition

**7.Improve engines**

Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update FileStorage: (models/engine/file_storage.py)

- Add a public method def close(self):: call reload() method for deserializing the JSON file to objects
Update DBStorage: (models/engine/db_storage.py)

- Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips
Update State: (models/state.py) - If it’s not already present

- If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State

**8.List of states**: [7-states_list.py](./7-states_list.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
- Routes:
  - /states_list: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
      - LI tag: description of one State: <state.id>: <B><state.name></B>
- Import this 7-dump to have some data
- You must use the option strict_slashes=False in your route definition

**9.Cities by states**: [8-cities_by_states.py](./8-cities_by_states.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- To load all cities of a State:
  - If your storage engine is DBStorage, you must use cities relationship
  - Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
- Routes:
  - /cities_by_states: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
      - LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
      - LI tag: description of one City: <city.id>: <B><city.name></B>
- Import this 7-dump to have some data
- You must use the option strict_slashes=False in your route definition

**10. States and State**: [9-states.py](./9-states.py)

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- To load all cities of a State:
  - If your storage engine is DBStorage, you must use cities relationship
  - Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
- Routes:
  - /states: display a HTML page: (inside the tag BODY)
    - H1 tag: “States”
    - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
      - LI tag: description of one State: <state.id>: <B><state.name></B>
  - /states/<id>: display a HTML page: (inside the tag BODY)
    - If a State object is found with this id:
      - H1 tag: “State: ”
      - H3 tag: “Cities:”
      - UL tag: with the list of City objects linked to the State sorted by name (A->Z)
        - LI tag: description of one City: <city.id>: <B><city.name></B>
    - Otherwise:
      - H1 tag: “Not found!”
- You must use the option strict_slashes=False in your route definition
- Import this 7-dump to have some data

