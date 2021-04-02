# background-noice-reduction
Welcome to background noice reduction using [OpenCV](https://opencv.org/) and [python](https://www.python.org/).
This using opencv library [`fastNlMeansDenoisingColored`](https://docs.opencv.org/master/d1/d79/group__photo__denoise.html). 

## The parameters used

- *h* : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok) 
- *hForColorComponents*: same as h, but for color images only. (normally same as h) 
- *templateWindowSize* : should be odd. (recommended 7) 
- *searchWindowSize* : should be odd. (recommended 21)"

## Requirements

- [OpenCV](https://opencv.org/)
- [Numpy](https://numpy.org/)
- [Gradio](https://www.gradio.app/)

## How to use

- Clone the project and run :

  `python main.py`
  
- The demo will be live at [http://127.0.0.1:7860/](http://127.0.0.1:7860/)

## How to deploy

Since you can only deploy static page in [GitHub pages](https://pages.github.com/).

You can use [Heroku](https://www.heroku.com/) or [Pythoneverywhere](https://www.pythonanywhere.com/) for deployment.
