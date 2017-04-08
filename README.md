# NexposeParser

<a href="https://raw.githubusercontent.com/jhalon/jhalon.github.io/master/images/nexpose_parse.png"><img src="https://raw.githubusercontent.com/jhalon/jhalon.github.io/master/images/nexpose_parse.png"></a>

## What is NexposeParser?

NexposeParser was a tool created in Python aimed at supporting a Vulnerability Management Program. 

The purpose of the tool was simple; parse the Nexpose Scans and identify missing Asset Names and Asset Owners providing the Security Team a list of devices that needed to be identified.

## Why do you need to identify the Asset Name or Owner?

By identifying the Asset Name and Owner the Security Team was able to quickly asses who was responsible for system patching and vulnerability mitigations on the specified system.

Having a list of unidentified devices allowed IT Security to submit the list to the Network Infrastructure team to properly identify and tag the machines, which later was used to update Nexpose.

## Install:

You can install NexposeParse by cloning this Git Repository

```console
$ git https://github.com/jhalon/NexposeParse.git
```

## Usage:

```console
NeXpose Parser - A Quick Python Script to Parse NeXpose Scans
-------------------------------------------------------------

Usage Information:
Step 1: Enter the .cvs file name of the NeXpose Scan
Step 2: Select one of the following parse options:
         - 1: Print out all Asset Names that don't have an Asset Owner
         - 2: Print out all Asset IP's that don't have an Asset Name
         - 3: Print out all Asset IP's that don't have an Asset Name or Asset Owner
Step 3: Enter a name for the output file
Step 4: Wait for the parse to complete
Step 5: Done!
```

You can use NexposeParser both on Windows and Linux. You have an option of just running the Python Script, or, if you already want a prepackaged application, you can download the __dist__ folder which contains a __x64__ executable for Windows.

I will also include a __setup.py__ file which is used to package the python program into an executable file.

#### For Linux:

```console
$ ./nexpose_parse.py
```

#### For Windows:

```console
C:\Users\UserName\Desktop\dist\nexpose_parse.exe
```

## Requirements:

Since this was created using Python v2.7.13 it will not be compatible with Python v3.x.

* Python v2.7.13 - [Download](https://www.python.org/downloads/release/python-2713/)

If you want to utilize the __setup.py__ file to package the application you will need to download __py2exe__. 

* py2exe v0.6.9 - [Download](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

## Bugs?

* Please Submit a new Issue
* Submit a Pull Request
* Contact me

## License:

NexposeParser is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), follow clarification in the [License File](https://github.com/jhalon/NexposeParse/blob/master/LICENSE).
