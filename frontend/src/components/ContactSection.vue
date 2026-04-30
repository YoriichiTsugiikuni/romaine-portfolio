<template>
  <section class="section" id="contact" style="background: var(--color-bg-secondary);">
    <div class="container contact-inner">
      <div class="contact-text">
        <p class="section-label">Get In Touch</p>
        <h2 class="section-title">Contact Me</h2>
        <p class="section-subtitle">
          Whether you have an opportunity, a question, or just want to connect —
          my inbox is always open.
        </p>

        <div class="contact-links">
          <a href="mailto:romainedixon66@gmail.com" class="contact-item">
            <span class="contact-icon">✉</span>
            <span>romainedixon66@gmail.com</span>
          </a>
          <a href="https://www.linkedin.com/in/romaine-dixon-333754219/" target="_blank" class="contact-item">
            <span class="contact-icon">in</span>
            <span>Connect on LinkedIn</span>
          </a>
          <a href="https://github.com/YoriichiTsugiikuni" target="_blank" class="contact-item">
            <span class="contact-icon">gh</span>
            <span>Follow on GitHub</span>
          </a>
        </div>
      </div>

      <form class="contact-form" @submit.prevent="submitForm">
        <div class="form-group">
          <label>Name</label>
          <input v-model="form.name" type="text" placeholder="Your name" required />
        </div>
        <div class="form-group">
          <label>Email</label>
          <input v-model="form.email" type="email" placeholder="your@email.com" required />
        </div>
        <div class="form-group">
          <label>Subject</label>
          <input v-model="form.subject" type="text" placeholder="What's this about?" required />
        </div>
        <div class="form-group">
          <label>Message</label>
          <textarea v-model="form.body" rows="5" placeholder="Your message..." required></textarea>
        </div>

        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Sending...' : 'Send Message' }}
        </button>

        <p v-if="success" class="form-success">Message sent successfully. I'll be in touch soon.</p>
        <p v-if="error" class="form-error">Something went wrong. Please try again.</p>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { usePortfolioStore } from '../stores/portfolio'
import { sendMessage } from '../api'

const store = usePortfolioStore()
const profile = computed(() => store.profile)

const loading = ref(false)
const success = ref(false)
const error = ref(false)

const form = ref({
  name: '',
  email: '',
  subject: '',
  body: ''
})

async function submitForm() {
  loading.value = true
  success.value = false
  error.value = false
  try {
    await sendMessage(form.value)
    success.value = true
    form.value = { name: '', email: '', subject: '', body: '' }
  } catch (err) {
    error.value = true
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.contact-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: flex-start;
}

.contact-links {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 40px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 16px;
  color: var(--color-text-muted);
  font-size: 14px;
  font-weight: 500;
  transition: var(--transition);
}

.contact-item:hover {
  color: var(--color-primary);
}

.contact-icon {
  width: 40px;
  height: 40px;
  border: 1px solid var(--color-border);
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  color: var(--color-primary);
  flex-shrink: 0;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-muted);
}

.form-group input,
.form-group textarea {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: 2px;
  padding: 12px 16px;
  color: var(--color-text);
  font-family: var(--font-main);
  font-size: 14px;
  transition: var(--transition);
  outline: none;
  resize: vertical;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--color-primary);
}

.form-group input::placeholder,
.form-group textarea::placeholder {
  color: var(--color-text-muted);
}

.form-success {
  font-size: 14px;
  color: #10b981;
}

.form-error {
  font-size: 14px;
  color: #ef4444;
}

@media (max-width: 768px) {
  .contact-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}
</style>