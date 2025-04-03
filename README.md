# Updated-Python-3.12-Ultralytics-PyTorch-To-TensorFlow-Lite-Converter
This code is an updated version of the Ultralytics PyTorch to Tensorflow Lite converter. This repo contains a .yaml file with all the needed updated dependencies and minor updates to Ultralytics source code. Bellow is instructions on how to use.

# Converting To TFLITE
## Step 1: Setup Python File: 
To start, set up the python code file in your IDE of choice. Git clone the code from this repository. Once you have done that, open the newly downloaded “obj_vision” folder. There you should see a file structure similar to this. Don’t worry if you are missing a few files, they will be generated when you run the code.

## Step 2: Setup Dependencies:
In this file is a .yaml file for a virtual environment that contains all the necessary updated dependencies for the converter to run. The default Ultralytics PyTorch to Tensorflow Lite converter is deprecated and this file is needed to run the program. The virtual environment used in this code was MiniConda, however you may be able to use any virtual environment as long as you follow the specifications in the .yaml file exactly. This is because some changes have been made to the source code for updating to python 3.12. Below are the .yaml file specifications.  

```python
name: obj_vision
channels:
  - defaults
dependencies:
  - python=3.12  # Allows Python 3.12
  - pip
  - pip:
    - tf_keras
    - tensorflow
    - ultralytics
    - onnx
    - onnx-tf
    - onnx2tf>1.17.5,<=1.26.3
    - onnxslim>=0.1.31
    - tflite.support
    - onnxruntime
    - tflite-support
```
## Step 3: Convert Desired Model:
Next, you are mostly likely going to need to update a few files in the code in order for the converter to work. To do this we are going to run the python file a few times. Run the file and then click on the error link, this should take you to one of the files. Do a control+f search and make the necessary changes depending on the error you got. This is a little trial and error but it should be one of these two issues. When you make the changes run the file again and click the error link. Make the necessary changes again. Once both files have had their changes the program should now work. If it does not there may be more files that need manual updating, however all dependencies are in the .yaml file and no other imports should be needed. To make more changes, repeat this process until the program works.

Fix 1: Importlib as imp.
```python
import sys
import importlib as imp
```

Fix 2: Find module fix.
```python
try :
     imp. util. find _ spec ( " numpy" )
     numpy exists = True
except ImportError:
```

## Step 4: Convert Desired Model:
When you are ready to convert your model. Drag and drop the model into the file tree or move it through the command line into the “obj_detection” folder. Next you need to open the file “yolo_to_tflite.py” and set the file path to your model in the code. The easiest way to do this is to right click on your model file in your file explorer and paste it into the code where it says, “Path to your model file.” 

```python
from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO(r"Path to your model file")

# Export the model to TFLite format
model.export(format="tflite")  # creates 'yolo11n_float32.tflite'
```

Once you’ve done that, activate your virtual environment if it isn’t already and run the file. Once it is done you should see a few files that have been generated. It should look something like this.
These should be all the files you need. There should be a couple of different file formats for the model output such as .onnx and different float types. The metadata should also be there as well.
