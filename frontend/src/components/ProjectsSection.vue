<template>
  <section class="section" id="projects">
    <div class="container">
      <p class="section-label">What I've Built</p>
      <h2 class="section-title">Projects</h2>
      <p class="section-subtitle">A selection of real projects I've designed and developed.</p>

      <div class="projects-grid">
        <div v-for="project in projects" :key="project.id" class="project-card">
          <div class="project-header">
            <div class="project-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="16 18 22 12 16 6"></polyline>
                <polyline points="8 6 2 12 8 18"></polyline>
              </svg>
            </div>
          </div>

          <h3 class="project-title">{{ project.title }}</h3>
          <p class="project-description">{{ project.description }}</p>

          <div class="project-tech">
            <span v-for="tech in project.tech_stack.split(',')" :key="tech" class="tech-tag">
              {{ tech.trim() }}
            </span>
          </div>

          <div v-if="project.featured" class="featured-badge">Featured</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { usePortfolioStore } from '../stores/portfolio'

const store = usePortfolioStore()
const projects = computed(() => store.projects)
</script>

<style scoped>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  margin-top: 56px;
}

.project-card {
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 32px;
  position: relative;
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.project-card:hover {
  border-color: var(--color-primary);
  transform: translateY(-4px);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-icon {
  color: var(--color-primary);
}

.project-title {
  font-size: 20px;
  font-weight: 600;
  color: var(--color-text);
}

.project-description {
  font-size: 14px;
  color: var(--color-text-muted);
  line-height: 1.7;
  flex: 1;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.tech-tag {
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  color: var(--color-primary);
  border-radius: 2px;
}

.featured-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: 3px 8px;
  border-radius: 2px;
}
</style>