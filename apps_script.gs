function doGet(e) {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var timestamp = new Date();

    var temp = e.parameter.temp;
    var pressure = e.parameter.pressure;

if (!temp || !pressure) {
    return ContentService.createTextOutput("Error: Missing Parameters");
}


// Checking if the sheet has headers and if not adding headers
if (sheet.getLastRow() === 0) {
    sheet.appendRow(["Timestamp", "Temperature (°C)", "Pressure (hPa)"]);
    sheet.getRange("E1").setValue("Total Entries"); // Labelling for total count
}


// Appendding the new data
sheet.appendRow([timestamp, temp, pressure]);


// Updating the total count in cell
var totalEntries = sheet.getLastRow() - 1;
sheet.getRange("E2").setValue(totalEntries);

    return ContentService.createTextOutput("Data logged successfully. Total Entries: " + totalEntries);
}