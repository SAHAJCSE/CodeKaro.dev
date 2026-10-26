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
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", updateNav);
  } else {
    updateNav();
  }
})();
