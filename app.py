from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    # Display index.html
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
