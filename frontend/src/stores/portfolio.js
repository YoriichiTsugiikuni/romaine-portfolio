import { defineStore } from 'pinia'
import { getProfile, getProjects, getSkills, getExperience, getEducation } from '../api'

export const usePortfolioStore = defineStore('portfolio', {
  state: () => ({
    profile: null,
    projects: [],
    skills: [],
    experience: [],
    education: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchAll() {
      this.loading = true
      try {
        const [profile, projects, skills, experience, education] = await Promise.all([
          getProfile(),
          getProjects(),
          getSkills(),
          getExperience(),
          getEducation()
        ])
        this.profile = profile.data
        this.projects = projects.data
        this.skills = skills.data
        this.experience = experience.data
        this.education = education.data
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    }
  }
})
