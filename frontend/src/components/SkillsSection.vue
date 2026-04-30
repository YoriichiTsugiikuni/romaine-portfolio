<template>
  <section class="section" id="skills" style="background: var(--color-bg-secondary);">
    <div class="container">
      <p class="section-label">What I Know</p>
      <h2 class="section-title">Skills & Technologies</h2>
      <p class="section-subtitle">Technologies I've worked with across full-stack development.</p>

      <div class="skills-grid">
        <div v-for="category in categories" :key="category.name" class="skill-category">
          <h3 class="category-title">{{ category.label }}</h3>
          <div class="skill-list">
            <div v-for="skill in getSkillsByCategory(category.name)" :key="skill.id" class="skill-item">
              <div class="skill-header">
                <span class="skill-name">{{ skill.name }}</span>
                <span class="skill-percent gold">{{ skill.proficiency }}%</span>
              </div>
              <div class="skill-bar">
                <div class="skill-fill" :style="{ width: skill.proficiency + '%' }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { usePortfolioStore } from '../stores/portfolio'

const store = usePortfolioStore()
const skills = computed(() => store.skills)

const categories = [
  { name: 'language', label: 'Languages' },
  { name: 'framework', label: 'Frameworks' },
  { name: 'database', label: 'Databases' },
  { name: 'tool', label: 'Tools' }
]

function getSkillsByCategory(category) {
  return skills.value.filter(s => s.category === category)
}
</script>

<style scoped>
.skills-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  margin-top: 56px;
}

.category-title {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--color-primary);
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--color-border);
}

.skill-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.skill-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.skill-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.skill-name {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text);
}

.skill-percent {
  font-size: 13px;
  font-weight: 600;
}

.gold {
  color: var(--color-primary);
}

.skill-bar {
  height: 3px;
  background: var(--color-border);
  border-radius: 0;
  overflow: hidden;
}

.skill-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 0;
  transition: width 1s ease;
}

@media (max-width: 768px) {
  .skills-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
</style>