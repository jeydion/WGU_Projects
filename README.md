# WGU MSCS Projects

[![GitHub Tests](https://github.com/jeydion/WGU_Projects/actions/workflows/test-d793.yml/badge.svg)](https://github.com/jeydion/WGU_Projects/actions)
[![GitLab Pipeline](https://gitlab.com/jhughe13/WGU_Projects/badges/main/pipeline.svg)](https://gitlab.com/jhughe13/WGU_Projects/-/pipelines)
[![Coverage](https://gitlab.com/jhughe13/WGU_Projects/badges/main/coverage.svg)](https://jhughe13.gitlab.io/WGU_Projects/)

Master of Science in Computer Science - Western Governors University

## Courses

### D793 - Formal Languages Overview
- **Status**: In Progress
- **Coverage Report**: [View Report](https://jhughe13.gitlab.io/WGU_Projects/d793/)
- **Tests**: Fortran-to-Python equivalence testing

### D794 - Computer Architecture  
- **Status**: In Progress
- **Submission**: Portal-based (no GitLab remote)

## CI/CD Pipeline

This repository uses dual CI/CD:
- **GitHub Actions**: Runs tests on every push
- **GitLab CI/CD**: Advanced coverage reporting and GitLab Pages

## Local Development
```bash
# Run tests locally
cd d793-working
pytest --cov=python --cov-report=html

# Commit triggers automatic testing and submission
git commit -m "Your message"
```

## Automated Workflow

1. ✅ Pre-commit: Runs tests locally
2. ✅ Post-commit: Auto-submits to WGU GitLab
3. ✅ GitHub Actions: Cloud testing
4. ✅ GitLab CI/CD: Coverage reports + Pages

