// Animate the button on scroll
gsap.from("button", {
  scrollTrigger: "button",
  scale: 0,
  duration: 0.6,
  ease: "back.out(1.7)"
});

// Animate the footer on scroll
gsap.from("footer", {
  scrollTrigger: "footer",
  y: 50,
  opacity: 0,
  duration: 1
});
