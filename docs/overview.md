# Project Overview

This version of Repo 7 changes the earlier web-blueprint pattern into a clearer layered flow:

Browser (Frontend JS)
        ↓
API Layer (Backend)
        ↓
Service Layer
        ↓
Database-style Storage

The browser now uses JavaScript `fetch` calls to consume JSON endpoints.
The web blueprint only serves pages.
