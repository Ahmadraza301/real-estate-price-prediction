function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function showLoading() {
  var estPrice = document.getElementById("uiEstimatedPrice");
  estPrice.innerHTML = "<h2>Calculating...</h2>";
  estPrice.style.backgroundColor = "#f0f0f0";
}

function showError(message) {
  var estPrice = document.getElementById("uiEstimatedPrice");
  estPrice.innerHTML = "<h2>Error: " + message + "</h2>";
  estPrice.style.backgroundColor = "#ffcccc";
}

function showResult(price) {
  var estPrice = document.getElementById("uiEstimatedPrice");
  estPrice.innerHTML = "<h2>" + price.toString() + " Lakh</h2>";
  estPrice.style.backgroundColor = "#dcd686";
}

function validateInputs(sqft, bhk, bathrooms, location) {
  if (!sqft || sqft <= 0) {
    showError("Please enter a valid area");
    return false;
  }
  if (bhk === -1) {
    showError("Please select number of bedrooms");
    return false;
  }
  if (bathrooms === -1) {
    showError("Please select number of bathrooms");
    return false;
  }
  if (!location || location === "") {
    showError("Please select a location");
    return false;
  }
  return true;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  
  // Validate inputs
  if (!validateInputs(parseFloat(sqft.value), bhk, bathrooms, location.value)) {
    return;
  }
  
  showLoading();
  
  // Use direct URLs for Flask development server
  var url = "/predict_home_price";

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value
  })
  .done(function(data, status) {
      console.log("Prediction successful:", data);
      if (data.estimated_price) {
        showResult(data.estimated_price);
      } else {
        showError("Invalid response from server");
      }
  })
  .fail(function(xhr, status, error) {
      console.error("Prediction failed:", error);
      var errorMessage = "Unable to get prediction";
      if (xhr.responseJSON && xhr.responseJSON.error) {
        errorMessage = xhr.responseJSON.error;
      }
      showError(errorMessage);
  });
}

function onPageLoad() {
  console.log("Document loaded");
  
  // Use direct URL for Flask development server
  var url = "/get_location_names";
  
  $.get(url)
  .done(function(data, status) {
      console.log("Got response for get_location_names request");
      if(data && data.locations) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          
          // Add default option
          var defaultOpt = new Option("Choose a Location", "");
          defaultOpt.disabled = true;
          defaultOpt.selected = true;
          $('#uiLocations').append(defaultOpt);
          
          // Add all locations
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
          console.log("Loaded " + locations.length + " locations");
      } else {
          console.error("No locations data received");
          showError("Unable to load locations");
      }
  })
  .fail(function(xhr, status, error) {
      console.error("Failed to load locations:", error);
      showError("Unable to load locations");
  });
}

window.onload = onPageLoad;