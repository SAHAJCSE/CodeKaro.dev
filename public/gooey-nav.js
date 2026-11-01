(() => {
  if (window.__codeKaroNavInitialized) return;
  window.__codeKaroNavInitialized = true;

  const currentPath = window.location.pathname.replace(/\/+$/, "") || "/";

  function getStoredUser() {
    try {
      const sessionRaw = localStorage.getItem("oops_session");
      const ckRaw = localStorage.getItem("ck_user");
      const user = (sessionRaw && JSON.parse(sessionRaw)) || (ckRaw && JSON.parse(ckRaw)) || null;
      if (user && (user.id || user.uid || user.username || user.email)) {
        return user;
      }
    } catch (_e) {}
    return null;
  }

  function updateIslandWidths() {
    document.querySelectorAll("[data-nav-island]").forEach((island) => {
      const brand = island.querySelector(".nav-island__brand");
      const links = island.querySelector(".nav-island__links");
      if (!brand || !links) return;

      // Measure natural widths even if currently collapsed or hidden
      const brandRectW = Math.ceil(brand.getBoundingClientRect().width || brand.offsetWidth || 0);
      const brandW = Math.max(brandRectW, 114);

      let measuredLinksW = 0;
      const linkItems = links.querySelectorAll(".nav-island__link");
      linkItems.forEach((item) => {
        const w = Math.ceil(item.getBoundingClientRect().width || item.offsetWidth || item.scrollWidth || 76);
        measuredLinksW += w;
      });
      if (linkItems.length > 1) {
        measuredLinksW += (linkItems.length - 1) * 4 + 12;
      }

      const linksW = Math.max(measuredLinksW, Math.ceil(links.scrollWidth || 0), 420);
      const collapsedW = brandW + 10;
      const expandedW = brandW + linksW + 20;

      island.style.setProperty("--island-collapsed-w", `${collapsedW}px`);
      island.style.setProperty("--island-expanded-w", `${expandedW}px`);
    });
  }

  function initDesktopNavIslands() {
    const islands = document.querySelectorAll("[data-nav-island]");
    islands.forEach((island) => {
      if (island.dataset.bound === "true") return;
      island.dataset.bound = "true";

      island.querySelectorAll("[data-nav-link]").forEach((link) => {
        try {
          const targetPath = new URL(link.href, window.location.href).pathname.replace(/\/+$/, "") || "/";
          if (targetPath === currentPath || (targetPath !== "/" && currentPath.startsWith(`${targetPath}/`))) {
            link.setAttribute("aria-current", "page");
          } else {
            link.removeAttribute("aria-current");
          }
        } catch (_e) {}
      });

      const brand = island.querySelector(".nav-island__brand");
      if (brand) {
        brand.addEventListener("click", (e) => {
          // Toggle expansion on click so clicking "CodeKaro" opens/closes the menu on all devices
          e.preventDefault();
          e.stopPropagation();
          updateIslandWidths();
          const isExpanded = island.getAttribute("data-expanded") === "true";
          if (isExpanded) {
            island.removeAttribute("data-expanded");
            island.classList.remove("is-open");
          } else {
            island.setAttribute("data-expanded", "true");
            island.classList.add("is-open");
          }
        });
      }

      island.addEventListener("mouseenter", () => {
        updateIslandWidths();
      });
    });

    document.addEventListener("click", (e) => {
      document.querySelectorAll("[data-nav-island]").forEach((island) => {
        if (!island.contains(e.target)) {
          island.removeAttribute("data-expanded");
          island.classList.remove("is-open");
        }
      });
    });
  }

  // Full-screen mobile hamburger menu + Cross (X) close button initialization
  function initMobileFullScreenMenu() {
    document.querySelectorAll(".navbar-hamburger-wrapper").forEach((wrapper) => {
      if (wrapper.dataset.bound === "true") return;
      wrapper.dataset.bound = "true";

      const hamBtn = wrapper.querySelector(".hamburger-btn");
      const hamDropdown = wrapper.querySelector(".hamburger-dropdown");
      if (!hamBtn || !hamDropdown) return;

      // Portal the full-screen dropdown directly to document.body so parent navbar
      // backdrop-filter or hero overflow:hidden can NEVER clip or trap position:fixed!
      if (hamDropdown.parentElement !== document.body) {
        document.body.appendChild(hamDropdown);
      }

      // Ensure a dedicated Cross (X) close button exists inside the full-screen overlay
      let closeBtn = hamDropdown.querySelector(".hamburger-close-btn");
      if (!closeBtn) {
        closeBtn = document.createElement("button");
        closeBtn.type = "button";
        closeBtn.className = "hamburger-close-btn";
        closeBtn.setAttribute("aria-label", "Close navigation menu");
        closeBtn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
        hamDropdown.insertBefore(closeBtn, hamDropdown.firstChild);
      }

      // Highlight current page link in mobile menu
      hamDropdown.querySelectorAll("a").forEach((link) => {
        try {
          const linkUrl = new URL(link.href, window.location.href);
          if (linkUrl.origin === window.location.origin) {
            const targetPath = linkUrl.pathname.replace(/\/+$/, "") || "/";
            if (targetPath === currentPath) {
              link.setAttribute("aria-current", "page");
            }
          }
        } catch (_e) {}
      });

      const setMenuOpen = (open) => {
        wrapper.setAttribute("data-open", open ? "true" : "false");
        hamBtn.setAttribute("aria-expanded", open ? "true" : "false");
        hamDropdown.classList.toggle("is-open", open);
        document.body.style.overflow = open ? "hidden" : "";
      };

      hamBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = hamDropdown.classList.contains("is-open");
        setMenuOpen(!isOpen);
      });

      closeBtn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        setMenuOpen(false);
      });

      hamDropdown.addEventListener("click", (e) => {
        if (e.target === hamDropdown) {
          setMenuOpen(false);
        }
      });

      hamDropdown.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
          setMenuOpen(false);
        });
      });

      document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && hamDropdown.classList.contains("is-open")) {
          setMenuOpen(false);
        }
      });
    });
  }

  // Initialize Account Menu (.home-auth) click/hover & logged-in/logged-out state
  function initHomeAuthMenu() {
    document.querySelectorAll(".home-auth").forEach((authWrap) => {
      const btn = authWrap.querySelector(".home-auth__button");
      const panel = authWrap.querySelector(".home-auth__panel");
      if (!btn || !panel) return;

      const renderAuthPanel = () => {
        const user = getStoredUser();
        if (user) {
          const name = user.name || user.username || (user.email ? user.email.split("@")[0] : "Coder");
          const handle = user.username || (user.email ? user.email.split("@")[0] : "coder");
          const initial = String(name).trim().charAt(0).toUpperCase() || "C";
          panel.innerHTML = `
            <div class="home-auth__user-pill">
              <div class="home-auth__avatar">${initial}</div>
              <div class="home-auth__user-meta">
                <span class="home-auth__user-name"></span>
                <span class="home-auth__user-handle"></span>
              </div>
            </div>
            <div class="home-auth__actions" style="display:flex;flex-direction:column;gap:8px;">
              <a class="home-auth__link" href="/dashboard">Dashboard</a>
              <a class="home-auth__link" href="/profile">Profile &amp; Stats</a>
              <button class="home-auth__link home-auth__link--logout" type="button" data-home-logout>Log out</button>
            </div>
          `;
          const nameEl = panel.querySelector(".home-auth__user-name");
          const handleEl = panel.querySelector(".home-auth__user-handle");
          if (nameEl) nameEl.textContent = name;
          if (handleEl) handleEl.textContent = `@${handle}`;
          const logoutBtn = panel.querySelector("[data-home-logout]");
          if (logoutBtn) {
            logoutBtn.addEventListener("click", (e) => {
              e.preventDefault();
              localStorage.removeItem("oops_session");
              localStorage.removeItem("ck_user");
              authWrap.setAttribute("data-open", "false");
              btn.setAttribute("aria-expanded", "false");
              renderAuthPanel();
            });
          }
        } else {
          panel.innerHTML = `
            <p class="home-auth__prompt">Code-Karo Account</p>
            <div class="home-auth__actions" style="display:flex;gap:8px;">
              <a class="home-auth__link" href="/auth?auth=signup">Sign up</a>
              <a class="home-auth__link" href="/auth">Log in</a>
            </div>
          `;
        }
      };

      renderAuthPanel();

      if (authWrap.dataset.bound !== "true") {
        authWrap.dataset.bound = "true";
        btn.addEventListener("click", (e) => {
          e.preventDefault();
          e.stopPropagation();
          const isOpen = authWrap.getAttribute("data-open") === "true";
          authWrap.setAttribute("data-open", isOpen ? "false" : "true");
          btn.setAttribute("aria-expanded", isOpen ? "false" : "true");
        });

        document.addEventListener("click", (e) => {
          if (!authWrap.contains(e.target)) {
            authWrap.setAttribute("data-open", "false");
            btn.setAttribute("aria-expanded", "false");
          }
        });
      }
    });
  }

  function initAllNav() {
    initDesktopNavIslands();
    updateIslandWidths();
    initMobileFullScreenMenu();
    initHomeAuthMenu();
  }

  window.updateIslandWidths = updateIslandWidths;
  initAllNav();
  window.addEventListener("DOMContentLoaded", initAllNav);
  window.addEventListener("load", () => {
    initAllNav();
    updateIslandWidths();
  });
  window.addEventListener("resize", updateIslandWidths);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(updateIslandWidths).catch(() => {});
  }
})();
