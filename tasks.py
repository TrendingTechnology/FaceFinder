from argparse import ArgumentParser
from model import Model
from gc import collect

parser = ArgumentParser(
    description = """An elegant and heavily optimized(fast) program which performs face recognition."""
    )
parser.add_argument(
    '--data_path',
    help = "The path to the directory where the image data is located. The program assumes that if there are more than one faces in the image, they are all of the same person.",
    required = True
    )
parser.add_argument(
    '--input_image',
    help = "The image which contains the face that needs to be identified. The program assumes all faces in the image are of the same person.",
    required = True
    )
arguments = parser.parse_args()

del parser; collect()

model = Model()
model.tune_and_evaluate(arguments.data_dir, arguments.image_path)

del model; collect()