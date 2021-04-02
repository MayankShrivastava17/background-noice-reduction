import gradio as gr
import numpy as np
import cv2 as cv 

def backgroundNoiceReduction(image, h, color_components, template_window_size, search_window_size):
    result = cv.fastNlMeansDenoisingColored(image, None, h, color_components, template_window_size, search_window_size)
    return result

tit = "Background Noice Reduction"
des = "Welcome to background noice reduction using opencv and python, \n This using opencv library \"fastNlMeansDenoisingColored\". \n The parameters used are \n h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok) \n hForColorComponents : same as h, but for color images only. (normally same as h) \n templateWindowSize : should be odd. (recommended 7) \n searchWindowSize : should be odd. (recommended 21)"

iface = gr.Interface(fn = backgroundNoiceReduction, inputs = [gr.inputs.Image(shape = (200, 200)), gr.inputs.Slider(0, 100, 1, 3), gr.inputs.Slider(0, 100, 1, 3), gr.inputs.Slider(1, 100, 2, 7), gr.inputs.Slider(1, 100, 2, 21)], outputs = "image", title = tit, description = des)

iface.launch(share = True)