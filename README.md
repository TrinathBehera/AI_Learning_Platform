# AI Learning Platform 🚀

**Status: In Progress**

An AI-powered personalized learning platform designed to help students build customized learning paths based on their goals, existing knowledge, and assessment performance.

The platform aims to curate free educational resources, organize them into structured courses, and provide personalized learning recommendations, AI-assisted tutoring, and progress tracking.

## 🎯 Project Vision

The goal is to build a learning platform where students can describe what they want to learn through a conversational interface. The system will assess their existing knowledge, discover relevant educational resources, and create a personalized course that they can review and approve.

Instead of generating videos, the platform will curate existing resources such as YouTube videos, documentation, tutorials, and other suitable learning materials.

## ✨ Planned Features

- **AI Learning Chatbot:** Conversational interface for learning goals and general questions.
- **Personalized Course Generation:** Structured learning paths based on student goals and assessment results.
- **Educational Resource Discovery:** Find and organize relevant free resources from external educational sources.
- **Skill Assessment:** Evaluate existing knowledge and identify learning gaps.
- **Shared Course Library:** Reuse course blueprints to reduce redundant research and AI costs.
- **Adaptive Learning:** Recommend course changes based on student progress, with approval required before applying changes.
- **Progress Tracking:** Track topic completion and individual course progress.
- **Assessment System:** Configurable pass scores, unlimited retakes, and saved question pools.
- **Course Version History:** Restore previous personalized course versions while preserving learning history.
- **Personal Notes and AI Tutor:** Support student notes and context-aware learning assistance.
- **AI Usage Management:** Enforce a limit of five course-generation requests per student per day, including failed requests.

## 🛠️ Technology Stack

### Implemented
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy with asynchronous database access
- Pydantic
- Alembic

### Planned
- React and JavaScript for the frontend
- Large Language Models (LLMs)
- AI agents and tool orchestration
- Retrieval-Augmented Generation (RAG)
- Embeddings and semantic search
- Model Context Protocol (MCP), if useful for external tool integration

*Planned technologies and features are not yet implemented.*

## ✅ Completed

- Set up the FastAPI backend.
- Integrated PostgreSQL with asynchronous database access.
- Implemented course CRUD APIs: create, read, update, and delete.
- Configured database schema migrations using Alembic.
- Added centralized exception handling.
- Added HTTP request/response logging.

## 🚧 In Progress

- Planning the complete application architecture and implementation roadmap.
- Preparing the project for incremental development and testing.

## 📌 Upcoming

- Automated backend tests.
- User authentication and authorization.
- React frontend and student dashboard.
- Conversational AI and course-generation workflow.
- Resource discovery and validation.
- Skill assessments and question-pool management.
- Shared course library and personalized course structures.
- Course approval, versioning, and restoration.
- Learning progress tracking and personal notes.
- AI tutor, RAG, and usage-cost controls.

## 🏗️ Architecture Principles

- Keep shared course blueprints separate from private student learning data.
- Require student approval before applying AI-recommended course changes.
- Preserve assessment attempts and course revision history.
- Reuse existing resources and question pools to control AI costs.
- Keep private student notes and progress isolated from shared course content.

## 💻 Local Development

The backend is built with FastAPI and Python 3.12. PostgreSQL is used for persistence, SQLAlchemy for database access, and Alembic for schema migrations.

Local setup instructions and environment configuration will be documented as the project evolves.

Never commit `.env` files, passwords, API keys, or other secrets to the repository.

## 📈 Project Progress

This is an actively developed personal project. Features will be moved from Upcoming to Completed as they are implemented and tested.

## 👨‍💻 Author

Personal project — developed incrementally as a learning and engineering project.