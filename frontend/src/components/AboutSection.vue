<template>
  <section class="section" id="about">
    <div class="container about-inner">
      <div class="about-text">
        <p class="section-label">About Me</p>
        <h2 class="section-title">Who I Am</h2>
        <p class="about-bio">{{ profile?.bio ?? 'Loading...' }}</p>
        <p class="about-extra">
          I'm currently pursuing my BSc in Software Engineering at the
          <span class="gold">University of the West Indies</span>, where I've worked on
          full-stack projects using Flask, Vue 3, and PostgreSQL. I'm passionate about
          writing clean code and building things that actually work in the real world.
        </p>
        <a :href="profile?.resume_url ?? '#'" target="_blank" class="btn btn-outline" style="margin-top: 28px;">
          Download Resume
        </a>
      </div>

      <div class="about-stats">
        <div class="stat-card">
          <span class="stat-number gold">5+</span>
          <span class="stat-label">Years of coding</span>
        </div>
        <div class="stat-card">
          <span class="stat-number gold">5+</span>
          <span class="stat-label">Projects built</span>
        </div>
        <div class="stat-card">
          <span class="stat-number gold">10+</span>
          <span class="stat-label">Technologies used</span>
        </div>
        <div class="stat-card">
          <span class="stat-number gold">UWI</span>
          <span class="stat-label">BSc Software Engineering</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { usePortfolioStore } from '../stores/portfolio'

const store = usePortfolioStore()
const profile = computed(() => store.profile)
</script>

<style scoped>
.about-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.about-bio {
  font-size: 16px;
  color: var(--color-text-muted);
  margin-bottom: 16px;
  line-height: 1.8;
}

.about-extra {
  font-size: 15px;
  color: var(--color-text-muted);
  line-height: 1.8;
}

.gold {
  color: var(--color-primary);
  font-weight: 600;
}

.about-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.stat-card {
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 28px 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stat-number {
  font-size: 32px;
  font-weight: 700;
}

.stat-label {
  font-size: 13px;
  color: var(--color-text-muted);
}

@media (max-width: 768px) {
  .about-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
</style>