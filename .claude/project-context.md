# Portfolio Site Project Context

## Overview

This is Eric McKenna's professional portfolio website, hosted on GitHub Pages at [emckenna.github.io](https://emckenna.github.io). The site showcases professional experience, technical skills, and personal projects for a Senior Software Engineer with 25+ years of web development experience and 11+ years of Ruby on Rails expertise.

## Technology Stack

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (no frameworks)
- **Fonts**: Google Fonts (Inter)
- **Hosting**: GitHub Pages
- **Domain**: emckenna.github.io

## File Structure

```
emckenna.github.io/
├── index.html              # Main portfolio page (single-page app)
├── styles.css              # All styling (vanilla CSS, no preprocessors)
├── resume/                 # Resume files
│   ├── Eric_McKenna_Resume.pdf
│   ├── Eric_McKenna_Resume.docx
│   └── eric-mckenna-resume.md
├── emckenna-profile.png    # Profile photo
├── og-image.png           # Social media share image
├── bin/                   # Utility scripts
├── scripts/               # Build/deployment scripts
├── README.md              # Project documentation
└── _config.yml            # Jekyll config (minimal)

```

## Key Features

- 📱 Responsive design (mobile-first)
- 🎨 Modern UI with clean aesthetics
- 🔄 Interactive flip card animations for project showcase
- 📄 Resume downloads (PDF, DOCX, Markdown)
- 🖼️ Social share image for LinkedIn/Twitter
- ♿ Accessible with semantic HTML and ARIA labels
- 🔗 Social media integration (GitHub, LinkedIn)

## Content Sections

1. **Hero Section** - Introduction with CTA buttons and resume downloads
2. **About Section** - Professional summary, experience highlights, and technical skills grid
3. **Experience Section** - Timeline of work history (Optoro, previous roles, military service)
4. **Projects Section** - Featured projects with flip cards (front: summary, back: detailed description)
5. **Contact Section** - Email, phone, GitHub, location

## Projects Featured

Current featured projects (update this section when adding/removing projects):

1. **Make a Coffee** - AI-powered coffee instruction generator (React + Vite, Hugging Face)
2. **Flash Cards** - Flashcard app with spaced repetition (React, GitHub Pages)
3. **Constitution Compass** - Interactive civic education tool (React, Vercel)
4. **VS Code Markdown Resume Manager** - VS Code extension for resume management (TypeScript, VS Code API, Pandoc)
5. **JobTrail** - Rails 8 job application tracker with analytics (Rails 8, Hotwire, PostgreSQL) *(Work in Progress)*

## Technical Skills

Organized in a 4-column grid:
- **Backend**: Ruby on Rails, PostgreSQL, MySQL, Redis, RESTful APIs
- **Frontend**: JavaScript, Vue.js, React (learning), HTML5, CSS3
- **Testing**: RSpec, Capybara, Jest, Test Coverage
- **Infrastructure**: Docker, CI/CD, GCP, AWS (learning), Git/GitHub Actions

## Design Patterns

- Single-page application with smooth anchor link navigation
- Flip cards for projects: Click to flip, links don't trigger flip
- Consistent color scheme and typography
- Mobile-responsive with breakpoints for tablets and desktop
- Semantic HTML with proper heading hierarchy

## Content Guidelines

### When Adding New Projects

1. Add to the projects grid in `index.html` (around line 220)
2. Use the flip card structure:
   - **Front**: Project emoji, title, one-line description, primary links
   - **Back**: Detailed description (2-3 sentences), all links
3. Update the projects list in `README.md`
4. Maintain consistent emoji usage for visual interest
5. Include both live demo and GitHub links when applicable
6. Mark work-in-progress projects with *(Work in Progress)* or *(Active Development)*

### When Updating Experience

1. Edit the timeline section in `index.html` (around line 150)
2. Keep most recent experience first (reverse chronological)
3. Use bullet points for achievements
4. Focus on impact and results (metrics when possible)
5. Maintain consistent formatting and tone

### When Updating Skills

1. Edit the skills grid in `index.html` (around line 102)
2. Keep categories: Backend, Frontend, Testing, Infrastructure
3. List most important/current skills first in each category
4. Mark learning skills with "(learning)" suffix

## Resume Files

Resume files in the `/resume` directory should be kept in sync with the main resume repository at `/home/eric-mckenna/work/github/resume`. The build process for resumes is managed separately using the VS Code Markdown Resume Manager extension.

**Resume naming convention:**
- `Eric_McKenna_Resume.pdf` - PDF version
- `Eric_McKenna_Resume.docx` - Word version
- `eric-mckenna-resume.md` - Markdown source

## Deployment

The site is automatically deployed via GitHub Pages when changes are pushed to the `main` branch. No build process is required since it's a static site.

**Deployment workflow:**
1. Make changes locally
2. Test by opening `index.html` in browser
3. Commit and push to GitHub
4. GitHub Pages automatically deploys (usually within 1-2 minutes)

## Version Tracking

The footer includes a version info link pointing to the current git commit hash. Update this after significant changes:

```html
<a href="https://github.com/emckenna/emckenna.github.io/commit/COMMIT_HASH">
    vCOMMIT_HASH
</a>
```

## SEO & Social Media

- **Title**: Eric McKenna | Senior Software Engineer
- **Description**: Senior Software Engineer with 25+ years web development experience, 11+ years Ruby on Rails
- **OG Image**: `/og-image.png` (used for LinkedIn/Twitter previews)
- **Keywords**: Ruby on Rails, Software Engineer, Full Stack Developer, Team Lead, PostgreSQL, Vue.js, React, AWS, Docker

## Maintenance Notes

- Keep resume files updated quarterly or when applying to jobs
- Update projects section when launching new projects
- Review and update technical skills annually
- Ensure all external links are valid (check quarterly)
- Update copyright year in footer annually
- Test responsive design on multiple devices after content changes

## Related Projects

- **Resume Repository**: `/home/eric-mckenna/work/github/resume` - Source of truth for resume content
- **VS Code Extension**: `/home/eric-mckenna/work/github/vscode-markdown-resume-manager` - Featured project
- **Other Projects**: See GitHub profile at [github.com/emckenna](https://github.com/emckenna)

## Contact Information

- **Email**: eric.mckenna@gmail.com
- **Phone**: 703-338-3722
- **Location**: Silver Spring, MD 20901
- **GitHub**: [github.com/emckenna](https://github.com/emckenna)
- **LinkedIn**: [linkedin.com/in/ericmckenna](https://linkedin.com/in/ericmckenna)

## Browser Support

Target modern browsers with graceful degradation:
- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile Safari (iOS 14+)
- Chrome Mobile (Android 10+)

## Performance Goals

- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Lighthouse Score: 90+ (Performance, Accessibility, Best Practices, SEO)
- Keep total page size < 1MB (including images)

## Accessibility

- Use semantic HTML elements
- Include ARIA labels for icon links
- Maintain proper heading hierarchy
- Ensure sufficient color contrast
- Keyboard navigation support
- Screen reader friendly

## Future Enhancements (Ideas)

- Add a blog section for technical articles
- Integrate GitHub API to show recent activity
- Add dark mode toggle
- Include testimonials/recommendations
- Add analytics (privacy-focused)
- Create a separate projects page for more detailed case studies
