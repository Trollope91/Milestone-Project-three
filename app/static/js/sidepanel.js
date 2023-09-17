//Removes class hidden from sidebar
function openSideBar() {
  var sdbarElements = document.querySelectorAll(".sdbar");

  sdbarElements.forEach(function (element) {
    element.classList.remove("hidden");
  });
}

//Reapplies class hidden to sidebar
function closeSidebar() {
  var sdbarElements = document.querySelectorAll(".sdbar");

  sdbarElements.forEach(function (element) {
    element.classList.add("hidden");
  });
}
