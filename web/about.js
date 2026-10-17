/**
 * Code-Karo.dev — About Page Script
 * Data-driven rendering for developer cards in Home's purple design language.
 */

(() => {
  "use strict";

  // Purple Verified Badge SVG
  function createVerifiedBadge() {
    const span = document.createElement("span");
    span.className = "card-badge";
    span.setAttribute("aria-label", "Verified Team Member");
    span.setAttribute("title", "Verified Team Member");
    span.innerHTML = `
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
      </svg>
    `;
    return span;
  }

  // LinkedIn SVG Icon
  function createLinkedInIcon() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "currentColor");
    svg.setAttribute("aria-hidden", "true");
    svg.innerHTML = `<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.64c-.88 0-1.6.72-1.6 1.6s.72 1.6 1.6 1.6 1.6-.72 1.6-1.6-.72-1.6-1.6-1.6z"/>`;
    return svg;
  }

  // GitHub SVG Icon
  function createGitHubIcon() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "currentColor");
    svg.setAttribute("aria-hidden", "true");
    svg.innerHTML = `<path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>`;
    return svg;
  }

  // Copy SVG Icon
  function createCopyIcon() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    svg.innerHTML = `
      <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
      <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
    `;
    return svg;
  }

  // Checkmark SVG Icon
  function createCheckIcon() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", "2.5");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    svg.innerHTML = `<polyline points="20 6 9 17 4 12"></polyline>`;
    return svg;
  }

  // Initials generator
  function getInitials(name) {
    if (!name) return "CK";
    const parts = name.trim().split(/\s+/);
    if (parts.length >= 2) {
      return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    }
    return name.slice(0, 2).toUpperCase();
  }

  // Copy with fallback
  function copyTextToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise((resolve, reject) => {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.left = "-999999px";
      textarea.style.top = "-999999px";
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      try {
        const success = document.execCommand("copy");
        document.body.removeChild(textarea);
        if (success) resolve();
        else reject(new Error("Copy command failed"));
      } catch (err) {
        document.body.removeChild(textarea);
        reject(err);
      }
    });
  }

  // Render Single Developer Card
  function renderCard(member, index) {
    const card = document.createElement("article");
    card.className = "dev-card";
    const safeId = member.name.toLowerCase().replace(/[^a-z0-9]+/g, "-");
    card.id = `dev-${safeId}`;

    // --- Tab Strip Header (Editor Mockup) ---
    const tabStrip = document.createElement("div");
    tabStrip.className = "card-tab-strip";

    const tabDot = document.createElement("span");
    tabDot.className = "card-tab-dot";
    tabStrip.appendChild(tabDot);

    const tabLabel = document.createElement("span");
    const firstName = member.name.trim().split(/\s+/)[0].toLowerCase();
    tabLabel.textContent = `${firstName}.java`;
    tabStrip.appendChild(tabLabel);

    card.appendChild(tabStrip);

    // --- Photo Container ---
    const mediaWrap = document.createElement("div");
    mediaWrap.className = "card-photo-wrap";

    const img = document.createElement("img");
    img.className = "card-photo";
    img.src = member.image;
    img.alt = `${member.name} — ${member.role}`;
    img.loading = index < 4 ? "eager" : "lazy";

    // Fallback if image fails to load
    img.addEventListener("error", () => {
      img.remove();
      const fallback = document.createElement("div");
      fallback.className = "card-photo-fallback";
      if (member.gradient) {
        fallback.style.background = member.gradient;
      }
      const initials = document.createElement("span");
      initials.className = "card-initials";
      initials.textContent = getInitials(member.name);
      fallback.appendChild(initials);
      mediaWrap.appendChild(fallback);
    });

    mediaWrap.appendChild(img);
    card.appendChild(mediaWrap);

    // --- Body Area ---
    const body = document.createElement("div");
    body.className = "card-body";

    // Name Row
    const nameRow = document.createElement("div");
    nameRow.className = "card-name-row";

    const nameHeading = document.createElement("h3");
    nameHeading.className = "card-name";
    nameHeading.textContent = member.name;
    nameRow.appendChild(nameHeading);

    nameRow.appendChild(createVerifiedBadge());
    body.appendChild(nameRow);

    // Role
    const roleDiv = document.createElement("div");
    roleDiv.className = "card-role";
    roleDiv.textContent = member.role;
    body.appendChild(roleDiv);

    // Description (cleanly clamped, consistent min-height)
    const descP = document.createElement("p");
    descP.className = "card-desc";
    descP.textContent = member.description || "Core maintainer at Code-Karo.dev.";
    body.appendChild(descP);

    card.appendChild(body);

    // --- Footer Row ---
    const footer = document.createElement("div");
    footer.className = "card-footer";

    const linksGroup = document.createElement("div");
    linksGroup.className = "card-links-group";

    // LinkedIn
    if (member.linkedin) {
      const inBtn = document.createElement("a");
      inBtn.className = "card-btn-pill";
      inBtn.href = member.linkedin;
      inBtn.target = "_blank";
      inBtn.rel = "noopener noreferrer";
      inBtn.setAttribute("aria-label", `${member.name}'s LinkedIn Profile (opens in new tab)`);
      inBtn.appendChild(createLinkedInIcon());
      const inSpan = document.createElement("span");
      inSpan.textContent = "LinkedIn";
      inBtn.appendChild(inSpan);
      linksGroup.appendChild(inBtn);
    }

    // GitHub
    if (member.github) {
      const ghBtn = document.createElement("a");
      ghBtn.className = "card-btn-pill";
      ghBtn.href = member.github;
      ghBtn.target = "_blank";
      ghBtn.rel = "noopener noreferrer";
      ghBtn.setAttribute("aria-label", `${member.name}'s GitHub Profile (opens in new tab)`);
      ghBtn.appendChild(createGitHubIcon());
      const ghSpan = document.createElement("span");
      ghSpan.textContent = "GitHub";
      ghBtn.appendChild(ghSpan);
      linksGroup.appendChild(ghBtn);
    }

    footer.appendChild(linksGroup);

    // Copy Button
    if (member.github) {
      const copyBtn = document.createElement("button");
      copyBtn.type = "button";
      copyBtn.className = "card-btn-copy";
      copyBtn.setAttribute("aria-label", `Copy ${member.name}'s GitHub profile link`);
      copyBtn.title = "Copy GitHub link";

      const copyIcon = createCopyIcon();
      copyBtn.appendChild(copyIcon);

      const tooltip = document.createElement("span");
      tooltip.className = "card-tooltip";
      tooltip.textContent = "Copied!";
      copyBtn.appendChild(tooltip);

      copyBtn.addEventListener("click", async (e) => {
        e.preventDefault();
        try {
          await copyTextToClipboard(member.github);
          copyBtn.classList.add("is-copied");
          tooltip.textContent = "Copied!";
          copyIcon.replaceWith(createCheckIcon());

          setTimeout(() => {
            copyBtn.classList.remove("is-copied");
            const currentSvg = copyBtn.querySelector("svg");
            if (currentSvg) currentSvg.replaceWith(createCopyIcon());
          }, 1500);
        } catch (err) {
          console.error("Failed to copy URL:", err);
          tooltip.textContent = "Failed";
          copyBtn.classList.add("is-copied");
          setTimeout(() => copyBtn.classList.remove("is-copied"), 1500);
        }
      });

      footer.appendChild(copyBtn);
    }

    card.appendChild(footer);
    return card;
  }

  // Load team data
  async function loadTeam() {
    const grid = document.getElementById("team-grid");
    if (!grid) return;

    try {
      const res = await fetch("/team.json");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const team = await res.json();

      grid.innerHTML = "";
      team.forEach((member, index) => {
        const card = renderCard(member, index);
        grid.appendChild(card);
      });
    } catch (err) {
      console.warn("Could not load /team.json dynamically:", err);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadTeam);
  } else {
    loadTeam();
  }
})();
