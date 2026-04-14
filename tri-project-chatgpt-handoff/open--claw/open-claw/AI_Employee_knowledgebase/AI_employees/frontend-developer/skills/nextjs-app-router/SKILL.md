---
name: nextjs-app-router
description: Production Next.js App Router workflow for modern websites and apps with metadata, server/client boundaries, and build verification.
category: Development
roles:
  - frontend-developer
  - ux-architect
  - seo-ai-discovery-strategist
  - sparky-chief-product-quality-officer
---


# Next.js App Router

## Status: READY

## Purpose
Use the current App Router model for production work. Build from a root layout, use the metadata API, keep Server Components as the default, and move client logic behind intentional boundaries.

## Standards
- Root layout must define `html` and `body`.
- Use the metadata API for titles, descriptions, and route-level SEO.
- Prefer Server Components by default; add `use client` only where interactivity requires it.
- Keep styling token-driven and consistent across light, dark, and system themes.
- Verify `next build` output and watch for static or dynamic route behavior intentionally.

## Workflow
1. Confirm the product goal, target routes, and metadata requirements.
2. Define route structure, shared layouts, and page-level data needs.
3. Split server and client concerns before implementation starts.
4. Build token-driven components and verify responsive behavior.
5. Run `next build`, inspect route output, and fix warnings before handoff.

## Evidence
- Root layout exists and is shared correctly.
- Metadata is explicit, not improvised with ad hoc head tags.
- Route rendering strategy is understood and validated.
- Screenshots and test evidence cover desktop, tablet, and mobile.

## Source Notes
- Based on Next.js App Router guidance from Context7 using `/vercel/next.js/v16.1.6`.
