from django.conf import settings
import os

# IMAGE_UPLOAD_API
IMAGE_UPLOAD_INVALID = "upload check invalid"
IMAGE_UPLOAD_UNSUPPORTED_FORMAT = "unsupported file format"
IMAGE_UPLOAD_SERVER_ERROR = "unsupported file format"
IMAGE_UPLOAD_SUCCESS = "success"

# FILE_PATH
LANDMARK_PREDICTOR_MODEL_NAME = 'shape_predictor_68_face_landmarks.dat'
LANDMARK_PREDICTOR_MODEL_PATH = os.path.join(settings.MODEL_DIR,
                                             LANDMARK_PREDICTOR_MODEL_NAME)

# FACE_DETECT
FACE_NOT_FOUND = 'face_not_found'
FOUND_TOO_MANY_FACES = 'found_too_many_faces'