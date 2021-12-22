from flask import Flask, render_template
import cv2
import json

app = Flask(__name__)
@app.route("/")
def main():
    img = cv2.imread("Puzzle-amico.png")
    result_dict =  {
        "width": img.size[0],
        'height': img.size[1]
    }
    return json.dumps(result_dict)

if __name__ == "__main__":
    app.run()