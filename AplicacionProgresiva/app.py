from flask import Flask, render_template, request, jsonify
import redis
import json

app = Flask(__name__)

# Conectar con Redis
db = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar datos desde y hacia Redis
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        name = request.json.get('name')
        career = request.json.get('career')
        if name and career:
            # Crear un nuevo registro y agregarlo a la lista en Redis
            new_entry = {'name': name, 'career': career}
            existing_data = db.get('entries')
            if existing_data:
                data_list = json.loads(existing_data)
            else:
                data_list = []
            
            data_list.append(new_entry)
            db.set('entries', json.dumps(data_list))
            return jsonify({'data': f'{name}, {career}'}), 201

    # Si es GET, devolver los datos almacenados
    stored_data = db.get('entries')
    if stored_data:
        entries = json.loads(stored_data)
        data = "\n".join([f"{entry['name']}, {entry['career']}" for entry in entries])
    else:
        data = "No hay datos almacenados."
    
    return jsonify({'data': data})

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)

