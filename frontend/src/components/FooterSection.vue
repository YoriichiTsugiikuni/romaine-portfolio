<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <span class="footer-logo">RD</span>
          <p class="footer-tagline">
            Software Engineer · Electronics Engineer · Problem Solver
          </p>
          <p class="footer-sub">
            Based in Jamaica · Open to remote & on-site opportunities
          </p>
        </div>

        <div class="footer-col">
          <p class="footer-col-title">Navigation</p>
          <a href="#about">About</a>
          <a href="#skills">Skills</a>
          <a href="#projects">Projects</a>
          <a href="#experience">Experience</a>
          <a href="#education">Education</a>
          <a href="#contact">Contact</a>
        </div>

        <div class="footer-col">
          <p class="footer-col-title">Connect</p>
          <a href="https://github.com/YoriichiTsugiikuni" target="_blank">GitHub</a>
          <a href="https://www.linkedin.com/in/romaine-dixon-333754219/" target="_blank">LinkedIn</a>
          <a href="mailto:romainedixon66@gmail.com">Email</a>
          <a href="https://drive.google.com/file/d/1dOSL7iOeIYEQsD-vGMy_cCzccgVLg1Dj/preview" target="_blank">Resume</a>
        </div>
      </div>

      <div class="footer-divider"></div>

      <div class="footer-bottom">
        <p>© {{ currentYear }} <span class="gold">Romaine Dixon</span>. All rights reserved.</p>
        <p class="footer-stack">Built with Flask · Vue 3 · PostgreSQL</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear()
</script>

<style scoped>
.footer {
  background: #0a0a0a;
  border-top: 1px solid var(--color-border);
  padding: 72px 0 0;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 60px;
  padding-bottom: 56px;
}

.footer-logo {
  font-size: 32px;
  font-weight: 700;
  color: var(--color-primary);
  letter-spacing: 2px;
  display: block;
  margin-bottom: 16px;
}

.footer-tagline {
  font-size: 14px;
  color: var(--color-text);
  font-weight: 500;
  margin-bottom: 8px;
}

.footer-sub {
  font-size: 13px;
  color: var(--color-text-muted);
  line-height: 1.7;
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-col-title {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: 4px;
}

.footer-col a {
  font-size: 14px;
  color: var(--color-text-muted);
  transition: var(--transition);
}

.footer-col a:hover {
  color: var(--color-primary);
  padding-left: 4px;
}

.footer-divider {
  height: 1px;
  background: var(--color-border);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 0;
  flex-wrap: wrap;
  gap: 12px;
}

.footer-bottom p {
  font-size: 13px;
  color: var(--color-text-muted);
}

.gold {
  color: var(--color-primary);
}

.footer-stack {
  font-size: 12px;
  color: var(--color-border);
}

@media (max-width: 768px) {
  .footer-top {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .footer-bottom {
    flex-direction: column;
    text-align: center;
  }
}
</style>