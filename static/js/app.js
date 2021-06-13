// Data file path
const url = "/api/dest_airports";
// const url = "https://flight-delay-predictor-ord.herokuapp.com/api/dest_airports";

console.log(url)

// Assign d3.json to variable
const airportData = d3.json(url);

// test data read as needed
airportData.then(row => {
  console.log(row);
});


// Create reference variables
const airportCodesElement = d3.select("#airportCodes");
const monthElement = d3.select("#selMonth");
const timeElement = d3.select("#selTime");

// #########################################
// Initialize charts and dropdowns
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
    console.log("codesArray", codesArray);

    // // populate region dropdown element
    // sortedRegions.forEach(row => {nocDropdownElement
    //   .append("option")
    //   .text(row)
    //   .property("value", row)
    // });
    // // console.log("sortedRegions", sortedRegions);

    // // Set default year
    // var filterYear = sortedYears[0];
    // console.log("Default Year:", filterYear);

    // // Set default region
    // // var filterRegion = sortedRegions[0];
    // var filterRegion = "USA";
    // console.log("Default Region:", filterRegion);
    
    // // Default charts
    // barTwo(filterYear);
    // getMetadata(filterRegion, filterYear);
    // buildPolarChart(filterRegion, filterYear);

  });
};

init();
