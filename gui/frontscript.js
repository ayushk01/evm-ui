function init() {
  document.getElementById("status_text").innerHTML =
    "Please Present Your RFID Card";

  eel.check_rfid()(function (res) {
    if (res.matched === true) {
      window.location.href = "pin.html";
    } else {
      return;
    }
  });
}
