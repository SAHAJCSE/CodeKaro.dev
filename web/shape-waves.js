(() => {
  const canvas = document.querySelector(".hero-canvas");
  const hero = canvas?.parentElement;
  const context = canvas?.getContext("2d", { alpha: true });
  if (!canvas || !hero || !context) return;

  const cellSize = 10;
  const dotSize = 0.75;
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const maskCanvas = document.createElement("canvas");
  const maskContext = maskCanvas.getContext("2d", { willReadFrequently: true });
  const ripples = [];
  let width = 0;
  let height = 0;
  let scale = 1;
  let maskPixels = null;
  let frame = 0;
  let lastFrame = 0;
  let visible = true;
  let introStarted = performance.now();
  let pointer = null;

  function colorToRgb(color) {
    const match = color.match(/^#([\da-f]{3}|[\da-f]{6})$/i);
    if (!match) return [146, 146, 146];
    let hex = match[1];
    if (hex.length === 3) hex = hex.replace(/./g, character => character + character);
    return [0, 2, 4].map(offset => parseInt(hex.slice(offset, offset + 2), 16));
  }

  function themeColors() {
    const styles = getComputedStyle(document.documentElement);
    return {
      base: colorToRgb(styles.getPropertyValue("--shape-color").trim() || "#929292"),
      hover: colorToRgb(styles.getPropertyValue("--shape-hover-color").trim() || "#ffffff")
    };
  }

  function createMask() {
    if (!width || !height || !maskContext) return;
    maskCanvas.width = Math.max(1, Math.round(width));
    maskCanvas.height = Math.max(1, Math.round(height));
    maskContext.clearRect(0, 0, maskCanvas.width, maskCanvas.height);
    maskContext.fillStyle = "#fff";
    maskContext.textAlign = "center";
    maskContext.textBaseline = "middle";
    let fontSize = height * 0.6;
    maskContext.font = `500 ${fontSize}px Geist, "Geist Sans", system-ui, sans-serif`;
    const maxWidth = width * 0.9;
    const textWidth = maskContext.measureText("</>").width;
    if (textWidth > maxWidth) {
      fontSize *= maxWidth / textWidth;
      maskContext.font = `500 ${fontSize}px Geist, "Geist Sans", system-ui, sans-serif`;
    }
    maskContext.fillText("</>", width / 2, height / 2);
    maskPixels = maskContext.getImageData(0, 0, maskCanvas.width, maskCanvas.height).data;
  }

  function resize() {
    const bounds = hero.getBoundingClientRect();
    width = bounds.width;
    height = bounds.height;
    scale = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.max(1, Math.round(width * scale));
    canvas.height = Math.max(1, Math.round(height * scale));
    context.setTransform(scale, 0, 0, scale, 0, 0);
    createMask();
    draw(performance.now());
  }

  function maskAt(x, y) {
    if (!maskPixels) return 0;
    const column = Math.max(0, Math.min(maskCanvas.width - 1, Math.floor(x)));
    const row = Math.max(0, Math.min(maskCanvas.height - 1, Math.floor(y)));
    return maskPixels[(row * maskCanvas.width + column) * 4 + 3] / 255;
  }

  function rippleAt(x, y, now) {
    let strength = 0;
    for (let index = ripples.length - 1; index >= 0; index -= 1) {
      const ripple = ripples[index];
      const age = (now - ripple.time) / 1000;
      if (age > 1.5) {
        ripples.splice(index, 1);
        continue;
      }
      const distance = Math.hypot(x - ripple.x, y - ripple.y);
      const radius = age * 190;
      const ring = Math.exp(-((distance - radius) ** 2) / 1500) * Math.exp(-age * 1.5);
      strength = Math.max(strength, ring * ripple.strength);
    }
    return strength;
  }

  function drawShape(x, y, size, shape) {
    context.beginPath();
    if (shape === 0) {
      context.rect(x - size / 2, y - size / 2, size, size);
    } else if (shape === 1) {
      context.arc(x, y, size / 2, 0, Math.PI * 2);
    } else {
      context.moveTo(x, y - size / 2);
      context.lineTo(x + size / 2, y + size / 2);
      context.lineTo(x - size / 2, y + size / 2);
      context.closePath();
    }
    context.fill();
  }

  function draw(now) {
    if (!width || !height) return;
    const motion = reducedMotion.matches ? 0 : now * 0.00035;
    const colors = themeColors();
    const isLight = document.documentElement.dataset.theme === "light";
    const columns = Math.ceil(width / cellSize);
    const rows = Math.ceil(height / cellSize);
    const intro = reducedMotion.matches ? 1 : Math.min(1, (now - introStarted) / 1600);

    context.clearRect(0, 0, width, height);
    for (let row = 0; row < rows; row += 1) {
      const y = row * cellSize + cellSize / 2;
      for (let column = 0; column < columns; column += 1) {
        const x = column * cellSize + cellSize / 2;
        const field = Math.sin(x * 0.009 + motion)
          * Math.sin(y * 0.012 - motion * 0.72)
          * 0.5 + Math.sin((x + y) * 0.004 + motion * 0.5) * 0.25;
        const text = maskAt(x, y);
        const ripple = rippleAt(x, y, now);
        const energy = Math.max(0, Math.min(1, 0.38 + field * 0.35 + text * 0.5 + ripple * 0.45));
        const random = (Math.sin(column * 127.1 + row * 311.7) * 43758.5453) % 1;
        const density = Math.max(0, Math.min(1, 0.18 + energy * 0.58 + text * 0.3 + ripple * 0.18));
        if (Math.abs(random) > density) continue;

        const introReveal = Math.max(0, Math.min(1, (intro - (y / height) * 0.2) / 0.8));
        if (introReveal <= 0) continue;
        const highlight = Math.max(text * 0.18, ripple);
        const color = colors.base.map((channel, index) =>
          Math.round(channel + (colors.hover[index] - channel) * highlight)
        );
        const size = cellSize * dotSize * (0.25 + energy * 0.75);
        const shape = (column * 73856093 + row * 19349663) >>> 0;
        context.globalAlpha = (isLight ? 0.16 : 0.22) + energy * (isLight ? 0.55 : 0.65);
        context.globalAlpha *= introReveal;
        context.fillStyle = `rgb(${color.join(" ")})`;
        drawShape(x, y, size, shape % 3);
      }
    }
    context.globalAlpha = 1;
  }

  function animate(now) {
    frame = 0;
    if (document.hidden || !visible) return;
    if (now - lastFrame < 40) {
      frame = requestAnimationFrame(animate);
      return;
    }
    draw(now);
    lastFrame = now;
    if (!reducedMotion.matches) frame = requestAnimationFrame(animate);
  }

  function wake() {
    if (frame || document.hidden || !visible) return;
    frame = requestAnimationFrame(animate);
  }

  function handlePointerMove(event) {
    const bounds = hero.getBoundingClientRect();
    const next = { x: event.clientX - bounds.left, y: event.clientY - bounds.top, time: performance.now() };
    if (pointer) {
      const distance = Math.hypot(next.x - pointer.x, next.y - pointer.y);
      if (distance > 6) {
        ripples.push({
          x: next.x,
          y: next.y,
          time: next.time,
          strength: Math.min(1, 0.25 + distance * 0.005)
        });
        if (ripples.length > 12) ripples.shift();
      }
    }
    pointer = next;
    wake();
  }

  const resizeObserver = new ResizeObserver(resize);
  resizeObserver.observe(hero);
  hero.addEventListener("pointermove", handlePointerMove, { passive: true });
  document.addEventListener("visibilitychange", wake);
  reducedMotion.addEventListener("change", wake);
  document.addEventListener("code-karo-theme-change", () => draw(performance.now()));

  if ("IntersectionObserver" in window) {
    const visibilityObserver = new IntersectionObserver(entries => {
      visible = entries.some(entry => entry.isIntersecting);
      if (visible) wake();
      else if (frame) {
        cancelAnimationFrame(frame);
        frame = 0;
      }
    });
    visibilityObserver.observe(hero);
  }

  resize();
  wake();
})();
