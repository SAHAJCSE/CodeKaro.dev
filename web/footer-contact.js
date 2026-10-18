(() => {
  const repositoryLink = document.querySelector(".repository-link--social");
  if (repositoryLink) {
    const setRepositoryExpanded = expanded => {
      repositoryLink.dataset.expanded = String(expanded);
    };
    repositoryLink.addEventListener("pointerenter", event => {
      if (event.pointerType !== "touch") setRepositoryExpanded(true);
    });
    repositoryLink.addEventListener("pointerleave", () => {
      if (!repositoryLink.contains(document.activeElement)) setRepositoryExpanded(false);
    });
    repositoryLink.addEventListener("focusin", () => setRepositoryExpanded(true));
    repositoryLink.addEventListener("focusout", event => {
      if (!repositoryLink.contains(event.relatedTarget)) setRepositoryExpanded(false);
    });
  }

  const authMenu = document.querySelector(".home-auth");
  if (authMenu) {
    const authButton = authMenu.querySelector(".home-auth__button");
    const authPanel = authMenu.querySelector(".home-auth__panel");

    const isFile = window.location.protocol === "file:";
    const url = p => {
      if (isFile) {
        const clean = p.replace(/^\//, "") || "index";
        const query = clean.includes("?") ? "?" + clean.split("?")[1] : "";
        const base = clean.split("?")[0];
        return "./" + (base.endsWith(".html") ? base : base + ".html") + query;
      }
      return p;
    };

    function syncHomeAuthState() {
      let user = null;
      try {
        user = JSON.parse(localStorage.getItem("oops_session") || "null");
      } catch (e) {
        user = null;
      }

      if (user && (user.username || user.name)) {
        const displayName = user.name || user.username || "Coder";
        const handle = user.username || (user.email ? user.email.split("@")[0] : "coder");
        const initial = (displayName.charAt(0) || "U").toUpperCase();
        const avatarSrc = user.picture || user.avatar || "";

        authButton.setAttribute("aria-label", `Account: ${displayName}`);
        authButton.title = `Signed in as @${handle}`;
        if (avatarSrc) {
          authButton.innerHTML = `<img src="${avatarSrc}" alt="${displayName}" style="width:28px;height:28px;border-radius:50%;object-fit:cover;display:block;">`;
        } else {
          authButton.innerHTML = `<span style="width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#784bff,#26d7f4);color:#fff;font-size:12px;font-weight:700;display:grid;place-items:center;">${initial}</span>`;
        }

        if (authPanel) {
          authPanel.innerHTML = `
            <div class="home-auth__user-pill">
              <div class="home-auth__avatar">
                ${avatarSrc ? `<img src="${avatarSrc}" alt="${displayName}">` : `<span>${initial}</span>`}
              </div>
              <div class="home-auth__user-meta">
                <span class="home-auth__user-name">${displayName}</span>
                <span class="home-auth__user-handle">@${handle}</span>
              </div>
            </div>
            <div class="home-auth__actions" style="display:flex;flex-direction:column;gap:6px">
              <a class="home-auth__link" href="${url('/practice')}">Practice IDE</a>
              <a class="home-auth__link" href="${url('/profile')}">Profile &amp; Stats</a>
              <button class="home-auth__link home-auth__link--logout" type="button" id="home-logout-btn">Log out</button>
            </div>
          `;

          const logoutBtn = authPanel.querySelector("#home-logout-btn");
          if (logoutBtn) {
            logoutBtn.addEventListener("click", () => {
              try {
                localStorage.removeItem("oops_session");
                localStorage.removeItem("ck_user");
              } catch (e) {}
              syncHomeAuthState();
            });
          }
        }
      } else {
        authButton.setAttribute("aria-label", "Account options");
        authButton.title = "Account options";
        authButton.innerHTML = `
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <circle cx="12" cy="8" r="3.5" stroke="currentColor" stroke-width="1.7"/>
            <path d="M4.8 20c.7-3.3 3.2-5.1 7.2-5.1s6.5 1.8 7.2 5.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>
          </svg>
        `;
        if (authPanel) {
          authPanel.innerHTML = `
            <p class="home-auth__prompt">Join Code-Karo</p>
            <div class="home-auth__actions">
              <a class="home-auth__link" href="${url('/auth?auth=signup')}">Sign up</a>
              <a class="home-auth__link" href="${url('/auth')}">Log in</a>
            </div>
          `;
        }
      }
    }

    syncHomeAuthState();
    window.addEventListener("storage", syncHomeAuthState);

    const setAuthMenuOpen = open => {
      authButton.setAttribute("aria-expanded", String(open));
      authMenu.dataset.open = String(open);
    };
    authMenu.addEventListener("pointerenter", () => setAuthMenuOpen(true));
    authMenu.addEventListener("pointerleave", () => {
      if (!authMenu.contains(document.activeElement)) setAuthMenuOpen(false);
    });
    authMenu.addEventListener("focusin", () => setAuthMenuOpen(true));
    authMenu.addEventListener("focusout", event => {
      if (!authMenu.contains(event.relatedTarget)) setAuthMenuOpen(false);
    });
  }

  // If viewing over file:// protocol, ensure relative links work without 404
  if (window.location.protocol === "file:") {
    document.querySelectorAll("a[href^='/']").forEach(a => {
      const href = a.getAttribute("href");
      if (!href || href.startsWith("//")) return;
      const clean = href.replace(/^\//, "") || "index";
      const hash = clean.includes("#") ? "#" + clean.split("#")[1] : "";
      const pathOnly = clean.split("#")[0].split("?")[0];
      const search = clean.includes("?") ? "?" + clean.split("?")[1].split("#")[0] : "";
      const target = pathOnly ? (pathOnly.endsWith(".html") ? pathOnly : pathOnly + ".html") : "index.html";
      a.setAttribute("href", "./" + target + search + hash);
    });
  }

  const wrapper = document.querySelector("[data-footer-contact]");
  if (!wrapper) return;

  const button = wrapper.querySelector("button");
  let lockedOpen = false;

  function setOpen(open) {
    wrapper.dataset.open = String(open);
    button.setAttribute("aria-expanded", String(open));
  }

  wrapper.addEventListener("pointerenter", () => {
    if (!lockedOpen) setOpen(true);
  });

  wrapper.addEventListener("pointerleave", () => {
    if (!lockedOpen && !wrapper.contains(document.activeElement)) setOpen(false);
  });

  wrapper.addEventListener("focusin", () => setOpen(true));
  wrapper.addEventListener("focusout", event => {
    if (!wrapper.contains(event.relatedTarget) && !lockedOpen) setOpen(false);
  });

  button.addEventListener("click", () => {
    lockedOpen = !lockedOpen;
    setOpen(lockedOpen);
  });

  document.addEventListener("pointerdown", event => {
    if (!wrapper.contains(event.target)) {
      lockedOpen = false;
      setOpen(false);
    }
  });

  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && wrapper.dataset.open === "true") {
      lockedOpen = false;
      setOpen(false);
      button.focus();
    }
  });

  const eyes = document.querySelector("[data-follow-eyes]");
  if (eyes && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const pupils = [...eyes.querySelectorAll(".footer-follow-eye__pupil")];
    window.addEventListener("pointermove", event => {
      if (event.pointerType === "touch") return;
      pupils.forEach(pupil => {
        const eye = pupil.parentElement;
        const bounds = eye.getBoundingClientRect();
        const maxDistance = Math.max(0, (bounds.width - pupil.offsetWidth) / 2 * .8);
        const dx = event.clientX - (bounds.left + bounds.width / 2);
        const dy = event.clientY - (bounds.top + bounds.height / 2);
        const distance = Math.hypot(dx, dy);
        const scale = distance > maxDistance ? maxDistance / distance : 1;
        pupil.style.transform = `translate3d(${dx * scale}px, ${dy * scale}px, 0)`;
      });
    }, { passive: true });

    window.setInterval(() => {
      if (document.visibilityState !== "visible") return;
      eyes.classList.add("is-blinking");
      window.setTimeout(() => eyes.classList.remove("is-blinking"), 180);
    }, 3400);
  }
})();
