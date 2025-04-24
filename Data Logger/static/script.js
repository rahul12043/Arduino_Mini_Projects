// Function to fetch and update data every 2 seconds
function fetchData() {
    $.getJSON("/data", function(data) {
        // Clear previous data
        $("#sensor-data").empty();
        // Display new data
        data.forEach(function(item) {
            $("#sensor-data").append("<li>" + item + "</li>");
        });
    });
}

// Update data every 2 seconds
setInterval(fetchData, 2000);
