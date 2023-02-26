// Get the current page URL
var currentPage = window.location.href;

// Get all the navigation links
var navLinks = document.querySelectorAll("nav a");

// Loop through the navigation links
for (var i = 0; i < navLinks.length; i++) {
	// Get the link URL
	var link = navLinks[i].getAttribute("href");

	// If the link URL matches the current page URL
	if (link === currentPage) {
		// Add a "current" class to the link
		navLinks[i].classList.add("current");
	}
}
