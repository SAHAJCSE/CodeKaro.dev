/**
 * Code-Karo.dev — About Page Script
 * Loads and renders the 4 team cards from /team.json
 */
(() => {
  "use strict";

  const blueVerifiedBadgeSvg = `
    <svg class="verified-badge" viewBox="0 0 24 24" width="18" height="18" aria-label="Verified" fill="currentColor">
      <path fill="#38bdf8" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
    </svg>
  `;

  const linkedInSvg = `
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.64c-.88 0-1.6.72-1.6 1.6s.72 1.6 1.6 1.6 1.6-.72 1.6-1.6-.72-1.6-1.6-1.6z"/>
    </svg>
  `;

  const gitHubSvg = `
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
    </svg>
  `;

  function renderTeamCard(member) {
    const card = document.createElement("article");
    card.className = "team-card";

    // 1. Photo wrap on top with aspect ratio 4/5, gradient, and overlapping identity
    const photoWrap = document.createElement("div");
    photoWrap.className = "team-card__photo-wrap";

    const img = document.createElement("img");
    img.className = "team-card__photo";
    img.src = member.image;
    img.alt = `${member.name} — ${member.role}`;
    img.loading = "lazy";
    photoWrap.appendChild(img);

    const gradientOverlay = document.createElement("div");
    gradientOverlay.className = "team-card__photo-gradient";
    photoWrap.appendChild(gradientOverlay);

    // Overlapping identity: name with blue verified badge and role
    const identity = document.createElement("div");
    identity.className = "team-card__identity";

    const nameRow = document.createElement("div");
    nameRow.className = "team-card__name-row";

    const nameHeading = document.createElement("h3");
    nameHeading.className = "team-card__name";
    nameHeading.textContent = member.name;
    nameRow.appendChild(nameHeading);

    const badgeSpan = document.createElement("span");
    badgeSpan.innerHTML = blueVerifiedBadgeSvg;
    nameRow.appendChild(badgeSpan.firstElementChild);
    identity.appendChild(nameRow);

    const roleP = document.createElement("p");
    roleP.className = "team-card__role";
    roleP.textContent = member.role;
    identity.appendChild(roleP);

    photoWrap.appendChild(identity);
    card.appendChild(photoWrap);

    // 2. Full description (no clamping, no '...')
    const descP = document.createElement("p");
    descP.className = "team-card__desc";
    descP.textContent = member.description;
    card.appendChild(descP);

    // 3. Footer row with LinkedIn and GitHub buttons
    const footer = document.createElement("div");
    footer.className = "team-card__footer";

    if (member.linkedin) {
      const inBtn = document.createElement("a");
      inBtn.className = "team-card__btn";
      inBtn.href = member.linkedin;
      inBtn.target = "_blank";
      inBtn.rel = "noopener noreferrer";
      inBtn.setAttribute("aria-label", `${member.name} on LinkedIn`);
      inBtn.innerHTML = `${linkedInSvg}<span>LinkedIn</span>`;
      footer.appendChild(inBtn);
    }

    if (member.github) {
      const ghBtn = document.createElement("a");
      ghBtn.className = "team-card__btn";
      ghBtn.href = member.github;
      ghBtn.target = "_blank";
      ghBtn.rel = "noopener noreferrer";
      ghBtn.setAttribute("aria-label", `${member.name} on GitHub`);
      ghBtn.innerHTML = `${gitHubSvg}<span>GitHub</span>`;
      footer.appendChild(ghBtn);
    }

    card.appendChild(footer);
    return card;
  }

  async function loadTeam() {
    const grid = document.getElementById("team-grid");
    if (!grid) return;

    try {
      const res = await fetch("/team.json");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const members = await res.json();
      if (Array.isArray(members) && members.length > 0) {
        grid.replaceChildren();
        members.forEach(member => {
          grid.appendChild(renderTeamCard(member));
        });
      }
    } catch (err) {
      console.warn("Could not load dynamic team data:", err);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadTeam);
  } else {
    loadTeam();
  }
})();
