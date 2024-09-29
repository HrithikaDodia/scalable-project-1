import tflite_runtime.interpreter as tflite
import os
import cv2
import numpy

interpreter = tflite.Interpreter(model_path='tflite_model.tflite')
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

for x in os.listdir('./example_captchas'):
    # load image and preprocess it
    raw_data = cv2.imread(os.path.join('./example_captchas', x))
    rgb_data = cv2.cvtColor(raw_data, cv2.COLOR_BGR2RGB)
    image = numpy.array(rgb_data) / 255.0
    (c, h, w) = image.shape
    image = image.reshape([-1, c, h, w])
    interpreter.set_tensor(input_details[0]['index'], image)
    # output_file.write(x + ", " + decode(captcha_symbols, prediction) + "\n")
    print(f"{x}: {tflite.get_tensor(output_details)}")