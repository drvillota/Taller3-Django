from . .models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(id):
    measurement = []
    try:
        measurement.append(Measurement.objects.get(pk=id))
    except Exception:
        pass
    return measurement

def delete_measurement(id):
    Measurement.objects.filter(pk=id).delete()

def update_measurement(id, newVariable, newValue, newUnit, newPlace, newDateTime):
    measurement = Measurement.objects.filter(pk=id)
    measurement.update(variable = newVariable, value = newValue, unit = newUnit, place = newPlace, dateTime = newDateTime)
