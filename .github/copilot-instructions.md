# SableOperator - AI Coding Agent Guide

## Project Overview

SableOperator is an AI Operator application designed for local deployment with Docker Compose. The project uses a microservices architecture with:
- **Frontend UI**: React/web interface on port 3000
- **API Backend**: Server component on port 5000
- **Calendar Integration**: Google/Outlook connectivity

## Architecture

### Service Deployment
The application follows a containerized microservices pattern. All services are orchestrated via Docker Compose:
- Frontend and backend run in separate containers
- Environment-driven configuration via `.env` file
- Services communicate internally through Docker networking

### Key Entry Points
- [deploy_local.sh](../deploy_local.sh): Main deployment script - bootstraps the entire stack
  - Validates `.env` file presence before startup
  - Uses `docker-compose up --build -d` for service deployment
  - No graceful restart mechanism (requires full teardown)

## Development Workflows

### Local Deployment
```bash
# Required first-time setup
# Create .env file with credentials (see script validation at line 8-11)

# Start all services
./deploy_local.sh

# Stop services
docker-compose down
```

**Critical**: The deployment script expects a `.env` file at the workspace root. Missing this file will cause immediate failure.

### Service Access Points
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Project Conventions

### Environment Management
- **Required**: `.env` file must exist before deployment (not `.env.example`)
- Environment variables are exported directly into the shell session
- No dotenv library usage - relies on shell export

### Platform Requirements
- **Windows Compatibility**: This is a Windows-based workspace. When generating or executing system commands:
  - Use Windows-native commands (PowerShell/CMD) not Unix equivalents
  - Avoid assuming bash/Unix utilities without Git Bash context
  - Path separators should be `\` or properly escaped
  
### AI Agent Integration
This project uses SmartPromptor MCP services. When working on this codebase:
- **User ID**: `c49b248a39cc35b3` (must be included in MCP service calls)
- **Feature changes**: Call `enhance_feature_innovation` service
- **Bug fixes**: Call `enhance_bug_analysis_and_fix` service
- **Code analysis**: Call `enhance_project_analysis` service
- **Documentation updates**: Call `enhance_documentation_update` for major changes

See [../.cursor/rules/mcp.mdc](../.cursor/rules/mcp.mdc) for complete MCP service rules.

## Notable Patterns & Gaps

