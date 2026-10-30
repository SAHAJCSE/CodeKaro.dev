(() => {
  const currentPath = window.location.pathname.replace(/\/+$/, "") || "/";
  const islands = document.querySelectorAll("[data-nav-island]");

  function updateIslandWidths() {
    islands.forEach((island) => {
      const brand = island.querySelector(".nav-island__brand");
      const links = island.querySelector(".nav-island__links");
      if (!brand || !links) return;

      const brandW = Math.ceil(brand.getBoundingClientRect().width || brand.offsetWidth || 104);
      const linksW = Math.ceil(links.scrollWidth || 340);

      // Exact padding (4px left + 4px right + 2px borders = 10px)
      const collapsedW = brandW + 10;
      const expandedW = brandW + linksW + 12;

      island.style.setProperty("--island-collapsed-w", `${collapsedW}px`);
      island.style.setProperty("--island-expanded-w", `${expandedW}px`);
    });
  }

  islands.forEach((island) => {
    island.querySelectorAll("[data-nav-link]").forEach((link) => {
      const targetPath = new URL(link.href, window.location.href).pathname.replace(/\/+$/, "") || "/";
      if (targetPath === currentPath || (targetPath !== "/" && currentPath.startsWith(`${targetPath}/`))) {
        link.setAttribute("aria-current", "page");
      }
    });

    // Touch / click support for tablet screens where hover isn't persistent
    const brand = island.querySelector(".nav-island__brand");
    if (brand) {
      brand.addEventListener("click", (e) => {
        if (window.innerWidth > 720 && window.matchMedia("(hover: none)").matches) {
          const isExpanded = island.getAttribute("data-expanded") === "true";
          if (!isExpanded) {
            e.preventDefault();
            island.setAttribute("data-expanded", "true");
          }
        }
      });
    }
  });

  document.addEventListener("click", (e) => {
    islands.forEach((island) => {
      if (!island.contains(e.target)) {
        island.removeAttribute("data-expanded");
      }
    });
  });

  updateIslandWidths();
  window.addEventListener("load", updateIslandWidths);
  window.addEventListener("resize", updateIslandWidths);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(updateIslandWidths).catch(() => {});
  }
})();
