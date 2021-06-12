// Data file path
const url = "/api/dest_airports";

// test data read as needed
// olympicsData.then(row => {
//   console.log(row);
// });

// Assign d3.json to variable
const airportData = d3.json(url);

// Create reference variables
const dropdownElement = d3.select("#selYear");
const yearElement = d3.select("#Year");
const nocDropdownElement = d3.select("#selNOC");

// #########################################
// Initialize charts and dropdowns
// #########################################

function init() {

  // get data
  airportData.then(function(response) {
    console.log("Airport Data:", response);

    // // create Sets to avoid duplicates
    // let years = new Set();
    // let regions = new Set();

    // // Pull out elements for dropdowns
    // response.forEach((row) => {
    //   years.add(row.Year);
    //   regions.add(row.Region);
    // });

    // // create Arrays to sort 
    // var sortedYears = Array.from(years).sort();
    // var sortedRegions = Array.from(regions).sort();

    // // populate year dropdown element
    // sortedYears.forEach(year => {dropdownElement
    //   .append("option")
    //   .text(year)
    //   .property("value", year)
    // });
    // // console.log("sortedYears", sortedYears);

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
