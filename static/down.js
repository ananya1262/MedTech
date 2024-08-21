let prodDiv = document.getElementById('prod');
let numProdInput = document.getElementById('num_prod');

numProdInput.addEventListener('change', function() {
    let numProd = parseInt(numProdInput.value);
    prodDiv.innerHTML = '';
    for (let i = 1; i <= numProd; i++) {
        let div = document.createElement('div');
        div.innerHTML = `
            <label for="product_${i}">Product Name ${i}:</label>
            <input type="text" id="product_${i}" name="product_${i}" placeholder="Enter the product name"required><br>
            <label for="transport_mode1_${i}">Transportation mode:</label>
            <select id="transport_mode1_${i}" name="transport_mode1_${i}">
                <option value="road">Road</option>
                <option value="rail">Rail</option>
                <option value="sea">Sea</option>
                <option value="air">Air</option>
            </select><br>
            <label for="distances1_${i}">Distance travelled by product ${i}:</label>
            <input type="number" id="distances1_${i}" name="distances1_${i}" placeholder="Enter in KMs" required><br>
            <label for="fuel_${i}">Fuel Consumption:</label>
            <input type="number" id="fuel_${i}" name="fuel_${i}" placeholder="Enter the fuel consumption(in liters)" required><br>
            <label for="trans_${i}">Transport Efficiency:</label>
            <input type="number" id="trans_${i}" name="trans_${i}" placeholder="Enter the transport efficiency (in ton-km per liter)" required><br>
            <label for="distances2_${i}">Distribution center distance:</label>
            <input type="number" id="distances2_${i}" name="distances2_${i}" placeholder="Enter the distance to distribution center(in km)" required><br>
            <label for="distances3_${i}">Customer Distance :</label>
            <input type="number" id="distances3_${i}" name="distances3_${i}" placeholder="Enter the average customer distance(in km)" required><br>
        `;
        prodDiv.appendChild(div);
    }
});