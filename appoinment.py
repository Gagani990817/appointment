from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory storage for appointments
appointments = {}

@app.route('/appointment', methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointment_id = str(uuid4())
    appointment = {
        'id': appointment_id,
        'doctor': data['doctor'],
        'patient_id': data['patient_id'],
        'appointment_time': data['appointment_time'],
        'status': 'Scheduled'  # Default status
    }
    appointments[appointment_id] = appointment
    return jsonify(appointment), 201

@app.route('/appointment/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404
    return jsonify(appointment)

@app.route('/appointment/<appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()
    appointment = appointments.get(appointment_id)
    if not appointment:
        return jsonify({'message': 'Appointment not found'}), 404

    appointment['status'] = data.get('status', appointment['status'])
    return jsonify(appointment)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
