(() => {
  const heading = document.querySelector("[data-scroll-reveal]");
  if (!heading) return;

  const originalText = heading.textContent.replace(/\s+/g, " ").trim();
  const words = originalText.split(" ");
  heading.replaceChildren();

  const segments = words.map((word, index) => {
    const span = document.createElement("span");
    span.className = "reveal-word";
    span.style.setProperty("--word-index", String(index));
    span.textContent = word;
    heading.append(span);
    if (index < words.length - 1) heading.append(document.createTextNode(" "));
    return span;
  });

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reducedMotion.matches) {
    heading.classList.add("is-queued");
    segments.forEach(segment => {
      segment.style.opacity = "1";
      segment.style.transform = "none";
      segment.style.filter = "none";
    });
    return;
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        heading.classList.remove("is-queued");
        void heading.offsetWidth;
        heading.classList.add("is-queued");
      } else {
        heading.classList.remove("is-queued");
      }
    });
  }, { threshold: 0.15, rootMargin: "40px 0px" });

  observer.observe(heading);
})();
