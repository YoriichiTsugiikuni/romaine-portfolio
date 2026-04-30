<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container navbar-inner">
      <a href="#hero" class="navbar-logo">RD</a>

      <ul class="navbar-links">
        <li><a href="#about">About</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#experience">Experience</a></li>
        <li><a href="#education">Education</a></li>
        <li><a href="#contact" class="btn btn-primary navbar-cta">Contact</a></li>
      </ul>

      <button class="hamburger" @click="menuOpen = !menuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>

    <div class="mobile-menu" :class="{ open: menuOpen }">
      <a href="#about" @click="menuOpen = false">About</a>
      <a href="#skills" @click="menuOpen = false">Skills</a>
      <a href="#projects" @click="menuOpen = false">Projects</a>
      <a href="#experience" @click="menuOpen = false">Experience</a>
      <a href="#education" @click="menuOpen = false">Education</a>
      <a href="#contact" @click="menuOpen = false">Contact</a>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const menuOpen = ref(false)

function handleScroll() {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 20px 0;
  transition: var(--transition);
  background: transparent;
}

.navbar.scrolled {
  background: rgba(15, 15, 15, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--color-border);
  padding: 14px 0;
}

.navbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  font-size: 20px;
  font-weight: 700;
  color: var(--color-primary);
  letter-spacing: 1px;
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
}

.navbar-links a {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text);
  transition: var(--transition);
}

.navbar-links a:hover {
  color: var(--color-primary);
}

.navbar-cta {
  padding: 8px 20px !important;
  font-size: 14px !important;
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.hamburger span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--color-text);
  transition: var(--transition);
}

.mobile-menu {
  display: none;
  flex-direction: column;
  padding: 16px 24px;
  background: var(--color-bg-secondary);
  border-top: 1px solid var(--color-border);
}

.mobile-menu a {
  padding: 12px 0;
  font-size: 15px;
  font-weight: 500;
  color: var(--color-text-muted);
  border-bottom: 1px solid var(--color-border);
}

@media (max-width: 768px) {
  .navbar-links { display: none; }
  .hamburger { display: flex; }
  .mobile-menu.open { display: flex; }
}
</style>