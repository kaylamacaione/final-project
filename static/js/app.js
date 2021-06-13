// Local URL
const url = "/api/dest_airports";

// Deployed db URL
// const url = "https://flight-delay-predictor-ord.herokuapp.com/api/dest_airports";
console.log(url)

// Assign d3.json to variable
const airportData = d3.json(url);

// // test data read as needed
// airportData.then(row => {
//   console.log(row);
// });

// Create reference variables
const airportCodesElement = d3.select("#airportCodes");
const monthElement = d3.select("#selMonth");
const timeElement = d3.select("#selTime");

// #########################################
// Fill dropdown
// #########################################

function init() {

  // get data
  airportData.then(function(response) {

    // // create Sets to avoid duplicates
    let codes = new Set();

    // Pull out elements for dropdowns
    response.forEach((row) => {
      codes.add(row.DEST);
    });

    // create Arrays to sort 
    var codesArray = Array.from(codes).sort();

    // populate airport dropdown element
    codesArray.forEach(code => {airportCodesElement
      .append("option")
      .text(code)
      .property("value", code)
    });
    // console.log("codesArray", codesArray);

  });
};

init();
