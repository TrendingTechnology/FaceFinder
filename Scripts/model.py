# Welcome to my code, aliens!
 
from cv2 import cvtColor, imread, COLOR_BGR2RGB, imshow, waitKey, rectangle, putText, FONT_HERSHEY_SIMPLEX   # Import statements fresh as a flower!
from face_recognition import face_locations, face_encodings, compare_faces  # Import statements fresh as a flower!
from imutils.paths import list_images  # Import statements fresh as a flower!
from pydron import functional, schedule
from os.path import sep  # Import statements fresh as a flower!


class Model:

    def __init__(self): pass

    @functional
    def preprocess_data(self, data_dir):  # Encode images as arrays with 128 dimensions

        recognized_encodings = recognized_names = []  # Create lists to store the names of the faces in the images and their encodings.

        for image_path in list(list_images(data_dir)):
            RGB = cvtColor((imread(image_path)), COLOR_BGR2RGB)  # Change image ordering from BGR to RGB so that it can be used by dlib.
            holders = face_locations(RGB, model="cnn")  # The boxes of where the face is in the image.
            encodings = face_encodings(RGB, holders)  # Calculate encodings to store in list.

            for i in encodings:  #Store encodings and names in previously created lists.
                recognized_encodings.append(i)  # Store encoding
                recognized_names.append(image_path.split(sep)[-2])  # Store name of face in image
        
        return recognized_names, recognized_encodings


    @functional
    def compare_face(self, img_path, face_names, face_encodings):  # Compare processed data with input image.
        
        RGB = cvtColor(imread(img_path), COLOR_BGR2RGB)
        holders = face_locations(RGB, model="cnn")
        encodings = face_encodings(RGB, holders)  # Get the location of binding holder to each face in image and calculate embeddings.
        people_faces = []  # List to store the people whose faces are in the image.
        
        for encoding in encodings:
            matching_faces, face_name = compare_faces(face_encodings, encoding), "UNRECOGNIZED"  # Matches obtained for faces, default name is "unrecognized".
            
            if True in matching_faces:  # If any of the faces match...
                alike_indexes, dict_counter = list(i for (i, b) in enumerate(matching_faces) if b), {}  # Indexes of matching faces, initialize counter.

                for index in alike_indexes:  # Store faces by index
                    face_name = face_names[index]
                    dict_counter[face_name] = dict_counter.get(face_name, 0) + 1

                face_name = max(dict_counter, key = dict_counter.get)

            people_faces.append(face_name)
        
        return holders, people_faces, imread(img_path)

    @functional
    def display_image(self, holders, faces, input_image):

        for ((up, right, down, left), face_name) in zip(holders, faces):

            rectangle(
                input_image,
                (left, up),
                (right, down),
                (0, 255, 0), 2
                )

            if up - 15 > 15:
                vert_pos = up - 15
            else:
                vert_pos = up + 15

            putText(
                input_image,
                face_name,
                (left, vert_pos),
                FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 0),
                2
                )
        
        imshow("Image", input_image)
        waitKey(0)

    @schedule
    def tune_and_evaluate(self, data_dir, image_path):
        self.model = Model()
        
        recognized_names, recognized_encodings = self.model.preprocess_data(
            data_dir = data_dir
            )
        holders, faces, image = self.model.compare_face(
            img_path = image_path,
            face_names = recognized_names,
            face_encodings = recognized_encodings
            )
        self.model.display_image(
            holders = holders,
            faces = faces,
            input_image = image
        )
