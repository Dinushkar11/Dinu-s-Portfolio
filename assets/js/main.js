document.addEventListener("DOMContentLoaded", function () {
  AOS.init({
    duration: 900,
    once: true,
    easing: "ease-in-out"
  });

  const navLinks = document.querySelectorAll("#navbar .nav-link");

  navLinks.forEach(link => {
    link.addEventListener("click", function () {
      navLinks.forEach(item => item.classList.remove("active"));
      this.classList.add("active");
    });
  });

  function activateSkills() {
    const progressBars = document.querySelectorAll(".progress .progress-bar");
    progressBars.forEach((bar) => {
      bar.style.width = bar.getAttribute("aria-valuenow") + "%";
    });
  }

  activateSkills();

  window.addEventListener("load", activateSkills);

  navLinks.forEach(link => {
    link.addEventListener("click", function () {
      setTimeout(activateSkills, 400);
    });
  });
});