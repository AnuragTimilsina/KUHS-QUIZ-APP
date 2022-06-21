var startTimer = document.getElementById("start-btn"); //Id of Start button
var startTimeField = document.getElementById("startTimeField");
if (startTimer) {
  startTimer.addEventListener("click", function () {
    startTimer = new Date();
    sessionStorage.setItem("startTimer", startTimer);
    console.log("starting time ", startTimer);
  });
}

var endTimer = document.getElementById("finish-btn"); //Id of Finish button
var endTimeField = document.getElementById("endTimeField");
if (endTimer) {
  endTimer.addEventListener("click", function () {
    endTimer = new Date();
    startTimeField.value = sessionStorage.getItem("startTimer");
    endTimeField.value = endTimer;
    console.log("ending time ", endTimer);
  });
}
