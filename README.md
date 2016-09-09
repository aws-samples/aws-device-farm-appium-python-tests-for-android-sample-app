# Appium Python Sample Tests for AWS Device Farm Sample Android App
This is a collection of sample Appium Python tests written for the AWS Device Farm [Android sample app](https://github.com/awslabs/aws-device-farm-sample-app-for-android). This test suite uses the [Appium page model](http://appium.io/slate/en/tutorial/android?java#page-object-pattern) to separate the tests from the page logic. You may use these tests as a starting reference for writing your own AWS Device Farm Appium Python Tests. 
Note: Your tests may be different than these and it is not a hard requirement that they exactly follow this model. This is an example for lookup.

## Getting Started - Installing Appium
### Using the Appium GUI
1. Download and install the Appium GUI. [[Windows Download]](https://bitbucket.org/appium/appium.app/downloads/AppiumForWindows_1_4_16_1.zip). [[OS X Download]](https://bitbucket.org/appium/appium.app/downloads/appium-1.4.13.dmg).

    **Currently, AWS Device Farm supports Appium version 1.4.16. Using a different version locally may cause unexpected results when running Appium tests on AWS Device Farm.**
    
    **Note:** It would be always helpful to check the AWS Forums for checking the latest supported version and to use the same version in the steps below.

2. Read the Appium GUI [documentation](http://appium.io/slate/en/v1.4.13/#appium-gui).

### Using the Appium CLI
1. Follow the **[official Appium getting started guide](http://appium.io/slate/en/tutorial/android.html?java#getting-started-with-appium)** and install the Appium server and dependencies.

    **Currently, AWS Device Farm supports Appium version 1.4.16. Using a different version locally may cause unexpected results when running Appium tests on AWS Device Farm.**

    **Note:** It would be always helpful to check the AWS Forums for checking the latest supported version and to use the same version in the steps below.
2. In order to use 1.4.16, download Appium through NPM with this command:

    ```
    $ npm install -g appium@1.4.16
    ```
    
3. Verify that you have Appium installed with this command:

    ```
    $ appium -v
    ```
    
   You should get "1.4.16" as the output

## Set up the Appium Python environment
1. We recommend setting up [Python's virtualenv](https://pypi.python.org/pypi/virtualenv) for developing and packaging tests so that unnecessary dependencies are not including in the bundled zip file.
2. Create your workspace and install py.test in your virtual environment. For example:

    ```
    $ virtualenv workspace
    $ cd workspace
    $ source bin/activate
    $ pip install pytest
    $ pip install Appium-Python-Client
    ```
    
3. Put all Python test scripts under a **tests/** folder in your workspace.

    ```
    - workspace
        └─ tests/ (tests go here)
    ```

## Running Your Tests Locally on Real Devices

### **Important Note**
Certain desired capabilities must be set when running locally. Refer to [BaseTest.java](./tests/tests/base_tests/base_test.py#L26-L32)

### Appium GUI
1. Start the Appium server.
    1. Click on the Android button.
    2. Set the "App Path", "Package", and "Device Name" and make sure their checkboxes are checked.
    3. Press the "Launch" button to start the Appium server locally.
2. Navigate into your workspace project directory in the terminal and activate the virtualenv.

    ```
    $ source bin/activate
    ```
    
3. Verify that your test cases are discoverable by the following command, which should be run from your workspace folder.

    ```
    $ py.test --collect-only tests/
    ```
    
4. Run your tests.

    ```
    $ py.test tests/
    ```

### Appium CLI
1. Start the Appium server.
    1. Make sure that you have followed all the steps in the [Appium getting started guide](http://appium.io/slate/en/tutorial/ios.html?java#getting-started-with-appium).
    2. Edit the [start-appium-android.sh](./start-appium-android.sh) script to include your app's absolute path and your device's UDID.
    3. Run [start-appium-android.sh](./start-appium-android.sh) to start the Appium server locally.
2. Navigate into your workspace project directory in the terminal and activate the virtualenv.

    ```
    $ source bin/activate
    ```
    
3. Verify that your test cases are discoverable by the following command, which should be run from your workspace folder.

    ```
    $ py.test --collect-only tests/
    ```
4. Run your tests.

    ```
    $ py.test tests/
    ```


### Running tests on AWS Device Farm
#### Step 1: Navigate into your workspace project directory and activate the virtualenv.

```
$ source bin/activate
```

#### Step 2: Package your tests.

```
$ ./package_tests.sh
```

#### Step 3: Upload to AWS Device Farm.
Follow these [instructions](http://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types-android-appium-python.html#test-types-android-appium-python-upload) and upload **test_bundle.zip** on Step 9.

