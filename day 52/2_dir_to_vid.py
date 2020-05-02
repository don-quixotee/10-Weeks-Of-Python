from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnails_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_frame")
thumbnail_per_half_Second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")

output_video = os.path.join(SAMPLE_OUTPUTS, "thumbs.mp4")


this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname ) for fname in this_dir if fname.endswith("jpg")]

 

clip = ImageSequenceClip(filepaths, fps=4)
clip.write_videofile(output_video)
