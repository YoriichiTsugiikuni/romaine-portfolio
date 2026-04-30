<template>
  <section class="section" id="education">
    <div class="container">
      <p class="section-label">My Background</p>
      <h2 class="section-title">Education</h2>

      <div class="education-grid">
        <div v-for="edu in education" :key="edu.id" class="edu-card">
          <div class="edu-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
              <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
            </svg>
          </div>
          <div class="edu-info">
            <h3 class="edu-degree">{{ edu.degree }} in <span class="gold">{{ edu.field }}</span></h3>
            <p class="edu-institution">{{ edu.institution }}</p>
            <p class="edu-years">{{ edu.start_year }} — {{ edu.end_year }}</p>
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
const education = computed(() => store.education)
</script>

<style scoped>
.education-grid {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-top: 56px;
}

.edu-card {
  display: flex;
  align-items: flex-start;
  gap: 24px;
  background: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 32px;
  transition: var(--transition);
}

.edu-card:hover {
  border-color: var(--color-primary);
}

.edu-icon {
  color: var(--color-primary);
  flex-shrink: 0;
  margin-top: 4px;
}

.edu-degree {
  font-size: 20px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 6px;
}

.gold {
  color: var(--color-primary);
}

.edu-institution {
  font-size: 15px;
  color: var(--color-text-muted);
  margin-bottom: 6px;
}

.edu-years {
  font-size: 13px;
  color: var(--color-text-muted);
}
</style>