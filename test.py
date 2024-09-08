from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/test', methods=['POST'])
def test():
    obj = request.form.to_dict(flat=False)
    return render_template('answer.html', obj=obj)

if __name__ == '__main__':
    app.run(debug=True)
