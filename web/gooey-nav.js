(() => {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function currentIndex(links) {
    const path = window.location.pathname.replace(/\/+$/, "") || "/";
    let selected = 0;
    let bestLength = -1;
    links.forEach((link, index) => {
      const target = new URL(link.href, window.location.href).pathname.replace(/\/+$/, "") || "/";
      if ((target === path || (target !== "/" && path.startsWith(`${target}/`))) && target.length > bestLength) {
        selected = index;
        bestLength = target.length;
      }
    });
    return selected;
  }

  document.querySelectorAll("[data-gooey-nav]").forEach(nav => {
    const stage = nav.querySelector(".gooey-nav__stage");
    const links = [...nav.querySelectorAll("[data-nav-link]")];
    const pill = nav.querySelector(".gooey-nav__pill");
    const particleLayer = nav.querySelector(".gooey-nav__particles");
    if (!stage || !pill || !particleLayer || !links.length) return;

    const active = currentIndex(links);
    let preview = active;

    function positionPill(index) {
      const linkBounds = links[index].getBoundingClientRect();
      const stageBounds = stage.getBoundingClientRect();
      const inset = parseFloat(getComputedStyle(nav).getPropertyValue("--gn-pad")) || 0;
      pill.style.width = `${linkBounds.width}px`;
      pill.style.height = `${linkBounds.height}px`;
      pill.style.transform = `translate(${linkBounds.left - stageBounds.left - inset}px, ${linkBounds.top - stageBounds.top - inset}px)`;
    }

    function setPreview(index) {
      preview = index;
      links.forEach((link, linkIndex) => {
        if (linkIndex === active) link.setAttribute("aria-current", "page");
        else link.removeAttribute("aria-current");
      });
      positionPill(index);
    }

    function burst(index) {
      if (prefersReducedMotion.matches) return;
      const box = links[index].getBoundingClientRect();
      const centerX = box.left + box.width / 2;
      const centerY = box.top + box.height / 2;
      const stageBox = stage.getBoundingClientRect();
      const count = 12;
      for (let particle = 0; particle < count; particle += 1) {
        const angle = Math.PI * 2 * particle / count + Math.random() * .25;
        const distance = 20 + Math.random() * 36;
        const dot = document.createElement("span");
        dot.className = "gooey-nav__particle";
        dot.style.setProperty("--particle-size", `${4 + Math.random() * 6}px`);
        dot.style.setProperty("--particle-x", `${centerX - stageBox.left}px`);
        dot.style.setProperty("--particle-y", `${centerY - stageBox.top}px`);
        dot.style.setProperty("--particle-end-x", `${centerX - stageBox.left + Math.cos(angle) * distance}px`);
        dot.style.setProperty("--particle-end-y", `${centerY - stageBox.top + Math.sin(angle) * distance}px`);
        dot.style.setProperty("--particle-duration", `${460 + Math.random() * 280}ms`);
        particleLayer.append(dot);
        dot.addEventListener("animationend", () => dot.remove(), { once: true });
      }
    }

    links.forEach((link, index) => {
      if (index === active) link.setAttribute("aria-current", "page");
      link.addEventListener("pointerenter", event => {
        if (event.pointerType === "mouse") setPreview(index);
      });
      link.addEventListener("pointerleave", event => {
        if (event.pointerType === "mouse" && preview === index) setPreview(active);
      });
      link.addEventListener("focus", () => setPreview(index));
      link.addEventListener("click", () => {
        burst(index);
      });
    });

    nav.addEventListener("focusout", event => {
      if (!nav.contains(event.relatedTarget)) setPreview(active);
    });
    nav.addEventListener("keydown", event => {
      const index = links.indexOf(document.activeElement);
      if (index < 0) return;
      const targetIndex = {
        ArrowLeft: index - 1,
        ArrowRight: index + 1,
        Home: 0,
        End: links.length - 1
      }[event.key];
      if (targetIndex === undefined) return;
      event.preventDefault();
      links[Math.max(0, Math.min(links.length - 1, targetIndex))].focus();
    });

    const observer = new ResizeObserver(() => positionPill(preview));
    observer.observe(stage);
    links.forEach(link => observer.observe(link));
    positionPill(active);
  });
})();
