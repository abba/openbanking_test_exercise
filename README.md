
## Requirements
install python version 3 - can download from here https://www.python.org/downloads/

would also require `pip3` but this is distributed with python version 3

### Libraries

These are declared in requirements.txt

+ Flask version version 0.12.2
+ requests version 2.18.4
+ pytest version 3.5.0

### To Run Tests

#### Create and activate virtual environment - (OPTIONAL BUT ADVISED)
1. make a virtual environment (folder name - venv)
    ```
    python3 -m venv ./venv
    ```

    A new folder ```venv``` should be create

2. activate virtual environment
    ```
    source venv/bin/activate
    ```
    *NOTE: I have not tested this on other linux distributions just OSX.*

    If activation is successful (venv) should be appended to new line on terminal

3. To deactivate virtual environment run
    ```
    deactivate
    ```

#### Install dependencies
*NOTE: if you opt to not use virtual environment the dependencies will be installed globally*

Run the below command
```
pip3 install -r requirements.txt
```


#### Run tests
I have added some make tasks to ease the running of the tests and starting stopping of server easier

to run the tests
```
make test
```

*NOTE: the test command will start the server up and run the tests*

#### To stop the server
```
make stop_server
```


