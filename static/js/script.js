
	  function openSearch() {
            document.getElementById('searchoverlay').style.visibility ="visible";
            document.getElementById('searchoverlay').style.opacity ="1";
        };

        function closeSearch() {
            document.getElementById('searchoverlay').style.visibility ="hidden";
            document.getElementById('searchoverlay').style.opacity ="0";
        };


const navToggler = document.querySelector(".nav-toggler");
	navToggler.addEventListener("click", navToggle);

	function navToggle() {
		navToggler.classList.toggle("active");
		const nav = document.querySelector(".nav-menu");
		nav.classList.toggle("open");
		if (nav.classList.contains("open")) {
			nav.style.maxHeight = nav.scrollHeight + "px"
		}else{
			nav.removeAttribute("style");
		}
	}


	/* accordion*/
const accord = document.getElementsByClassName('show-reply-form');
let i;

for (i = 0; i < accord.length; i++) {
	accord[i].addEventListener("click", function(){
		this.classList.toggle("active");
		let reply = this.nextElementSibling;
		if (reply.style.display === "block"){
			reply.style.display = "none";

		}else{
			reply.style.display = "block";
		}
	});
}





