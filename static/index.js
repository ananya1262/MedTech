window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;
    const heading = document.getElementsByTagName('h1');
    const formContainer = document.getElementsByTagName('form');
  
    if (scrollPosition > 0) {
      heading.classList.add('fixed');
      formContainer.classList.add('pushed-down');
    } else {
      heading.classList.remove('fixed');
      formContainer.classList.remove('pushed-down');
    }
  });
  
let manufacturerDiv = document.getElementById('manufacturer');
let numManufacturerInput = document.getElementById('num_manufacturer');

numManufacturerInput.addEventListener('change', function() {
    let numManufacturer = parseInt(numManufacturerInput.value);
    manufacturerDiv.innerHTML = '';
    for (let i = 1; i <= numManufacturer; i++) {
        let div = document.createElement('div');
        div.innerHTML = `
            <h3>Energy consumed by manufacturer ${i}</h3>
            <label for="electricity_${i}">Electricity :</label>
            <input type="number" id="electricity_${i}" name="electricity_${i}" placeholder="Enter in kWh" required><br>
            <label for="natural_gas_${i}">Natural gas :</label>
            <input type="number" id="natural_gas_${i}" name="natural_gas_${i}" placeholder="Enter in kWh" required><br>
            <label for="coal_${i}">Coal :</label>
            <input type="number" id="coal_${i}" name="coal_${i}" placeholder="Enter in kWh" required><br>
            <label for="petroleum_${i}">Petroleum :</label>
            <input type="number" id="petroleum_${i}" name="petroleum_${i}" placeholder="Enter in liter" required><br>
            <label for="water_${i}">Water :</label>
            <input type="number" id="water_${i}" name="water_${i}" placeholder="Enter in liter" required><br>
        `;
        manufacturerDiv.appendChild(div);
    }
});




let materialsDiv = document.getElementById('materials');
let numMaterialsInput = document.getElementById('num_materials');

numMaterialsInput.addEventListener('change', function() {
    let numMaterials = parseInt(numMaterialsInput.value);
    materialsDiv.innerHTML = '';
    for (let i = 1; i <= numMaterials; i++) {
        let div = document.createElement('div');
        div.innerHTML = `
            <label for="quantity_${i}">Quantity of material ${i}:</label>
            <input type="number" id="quantity_${i}" name="quantity_${i}" placeholder="Enter the quantity"required><br>
            <label for="transport_mode_${i}">Transport mode of material ${i}:</label>
            <select id="transport_mode_${i}" name="transport_mode_${i}">
                <option value="road">Road</option>
                <option value="rail">Rail</option>
                <option value="sea">Sea</option>
                <option value="air">Air</option>
            </select><br>
            <label for="distance_${i}">Distance travelled by material ${i}:</label>
            <input type="number" id="distance_${i}" name="distance_${i}" placeholder="Enter in KMs" required><br>
        `;
        materialsDiv.appendChild(div);
    }
});

let tripTable = document.getElementById('tripTable');
let numTripInput = document.getElementById('num_trip');

numTripInput.addEventListener('change', function() {
    let numTrip = parseInt(numTripInput.value);
    tripTable.querySelector('tbody').innerHTML = '';
    for (let i = 1; i <= numTrip; i++) {
        let tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${i}</td>
            <td>
                <select id="mode_${i}" name="mode_${i}">
                    <option value="car">Car</option>
                    <option value="train">Train</option>
                    <option value="plane">Plane</option>
                </select>
            </td>
            <td>
                <input type="number" id="distance1_${i}" name="distance1_${i}" placeholder="Enter in KMs" required>
            </td>
        `;
        tripTable.querySelector('tbody').appendChild(tr);
    }
});

