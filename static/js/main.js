/* function previewImage in oder to display an image  before confirming an image */
function previewImage(event){
    const input = event.target;
    const preview = document.getElementById('imagePreview');

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
        };
        reader.readAsDataURL(input.files[0]);
    } else {
          preview.src = '#';
          preview.style.display = 'none';
    }
}