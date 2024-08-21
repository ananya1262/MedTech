from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upstream')
def upstream():
    return render_template('upstream.html')

@app.route('/upstream_emission_calculate', methods=['POST'])
def upstream_emission_calculate():
    # emission1
    num_manufacturer = int(request.form['num_manufacturer'])
    electricity = []
    natural_gas = []
    coal = []
    petroleum = []
    water = []

    for i in range(num_manufacturer):
        electricity.append(float(request.form[f'electricity_{i+1}']))
        natural_gas.append(float(request.form[f'natural_gas_{i+1}']))
        coal.append(float(request.form[f'coal_{i+1}']))
        petroleum.append(float(request.form[f'petroleum_{i+1}']))
        water.append(float(request.form[f'water_{i+1}']))

    emission1 = 0
    for i in range(num_manufacturer):
        emission1 = 0.35*electricity[i] + 0.2*natural_gas[i] + \
            0.4*coal[i] + 0.3*petroleum[i] + 0.001*water[i]

    # emission2
    building1 = float(request.form['construction'])
    building2 = float(request.form['energy_use'])
    building3 = float(request.form['decommissioning'])

    machinery1 = float(request.form['manu'])
    machinery2 = float(request.form['energy_use1'])
    machinery3 = float(request.form['disposal'])

    tools1 = float(request.form['manu1'])
    tools2 = float(request.form['energy_use2'])
    tools3 = float(request.form['disposal1'])

    emission4 = 0
    emission4 = (100*building1 + 50*building2 + 50*building3)+(500*machinery1 +
                                                               50*machinery2 + 100*machinery3) + (200*tools1 + 20*tools2 + 50*tools3)
    # Get inputs from form
    num_materials = int(request.form['num_materials'])
    quantities = []
    transport_modes = []
    distances = []
    for i in range(num_materials):
        quantities.append(float(request.form[f'quantity_{i+1}']))
        transport_modes.append(request.form[f'transport_mode_{i+1}'])
        distances.append(float(request.form[f'distance_{i+1}']))

    # Calculate total emissions
    transport_mode_dict = {
        'road': 0.1,
        'rail': 0.05,
        'sea': 0.02,
        'air': 0.5
    }
    emissions = 0
    for i in range(num_materials):
        emissions += transport_mode_dict[transport_modes[i]
                                         ] * quantities[i] * distances[i]

    landfill_emission = float(request.form['landfill'])
    incineration_emission = float(request.form['incineration'])
    recycling_emission = float(request.form['recycling'])

    emission2 = landfill_emission*0.5 + \
        incineration_emission*1.5 + recycling_emission*0.2

    # business travel
    num_trip = int(request.form['num_trip'])
    business_transport_modes = []
    distances1 = []
    for i in range(num_trip):
        business_transport_modes.append(request.form[f'mode_{i+1}'])
        distances1.append(float(request.form[f'distance1_{i+1}']))

    # Calculate total emissions
    mode_dict = {
        'car': 0.2,
        'train': 0.03,
        'plane': 0.25,
    }
    emission3 = 0
    for i in range(num_materials):
        emission3 += mode_dict[business_transport_modes[i]] * distances1[i]

    # emission6
    # emission2
    annual_usage1 = float(request.form['annual_usage1'])
    lease_term1 = float(request.form['lease_term1'])

    annual_usage2 = float(request.form['annual_usage2'])
    lease_term2 = float(request.form['lease_term2'])
    annual_usage3 = float(request.form['annual_usage3'])
    lease_term3 = float(request.form['lease_term3'])

    emission6 = (annual_usage1*lease_term1*0.2)+(annual_usage1*lease_term1*0.05)+(annual_usage2*lease_term2*0.1) + \
        (annual_usage2*lease_term2*0.02)+(annual_usage3 *
                                          lease_term3*0.05)+(annual_usage3*lease_term3*0.01)

    return render_template('result.html', emission1=emission1, emissions=emissions, emission2=emission2, emission3=emission3, emission4=emission4, emission6=emission6)


@app.route('/downstream')
def downstream():
    return render_template('downstream.html')


@app.route('/downstream_emission_calculate', methods=['POST'])
def downstream_emission_calculate():
    num_prod = int(request.form['num_prod'])
    transport_modes = []
    distances1 = []
    fuel = []
    trans = []
    distances2 = []
    distances3 = []

    for i in range(num_prod):
        transport_modes.append(request.form[f'transport_mode1_{i+1}'])
        distances1.append(float(request.form[f'distances1_{i+1}']))
        fuel.append(float(request.form[f'fuel_{i+1}']))
        trans.append(float(request.form[f'trans_{i+1}']))
        distances2.append(float(request.form[f'distances2_{i+1}']))
        distances3.append(float(request.form[f'distances3_{i+1}']))
    # Calculate total emissions
    transport_mode_dict = {
        'road': 0.03,
        'rail': 0.01,
        'sea': 0.0001,
        'air': 0.25
    }
    emission1 = 0
    tot_dist = 0
    for i in range(num_prod):
        tot_dist = distances1[i] + 2*distances2[i] + 2*distances3[i]
        emission1 += transport_mode_dict[transport_modes[i]
                                         ]*tot_dist * fuel[i] * trans[i]

    a = float(request.form['num_prods'])
    b = float(request.form['energy'])
    c = float(request.form['mate'])
    d = float(request.form['transport'])

    emission2 = 0
    emission2 = a*(b+c+d)

    emission3 = 0
    e = float(request.form['sold'])
    emission3 = e*(0.5+0.2)

    emission4 = 0
    f = float(request.form['sold1'])
    g = float(request.form['wei'])
    h = float(request.form['dis'])

    emission4 = f*g*h

    return render_template('result2.html', emission1=emission1, emission2=emission2, emission3=emission3, emission4=emission4)


if __name__ == '__main__':
    app.run(debug=True)
