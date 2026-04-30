<template>
  <section class="hero" id="hero">
    <div class="container hero-inner">
      <div class="hero-content">
        <p class="section-label">Welcome to my portfolio</p>
        <h1 class="hero-name">
          Hi, I'm <span class="highlight">{{ profile?.name ?? 'Romaine Dixon' }}</span>
        </h1>
        <h2 class="hero-title">{{ profile?.title ?? 'Software Engineer' }}</h2>
        <p class="hero-tagline">{{ profile?.tagline ?? 'Building clean, scalable web applications' }}</p>

        <div class="hero-actions">
          <a href="#projects" class="btn btn-primary">View My Work</a>
          <a href="#contact" class="btn btn-outline">Contact Me</a>
        </div>

        <div class="hero-links">
          <a :href="profile?.github_url ?? '#'" target="_blank" rel="noopener">GitHub</a>
          <span class="divider">·</span>
          <a :href="profile?.linkedin_url ?? '#'" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>

      <div class="hero-visual">
        <div class="avatar-ring">
            <img 
             v-if="profile?.avatar_url" 
             :src="profile.avatar_url" 
             alt="Romaine Dixon" 
             class="avatar-img"
                />
         <div v-else class="avatar-initials">RD</div>
            </div>
        <div class="floating-card card-one">
          <span class="card-dot"></span> Flask API running
        </div>
        <div class="floating-card card-two">
          <span class="card-dot green"></span> Vue 3 connected
        </div>
      </div>
    </div>

    <div class="hero-scroll" :style="{ opacity: scrollOpacity, transition: 'opacity 0.3s ease' }">
      <span>Scroll down</span>
      <div class="scroll-line"></div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { usePortfolioStore } from '../stores/portfolio'

const store = usePortfolioStore()
const profile = computed(() => store.profile)

const scrollOpacity = ref(1)

function handleScroll() {
  const scrollY = window.scrollY
  scrollOpacity.value = Math.max(0, 1 - scrollY / 200)
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: var(--color-bg);
  padding-top: 80px;
  position: relative;
  
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.hero-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 60px;
  padding-top: 40px;
}

.hero-name {
  font-size: 52px;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 12px;
  color: var(--color-text);
}

.highlight {
  color: var(--color-primary);
}

.hero-title {
  font-size: 22px;
  font-weight: 500;
  color: var(--color-text-muted);
  margin-bottom: 16px;
}

.hero-tagline {
  font-size: 16px;
  color: var(--color-text-muted);
  max-width: 480px;
  margin-bottom: 36px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  gap: 16px;
  margin-bottom: 28px;
  flex-wrap: wrap;
}

.hero-links {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
}

.hero-links a {
  color: var(--color-text-muted);
  font-weight: 500;
  transition: var(--transition);
}

.hero-links a:hover {
  color: var(--color-primary);
}

.divider {
  color: var(--color-border);
}

.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 400px;
}

.avatar-ring {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  border: 2px solid var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg-secondary);
}

.avatar-initials {
  font-size: 64px;
  font-weight: 700;
  color: var(--color-primary);
  letter-spacing: 2px;
}

.floating-card {
  position: absolute;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 10px 16px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text);
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.card-one { top: 60px; right: 20px; }
.card-two { bottom: 80px; left: 20px; }

.card-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary);
  display: inline-block;
}

.card-dot.green {
  background: #10b981;
}

.hero-scroll {
  position: absolute;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--color-text-muted);
  font-size: 12px;
  letter-spacing: 1px;
}

.scroll-line {
  width: 1px;
  height: 40px;
  background: var(--color-border);
}

@media (max-width: 768px) {
  .hero-inner {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .hero-name { font-size: 36px; }
  .hero-visual { display: none; }
  .hero-actions { justify-content: center; }
  .hero-links { justify-content: center; }
}
</style>