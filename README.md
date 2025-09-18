# Operations Dashboard Project

### Summary:  
This project delivers an automated, cloud-native dashboard solution designed to monitor and visualize operational metrics. Leveraging modern web technologies (Dash/Plotly, Bootstrap) and a scalable deployment pipeline (GitHub → Google Cloud Build → Cloud Run), the system streamlines data presentation for decision-makers. The dashboard integrates data and cloud-based analytics, supporting modular, reusable chart components with a responsive design optimized for desktop and mobile users. Automated CI/CD pipelines ensure seamless container builds and deployments from GitHub.

### Project Structure:

**Development**

-	data/ - Contains synthetic and sample datasets used for local testing and development, supporting safe experimentation without exposing sensitive information.
-	components/ - Houses reusable, modular chart functions and visualization building blocks that compose the interactive dashboard elements.
-	assets/ - Frontend resources including Bootstrap-based layout files, stylesheets, and static assets ensuring a polished, responsive UI across devices.
-	utils/ - Collection of helper scripts, test utilities, and deployment automation tools that streamline development workflows and maintain code hygiene.
-	app.py - The main entry point script launching the Dash dashboard application, orchestrating layout and component integration for seamless user interaction.
  
**Deployment**

-	cloudbuild.yaml - Defines the automated CI/CD pipeline steps for building, testing, and deploying the dashboard using Google Cloud Build.
-	Dockerfile - Specifies the container image build instructions tailored to package the dashboard app for consistent, portable deployment.
-	requirements.txt - Lists all Python dependencies required to run the dashboard in the containerized environment.
-	Additional deployment-specific modifications and optimizations applied to development files ensure the solution is fully production-ready, secure, and compliant.

### Pre-requisites:
- Python 3.9 +
- dash-bootstrap-components 1.5.0
- pandas 2.2.1
- plotly 5.18.0
- google-cloud-storage 2.14.0
- openpyxl – 3.1.5

### Highlights and Best Practices:
- Modular Codebase: Chart logic and layout components are organized for maximum reuse and maintainability.  
- Responsive Design: Uses Bootstrap grid system with max-width constraints and auto margins for seamless rendering on various devices.  
- Secure Deployment Pipeline: Enforces compliance by scrubbing sensitive data from repo history and automating builds with scoped triggers filtered to deployment artifacts.  
- Cloud-Native CI/CD: Leveraging Google Cloud Build triggers connected to GitHub, with automated container builds pushed to Artifact Registry and deployed to Cloud Run.  
- Recruiter-Friendly Presentation: Clean, clear project structure and documentation aimed at maximizing technical transparency and demonstrating operational excellence.

### App Preview:

<img width="975" height="466" alt="image" src="https://github.com/user-attachments/assets/561980f5-f40d-4a4d-b9a3-becd39f8fdf1" />

### Architecture:

<img width="833" height="356" alt="image" src="https://github.com/user-attachments/assets/becaff65-bf2a-470e-b21a-29095f5da976" />
