const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

//new function called slugify

const slugify = (val) => {
	return val.toString().toLowerCase().trim()
		.replace(/&/g, '-and-') //replace & with '-and-'
		.replace(/[\s\W-]+/g, '-') //replace spaces, non word class and dashes with single dash.
}

titleInput.addEventListener('keyup',(e) => {
	slugInput.setAttribute('value', slugify(titleInput.value));

});