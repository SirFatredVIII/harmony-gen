# Import flask and datetime module for showing date and time
from flask import Flask
import test_model as model

# Initializing flask app
app = Flask(__name__)

# Route for seeing a data
@app.route('/model')
def run_model():
    '''
    returns bullshit
    '''

    harmony = model.run_model()
    # Returning an api for showing in reactjs
    return {
        'response': str(harmony.instruments[0].notes)
        }

# Running app
if __name__ == '__main__':
    app.run(debug=True)
