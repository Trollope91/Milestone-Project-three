function openFilePicker() {
  // Trigger the file picker
  document.getElementById("filePicker").click();
}

function saveimage(event){
    const fileInput = event.target;
    const avatarImage = document.getElementById("avatarImage");
    const base64ImageInput = document.getElementById("base64Image");

    if (fileInput.files && fileInput.files[0]) {
      const file = fileInput.files[0];

      // Check if the selected file is an image
      if (file.type.startsWith("image/")) {
        const reader = new FileReader();

        reader.onload = function (e) {
          // Set the src attribute of the <img> element to the base64 data URL
          avatarImage.src = e.target.result;

          // Set the base64-encoded image data in the hidden input field
          base64ImageInput.value = e.target.result.split(",")[1];
        };

        // Read the file as a data URL (base64)
        reader.readAsDataURL(file);
      } else {
        alert("Please select a valid image file (JPG, GIF, or PNG).");
      }
    }

}
