# from flask import Flask, render_template
# import subprocess

# app = Flask(__name__)

# @app.route('/')
# def index():
#     try:
#         subprocess.Popen(['python', 'crossy_road.py'])
#     except Exception as e:
#         print(f"Error: {e}")
#     return render_template('TRgame.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    try:
        subprocess.Popen(['python', 'crossy_road.py'])
    except Exception as e:
        print(f"Error: {e}")
    return render_template('TRgame.html')

if __name__ == '__main__':
    app.run(debug=True)



