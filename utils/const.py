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


# FACE_LAND_MARK_NUM
contour_left1 = 0
contour_left2 = 1
contour_left3 = 2
contour_left4 = 3
contour_left5 = 4
contour_left6 = 5
contour_left7 = 6
contour_left8 = 7

contour_chin = 8

contour_right1 = 16
contour_right2 = 15
contour_right3 = 14
contour_right4 = 13
contour_right5 = 12
contour_right6 = 11
contour_right7 = 10
contour_right8 = 9

left_eyebrow_left_corner = 17
left_eyebrow_upper_left_quarter = 18
left_eyebrow_upper_middle = 19
left_eyebrow_upper_right_quarter = 20
left_eyebrow_right_corner = 21

right_eyebrow_left_corner = 22
right_eyebrow_upper_left_quarter = 23
right_eyebrow_upper_middle = 24
right_eyebrow_upper_right_quarter = 25
right_eyebrow_right_corner = 26

nose_contour_middle1 = 27
nose_contour_middle2 = 28
nose_contour_middle3 = 29
nose_tip = 30
nose_left = 31
nose_contour_left = 32
nose_contour_lower_middle = 33
nose_contour_right = 34
nose_right = 35

left_eye_left_corner = 36
left_eye_upper_left_quarter = 37
left_eye_upper_right_quarter = 38
left_eye_right_corner = 39
left_eye_lower_right_quarter = 40
left_eye_lower_left_quarter = 41

right_eye_left_corner = 42
right_eye_upper_left_quarter = 43
right_eye_upper_right_quarter = 44
right_eye_right_corner = 45
right_eye_lower_right_quarter = 46
right_eye_lower_left_quarter = 47


mouth_left_corner = 48
mouth_upper_lip_left_contour2 = 49
mouth_upper_lip_left_contour1 = 50
mouth_upper_lip_top = 51
mouth_upper_lip_right_contour1 = 52
mouth_upper_lip_right_contour2 = 53
mouth_right_corner = 54

mouth_lower_lip_right_contour1 = 55
mouth_lower_lip_right_contour2 = 56
mouth_lower_lip_bottom = 57
mouth_lower_lip_left_contour2 = 58
mouth_lower_lip_left_contour1 = 59

mouth_upper_lip_left_contour3 = 60
mouth_upper_lip_left_contour4 = 61
mouth_upper_lip_bottom = 62
mouth_upper_lip_right_contour3 = 63
mouth_upper_lip_right_contour4 = 64
mouth_lower_lip_right_contour3 = 65
mouth_lower_lip_top = 66
mouth_lower_lip_left_contour3 = 67





