(() => {
  function updateNav() {
    const currentPath = window.location.pathname.replace(/\.html$/, "").replace(/\/+$/, "") || "/";
    document.querySelectorAll("[data-nav-island]").forEach(nav => {
      const brand = nav.querySelector(".nav-island__brand");
      const linksContainer = nav.querySelector(".nav-island__links");
      const links = nav.querySelectorAll("[data-nav-link]");
      if (!linksContainer || !brand || !links.length) return;

      let matched = false;
      links.forEach(link => {
        const targetPath = new URL(link.href, window.location.href).pathname.replace(/\.html$/, "").replace(/\/+$/, "") || "/";
        const isCurrent = targetPath === currentPath || (targetPath !== "/" && currentPath.startsWith(`${targetPath}/`));
        if (isCurrent && !matched) {
          link.setAttribute("aria-current", "page");
          matched = true;
        } else {
          link.removeAttribute("aria-current");
        }
      });

      const prevMax = linksContainer.style.maxWidth;
      const prevVis = linksContainer.style.visibility;
      linksContainer.style.maxWidth = "none";
      linksContainer.style.visibility = "hidden";

      const gap = parseFloat(window.getComputedStyle(linksContainer).gap) || 4;
      let totalLinksWidth = 0;
      links.forEach((link, index) => {
        totalLinksWidth += link.getBoundingClientRect().width;
        if (index > 0) totalLinksWidth += gap;
      });
      totalLinksWidth = Math.ceil(totalLinksWidth);

      linksContainer.style.maxWidth = prevMax;
      linksContainer.style.visibility = prevVis;

      const brandWidth = Math.ceil(brand.getBoundingClientRect().width) || 104;
      const totalPillWidth = brandWidth + totalLinksWidth + 12;

      nav.style.setProperty("--island-links-width", `${totalLinksWidth}px`);
      nav.style.setProperty("--island-expanded-width", `${totalPillWidth}px`);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updateNav);
  } else {
    updateNav();
  }
  window.addEventListener("resize", updateNav);
  window.addEventListener("load", updateNav);
  if (document.fonts) {
    document.fonts.ready.then(updateNav);
  }
})();

