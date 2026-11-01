(() => {
  const root = document.documentElement;
  const preferenceKey = "code-karo-theme";
  const revealAttribute = "data-theme-reveal";
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let revealRunning = false;

  const SUPPORTED_THEMES = [
    "black-purple",
    "white-purple",
    "mono",
    "github",
    "ocean",
    "ember",
    "dark",
    "light"
  ];

  function readTheme() {
    try {
      const storedTheme = window.localStorage.getItem(preferenceKey);
      if (storedTheme && SUPPORTED_THEMES.includes(storedTheme)) {
        return storedTheme;
      }
    } catch (error) {
      console.warn("Code-Karo.dev could not read the saved theme preference.", error);
    }
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }

  function syncControls(theme) {
    // 1. Sync compact dark/light switch buttons if present
    document.querySelectorAll("[data-theme-switch]").forEach(button => {
      const isLight = theme === "light" || theme === "white-purple";
      const nextTheme = isLight ? "dark" : "light";
      button.setAttribute("aria-label", `Switch to ${nextTheme} theme`);
      button.setAttribute("aria-pressed", String(!isLight));
      button.title = `Switch to ${nextTheme} theme`;
      const label = button.querySelector("[data-theme-label]");
      if (label) label.textContent = isLight ? "Light" : "Dark";
    });

    // 2. Sync palette color circle buttons
    document.querySelectorAll("[data-theme-val]").forEach(circle => {
      const val = circle.getAttribute("data-theme-val");
      if (val === theme) {
        circle.classList.add("is-active");
        circle.setAttribute("aria-selected", "true");
      } else {
        circle.classList.remove("is-active");
        circle.setAttribute("aria-selected", "false");
      }
    });
  }

  function applyTheme(theme, persist = true) {
    if (!SUPPORTED_THEMES.includes(theme)) {
      theme = "dark";
    }
    root.dataset.theme = theme;
    root.style.colorScheme = (theme === "light" || theme === "white-purple") ? "light" : "dark";
    if (themeMeta) {
      if (theme === "black-purple") themeMeta.content = "#0d0814";
      else if (theme === "white-purple") themeMeta.content = "#f6f3fc";
      else if (theme === "mono") themeMeta.content = "#000000";
      else if (theme === "github") themeMeta.content = "#0d1117";
      else if (theme === "ocean") themeMeta.content = "#030c1a";
      else if (theme === "ember") themeMeta.content = "#120a09";
      else if (theme === "light") themeMeta.content = "#f0f0f2";
      else themeMeta.content = "#101014";
    }
    syncControls(theme);
    if (persist) {
      try {
        window.localStorage.setItem(preferenceKey, theme);
      } catch (error) {
        console.warn("Code-Karo.dev could not save the theme preference.", error);
      }
    }
    document.dispatchEvent(new CustomEvent("code-karo-theme-change", { detail: { theme } }));
  }

  function revealTheme(button, theme) {
    const doc = document;
    if (
      typeof doc.startViewTransition !== "function"
      || reducedMotion.matches
      || revealRunning
      || doc.activeViewTransition
    ) {
      applyTheme(theme);
      return;
    }

    const bounds = button.getBoundingClientRect();
    const x = bounds.left + bounds.width / 2;
    const y = bounds.top + bounds.height / 2;
    const radius = Math.hypot(
      Math.max(x, window.innerWidth - x),
      Math.max(y, window.innerHeight - y),
    );
    root.setAttribute(revealAttribute, "");
    revealRunning = true;

    let transition;
    try {
      transition = doc.startViewTransition(() => applyTheme(theme));
    } catch (error) {
      root.removeAttribute(revealAttribute);
      revealRunning = false;
      applyTheme(theme);
      console.warn("Theme reveal was unavailable; changed theme without the reveal.", error);
      return;
    }

    transition.ready.then(() => {
      root.animate(
        {
          clipPath: [
            `circle(0px at ${x}px ${y}px)`,
            `circle(${radius}px at ${x}px ${y}px)`,
          ],
        },
        {
          duration: 500,
          easing: "cubic-bezier(.4, 0, .2, 1)",
          pseudoElement: "::view-transition-new(root)",
        },
      );
    }, () => {});

    const cleanup = () => {
      root.removeAttribute(revealAttribute);
      revealRunning = false;
    };
    transition.finished.then(cleanup, cleanup);
  }

  window.CodeKaroTheme = {
    applyTheme,
    readTheme,
    SUPPORTED_THEMES
  };

  applyTheme(readTheme(), false);

  document.addEventListener("DOMContentLoaded", () => {
    syncControls(root.dataset.theme);

    // Toggle theme palette dropdown
    document.addEventListener("click", event => {
      const paletteToggle = event.target.closest("[data-theme-palette-toggle]");
      const dropdowns = document.querySelectorAll("[data-theme-palette-dropdown]");

      if (paletteToggle) {
        event.stopPropagation();
        const wrapper = paletteToggle.closest("[data-theme-palette-wrapper]");
        const dropdown = wrapper ? wrapper.querySelector("[data-theme-palette-dropdown]") : null;
        if (dropdown) {
          const isOpen = dropdown.classList.contains("is-open");
          dropdowns.forEach(d => d.classList.remove("is-open"));
          if (!isOpen) dropdown.classList.add("is-open");
        }
        return;
      }

      // Handle circle selection
      const circleBtn = event.target.closest("[data-theme-val]");
      if (circleBtn) {
        const selectedTheme = circleBtn.getAttribute("data-theme-val");
        if (selectedTheme) {
          revealTheme(circleBtn, selectedTheme);
          dropdowns.forEach(d => d.classList.remove("is-open"));
        }
        return;
      }

      // Close dropdown when clicking outside
      dropdowns.forEach(d => {
        if (!d.contains(event.target)) {
          d.classList.remove("is-open");
        }
      });

      // Dark / light fallback toggle button
      const switchBtn = event.target.closest("[data-theme-switch]");
      if (switchBtn) {
        const currentTheme = root.dataset.theme;
        const isLight = currentTheme === "light" || currentTheme === "white-purple";
        const nextTheme = isLight ? "dark" : "light";
        revealTheme(switchBtn, nextTheme);
      }
    });
  });
})();
