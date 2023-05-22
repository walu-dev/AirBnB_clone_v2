<<<<<<< HEAD
# The AirBnB Clone Project

## Project Description
This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

## Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object

## How to start it
These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

## Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/jzamora5/AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel



## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
=======
# AirBnB_clone
<p align=center>
<img src = "https://a0.muscache.com/airbnb/static/logos/belo-400x400.png" />
</p>


# <p align=center >`AirBnB clone - The console`</p>
## <p align=center> `Project's obejectives` </p>
Be able to explain:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## <p align=center> `First step: Write a command interpreter to manage your AirBnB objects.` </p>
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine (All your tests should be executed by using this command: python3 -m unittest discover tests)

## <p align=center> `What’s a command interpreter?` </p>
It’s exactly the same as the Shell, but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## <p align=center> `Resources` </p>
Read or watch:

- [cmd module](https://intranet.hbtn.io/rltoken/_mUwX-Mn69bDBP5iTQmCJA)
- [uuid module](https://intranet.hbtn.io/rltoken/4HNpF8nsTMociNaTgMYAeQ)
- [datetime](https://intranet.hbtn.io/rltoken/xnmMG0Qin2K9CxXdmQoZkA)
- [unittest module](https://intranet.hbtn.io/rltoken/MKNUT1FRSdUiGIpwMmrtgw)
- [args/kwargs](https://intranet.hbtn.io/rltoken/mY-8n8I-ohQIjkUOqcK6Rw)
- [Python test cheatsheet](https://intranet.hbtn.io/rltoken/9PsyQoeiVNhWGcj_1PkZJg)


## <p align=center> `Execution` </p>
The shell should work like this in interactive mode:
```bash
>>>>>>> 174ffdf755857fff6d47ed33321866a6c6e1c698
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

<<<<<<< HEAD
In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


```
=======
But also in non-interactive mode: (like the Shell project in C)
```bash
>>>>>>> 174ffdf755857fff6d47ed33321866a6c6e1c698
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<<<<<<< HEAD
## Format of Command Input

In order to give commands to the console, these will need to be piped through an echo in case of  **Non-interactive mode**.

In  **Interactive Mode**  the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the **CTRL + D** combination,  **CTRL + C**, or the command **quit** or **EOF**.

## Arguments

Most commands have several options or arguments that can be used when executing the program. In order for the Shell to recognize those parameters, the user must separate everything with spaces.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Author
Jonathan Walugembe

=======
## <p align=center>`Tasks`</p>
### <p align=center>`0. README, AUTHORS`</p>
- Write a README.md:
  - description of the project
  - description of the command interpreter:
    - how to start it
    - how to use it
    - examples
- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
- You should use branches and pull requests on GitHub - it will help you as team to organize your work
-------------------------------------------------------------------------------
### <p align=center>`1. Be pycodestyle compliant!`</p>
Write beautiful code that passes the pycodestyle checks.

-------------------------------------------------------------------------------
### <p align=center>`2. Unittests`</p>
All your files, classes, functions must be tested with unit tests

-------------------------------------------------------------------------------
### <p align=center>`3. BaseModel`</p>
Write a class BaseModel that defines all common attributes/methods for other classes:

- models/base_model.py
- Public instance attributes:
  - id: string - assign with an uuid when an instance is created:
    - you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
    - the goal is to have unique id for each BaseModel
  - created_at: datetime - assign with the current datetime when an instance is created
  - updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
- __str__: should print: [<class name>] (<self.id>) <self.__dict__>
- Public instance methods:
  - save(self): updates the public instance attribute updated_at with the current datetime
  - to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
    - by using self.__dict__, only instance attributes set will be returned
    - a key __class__ must be added to this dictionary with the class name of the object
    - created_at and updated_at must be converted to string object in ISO format:
      - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
      - you can use isoformat() of datetime object
    - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
-------------------------------------------------------------------------------
### <p align=center>`4. Create BaseModel from dictionary`</p>
Update models/base_model.py:

- __init__(self, *args, **kwargs):
  - you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
  - *args won’t be used
  - if kwargs is not empty:
    - each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
    - each value of this dictionary is the value of this attribute name
    - Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
  - otherwise:
    - create id and created_at as you did previously (new instance)
-------------------------------------------------------------------------------
### <p align=center>`5. Store first object`</p>
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

- models/engine/file_storage.py
- Private class attributes:
  - __file_path: string - path to the JSON file (ex: file.json)
  - __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
- Public instance methods:
  - all(self): returns the dictionary __objects
  - new(self, obj): sets in __objects the obj with key <obj class name>.id
  - save(self): serializes __objects to the JSON file (path: __file_path)
  - reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Update models/__init__.py: to create a unique FileStorage instance for your application

- import file_storage.py
- create the variable storage, an instance of FileStorage
- call reload() method on this variable
Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

- import the variable storage
- in the method save(self):
  - call save(self) method of storage
- __init__(self, *args, **kwargs):
  - if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
-------------------------------------------------------------------------------
### <p align=center>`6. Console 0.0.1`</p>
Write a program called console.py that contains the entry point of the command interpreter:

- You must use the module cmd
- Your class definition must be: class HBNBCommand(cmd.Cmd):
- Your command interpreter should implement:
  - quit and EOF to exit the program
  - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
  - a custom prompt: (hbnb)
  - an empty line + ENTER shouldn’t execute anything
- Your code should not be executed when imported

You should end your file with:
```bash
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
-------------------------------------------------------------------------------
### <p align=center>`7. Console 0.1`</p>
Update your command interpreter (console.py) to have these commands:

- create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
  - If the class name is missing, print ** class name missing ** (ex: $ create)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
- show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
  - If the class name is missing, print ** class name missing ** (ex: $ show)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
  - If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)
- destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
  - If the class name is missing, print ** class name missing ** (ex: $ destroy)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
  - If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)
- all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
  - The printed result must be a list of strings (like the example below)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
- update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
  - Usage: update <class name> <id> <attribute name> "<attribute value>"
  - Only one attribute can be updated at the time
  - You can assume the attribute name is valid (exists for this model)
  - The attribute value must be casted to the attribute type
  - If the class name is missing, print ** class name missing ** (ex: $ update)
  - If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
  - If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
  - If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)
  - If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
  - If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)
  - All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
  - id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
  - Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
-------------------------------------------------------------------------------
### <p align=center>`8. First User`</p>
Write a class User that inherits from BaseModel:

- models/user.py
- Public class attributes:
  - email: string - empty string
  - password: string - empty string
  - first_name: string - empty string
  - last_name: string - empty string
  - Update FileStorage to manage correctly serialization and deserialization of User.

Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.
-------------------------------------------------------------------------------
### <p align=center>`9. More classes!`</p>
Write all those classes that inherit from BaseModel:

- State (models/state.py):
  - Public class attributes:
    - name: string - empty string
- City (models/city.py):
  - Public class attributes:
    - state_id: string - empty string: it will be the State.id
    - name: string - empty string
- Amenity (models/amenity.py):
  - Public class attributes:
    - name: string - empty string
- Place (models/place.py):
  - Public class attributes:
    - city_id: string - empty string: it will be the City.id
    - user_id: string - empty string: it will be the User.id
    - name: string - empty string
    - description: string - empty string
    - number_rooms: integer - 0
    - number_bathrooms: integer - 0
    - max_guest: integer - 0
    - price_by_night: integer - 0
    - latitude: float - 0.0
    - longitude: float - 0.0
    - amenity_ids: list of string - empty list: it will be the list of Amenity.id later
- Review (models/review.py):
  - Public class attributes:
    - place_id: string - empty string: it will be the Place.id
    - user_id: string - empty string: it will be the User.id
    - text: string - empty string
-------------------------------------------------------------------------------
### <p align=center>`10. Console 1.0`</p>
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!

-------------------------------------------------------------------------------
>>>>>>> 174ffdf755857fff6d47ed33321866a6c6e1c698
