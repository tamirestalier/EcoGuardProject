from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_fire', methods=['POST'])
def report_fire():
    location = request.form.get('location')
    fire_type = request.form.get('fire_type')
    # Aqui você pode processar os dados recebidos, como enviá-los para um servidor, armazená-los em um banco de dados, etc.
    return 'Relatório de incêndio recebido com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
