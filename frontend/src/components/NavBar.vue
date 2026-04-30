<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container navbar-inner">
      <a href="#hero" class="navbar-logo">RD</a>

      <ul class="navbar-links">
        <li v-for="link in links" :key="link.href">
          <a :href="link.href" :class="{ active: activeSection === link.section }" @click="setActive(link.section)">
            {{ link.label }}
          </a>
        </li>
      </ul>

      <button class="hamburger" @click="menuOpen = !menuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>

    <div class="mobile-menu" :class="{ open: menuOpen }">
      <a v-for="link in links" :key="link.href" :href="link.href" @click="menuOpen = false">{{ link.label }}</a>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const menuOpen = ref(false)
const activeSection = ref('hero')

const links = [
  { href: '#about', label: 'About', section: 'about' },
  { href: '#skills', label: 'Skills', section: 'skills' },
  { href: '#projects', label: 'Projects', section: 'projects' },
  { href: '#experience', label: 'Experience', section: 'experience' },
  { href: '#education', label: 'Education', section: 'education' },
  { href: '#contact', label: 'Contact', section: 'contact' },
]

const sections = ['hero', 'about', 'skills', 'projects', 'experience', 'education', 'contact']

function setActive(section) {
  activeSection.value = section
}

function handleScroll() {
  isScrolled.value = window.scrollY > 50

  for (const section of sections) {
    const el = document.getElementById(section)
    if (el) {
      const rect = el.getBoundingClientRect()
      if (rect.top <= 100 && rect.bottom >= 100) {
        activeSection.value = section
        break
      }
    }
  }
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
  gap: 8px;
  list-style: none;
}

.navbar-links a {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text);
  transition: var(--transition);
  padding: 8px 20px;
  border-radius: 2px;
  border: 1.5px solid transparent;
  letter-spacing: 0.3px;
}

.navbar-links a:hover {
  color: var(--color-primary);
  border-color: var(--color-primary);
  letter-spacing: 1px;
}

.navbar-links a.active {
  background: var(--color-primary);
  color: #0f0f0f;
  font-weight: 600;
  border-color: var(--color-primary);
  padding: 8px 20px;
  letter-spacing: 0.3px;
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