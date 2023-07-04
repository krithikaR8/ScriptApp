from flask import Flask, render_template, request
import script


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    script.my_script()
    
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run()
