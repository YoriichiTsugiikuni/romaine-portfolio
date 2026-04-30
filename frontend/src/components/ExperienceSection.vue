<template>
  <section class="section" id="experience" style="background: var(--color-bg-secondary);">
    <div class="container">
      <p class="section-label">Where I've Been</p>
      <h2 class="section-title">Experience</h2>

      <div class="timeline">
        <div v-for="exp in experience" :key="exp.id" class="timeline-item">
          <div class="timeline-marker"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <div>
                <h3 class="timeline-role">{{ exp.role }}</h3>
                <p class="timeline-company">
                  <span class="gold">{{ exp.company }}</span>
                </p>
              </div>
              <span class="timeline-date">
                {{ exp.start_date }} — {{ exp.current ? 'Present' : exp.end_date }}
              </span>
            </div>
            <p class="timeline-description">{{ exp.description }}</p>
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
const experience = computed(() => store.experience)
</script>

<style scoped>
.timeline {
  margin-top: 56px;
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
  padding-left: 32px;
  border-left: 1px solid var(--color-border);
}

.timeline-item {
  position: relative;
  padding-bottom: 48px;
}

.timeline-item:last-child {
  padding-bottom: 0;
}

.timeline-marker {
  position: absolute;
  left: -39px;
  top: 6px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--color-primary);
  border: 2px solid var(--color-bg-secondary);
}

.timeline-content {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 28px;
  transition: var(--transition);
}

.timeline-content:hover {
  border-color: var(--color-primary);
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  gap: 16px;
  flex-wrap: wrap;
}

.timeline-role {
  font-size: 18px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 4px;
}

.timeline-company {
  font-size: 14px;
  font-weight: 500;
}

.gold {
  color: var(--color-primary);
}

.timeline-date {
  font-size: 12px;
  color: var(--color-text-muted);
  white-space: nowrap;
  padding: 4px 10px;
  border: 1px solid var(--color-border);
  border-radius: 2px;
}

.timeline-description {
  font-size: 14px;
  color: var(--color-text-muted);
  line-height: 1.8;
}
</style>